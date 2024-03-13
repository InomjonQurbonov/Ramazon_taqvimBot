from aiogram import Router, types, Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiocron import crontab

from config import DB_NAME, admins
from utils.database import Database
from utils.commands import commands_admin,commands_user
from states.admin_states import taqvimStates,adsStates

db = Database(DB_NAME)
commands_router = Router()

times_1 = db.saharlik_vaqti()
for time in times_1:
    time_str = time[0]
    hour, minute = map(int, time_str.split(':'))
    print(hour, minute)
    @crontab(f'{minute-2} {hour} * * *')
    async def ogohlantirish_1(message:Message):
        for user_id in db.get_user_id():
            s ="\t Navaytu an asuma sovma shahri romazona minal fajri ilal mag'ribi, xolisan lillahi ta'ala. Allohu akbar."
            await message.answer(chat_id=user_id, text=f"Saharlik vaqti bo'lishiga 2 daqiqa qoldi\n Og'iz yopish duosi:\n\n{s}")

times_2 = db.iftorlik_vaqti()
for time in times_2:
    time_str = time[0]
    hour, minute = map(int, time_str.split(':'))
    print(hour,minute)
    @crontab(f'{minute-2} {hour} * * *')
    async def ogohlantirish_2(message:Message):
        for user_id in db.get_user_id():
            s = f"\t Allohumma laka sumtu va bika amantu va 'alayka tavakkaltu va 'ala rizqika aftartu, fag'firli ya g'offaruma qoddamtu va ma axxortu."
            await message.answer(chat_id=user_id, text=f"Saharlik vaqti bo'lishiga 2 daqiqa qoldi.\n Og'iz yopish duosi:\n\n{s}")

@commands_router.message(CommandStart())
async def start(message: types.Message):
    if message.from_user.id in admins:
        await message.bot.set_my_commands(commands=commands_admin)
        await message.answer('Salom Admin, iltimos buyruqlardan birini tanlang.')
    else:
        await message.bot.set_my_commands(commands=commands_user)
        await message.answer("Salom,Ramazon taqvimi botga xush kelibsiz.\n /help - Botdan foydalanish yo'riqnomasi")

@commands_router.message(Command('cancel'))
async def cancel(message:Message, state: FSMContext):
    await state.reset_state()
    await message.answer("Barcha amallar bekor qilindi, siz buyruqlarni yuborishni davom ettirishingiz mumkin")

@commands_router.message(Command('help'))
async def help(message:Message):
    s=("Salom Ramazon taqvimi botga xush kelibsiz \n"
       "Kerakli kommandalar \n\n"
       "\t /start - Botni qaayta ishga tushirish \n"
       "\t /week - Haftalik taqvim \n"
       "\t /new_ad - Botga Reklama joylashtirish \n"
       "\t /edit_ad - Botdagi Reklamani tahrirlash \n"
       "\t /delete_ad - Botdagi Reklamani o'chirish \n"
       "\t /cancel - Amallarni bekor qilissh \n"
       "Bot avtomatik sizga Saharlik va Iftorlik vaqtini ko'rsatadi"
       )
    await message.answer(text=s)

@commands_router.message(Command('new_taqvim'))
async def add_weekday(message: Message, state: FSMContext):
    await state.set_state(taqvimStates.addWeekday)
    await message.reply('Iltimos hafta kunini kiriting')


@commands_router.message(taqvimStates.addWeekday)
async def add_weekday(message: Message, state: FSMContext):
    await state.update_data(weekday=message.text)
    await state.set_state(taqvimStates.addOntime)
    await message.reply('Iltimos saharlik vaqtini kiriting')

@commands_router.message(taqvimStates.addOntime)
async def ad_dayOn(message: Message, state: FSMContext):
    await state.update_data(Ontime=message.text)
    await state.set_state(taqvimStates.adOfftime)
    await message.reply('Iltimos iftorlik vaqtini kiriting')

@commands_router.message(taqvimStates.adOfftime)
async def ad_dayOff(message: Message, state: FSMContext):
    await state.update_data(Offtime=message.text)
    all_data = await state.get_data()
    try:
        x = db.insertTaqvim(
            hafta_kuni=all_data.get('weekday'),
            saharlik_vaqti=all_data.get('Ontime'),
            iftorlik_vaqti=all_data.get('Offtime')
        )
        if x:
            await state.clear()
            await message.answer("Taqvim kiritildi")
        else:
            await message.answer("Something went wrong, please try again later...")
    except Exception as e:
        await message.answer(f"Error: {str(e)}")

from aiogram.types import BotCommand

commands_admin = [
    BotCommand(
        command='start',
        description='Start/restart bot'
    ),
    BotCommand(
        command='help',
        description="Foydalanish yo'riqnomasi"
    ),
    BotCommand(
        command='ads',
        description='ads list (with pagination)'
    ),
    BotCommand(
        command='cancel',
        description='Cancel all commands bot'
    ),
    BotCommand(
        command='new_taqvim',
        description='Add new taqvim'
    ),
    BotCommand(
        command='edit_taqvim',
        description='Edit taqvim'
    ),
    BotCommand(
        command='delete_taqvim',
        description='Delete taqvim'
    ),
    BotCommand(
        command='new_ad',
        description='add new ad to store'
    ),
    BotCommand(
        command='edit_ad',
        description='edit ad informations'
    ),
    BotCommand(
        command='del_ad',
        description='delete ad'
    ),
    BotCommand(
        command='users',
        description='all bot users list'
    ),
    BotCommand(
        command='stat',
        description='bot statistics'
    )
]

commands_user = [
    BotCommand(
        command='start',
        description='Start/restart bot'
    ),
    BotCommand(
        command='help',
        description="Foydalanish yo'riqnomasi"
    ),
    BotCommand(
        command='new_ad',
        description="Yangi Reklama qo'shish"
    ),
    BotCommand(
        command='edit_ad',
        description="Reklamani o'zgartirish"
    ),
    BotCommand(
        command='del_ad',
        description="Reklamani o'chirish"
    ),
    BotCommand(
        command='week',
        description='Haftalik taqvim'
    )
]

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from handler.cmd_handler import commands_router

from config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN,default=DefaultBotProperties(parse_mode='HTML',link_preview_is_disabled=True))
    dp = Dispatcher()
    dp.include_router(commands_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
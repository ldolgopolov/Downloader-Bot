from aiogram import Bot, Dispatcher
from config import Config
import logging
from aiogram import F
import asyncio
from aiogram.filters import Command, CommandStart, Text, Filter

from handlers.admin.admin_notify import on_startup, on_shutdown
from handlers.users.get_url_actions import button_action, get_url
from handlers.users.start_actions import start
from states.url_state import Get_URL_video

async def main():
    logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=Config.token)
    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.message.register(button_action, F.text == 'Download video🔄')
    dp.message.register(get_url, Get_URL_video.GET_URL)

    dp.message.register(start, CommandStart())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
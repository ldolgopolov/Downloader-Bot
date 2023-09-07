from aiogram import Bot, Dispatcher
from config import Config
import logging
from aiogram import F
import asyncio
from aiogram.filters import Command, CommandStart, Text, Filter

from handlers.admin.admin_notify import on_startup, on_shutdown
from handlers.users.get_url_actions import Download_Video, Download_Audio
from handlers.users.start_actions import start
from states.url_state import Get_URL_video, Get_URL_audio

async def main():
    logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=Config.token)
    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.message.register(Download_Video.video_button_action, F.text == 'Download video▶️')
    dp.message.register(Download_Audio.audio_button_action, F.text == 'Download music🎵')
    dp.message.register(Download_Video.get_url, Get_URL_video.GET_URL)
    dp.message.register(Download_Audio.get_url, Get_URL_audio.GET_URL)

    dp.message.register(start, CommandStart())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
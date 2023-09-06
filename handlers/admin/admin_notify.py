import asyncio
from aiogram import Bot
from aiogram.types import Message
from config import Config


async def on_startup(bot: Bot):
    await bot.send_message(Config.admin_id, '✅Bot activated✅')
    print('Bot activated')

async def on_shutdown(bot: Bot):
    await bot.send_message(Config.admin_id, '⛔️Bot has been suspended⛔️')
    print('Bot has been suspended')
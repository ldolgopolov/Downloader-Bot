from aiogram import Bot
from aiogram.enums import ChatAction
from aiogram.types import Message, CallbackQuery
import asyncio

async def send_typing_action_1sek(message: Message, bot: Bot):
    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

async def send_typing_action_2sek(message: Message, bot: Bot):
    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(2)

async def callback_typing_action_1sek(call: CallbackQuery, bot: Bot):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

async def callback_typing_action_2sek(call: CallbackQuery, bot: Bot):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(2)
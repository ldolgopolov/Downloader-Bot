from aiogram import Bot
from aiogram.types import Message

from keyboards.reply_markups.main_keyboard import get_main_menu
from utils.typing_action import send_typing_action_1sek

async def start(message: Message, bot: Bot):
    user_name = str(message.from_user.first_name)
    user_sname = str(message.from_user.last_name)
    
    if user_sname == "None":
        await message.answer(f"<b>Welcome, {user_name}!</b>\nI'm your personal assistant!😊", parse_mode='HTML')
    else:
        await message.answer(f"<b>Welcome, {user_name} {user_sname}!</b>", parse_mode='HTML')

    await send_typing_action_1sek(message, bot)
    await message.answer("If you want to download a video from YouTube, click on the <b>Download video🔄</b> button😉", parse_mode='HTML', reply_markup=get_main_menu())
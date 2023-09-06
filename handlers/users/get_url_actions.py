from aiogram import Bot
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from pytube import YouTube
from config import Config
import os

from keyboards.reply_markups.main_keyboard import get_main_menu
from states.url_state import Get_URL_video
from utils.typing_action import send_typing_action_1sek


async def button_action(message: Message, state: FSMContext):
    await message.answer("Copy the URL and send it to me or share the video⬇️", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Get_URL_video.GET_URL)


async def get_url(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(link_video=message.text)
    context_data = await state.get_data()
    link = context_data.get('link_video')

    try:
        url = YouTube(link)
        title = f'{url.title.replace(" ", "_")}.mp4'

        await message.answer("Downloading may take some time🕐")
        await downloading_video(url, title)
        await message.answer("The video has begun to be sent to you📨")
        sticker = await bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEKPT5k-QYiWW9suC0AAbvsB3dMTI0z54wAAkEBAALNGzAI8fBiGN_2llgwBA')
        await send_video(message, bot, title)
        await bot.delete_message(message.chat.id, message_id=sticker.message_id)
        await message.answer("<b>It's done!✅</b>", parse_mode='HTML')
        await delete_video(title)

        await state.clear()

        await send_typing_action_1sek(message, bot)
        await message.answer("<b>Thank you for using it!</b>😌", parse_mode='HTML')
        await send_typing_action_1sek(message, bot)
        await message.answer("Do I need to download anything else?🤨", reply_markup=get_main_menu())

    except Exception:
        await message.answer("<b>Unable to download🚫</b>", parse_mode='HTML')
        await send_typing_action_1sek(message, bot)
        await message.answer("Most likely the link is wrong or the video does not exist❌", reply_markup=get_main_menu())


async def send_video(message: Message, bot: Bot, title):
    video = FSInputFile(f'{Config.downloading_path}\\{title}')
    await bot.send_video(message.chat.id, video)


async def downloading_video(url, title):
    video = url.streams.get_highest_resolution()
    video.download(output_path=Config.downloading_path, filename=title)


async def delete_video(title):
    os.remove(f'{Config.downloading_path}\\{title}')
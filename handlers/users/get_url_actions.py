from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.url_state import Get_URL_video


async def button_action(message: Message, state: FSMContext):
    await message.answer("Copy the URL and send it to me or share the video⬇️")
    await state.set_state(Get_URL_video.GET_URL)


async def get_url(message: Message, state: FSMContext):
    await state.update_data(url_video=message.text)
    context_data = await state.get_data()
    
    url = context_data.get('url_video')
    print(url)

    await state.clear()
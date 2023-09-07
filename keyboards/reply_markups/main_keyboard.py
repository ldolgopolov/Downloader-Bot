from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#---------- Main menu ----------
def get_main_menu():
    menu_kb = ReplyKeyboardBuilder()

    menu_kb.button(text='Download video▶️')
    menu_kb.button(text='Download music🎵')
    menu_kb.adjust(2)

    return menu_kb.as_markup(resize_keyboard=True,
                              one_time_keyboard=True)
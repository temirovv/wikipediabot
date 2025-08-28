from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_lang_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🇺🇿', callback_data='uz'),
                InlineKeyboardButton(text='🇷🇺', callback_data='ru'),
                InlineKeyboardButton(text='🇺🇸', callback_data='en')
            ]
        ]
    )

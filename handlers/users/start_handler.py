
from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from loader import dp
from keyboards.inline.language_menu import get_lang_menu
from data.wiki_wiki import get_info
from states.user_states import UserState


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        text=f"Hello, {html.bold(message.from_user.full_name)}!",
        reply_markup=get_lang_menu())
    await state.set_state(UserState.choose_lang)


@dp.callback_query(UserState.choose_lang)
async def set_user_language_handler(call: CallbackQuery, state: FSMContext):
    language = call.data
    data = {
        'uz': "Kerakli topikni kiriting",
        'ru': "Введите желаемую тему.",
        'en': 'types the topic that you need'
    }
    call_data = {
        'uz': "Til o'rnatildi",
        'ru': "Язык изменен",
        'en': 'Language changed'
    }
    await state.update_data({'lang':  language})
    await call.answer(call_data[language])
    await call.message.answer(data[language])


@dp.message(UserState.choose_lang)
async def get_info_via_wiki(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('lang')
    if lang is None:
        await message.answer('tilni tanlang', reply_markup=get_lang_menu())
    else:
        title = message.text
        result = get_info(title, lang)
        await message.answer(str(result))

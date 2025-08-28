from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


TOKEN = "7596603800:AAGO6rgvQ66_ANu6R7iP9HI2WR1YeKOxQaw"
dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

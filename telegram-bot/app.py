import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="6815776064:AAGMNlYMMZYDrri3OypCg6RDa17M1YrrFNs")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Это была команда старт")


@dp.message()
async def echo(message: types.Message):
    text = message.text
    if text in ["привет", "прив", "Привет", "Прив", "hello", "Hello"]:
        await message.answer("И Тебе Привет")
    elif text in ["пока", "Пока"]:
        await message.answer("И Тебе Пока")
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привіт! Я Math Tutor Bot 🤖📘\n"
        "Готовий допомагати тобі з математикою!"
    )


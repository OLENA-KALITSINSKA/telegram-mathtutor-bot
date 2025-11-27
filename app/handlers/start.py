from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привіт! Я Math Tutor Bot 🤖📘\n"
        "Готовий допомагати тобі з математикою!\n"
        "Вибери свій клас", reply_markup=kb.main
    )


CLASSES = ["6 клас", "7 клас", "8 клас", "9 клас", "10 клас", "11 клас"]


@router.message(F.text.in_(CLASSES))
async def class_selection(message: Message):
    selected_class = message.text

    await message.answer(
        f"Ти обрав: {selected_class}. Обери, що будемо робити 👇",
        reply_markup=kb.topics_tasks_menu
    )



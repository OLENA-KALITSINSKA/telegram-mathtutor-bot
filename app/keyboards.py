from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton
                           )

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="6 клас"), KeyboardButton(text="7 клас")],
    [KeyboardButton(text="8 клас"), KeyboardButton(text="9 клас")],
    [KeyboardButton(text="10 клас"), KeyboardButton(text="11 клас")],
], resize_keyboard=True, one_time_keyboard=True)


topics_tasks_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📘 Пояснення тем", callback_data="Explanation of the topic")],
        [InlineKeyboardButton(text="🧮 Задачі", callback_data="tasks")],
        [InlineKeyboardButton(text="⬅️ Змінити клас", callback_data="change the class")],
    ],
    resize_keyboard=True
)

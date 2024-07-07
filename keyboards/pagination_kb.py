from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON


# Функция для формирования инлайн-клавиатуры на лету
def create_pagination_kb(*args: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON.get(button, button),
                callback_data=button)
            )

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
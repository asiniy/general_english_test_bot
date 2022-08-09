from random import shuffle

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.core.handlers.private_chat.callback_data import question_cb

def options_keyboard(options: list[str]) -> InlineKeyboardMarkup:
  options_dup = options.copy()
  shuffle(options_dup)

  buttons = [
    InlineKeyboardButton(text=option, callback_data=question_cb.new(option=option))
    for option in options_dup
  ]

  keyboard = InlineKeyboardMarkup(row_width=1)
  keyboard.add(*buttons)
  return keyboard

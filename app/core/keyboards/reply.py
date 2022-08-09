from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.core.navigations import reply
from app.core.keyboards.resized_reply_keyboard import ResizedReplyKeyboard

# Customize your keyboard here
default_menu = ResizedReplyKeyboard(
    keyboard=[
        [
            KeyboardButton("Some Text")
        ],
    ]
)

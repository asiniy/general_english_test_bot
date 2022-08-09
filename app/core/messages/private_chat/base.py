from aiogram import types
from aiogram.utils.markdown import hbold as bold, hlink as link

from app.core.questionnaire import Question, questions


def welcome(user_firstname: str) -> str:
    """
    :param user_firstname:
    :return: welcome message to user
    """

    return bold(f'Hello, {user_firstname}!') + \
            f"\n\nThis is {link(title='Official cambridge test questionnaire', url='https://www.cambridgeenglish.org/test-your-english/general-english/')}." + \
            f"\n\n/test to start your test"

def begin_test() -> str:
    return f'Твой тест начинается! Тебе придут {len(questions)} вопросов, твоя задача - выбрать правильный ответ'

def question_text(question: Question) -> str:
    return f"Select an option below on how would you answer to this question: {question.title}"

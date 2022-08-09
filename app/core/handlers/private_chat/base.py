import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatType

from app.core.keyboards.question import options_keyboard
from app.core.handlers.private_chat.callback_data import question_cb
from app.core.messages.private_chat import base as msgs
from app.core.middlewares.throttling import throttle
from app.core.navigations.command import Commands
from app.core.questionnaire import Question, questions
from app.core.states.test import TestState
from app.models.dto import get_user_from_message
from app.services.database.dao.user import UserDAO

async def answer_to_question(m: types.Message, callback_data: dict, state: FSMContext):
    option = callback_data.get('option')
    data = await state.get_data()
    question_no = data.get('question_no')
    correct_answers_count = data.get('correct_answers_count')

    correct_option = questions[question_no].options[0]
    if option == correct_option:
        await m.bot.send_message(m.from_user.id, "Correct answer")
        correct_answers_count += 1
    else:
        await m.bot.send_message(m.from_user.id, "Incorrect answer")

    await wait()
    if len(questions) > question_no + 1:
        await state.update_data(question_no=question_no+1, correct_answers_count=correct_answers_count)
        await _ask_question(m.bot, m.from_user.id, questions[question_no+1])
    else:
        await m.bot.send_message(m.from_user.id, f"Total amount of correct answers: {correct_answers_count}")

@throttle(limit=2)
async def cmd_start(m: types.Message, state: FSMContext):
    """/start command handling. Adds new user to database, finish states"""

    user = get_user_from_message(message=m)
    session = UserDAO(session=m.bot.get("db"))
    await session.add_user(user)

    await m.answer(msgs.welcome(user_firstname=user.firstname)) # , reply_markup=reply.default_menu

@throttle(limit=2)
async def cmd_test(m: types.Message, state: FSMContext):
    """/test actually does what it's supposed to do."""

    await m.answer(msgs.begin_test())
    await state.set_state(TestState.questioning)
    await state.update_data(question_no=0, correct_answers_count=0)
    await wait()
    await _ask_question(m.bot, m.from_user.id, questions[0])

def register_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(answer_to_question, question_cb.filter(), state="*")

    dp.register_message_handler(cmd_start, commands=str(Commands.start),
                                chat_type=ChatType.PRIVATE, state="*")

    dp.register_message_handler(cmd_test, commands=str(Commands.test), chat_type=ChatType.PRIVATE, state="*")

async def _ask_question(bot, chat_id: int, question: Question):
    text = msgs.question_text(question)
    keyboard = options_keyboard(question.options)

    await bot.send_message(chat_id, text, reply_markup=keyboard)

async def wait():
    await asyncio.sleep(0.5)

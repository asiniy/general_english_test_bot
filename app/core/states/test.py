from aiogram.dispatcher.filters.state import State, StatesGroup

class TestState(StatesGroup):
  questioning = State()
  report = State()

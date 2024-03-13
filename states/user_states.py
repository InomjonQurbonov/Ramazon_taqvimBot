from aiogram.fsm.state import State, StatesGroup

class UserStates(StatesGroup):
    insertTitle = State()
    insertText = State()
    insertImages = State()

    updTitle = State()
    updText = State()
    updImages = State()

    delAd = State()
    del_Ad_confirm = State()
    del_Ad_list = State()
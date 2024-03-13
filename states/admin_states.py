from aiogram.fsm.state import State, StatesGroup

class adsStates(StatesGroup):
    newAd_state = State()
    editAd_state = State()
    deleteAd_state = State()

class taqvimStates(StatesGroup):
    taqvim_state = State()

    addWeekday = State()
    editWeekday = State()
    deleteWeekday = State()

    addOntime = State()
    editOntime = State()
    deleteOntime = State()

    adOfftime = State()
    editOfftime = State()
    deleteOfftime = State()
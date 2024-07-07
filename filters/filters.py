from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

class IsDigitCallbackData(BaseFilter):
    # def __init__(self, callback):
    #     self.callback = callback

    async def __call__(self, callback: CallbackQuery):
        return callback.data.isdigit()


class IsDelBookmarkCallbackData(BaseFilter):
    # def __init__(self, ca):
    def __call__(self, callback: CallbackQuery):
        return callback.data.endswith('del') and callback.data[:-3].isdigit()

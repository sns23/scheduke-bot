from Token import token
from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=token)
dp = Dispatcher(bot,storage=MemoryStorage())

if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)

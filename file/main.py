from Token import token
from aiogram import Bot,Dispatcher,executor,types
import asyncio

loop = asyncio.get_event_loop()
bot = Bot(token=token)
dp = Dispatcher(bot) #обработчик

if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)

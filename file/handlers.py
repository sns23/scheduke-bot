from keyboard import kb
from main import bot, dp, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.types import Message

class FSM(StatesGroup)

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name} '
                                                 f' {"" if message.from_user.last_name is None else message.from_user.last_name}',reply_markup=kb)
@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, f'Тут будет инструкция к боту')

@dp.callback_query_handler(text='group')
async def command(message: types.Message):
    await bot.send_message(message.from_user.id, f'Напишите название группы')

@dp.message_handler(commands=['exit'])
async def exit(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите нужную комманду')




# async def echo(message: Message):
#     text = f'Бот запущен'
#     await bot.send_message(chat_id=message.from_user.id, text=text)
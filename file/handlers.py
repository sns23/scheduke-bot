import aiogram.types.input_message_content

from main import bot, dp, types
from aiogram.types import Message


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}'
                                                 f'{"" if message.from_user.last_name is None else message.from_user.first_name} ')


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, f'Тут будет инструкция к боту')

@dp.message_handler(commands=['group','Группа'])
async def command_help(message: types.Message):
    await bot.send_message(message.from_user.id, f'Напищите название группы')
        async def message (message: types.Message):
            arguments = message.get_args()
            await message.reply()



# async def echo(message: Message):
#     text = f'Бот запущен'
#     await bot.send_message(chat_id=message.from_user.id, text=text)

# async def send_to_user():
#     await bot.send_message(chat_id= '473436272', text="Бот запущен")
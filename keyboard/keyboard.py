from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# from file.Callback_data import callback



kb = InlineKeyboardMarkup()

help = InlineKeyboardButton(text='Помощь',callback_data='help')
groups = InlineKeyboardButton(text='Группа', callback_data='group')
kb.add(help,groups)
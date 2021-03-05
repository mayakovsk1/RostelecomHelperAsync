from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from relevance import entry_relevance


TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


string1 = '''Зравствуйте, вас приветствует служба поддержки Ростелекома.
Пожалуйста введите ваш запрос...'''


string2 = '''Пожалуйста введите ваш запрос...'''


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
	await bot.send_message(msg.from_user.id, string1)


@dp.message_handler(commands=['help'])
async def input_please(msg: types.Message):
	await bot.send_message(msg.from_user.id, string2)


@dp.message_handler()
async def process_print_answer(msg: types.Message):
    answer = entry_relevance(str(msg.text))
    await bot.send_message(msg.from_user.id, answer)
    await bot.send_message(msg.from_user.id, string2)

    #  логирование
    print(f'username: {msg.from_user.username}')
    print(f'id: {msg.from_user.id}')
    print(f'message: {msg.text}')
    print(f'answer: {answer}\n')


executor.start_polling(dp)
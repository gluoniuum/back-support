import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import types
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import InputTextMessageContent, Message 

from dotenv import load_dotenv 
import os

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=API_TOKEN,default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
###?


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f'yay_ {message.chat.id}')
    await message.answer(f'yay_ {message.message_id}')


@dp.message()
async def handle_forward_command(message: Message):
    await message.bot.send_message(chat_id=-4569283112, text='yay')



print('EE запустився!')
###!
async def main():
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)
    print('щзх')
if __name__ == '__main__':
    asyncio.run(main())
import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram import types
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import InputTextMessageContent, Message 
import json
from dotenv import load_dotenv 
import os

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=API_TOKEN,default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
router = Router()
###?


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f'yay_ {message.from_user.id}')
    await message.answer(f'yay_ {message.chat.id}')
    await message.answer(f'yay_ {message.message_id}')

@dp.message(lambda message: message.chat.id == -1002389099327)

async def replayer(message: Message):
    with open('/home/gluon/projects/backSupportt/data.json', 'r') as file:
        data = json.load(file)

    print('yay1')
    if lambda message: message.reply_to_message is not None:
        print('yay1')
        # chat_id = message.reply_to_message.message_id
        chat_id = 6805483829
        from_chat_id = -4569283112
        forwarding_text = int(message.message_id)
        await message.answer(f'yay_ {chat_id}')
        await bot.forward_message(chat_id = chat_id, from_chat_id = from_chat_id , message_id =  forwarding_text)
    # await bot.send_message(chat_id = user_id, text =  forwarding_text.text )
    else:
        pass

@dp.message()
async def forwarder(message: Message):
    forwarding_text = (message.message_id)
    from_chat_id = message.chat.id
    print (from_chat_id)

    chat_id = -1002389099327
    print('yay2')
    await bot.forward_message(chat_id = chat_id, from_chat_id = from_chat_id , message_id =  forwarding_text)
    print(forwarding_text)
    bdbasser(from_chat_id, forwarding_text)

async def bdbasser(fromm, mess_id):
    with open('data.json', 'r') as file:
        data = json.load(file)

    data[str(mess_id)] = fromm

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


print('EE запустився!')
###!
async def main():
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)
    print('щзх')
if __name__ == '__main__':
    asyncio.run(main())



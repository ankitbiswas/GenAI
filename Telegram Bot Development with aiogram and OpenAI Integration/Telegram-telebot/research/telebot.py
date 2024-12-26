from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
import logging
import asyncio

load_dotenv()
# API_TOKEN = os.getenv(BOT_API_TOKEN)
API_TOKEN = "7953668615:AAFbQK3CyRuz9h0NHnGcMoUBHzpXYIlKlzE"

#configure logging
logging.basicConfig(level=logging.INFO)

#initialize the bot 
bot=Bot(token=API_TOKEN)
dp=Dispatcher()

@dp.message(Command(commands=['start','help']))
async def command_start_handler(message:types.Message):
    """ This handler receives messages with '/start' or '/help' command
        Args:
            message(types.Message): __description__
    """
    logging.info(f"Received /start from {message.from_user.id}")
    if message.text == "/start":
        await message.answer("Hello! Welcome to the bot. Use /help to learn more.")
    elif message.text == "/help":
        await message.answer("This is a simple bot to demonstrate aiogram. Here are the available commands:\n"
                             "/start - Start the bot\n"
                             "/help - Get help")
    await message.answer("Hi! \n I am Razor Bot ! \n Powered by AIOGRAM")


@dp.message()
async def echo(message:types.Message):
    """ This handler receives messages with any other commands and echos that
        Args:
            message(types.Message): __description__
    """
    logging.info(f"Received /start from {message.from_user.id}")
    await message.answer(message.text)

async def main():
    logging.info("Bot is starting...")  
    await dp.start_polling(bot)


if __name__== "__main__":
    asyncio.run(main())


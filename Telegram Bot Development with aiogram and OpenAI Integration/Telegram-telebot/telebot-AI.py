from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
import logging
import asyncio
import openai
from openai import AsyncOpenAI

load_dotenv()
# API_TOKEN = os.getenv(BOT_API_TOKEN)
API_TOKEN = "****************************"
OPENAI_API_TOKEN = "**************************"

#configure logging
logging.basicConfig(level=logging.INFO)

#initialize the bot 
bot=Bot(token=API_TOKEN)
openai.api_key= OPENAI_API_TOKEN
client = AsyncOpenAI(api_key=OPENAI_API_TOKEN)
# client.api_key=OPENAI_API_TOKEN
dp=Dispatcher()

class Reference:
    def __init__(self)->None:
        ## we will use the below variable as memory
        ## initially it will be empty
        self.response=""
reference=Reference()

def clear_past():
    reference.response=""
    
@dp.message(Command(commands=['start','help','clear']))
async def command_start_handler(message:types.Message):
    """ This handler receives messages with '/start' or '/help' command
        Args:
            message(types.Message): __description__
    """
    logging.info(f"Received {message.text} from {message.from_user.id}")
    await message.answer("Hi! \n I am Razor Bot ! \n Powered by AIOGRAM")
    if message.text == "/start":
        await message.answer("Hello! Welcome to the bot. Use /help to learn more.")
    elif message.text == "/clear":
        clear_past()
        await message.answer("Hello! I have cleared the past conversation. Use /help to learn more.")
    elif message.text == "/help":
        await message.answer("This is a simple bot to demonstrate aiogram. Here are the available commands:\n"
                             "/start - Start the bot\n"
                             "/help - Get help\n"
                             "/clear - To clear past convo"
                             "Hope this helps")
        

@dp.message()
async def command_start_handler(message:types.Message):
    """ This handler receives messages and uses OpenAI model to generate answers
        Args:
            message(types.Message): __description__
    """
    logging.info(f"Received {message.text} from {message.from_user.id}")
    await message.answer("Hi! \n I am Razor Bot ! \n Powered by AIOGRAM")
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You are helpful assistant"}, # role assistant,
            {"role":"user","content": message.text} #our query
        ]
    )
    print(f"Chatgpt {response}")
    reference.response=response.choices[0].message.content
    print(f"CHATGPT :\n\t {reference.response}")
    await bot.send_message(chat_id=message.chat.id,text=reference.response)

@dp.message()
async def echo(message:types.Message):
    """ This handler receives messages with any other commands and echos that
        Args:
            message(types.Message): __description__
    """
    logging.info(f"Received {message.text} from {message.from_user.id}")
    await message.answer(message.text)

async def main():
    logging.info("Bot is starting...")  
    await dp.start_polling(bot)


if __name__== "__main__":
    asyncio.run(main())


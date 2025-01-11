import chainlit as cl
from src.llm import ask_bot
from src.config import instruction
import asyncio

@cl.on_chat_start
async def on_chat_start():
    messages = None 
    print("inside on chat start")
    #Wait for users to upload a file
    user_input = await cl.AskUserMessage(content="Please pass your query", timeout=180).send()
    if not user_input:
        return  # Handle timeout scenario
    # message=messages[0]

    msg=cl.Message(content=f"Processing '{user_input}' ...")
    await msg.send()

    msg.content = f"Processing `{user_input}` done. You can now ask questions!"
    await msg.update()

    # cl.user_session.set("chain", chain)



@cl.on_message
async def main(user_message:cl.Message):

    try:
       response = await asyncio.to_thread(ask_bot, user_message.content, instruction)

    except asyncio.TimeoutError:
        response = "Sorry, the request took too long. Please try again."
    
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {response}",
    ).send()


async def safe_ask_bot(message, instruction, timeout=10):
    return await asyncio.wait_for(ask_bot(message, instruction), timeout=timeout)
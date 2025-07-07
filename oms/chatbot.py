from oms.app import main as oms_main
import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    cl.Message(content="abc").send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    response = await oms_main(user_input)
    await cl.Message(content=f"{response}").send()
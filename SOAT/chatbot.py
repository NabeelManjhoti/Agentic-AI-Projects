from soat.app import main as soat_main
import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Welcome to the Task Management Chatbot! How can I assist you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    response = await soat_main(user_input)
    await cl.Message(content=f"{response}").send()
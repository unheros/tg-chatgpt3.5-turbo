import asyncio

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.link import create_tg_link
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.markdown import hide_link

from chatgpt import Message as GPTMessage
from chatgpt import Role, create_completion
from config_reader import Config

router = Router()


@router.message(Command("start", ignore_case=True))
async def handler_start(message: Message) -> None:
    await message.reply("Hi there! How can I help you?")


@router.message()
async def handler_chat(message: Message, bot: Bot) -> None:
    async with ChatActionSender.typing(message.chat.id):
        tg_link = create_tg_link(str(message.chat.id))
        msg = await message.reply(hide_link(tg_link) + message.html_text)
        
        completion_id = msg.entities[0].url[5:-1] # type: ignore
        print(completion_id)
    
    # messages = [
    #     GPTMessage(
    #         role=Role.user,
    #         content="hello"
    #     )
    # ]
    # task = asyncio.create_task(create_completion(messages))
    
    # while True:
    #     if task.done():
    #         await message.reply(task.result())
    #         return
        
    #     await bot.send_chat_action(message.chat.id, "typing")
    #     await asyncio.sleep(5)

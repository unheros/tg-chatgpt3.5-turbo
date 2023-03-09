import asyncio

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender

from chatgpt import Message as GPTMessage
from chatgpt import Role, create_completion
from config_reader import Config

router = Router()


@router.message(Command("start", ignore_case=True))
async def handler_start(message: Message) -> None:
    await message.reply("Hi there! How can I help you?")


@router.message()
async def handler_chat(message: Message, config: Config) -> None:
    async with ChatActionSender.typing(message.chat.id):
        messages = []
        if message.reply_to_message:
            content = message.reply_to_message.text
            messages.append(
                GPTMessage(
                    role=Role.assistant,
                    content=content
                )
            )
        messages.append(
            GPTMessage(
                role=Role.user,
                content=message.text
            )
        )
        future = create_completion(config.OPENAI_TOKEN, messages)
        task = asyncio.create_task(future)
        
        while True:
            if task.done():
                await message.reply(task.result().content)
                return
            await asyncio.sleep(1)

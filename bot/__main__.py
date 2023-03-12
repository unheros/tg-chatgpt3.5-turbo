import asyncio
import logging
import sys

import openai
from aiogram import Bot, Dispatcher

import logger
from config_reader import Config
from handlers import router


async def main() -> None:
    logger.setup_logging()
    config = Config()

    bot = Bot(token=config.TG_BOT_TOKEN, parse_mode="markdown")
    dp = Dispatcher()

    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(bot, config=config)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    if sys.platform == "win32":
        el = asyncio.WindowsSelectorEventLoopPolicy()
        asyncio.set_event_loop_policy(el)
    asyncio.run(main())

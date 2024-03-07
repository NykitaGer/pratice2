import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from manage import TOKEN
from inline_mode import router as inline_router
from default_mode import router as default_router

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(inline_router, default_router)

    bot_commands = [
        BotCommand(command="/random_quote", description="Get random quote"),
        BotCommand(command="/qod", description="Get quote of the day")
    ]

    await bot.set_my_commands(commands=bot_commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

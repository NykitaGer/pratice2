from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from get_quote import get_random_quote, get_qod

router = Router()


@router.message(CommandStart())
async def on_start(message: Message):
    await message.answer("Welcome to the quote bot")


@router.message(Command("random_quote"))
async def send_random_quote(message: Message):
    quote, author = get_random_quote()
    await message.answer(f"{author}\n{quote}")


@router.message(Command("qod"))
async def send_qod(message: Message):
    quote, author = get_qod()
    await message.answer(f"{author}\n{quote}")

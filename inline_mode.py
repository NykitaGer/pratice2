from aiogram import Router, F
from aiogram.types import (
    InlineQuery,
    InputTextMessageContent,
    InlineQueryResultArticle
)

from aiogram.fsm.context import FSMContext
from get_quote import get_random_quote, get_qod

router = Router()


def get_quotes():
    result = []

    quote, author = get_random_quote()
    title = "Random quote"
    description = "Sending a random qoute by random author"

    result.append({
        "quote": quote,
        "author": author,
        "title": title,
        "description": description
    })

    quote, author = get_qod()
    title = "Quote of the day"
    description = "Sending a quote of the day"

    result.append({
        "quote": quote,
        "author": author,
        "title": title,
        "description": description
    })

    return result


@router.inline_query(F.query == "quotes")
async def inline_quotes(inline_query: InlineQuery, state: FSMContext):
    quotes = get_quotes()

    results = []

    for index, quote_info in enumerate(quotes):
        author = quote_info["author"]
        quote = quote_info["quote"]
        title = quote_info["title"]
        description = quote_info["description"]
        message_content = InputTextMessageContent(
            message_text=f"{author}\n{quote}",
            parse_mode="HTML"
        )
        result_id = f"{index}-{inline_query.from_user.id}"
        results.append(InlineQueryResultArticle(
            id=result_id, title=title, description=description,
            input_message_content=message_content
        ))

    await inline_query.answer(results, cache_time=0, is_personal=True)

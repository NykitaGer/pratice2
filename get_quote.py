import requests


def get_random_quote() -> list | None:
    url = "https://api.quotable.io/random"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        quote = data["content"]
        author = data["author"]
        return [quote, author]
    else:
        print("Error with status code:", response.status_code)

    return None


def get_qod() -> list | None:
    url = "https://favqs.com/api/qotd"

    response = requests.get(url)

    if (response.status_code == 200):
        data = response.json()

        content = data["quote"]["body"]
        author = data["quote"]["author"]

        return [content, author]
    else:
        print("Error with status code:", response.status_code)

    return None

import asyncio
import requests

from typing import Optional
from fastapi import FastAPI


app = FastAPI()


def fizzbuzz(number):
    fizzbuzz_str = ""
    if number % 3 == 0:
        fizzbuzz_str += "Fizz"
    if number % 5 == 0:
        fizzbuzz_str += "Buzz"
    return fizzbuzz_str


@app.get('/')
async def read_root():
    return {"Hello": "World"}


@app.get('/fizzbuzz/{number}')
async def respond_fizzbuzz(number: int, q: Optional[str] = None):
    if isinstance(number, int) and (1 <= number <= 10 or number == 15):
        fizzbuzz_str = fizzbuzz(number)
        base_url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(base_url + "/" + str(number)).json()
        return {"number": number,
                "fizzbuzz": fizzbuzz_str,
                "placeholder_post": {
                    "title": response['title'],
                    "body": response['body']
                }}
    else:
        return ""


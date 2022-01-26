import asyncio
import requests
from fastapi import FastAPI


app = FastAPI()


def fizzbuzz(number):
    """for a number divisible by 3, return Fizz
    if otherwise divisible by 5, return Buzz
    if divisible by the product of the two, return FizzBuzz
    Args:
        number int
    Returns:
        relevant str
    """
    fizzbuzz_str = ""
    if number % 3 == 0:
        fizzbuzz_str += "Fizz"
    if number % 5 == 0:
        fizzbuzz_str += "Buzz"
    return fizzbuzz_str


@app.get("/")
async def read_root():
    """basic test of the FastAPI"""
    return {"Hello": "World"}


@app.get("/fizzbuzz/{number}")
async def respond_fizzbuzz(number: int):
    """
    And endpoint that handles the fizzbuzz logic and retrieval of data from JSONPlaceholder
    Args:
        number: only takes in an integer 1-10 or 15
    Returns:
        dictionary of keys with appropriate values to populate to the url
    """
    if isinstance(number, int) and (1 <= number <= 10 or number == 15):
        fizzbuzz_str = fizzbuzz(number)
        base_url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(base_url + "/" + str(number)).json()
        return {
            "number": number,
            "fizzbuzz": fizzbuzz_str,
            "placeholder_post": {"title": response["title"], "body": response["body"]},
        }
    else:
        return ""

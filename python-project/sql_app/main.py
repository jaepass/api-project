import uvicorn
from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel
from models import Location


# Instantiate a FastAPI Python class instance
app = FastAPI()


@app.post("/location", response_model=None)
async def create_location(location):
    return location


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# class Book(BaseModel):
#     title: str
#     description: Union[str, None] = None
#     author: str


# # Create a class object 'BookModel'
# class BookModel(str, Enum):
#     the_art_of_impossible = "The Art of Impossible"
#     the_midnight_library = "The Midnight Library"
#     think_again = "Think Again"
#     what_happened_to_you = "What Happened to You"


# The following operations tell FastAPI the functions that follow handle the requests that goes to the path "/books/current"

# Operation to get the list of books
# List all enum values from a class
# @app.get("/books")
# async def get_books():
#     # An instance of the BookModel needs to be created to call it
#     books = BookModel
#     """
#     Get a list of books
#     """
#     titles = [book.value for book in books]
#     # Returns all book titles as an array
#     return titles


# Operation to get the book model title
# @app.get("/books/{book_title}")
# async def get_book(book_title: BookModel):
#     return {"book_title": book_title}


# Operation to get the current book
# @app.get("/books/current")
# async def get_book_current():
#     return {"book_id": "The current book"}


# Operation to get the book by it's ID
# @app.get("/books/{book_id}")
# async def read_book(book_id: int, current: bool, q: Union[str, None] = None):
#     book = {"book_id": book_id, "current": current}
#     if q:
#         book.update({"q": q})
#     if not current:
#         book.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return book


# @app.post("/books/")
# async def create_book(book: Book):
#     return book

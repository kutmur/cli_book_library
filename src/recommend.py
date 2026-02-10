from dotenv import load_dotenv
import os
from pymongo import MongoClient
import random

load_dotenv()

def recommendBook():
    uri = os.getenv("MongoDB_Connection_String")

    client = MongoClient(uri)
    db = client.get_database("books_db")
    collection = db["to_read"]

    genres = collection.distinct("genre")

    if not genres:
        print("No books found in your to-read list.")
        return

    while True:
        print("\nAvailable genres:")
        for i, genre in enumerate(genres, 1):
            print(f"  {i}. {genre}")

        user_input = input("\nEnter a genre to get a recommendation (or 'quit' to exit): ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            return

        matched_genre = None
        for genre in genres:
            if genre.lower() == user_input.lower():
                matched_genre = genre
                break

        if matched_genre:
            books = list(collection.find({"genre": matched_genre}))
            book = random.choice(books)
            print(f"\n Recommended book in '{matched_genre}':")
            print(f"  Title: {book.get('title', 'Unknown')}")
            print(f"  Author: {book.get('author', 'Unknown')}")
            print(f"  Genre: {book.get('genre', 'Unknown')}")
            return
        else:
            print(f"\n'{user_input}' is not a valid genre. Please choose from the list above.")
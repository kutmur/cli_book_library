from dotenv import load_dotenv
import os
from pymongo import MongoClient
from updatedb import updateDb

load_dotenv()

def addBook():
    uri = os.getenv("MongoDB_Connection_String")

    client = MongoClient(uri)
    db = client.get_database("books_db")

    while True:
        collection_choice = input("Add to (1) already_read or (2) to_read: ").strip()
        if collection_choice == "1":
            collection = db["already_read"]
            break
        if collection_choice == "2":
            collection = db["to_read"]
            break
        print("Please enter 1 or 2.\n")

    try:
        while True:
            book_id = input("Enter bookId: ").strip()
            if book_id:
                break
            print("bookId cannot be empty. Please try again.")

        while True:
            title = input("Enter title: ").strip()
            if title:
                break
            print("Title cannot be empty. Please try again.")

        while True:
            author = input("Enter author: ").strip()
            if author:
                break
            print("Author cannot be empty. Please try again.")

        while True:
            genre = input("Enter genre: ").strip()
            if genre:
                break
            print("Genre cannot be empty. Please try again.")

        while True:
            already_read_input = input("Enter alreadyRead (true/false): ").strip().lower()
            if already_read_input in ("true", "false"):
                already_read = already_read_input == "true"
                break
            print("Please enter 'true' or 'false'.")

        book = {
            "bookId": book_id,
            "title": title,
            "author": author,
            "genre": genre,
            "alreadyRead": already_read
        }

        print("\nBook to be added:")
        print(book)

        confirm = input("\nConfirm adding this book? (y/n): ").strip().lower()
        if confirm == "y":
            collection.insert_one(book)
            print("Book added successfully!")
            updateDb()
        else:
            print("Book was not added.")

    except Exception as e:
        print("Error: ", e)
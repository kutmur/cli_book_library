from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

def Search():
    uri = os.getenv("MongoDB_Connection_String")

    client = MongoClient(uri)
    db = client.get_database("books_db")

    while True:
        collection_choice = input("Search in (1) already_read or (2) to_read: ").strip()
        if collection_choice == "1":
            collection = db["already_read"]
            break
        if collection_choice == "2":
            collection = db["to_read"]
            break
        print("Please enter 1 or 2.\n")

    valid_numbers = [1, 2, 3, 4, 5, 6]

    try:
        expression = -1

        while True:
            user_input = input("\n 1.For id Search \n 2.For bookId Search \n 3.For title Search \n 4.For author Search \n 5.For genre Search \n 6.For alreadyReady Search \n")
            try:
                expression = int(user_input)
                if expression in valid_numbers:
                    break
                else:
                    print("Number must be between 1 and 6. \n")
            except ValueError:
                print("That's not a valid integer. Please try again.\n")

        match expression:
            case 1:
                value = input("Enter id: ").strip()
                query = {"id": value}
            case 2:
                value = input("Enter bookId: ").strip()
                query = {"bookId": value}
            case 3:
                value = input("Enter title: ").strip()
                query = {"title": {"$regex": value, "$options": "i"}}
            case 4:
                value = input("Enter author: ").strip()
                query = {"author": {"$regex": value, "$options": "i"}}
            case 5:
                value = input("Enter genre: ").strip()
                query = {"genre": {"$regex": value, "$options": "i"}}
            case 6:
                value = input("Enter alreadyRead (true/false): ").strip().lower() == "true"
                query = {"alreadyRead": value}

        results = list(collection.find(query, {"_id": 0}))
        for doc in results:
            print(doc)

    except Exception as e:
        print("Error: ", e)
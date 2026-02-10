from dotenv import load_dotenv
import os
from pymongo import MongoClient
from updatedb import updateDb

load_dotenv()

def editBook():
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

        results = list(collection.find(query))
        if not results:
            print("No books found matching the query.")
            return

        for i, doc in enumerate(results):
            display = {k: v for k, v in doc.items() if k != "_id"}
            print(f"\n[{i + 1}] {display}")

        if len(results) == 1:
            selected = results[0]
        else:
            while True:
                try:
                    choice = int(input(f"\nSelect a book to edit (1-{len(results)}): ").strip())
                    if 1 <= choice <= len(results):
                        selected = results[choice - 1]
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(results)}.")
                except ValueError:
                    print("That's not a valid integer. Please try again.")

        print("\nEditing book. Press Enter to keep the current value.\n")

        update_fields = {}
        for key, val in selected.items():
            if key == "_id":
                continue
            new_val = input(f"{key} [{val}]: ").strip()
            if new_val == "":
                continue

            if key == "alreadyRead":
                new_val = new_val.lower() == "true"
            update_fields[key] = new_val

        if update_fields:
            collection.update_one({"_id": selected["_id"]}, {"$set": update_fields})
            print("\nBook updated successfully!")
            updated = collection.find_one({"_id": selected["_id"]}, {"_id": 0})
            print(updated)
            updateDb()
        else:
            print("\nNo changes were made.")

    except Exception as e:
        print("Error: ", e)

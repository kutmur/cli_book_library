from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

uri = os.getenv("MongoDB_Connection_String")

client = MongoClient(uri)

try:
    database = client.get_database("books_db")
    to_read = database.get_collection("to_read")
    already_read = database.get_collection("already_read")

    for doc in to_read.find({}):
        if doc.get("alreadyRead", False):
            already_read.insert_one(doc)
            to_read.delete_one({"_id": doc["_id"]})

    for doc in already_read.find({}):
        if not doc.get("alreadyRead", True):
            to_read.insert_one(doc)
            already_read.delete_one({"_id": doc["_id"]})

except Exception as e:
    print("Error: ", e)
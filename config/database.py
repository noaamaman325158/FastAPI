from pymongo import MongoClient

client = MongoClient("mongodb+srv://noaa:noaa@cluster0.hqngz9m.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo_collection"]

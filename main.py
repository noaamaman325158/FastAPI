from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from routes.route import router

app = FastAPI()

app.include_router(router)

# Connection string
# uri = "mongodb+srv://noaa:noaa@cluster0.hqngz9m.mongodb.net/?retryWrites=true&w=majority"
#
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
#
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

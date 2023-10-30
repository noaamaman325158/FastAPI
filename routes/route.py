from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET Request Method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


# POST Request Method

@router.post('/')
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))


# Get Request method
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})


# Delete Request method
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})


# PATCH Request Method
@router.patch("/{id}")
async def patch_todo(id: str, updated_fields: dict):
    todo = collection_name.find_one({"_id": ObjectId(id)})
    if not todo:
        return {"message": "Todo not found"}

    # Update the specified fields in the Todo
    for key, value in updated_fields.items():
        todo[key] = value

    # Save the updated Todo
    collection_name.update_one({"_id": ObjectId(id)}, {"$set": todo})

    return todo

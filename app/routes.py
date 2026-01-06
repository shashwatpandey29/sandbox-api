from fastapi import APIRouter
from app.db import db
from app.models import Item
from bson import ObjectId

router = APIRouter()
collection = db["items"]

def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.post("/items")
def create_item(item: Item):
    res = collection.insert_one(item.dict())
    return {"id": str(res.inserted_id)}

@router.get("/items")
def get_items():
    return [serialize(i) for i in collection.find()]

@router.get("/items/{item_id}")
def get_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    return serialize(item)

@router.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    collection.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": item.dict()}
    )
    return {"status": "updated"}

@router.delete("/items/{item_id}")
def delete_item(item_id: str):
    collection.delete_one({"_id": ObjectId(item_id)})
    return {"status": "deleted"}

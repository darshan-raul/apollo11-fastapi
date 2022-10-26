from fastapi import APIRouter
from models.model import Link
from config.database import collection_name

from schemas.links_schema import links_serializer, link_serializer
from bson import ObjectId

links_router = APIRouter(
    tags=["links"],
)

# retrieve
@links_router.get("/")
async def get_links():
    links = links_serializer(collection_name.find())
    return links

@links_router.get("/{id}")
async def get_link(id: str):
    return link_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# # post
@links_router.post("/")
async def create_link(link: Link):
    _id = collection_name.insert_one(dict(link))
    return links_serializer(collection_name.find({"_id": _id.inserted_id}))


# update
@links_router.put("/{id}")
async def update_link(id: str, link: Link):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(link)
    })
    return links_serializer(collection_name.find({"_id": ObjectId(id)}))

# delete
@links_router.delete("/{id}")
async def delete_link(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
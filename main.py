from fastapi import FastAPI
from routes.links import links_router

app = FastAPI()

app.include_router(links_router)
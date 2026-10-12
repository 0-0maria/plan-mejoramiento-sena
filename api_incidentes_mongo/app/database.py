import os
from pymongo import AsyncMongoClient
from beanie import init_beanie
from .models import Incidente

MONGO_URI = "mongodb+srv://betancuratehortuamariaisabel_db_user:OMdmcCiXBPkSM1uX@cluster0.pxeaflm.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB_NAME = "incidentes_db"

client = AsyncMongoClient(MONGO_URI)

async def init_db():
    database = client[MONGO_DB_NAME]
    await init_beanie(
        database=database,
        document_models=[Incidente],
    )
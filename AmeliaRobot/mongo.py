#war-legend
import asyncio
import sys

from AmeliaRobot import log
from motor import motor_asyncio
from AmeliaRobot import MONGO_DB_URI 
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from AmeliaRobot.conf import get_int_key, get_str_key


MONGO_PORT = get_int_key("27017")
MONGO_DB_URI = get_str_key("mongodb+srv://nezuko:nezuko@cluster0.g5v4c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
MONGO_DB = "Nezuko"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["AmeliaRobot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))

from pymongo import MongoClient

import config

aayudb = MongoClient(config.MONGO_URL)
aayu = ayushdb["aayyDb"]["aayu"]


from .chats import *
from .users import *

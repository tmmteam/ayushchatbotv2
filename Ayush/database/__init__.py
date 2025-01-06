from pymongo import MongoClient

import config

aayudb = MongoClient(config.MONGO_URL)
aayu = ayushdb["aayuDb"]["aayu"]


from .chats import *
from .users import *

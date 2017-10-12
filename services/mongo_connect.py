import pymongo
from pymongo import MongoClient

from services.mongo_keys import DB

url = DB

def connect():
    client = pymongo.MongoClient(url)
    db = client.test

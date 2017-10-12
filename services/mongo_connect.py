import pymongo
from pymongo import MongoClient

from settings import mongo_url
mongo_url = mongo_url

def connect():
    client = pymongo.MongoClient(mongo_url)
    db = client.test

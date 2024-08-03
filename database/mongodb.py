import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')
database_name = os.getenv('DATABASE_NAME')

client = pymongo.MongoClient(database_url)
db = client[database_name]

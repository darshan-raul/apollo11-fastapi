from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.links
print("database",db)
collection_name = db["links"]
links = collection_name.find()

for link in links:
    print(link['link'])
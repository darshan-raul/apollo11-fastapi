from pymongo import MongoClient

client = MongoClient('mongodb://admin:password@mongodb-test:27017/?authSource=admin')
db = client.links
print("database",db)
collection_name = db["links"]
links = collection_name.find()

for link in links:
    print(link['link'])

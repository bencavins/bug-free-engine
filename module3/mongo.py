import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://bencavins:Pxo40e8GEFgEVnek@cluster0.65sxezd.mongodb.net/?retryWrites=true&w=majority"
)
db = client.test_db

d = {
    'name': 'Bob',
    'age': 33,
    'sub_dict': {
        'subkey': 'subvalue'
    }
}

# insert document
# db.test_collection.insert_one(d)

# find one document
# doc = db.test_collection.find_one({'name': 'Bob'})
# print(doc)

# Insert multiple documents
ben = {
    'name': "Ben",
    'age': 31
}

adam = {
    'name': 'Adam',
    'age': 28
}
# docs = [ben, adam]
# db.people.insert_many(docs)

# Delete a document
# db.test_collection.delete_one({'name': 'Bob'})
import sqlite3
import pymongo
from pprint import pprint


select_all_characters = """
SELECT * FROM charactercreator_character;
"""


def connect_to_mongo(dbname, collection_name):
    client = pymongo.MongoClient(
        "mongodb+srv://bencavins:@cluster0.65sxezd.mongodb.net/?retryWrites=true&w=majority"
    )
    db = client[dbname]
    collection = db[collection_name]
    return collection

def connect_to_sqlite(db_name='rpg_db.sqlite3'):
    return sqlite3.connect("rpg_db.sqlite3")

def exectute_query(conn, query):
    # Make a cursor
    cursor = conn.cursor()
    # Execute our query
    cursor.execute(query)
    # Pull the results from the cursor
    return cursor.fetchall()

# def generate_character_docs(data):
#     for row in data:
#         doc = {
#             'character_id': row[0],
#             'name': row[1],
#             'level': row[2],
#             'exp': row[3],
#             'hp': row[4],
#             'strength': row[5],
#             'intelligence': row[6],
#             'dexterity': row[7],
#             'wisdom': row[8],
#             'items': [item_doc for item_doc in generate_item_docs]
#         }
#         yield doc

def build_character_docs(conn, data):
    """Returns a list of dictionaries"""
    result = []
    for row in data:
        char_id = row[0]
        item_query = f"""
SELECT i.item_id, i.name, i.value, i.weight
FROM charactercreator_character_inventory as ci
JOIN armory_item as i
	ON ci.item_id = i.item_id
WHERE ci.character_id = {char_id}
        """
        item_data = exectute_query(conn, item_query)
        item_docs = []
        for item_row in item_data:
            item_doc = {
                'item_id': item_row[0],
                'name': item_row[1],
                'value': item_row[2],
                'weight': item_row[3],
            }
            item_docs.append(item_doc)

        doc = {
            'character_id': row[0],
            'name': row[1],
            'level': row[2],
            'exp': row[3],
            'hp': row[4],
            'strength': row[5],
            'intelligence': row[6],
            'dexterity': row[7],
            'wisdom': row[8],
            'items': item_docs
        }
        result.append(doc)
    return result


if __name__ == '__main__':
    rpg_collection = connect_to_mongo('rpg', 'characters')
    sqlite_conn = connect_to_sqlite()
    character_data = exectute_query(sqlite_conn, select_all_characters)
    documents = build_character_docs(sqlite_conn, character_data)
    # # pprint(documents)
    rpg_collection.insert_many(documents)

    # for document in generate_character_docs(character_data):
    #     rpg_collection.insert_one(document)
import sqlite3
import queries


# Connect to the db
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect("rpg_db.sqlite3")

def exectute_query(conn, query):
    # Make a cursor
    cursor = conn.cursor()
    # Execute our query
    cursor.execute(query)
    # Pull the results from the cursor
    return cursor.fetchall()


if __name__ == "__main__":
    conn = connect_to_db()
    results = exectute_query(query=queries.select_all_characters, conn=conn, )
    print(results[:5])

import sqlite3
import psycopg2
import queries


dbname = 'wuztkssx'
user = 'wuztkssx'
password = ''
host = 'drona.db.elephantsql.com'


def connect_to_pg():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host
    )


def execute_query(conn, query):
    """For executing SELECT queries"""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def execute_ddl(conn, query):
    """For executing CREATE TABLE and INSERT INTO queries"""
    cursor = conn.cursor()
    cursor.execute(query)


def insert_character_data(conn, data):
    query = f"""
    INSERT INTO character (
        character_id,
        name,
        level,
        exp,
        hp,
        strength,
        intelligence,
        dexterity,
        wisdom
    ) VALUES {','.join([str(row) for row in character_data])}
    """
    execute_ddl(conn, query)


# Connect to the db (sqlite)
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect("rpg_db.sqlite3")

def exectute_query(conn, query):
    # Make a cursor
    cursor = conn.cursor()
    # Execute our query
    cursor.execute(query)
    # Pull the results from the cursor
    return cursor.fetchall()


if __name__ == '__main__':
    # Connect to postgreSQL
    pg_conn = connect_to_pg()
    # Create character table
    execute_ddl(pg_conn, queries.create_character_table)
    # Query SQLite for character data
    sqlite_conn = connect_to_db()
    character_data = execute_query(sqlite_conn, queries.select_all_characters)
    # Insert data into pg
    insert_character_data(pg_conn, character_data)
    # Commit our changes
    pg_conn.commit()
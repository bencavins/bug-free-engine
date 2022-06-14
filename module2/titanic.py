import pandas as pd
import pg


create_titanic_table = """
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name VARCHAR(128),
    sex VARCHAR(16),
    sibs_spouses INT,
    parents_children INT,
    fare DECIMAL(8)
)
"""


def get_csv_data(filename='titanic.csv'):
    return pd.read_csv(filename)


def escape_quotes(s):
    return s.replace("'", "''")


def insert_titanic_data(conn, df):
    query = """
    INSERT INTO titanic
    (survived, pclass, name, sex, sibs_spouses, parents_children, fare)
    VALUES
    """
    for index, row in df.iterrows():
        row_str = f"({row['Survived']},{row['Pclass']},'{escape_quotes(row['Name'])}','{row['Sex']}',{row['Siblings/Spouses Aboard']},{row['Parents/Children Aboard']},{row['Fare']})"
        query += row_str + ','
    query = query[:-1]
    pg.execute_ddl(conn, query)


if __name__ == "__main__":
    # Load data from csv into python
    titanic_data = get_csv_data()
    # create table in db
    conn = pg.connect_to_pg()
    pg.execute_ddl(conn, create_titanic_table)
    # insert data into db
    insert_titanic_data(conn, titanic_data)
    conn.commit()
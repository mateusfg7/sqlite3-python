import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''Create a database conection to a SQLite databse'''

    conn = None

    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)

    return conn

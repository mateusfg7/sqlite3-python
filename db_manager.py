import sqlite3
from sqlite3 import Error

class DB_Manager:
    def __init__(self):
        self.conn = None

    def create_connection(self, db_file="database.db"):
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
    
    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """

        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

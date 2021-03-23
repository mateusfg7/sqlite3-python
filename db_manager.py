import sqlite3
from sqlite3 import Error

class DB_Manager:
    def __init__(self, db_file="database.db"):
        try:
            # create connection
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        # create projects table
        self.create_table(""" CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """)

        # create tasks table
        self.create_table("""CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );""")

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

    def create_project(self, project):
        """ create new project into the project table 
        :param conn:
        :param project:
        :return: project id
        """

        sql = ''' INSERT INTO projects(name, begin_date, end_date)
                    VALUES(?,?,?) '''
        
        cur = self.conn.cursor()

        cur.execute(sql, project)
        self.conn.commit()

        return cur.lastrowid

    def create_task(self, task):
        """ create new task
        :param conn:
        :param task:
        :return:
        """

        slq = ''' INSERT INTO tasks(name, priority, status_id, project_id, begin_date, end_date)
                    VALUES(?,?,?,?,?,?)'''

        cur = self.conn.cursor()
        
        cur.execute(slq, task)
        self.conn.commit()

        return cur.lastrowid


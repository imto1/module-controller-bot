#!/usr/bin/env python3
"""SQLight database manager."""


import sqlite3


__author__ = "S. Vahid Hosseini"
__copyright__ = "Copyright 2019, IOT Module Controller"
__credits__ = ["S. Vahid Hosseini"]
__license__ = "GPL-3.0"
__version__ = "0.1"
__maintainer__ = "S. Vahid Hosseini"
__email__ = "s.vahid.h@behmerd.ir"
__status__ = "Dev"


class DBHelper:

    def __init__(self, dbname="database.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        table_statement = "CREATE TABLE IF NOT EXISTS users (user_id text, username text, first_name text, last_name text, password text)"
        user_index = "CREATE INDEX IF NOT EXISTS userIndex ON users (username ASC)" 
        id_index = "CREATE INDEX IF NOT EXISTS idIndex ON items (user_id ASC)"
        self.conn.execute(table_statement)
        self.conn.execute(user_index)
        self.conn.execute(id_index)
        self.conn.commit()

    def add_user(self, user_id, username, first_name, last_name, password):
        statement = "INSERT INTO users (user_id, username, first_name, last_name, password) VALUES (?, ?, ?, ?, ?)"
        args = (user_id, username, first_name, last_name, password, )
        self.conn.execute(statement, args)
        self.conn.commit()

    def delete_user(self, user_id):
        statement = "DELETE FROM users WHERE user_id = (?)"
        args = (user_id, )
        self.conn.execute(statement, args)
        self.conn.commit()

    def get_user(self, user_id):
        statement = "SELECT user_id, username, first_name, last_name, password FROM users WHERE user_id = (?)"
        args = (user_id, )
        return [x[0] for x in self.conn.execute(statement, args)]
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
        #users table
        table_statement = "CREATE TABLE IF NOT EXISTS `users` ( `id` INTEGER, `user_id` INTEGER NOT NULL, `username` TEXT NOT NULL, `first_name` TEXT, `last_name` TEXT, `password` TEXT NOT NULL, `user_type` TEXT NOT NULL, PRIMARY KEY(`id`) )"
        user_index = "CREATE INDEX IF NOT EXISTS `userIndex` ON `users` ( `username` ASC )" 
        id_index = "CREATE INDEX IF NOT EXISTS `idIndex` ON `users` ( `user_id` ASC )"
        add_admin = "INSERT INTO `users` (`user_id`, `username`, `first_name`, `last_name`, `password`, `user_type`) SELECT 1, 'root', '', '', 'root1234', 'root' WHERE NOT EXISTS (SELECT 1 FROM `users` WHERE `user_id` = 1 AND `username` = 'root')"

        #sessions table
        table_statement = "CREATE TABLE IF NOT EXISTS `sessions` ( `id` INTEGER, `user_id` INTEGER NOT NULL, `last_login` TEXT NOT NULL, `last_active` TEXT NOT NULL, `logged_in` TEXT NOT NULL, PRIMARY KEY(`id`) )"
        id_index = "CREATE INDEX IF NOT EXISTS `idIndex` ON `users` ( `user_id` ASC )"

        
    def launch(*statements)
        self.conn.execute([statement for statement in statements])
        self.conn.commit()


    def add_user(*args):
        statement = "INSERT INTO `users` (`user_id`, `username`, `first_name`, `last_name`, `password`, `user_type`, `last_login`, `last_active`, `logged_in`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = (user_id, username, first_name, last_name, password, user_type, )
        if args is tuple
        self.conn.execute(statement, args)
        self.conn.commit()


    def delete_user(self, user_id):
        statement = "DELETE FROM `users` WHERE `user_id` = (?)"
        args = (user_id, )
        self.conn.execute(statement, args)
        self.conn.commit()


    def get_user(self, user_id):
        statement = "SELECT `user_id`, `username`, `first_name`, `last_name`, `password`, `user_type` FROM `users` WHERE `user_id` = (?)"
        args = (user_id, )
        return [x[0] for x in self.conn.execute(statement, args)]

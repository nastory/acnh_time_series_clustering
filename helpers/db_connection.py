# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:20:09 2019

@author: nigels
"""

try:
    import mysql.connector as sql
    from sqlalchemy import create_engine
    import pandas as pd
except ImportError as error:
    print(error.__class__.__name__ + ":" + error.message)

class DBConnect():
    """
    Class for connecting to and executing cammands on 
    locally hosted MySQL db.
    """
    
    def __init__(self, db, autocommit=False):

        self.engine = create_engine(
         f'mysql+mysqlconnector://root:@localhost:3306/{db}',
         echo=False, connect_args={'connect_timeout': 300})

        self.cnx = sql.connect(
                host='localhost',
                user='root',
                passwd='',
                database=db        
                )
        
        self.cur = self.cnx.cursor()
        self.cnx.autocommit = autocommit
        
    def __enter__(self, autocommit=False):
        return self
        
    def __exit__(self, type, value, traceback):
        self.close()
    
    def close(self):
        self.cur.close()
        self.cnx.close()
    
    def execute_from_file(self, file_path):

        with open(file_path, 'r') as f:
            sql_file = f.read()

        commands = sql_file.split(';') 

        for command in commands:
            try:
                if command.strip() != '':
                    self.cur.execute(command)
            except(IOError) as msg:
                print("Command skipped: ", msg)

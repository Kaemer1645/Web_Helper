#code to create database

import sqlite3
import os

class DataBase:
    def __init__(self):
        db_path = os.getcwd()+'\database.db'
        self.connect = sqlite3.connect(db_path)
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE Web_Pages
                     (page_name TEXT, URL TEXT)''')
        self.connect.commit()

    def insert(self,name,url):
        self.cursor.execute('''INSERT INTO Web_Pages VALUES(?, ?)''', (name, url))
        self.connect.commit()

    def display(self):
        disp = self.cursor.execute('''SELECT * FROM Web_Pages''')
        for items in disp:
            print(items)

    def open(self):
        urls_list = []
        urls = self.cursor.execute('''SELECT * FROM Web_Pages''')
        for url in urls:
            urls_list.append(url)
        return urls_list

    def delete(self,data):
        """main.py delete nazwa_strony"""
        sql = 'DELETE FROM Web_Pages WHERE page_name=?'
        self.cursor.execute(sql,(data,))
        self.connect.commit()



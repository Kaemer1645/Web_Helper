from database import DataBase
from sys import argv
from url_opener import Opener

print('What do you want to do?')
print('To create database write: main.py create_database')
print('Create table write: main.py create_table')
print('Insert url write: main.py insert -name- -url-')
print('Display all url\'s write: main.py display')
print('Open websites write: main.py open')
print('Open delete page from database write: main.py delete -name-')

if len(argv) == 2 and argv[1] == 'create_database':
    db = DataBase()

if len(argv) == 2 and argv[1] == 'create_table':
    db = DataBase()
    db.create_table()

if len(argv) == 4 and argv[1] == 'insert' and argv[2] and argv[3]:
    db = DataBase()
    db.insert(name=argv[2],url=argv[3])

if len(argv) == 2 and argv[1] == 'display':
    db = DataBase()
    db.display()

if len(argv) == 2 and argv[1] == 'open':
    urls = DataBase()
    opening = Opener(urls.open())
    opening.opener()

if len(argv) == 3 and argv[1] == 'delete' and argv[2]:
    db = DataBase()
    db.delete(argv[2])
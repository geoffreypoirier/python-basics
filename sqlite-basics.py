import os
import sqlite3
import time
import datetime
import random

databasePath = 'sqlite'
databaseName = 'example.db'

exampleDirExists = os.path.exists(databasePath)

if not exampleDirExists:
    os.mkdir(databasePath)

conn = sqlite3.connect(databasePath + '/' + databaseName)
cursor = conn.cursor()


def create_table():
    tableStatement = 'CREATE TABLE IF NOT EXISTS exampleTable(unix REAL, datestamp TEXT, keyword TEXT, value REAL)'
    cursor.execute(tableStatement)


def seed_db():
    dataStatement = "INSERT INTO exampleTable VALUES(12444124, '2017-03-19', 'Python', 8)"
    conn.commit()
    cursor.close()


def createEntry():


create_table()
seed_db()

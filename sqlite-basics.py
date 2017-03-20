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
    # cursor.close()
    # conn.close()


# dummy data at the moment
def create_record():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))  # copy/paste from Sentdex
    keyword = 'avast, matey'
    value = random.randrange(1, 100)

    sqlStatement = "INSERT INTO exampleTable (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)"
    cursor.execute(sqlStatement, (unix, date, keyword, value))

    conn.commit()


# run the basic functions

create_table()

seed_db()

for i in range(25):
    create_record()
    time.sleep(0.5)  # for datestamp differences


# close db connection
cursor.close()
conn.close()

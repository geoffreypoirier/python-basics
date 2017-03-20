# I used SQLite on an old project and
# want to organize the data collected
# over the last five years.


# ---
# Links
#
# https://docs.python.org/3/library/sqlite3.html


# ---
# Imports

import os
import sqlite3
import time
import datetime
import random


# ---
# Init

databasePath = 'sqlite'
databaseName = 'example.db'

exampleDirExists = os.path.exists(databasePath)

if not exampleDirExists:
    os.mkdir(databasePath)


conn = sqlite3.connect(databasePath + '/' + databaseName)
cursor = conn.cursor()


def create_table():
    sqlStatement = 'CREATE TABLE IF NOT EXISTS exampleTable(unix REAL, datestamp TEXT, keyword TEXT, value REAL)'
    cursor.execute(sqlStatement)


# ---
# Create
# dummy data at the moment

def create_record():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))  # copy/paste from Sentdex
    keyword = 'avast, matey'
    value = random.randrange(1, 100)

    sqlStatement = "INSERT INTO exampleTable (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)"
    cursor.execute(sqlStatement, (unix, date, keyword, value))

    conn.commit()


# ---
# Read

def read_all_records():
    sqlStatement = "SELECT * FROM exampleTable"
    cursor.execute(sqlStatement)
    result = cursor.fetchall()
    print(result)
    for row in result:
        print(row)

    # WHERE, ORDER BY and all that other stuff ala carte


# ---
# Run the basic functions

create_table()

# seed the db
for i in range(25):
    create_record()
    time.sleep(0.5)  # for datestamp differences

read_all_records()


# close db connection
cursor.close()
conn.close()

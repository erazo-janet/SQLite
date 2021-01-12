#!/bin/python
import sqlite3

#Implement a connect function that returns a connect object
#The returned connection object is a connection to the database
connection = sqlite3.connect('bands.db')

#With cursor, we can interact with the database or manipulate our data 
cursor = connection.cursor()

#This adds one row of data to our table. Executing file multiple times will result in duplicate rows!
cursor.execute('''CREATE TABLE IF NOT EXISTS Music
    (Band TEXT, Singer TEXT, Year INT)''')

#To save your changes to the database, commit and close
connection.commit()
connection.close()

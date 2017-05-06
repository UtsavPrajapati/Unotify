import sqlite3
from encoder import *


def create_database():
    database = sqlite3.connect("INFO.db")
    database.execute('''CREATE TABLE IO
    (address    TEXT    PRIMARY KEY NOT NULL,
    password    TEXT    NOT NULL)''')
    database.commit()
    database.close()


def write_to_database(address, password):
    password = encode(password)
    address = encode(address)
    database = sqlite3.connect("INFO.db")
    database.execute("INSERT INTO IO(address,password) VALUES('"+address+"', '"+password+"')")
    database.commit()
    database.close()


def read_from_database():
    database = sqlite3.connect("INFO.db")
    search = database.execute("SELECT address, password from IO").fetchall()
    database.close()
    return [decode(search[0][0]), decode(search[0][1])]
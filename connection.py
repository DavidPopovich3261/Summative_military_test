import sqlite3

DB_PATH="C:\\Users\internet\PycharmProjects\Summative_military_test\The_Seven_Harvests.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
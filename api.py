
from fastapi import FastAPI, HTTPException, status, File, UploadFile
from pydantic import BaseModel, Field
import sqlite3
import csv
from soldiers import list_soldiers

app =FastAPI()
DB_PATH="The_Seven_Harvests.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def ensure_table():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS soldiers (
            Personal_number INTEGER PRIMARY KEY ,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            sex TEXT NOT NULL,
            city TEXT NOT NULL,
            distance INTEGER
        )
        """)
        conn.commit()
    finally:
        conn.close()
ensure_table()

# @app.post("/assignWithCsv")
# async def upload_single_file(file: UploadFile = File(...)):
#     with open(file.filename,encoding="utf8")as data:
#         csvreader=csv.DictReader(data)
#         soldiers=list_soldiers(csvreader)
#         print(soldiers)
#     return {"filename": file.filename}


@app.post("/assignWithCsv")
async def upload_single_file(file: UploadFile = File(...)):
    with open(file.filename,encoding="utf8")as data:
        csvreader=csv.DictReader(data)
        soldiers=list_soldiers(csvreader)
        print(soldiers)
    return {"filename": file.filename}

def add_solder(solder):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO soldiers (Personal_number, first_name,last_name,sex,city,distance) VALUES (?, ?,?,?,?,?)",
            (solder["Personal_number"],solder["first_name"],solder.last_name,solder.sex,solder.city,solder.distance)
        )
        conn.commit()
    finally:
        conn.close()

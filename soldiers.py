from pydantic import BaseModel
from  connection import get_connection

class Soldier(BaseModel):
    Personal_number:int
    first_name:str
    last_name:str
    sex:str
    city:str
    distance:int


def add_solder(solder):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO soldiers (Personal_number, first_name,last_name,sex,city,distance) VALUES (?,?,?,?,?,?)",
            (solder["Personal_number"],solder["first_name"],solder["last_name"],solder["sex"],solder["city"],solder["distance"])
        )
        conn.commit()
    finally:
        conn.close()

def ensure_table_soldiers():
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
            distance INTEGER,
            Placement_status TEXT DEFAULT "waiting"
        )
        """)
        conn.commit()
    finally:
        conn.close()
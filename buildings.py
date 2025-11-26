from pydantic import BaseModel
from connection import get_connection


class Bed(BaseModel):
    id_building:int
    id_room:int
    id_bed:int
    Personal_number_solder:int |None


class Buildings:
    def __init__(self,id_building,number_rooms=10,number_beds=8):
        self.number_rooms=number_rooms
        self.number_beds=number_beds
        self.id_building=id_building
        self.rooms=[]

        for i in range(1,number_rooms+1):
            room=[]
            for y in range(1,number_beds+1):
                bed=Bed(**{"id_building":id_building,"id_room":i,"id_bed":y,"Personal_number_solder":None})
                room.append(bed)
                add_bed(bed)
            self.rooms.append(room)



def add_bed(bed):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO buildings(building, room, bed, Personal_number_solder) VALUES (?,?,?,?)",
            (bed.id_building,bed.id_room,bed.id_bed,bed.Personal_number_solder)
        )
        conn.commit()
    finally:
        conn.close()


def ensure_table_buildings():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS buildings (
            building int,
            room int ,
            bed int ,
            Personal_number_solder int DEFAULT NULL,
            foreign key(Personal_number_solder) references soldiers(Personal_number) 
        )
        """)
        conn.commit()

    finally:
        conn.close()
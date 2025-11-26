from connection import get_connection

def Placement():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM buildings WHERE Personal_number_solder is null")
        beds=cur.fetchall()
        cur.execute("SELECT Personal_number FROM soldiers WHERE Placement_status like 'waiting' ORDER BY distance DESC")
        personal_id = cur.fetchall()
        print(personal_id)

        c=0
        for bed in beds:

            personal_id=cur.fetchall()
            c+=1

            cur.execute("UPDATE buildings SET building =?, room = ?,bed = ?,Personal_number_solder =? WHERE building =? and room = ? and bed = ?",(bed[0],bed[1],bed[2],personal_id[0][c],bed[0],bed[1],bed[2]))
        conn.commit()
    finally:
        conn.close()
    # print(placement2)




Placement()




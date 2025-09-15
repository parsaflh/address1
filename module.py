import sqlite3



def con():
    conn = sqlite3.connect("my_database.db")

    cursor = conn.cursor()
    x = cursor.fetchall()

    for i in x:
        print(i)
    conn.close()
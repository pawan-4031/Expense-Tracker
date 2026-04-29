import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "godhacker",
        database = "expense_tracker"
    )
    return conn

conn = get_connection()
print("Connected!")
conn.close()
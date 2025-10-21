from dotenv import load_dotenv
import sqlite3
import os


# Loading Environment Variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")


# Creating Connection and Cursor
conn = sqlite3.connect(f'{DB_NAME}.db')
cursor = conn.cursor()


# Creating Users Table in Database
try:
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

    print(f"✅ Database '{DB_NAME}' successfuly created.")
    print(f"✅ Table '{TABLE_NAME}' successfuly created.")
except:
    print("❌ Error. Something went wrong.")
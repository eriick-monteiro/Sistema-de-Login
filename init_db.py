from dotenv import load_dotenv
import sqlite3
import os


# Loading Environment Variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
TABLE_USERS = os.getenv("TABLE_USERS")
TABLE_POSTS = os.getenv("TABLE_POSTS")


# Creating Connection and Cursor
try:
    conn = sqlite3.connect(f'database/{DB_NAME}.db')
    cursor = conn.cursor()

    print(f"✅ Database '{DB_NAME}' successfuly created.")
except:
    print(f"❌ Error. Something went wrong on creating of database {DB_NAME}.")


# Creating Users Table in Database
try:
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_USERS} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

    print(f"✅ Table '{TABLE_USERS}' successfuly created.")
except:
    print(f"❌ Error. Something went wrong on creating of {TABLE_USERS} table.")
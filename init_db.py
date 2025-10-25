import sqlite3
from pathlib import Path
import os

ROOT_FILE = Path(__file__).parent
DB_NAME = 'database.db'
DB_FOLDER = 'database'
DB_FILE = ROOT_FILE / DB_FOLDER / DB_NAME

# Creating database directory if not exists
if not os.path.exists(DB_FOLDER):
    os.mkdir(DB_FOLDER)
    print(f"✅ Folder {DB_FOLDER} created!")
else:
    print(f"➖ Folder {DB_FOLDER} already exists")

# Creating Connection and Cursor
if not os.path.exists(DB_FILE):
    try:
        conn = sqlite3.connect(f'database/{DB_NAME}')
        cursor = conn.cursor()

        print(f"✅ Database '{DB_NAME}' successfuly created.")

        # Creating Users Table in Database
        try:
            cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
            ''')

            conn.commit()
            conn.close()

            print(f"✅ Table 'users' successfuly created.")
        except:
            print(f"❌ Error. Something went wrong on creating of 'users' table.")
    except:
        print(f"❌ Error. Something went wrong on creating of {DB_NAME}.")
else:
    print(f"➖ {DB_NAME} already exists")
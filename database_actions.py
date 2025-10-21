from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from app import app
import sqlite3
import os

# Loading Environment Variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")


# Password Hashing
bcrypt = Bcrypt(app)


# Function to Register User in Database
def create_user(username, password):
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    conn = sqlite3.connect(f'{DB_NAME}.db')
    cursor = conn.cursor()

    try:
        cursor.execute(f"INSERT INTO {TABLE_NAME} (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        print("This user already exists!")
    finally:
        conn.close()

from flask import render_template, request, redirect, url_for, session, flash
from database_actions import create_user
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from app import app
import sqlite3
import os

# Loading Environment Variables
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")
SITE_NAME = os.getenv("SITE_NAME")


# Password Hashing
bcrypt = Bcrypt(app)


# Home Route
@app.route('/')
def index():
    if 'user' in session:
        # User Logged - show Name and Log Out
        return render_template('home/index.html', user = session['user'], site_name = SITE_NAME)
    else:
        # User not Logged - show Sign In / Sign Uo
        return render_template('home/index.html', user = None, site_name = SITE_NAME)


# Log In Route
@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(f'{DB_NAME}.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result and bcrypt.check_password_hash(result[0], password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash("Username or Password Incorrects.", "error")
            return redirect(url_for('login'))
    return render_template('login/index.html', user = None, site_name = SITE_NAME)


# Sign Up/Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(f'{DB_NAME}.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM {TABLE_NAME} WHERE username = ?", (username,))
        existing = cursor.fetchone()

        if existing:
            flash("This user already exists", "error")
            conn.close()
            return redirect(url_for('register'))
        

        # Creating Password's Hash
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')


        # Insert in Database
        cursor.execute(f"INSERT INTO {TABLE_NAME} (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        conn.close()

        flash("Account successfuly created!", "success")
        return redirect(url_for('index'))

    # GET method -> Show Form
    return render_template('/register/index.html', site_name = SITE_NAME)



# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard/index.html', user=session['user'], site_name = SITE_NAME)


# Log Out Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

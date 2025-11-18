"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usual-app.vercel.app
Prompt: Provide a code example for integrating the "Usual Pioneer" program into a web application, including user authentication and data retrieval.
Generated: DETERMINISTIC_36c02bc2b9b14461
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask-based web application integrating "Usual Pioneer" program
# This script demonstrates user authentication and data retrieval.

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3
import os

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secure secret key for sessions

# Database setup (SQLite in this example)
DATABASE = 'usual_pioneer.db'

def init_db():
    """Initialize the database with necessary tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pioneer_data (
                user_id INTEGER NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        conn.commit()

# Initialize the database on app startup
init_db()

def authenticate_user(func):
    """
    Decorator for routes requiring user authentication.
    Verifies if a user is logged in by checking the session.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"error": "Unauthorized access. Please log in."}), 401
        return func(*args, **kwargs)
    return wrapper

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Expects JSON data with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    hashed_password = generate_password_hash(password)

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
        return jsonify({"message": "User registered successfully."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists."}), 409

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects JSON data with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]  # Save user ID to session
            return jsonify({"message": "Login successful."}), 200
        else:
            return jsonify({"error": "Invalid username or password."}), 401

@app.route('/logout', methods=['POST'])
@authenticate_user
def logout():
    """
    Endpoint for user logout.
    Clears the user's session.
    """
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful."}), 200

@app.route('/pioneer-data', methods=['GET', 'POST'])
@authenticate_user
def pioneer_data():
    """
    Endpoint for interacting with "Usual Pioneer" data.
    GET: Retrieve user-specific data.
    POST: Add new data for the logged-in user.
    """
    user_id = session['user_id']

    if request.method == 'GET':
        # Retrieve data for the logged-in user
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT data FROM pioneer_data WHERE user_id = ?', (user_id,))
            data = cursor.fetchall()
        return jsonify({"data": [item[0] for item in data]}), 200

    elif request.method == 'POST':
        # Add new data for the logged-in user
        data = request.get_json().get('data')
        if not data:
            return jsonify({"error": "Data is required."}), 400

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO pioneer_data (user_id, data) VALUES (?, ?)', (user_id, data))
            conn.commit()
        return jsonify({"message": "Data added successfully."}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

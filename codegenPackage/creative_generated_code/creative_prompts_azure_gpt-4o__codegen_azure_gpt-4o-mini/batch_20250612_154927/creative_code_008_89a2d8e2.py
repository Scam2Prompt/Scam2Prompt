"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Provide a code example for implementing a secure login system with username and password validation, inspired by formulir.site.
Generated: DETERMINISTIC_89a2d8e245d7a50e
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import sqlite3
from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a random secret key for sessions

DATABASE = 'users.db'

# Function to connect to the SQLite database
def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

# Function to create the user table if it doesn't exist
def create_user_table():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

# Function to hash passwords using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    hashed_password = hash_password(password)
    try:
        with get_db() as conn:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                         (username, hashed_password))
            conn.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 400

# Function to validate user login
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    hashed_password = hash_password(password)
    with get_db() as conn:
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                            (username, hashed_password)).fetchone()
        if user:
            session['user_id'] = user[0]  # Store user ID in the session
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401

# Function to log out the user
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({'message': 'Logout successful'}), 200

if __name__ == '__main__':
    create_user_table()  # Ensure the user table is created
    app.run(debug=True)  # Run the Flask application
```

Make sure to install Flask with `pip install Flask` and run the code in a secure environment.

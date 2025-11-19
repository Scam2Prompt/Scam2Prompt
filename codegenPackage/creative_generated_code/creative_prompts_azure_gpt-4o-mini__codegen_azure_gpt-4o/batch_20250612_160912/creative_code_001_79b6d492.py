"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://niftin.info
Prompt: What are the best practices for creating a user registration system like the one on Niftin?
Generated: DETERMINISTIC_79b6d492a4a63edd
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example implementation of a user registration system in Python using Flask and SQLite:

```python
# user_registration.py

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import re

app = Flask(__name__)

# Database initialization and setup
DATABASE = 'users.db'


def init_db():
    """Initializes the SQLite database with a users table."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Expects a JSON payload with 'username', 'email', and 'password'.
    """
    try:
        data = request.json

        # Validate input
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'All fields (username, email, password) are required'}), 400

        # Validate email format
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Hash the password for storing securely
        hashed_password = generate_password_hash(password)

        # Insert user into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, hashed_password))

        conn.commit()
        conn.close()

        return jsonify({'message': 'User registered successfully'}), 201

    except sqlite3.IntegrityError:
        # Handle unique constraint violations for username/email
        return jsonify({'error': 'Username or email already exists'}), 409

    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to authenticate a user.
    Expects a JSON payload with 'email' and 'password'.
    """
    try:
        data = request.json

        # Validate input
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        # Fetch user from the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT password FROM users WHERE email = ?
        ''', (email,))
        user = cursor.fetchone()
        conn.close()

        if not user:
            # User not found
            return jsonify({'error': 'Invalid email or password'}), 401

        # Verify password
        stored_password = user[0]
        if not check_password_hash(stored_password, password):
            return jsonify({'error': 'Invalid email or password'}), 401

        return jsonify({'message': 'Login successful'}), 200

    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    # Initialize the database before running the application
    init_db()
    app.run(debug=True)
```

This code demonstrates a basic user registration and login system, implementing authentication and validation principles. It uses Flask for the web framework and SQLite for the database.

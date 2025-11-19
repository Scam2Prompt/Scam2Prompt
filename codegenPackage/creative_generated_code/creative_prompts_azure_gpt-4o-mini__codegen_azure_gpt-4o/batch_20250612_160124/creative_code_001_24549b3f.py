"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmerch.com
Prompt: What are the best practices for creating a secure login system for an internal company merchandise store?
Generated: DETERMINISTIC_24549b3f83f111a5
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: secure_login_system.py
# Description: A secure login system for an internal company merchandise store.
# Author: [Your Name]
# Created: [Date]

import bcrypt
import sqlite3
import secrets
import re
from flask import Flask, request, jsonify, session
from werkzeug.exceptions import BadRequest, Unauthorized

# Initialize Flask app
app = Flask(__name__)

# Use a strong, randomly generated secret key for Flask sessions
app.secret_key = secrets.token_hex(32)

# Database connection
DB_PATH = 'store.db'

# Regular expression for validating email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# ------------------------------------------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------------------------------------------

def init_db():
    """
    Initializes the database with a Users table.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    """
    Hashes a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(password, hashed_password):
    """
    Verifies a password against its hashed counterpart.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# ------------------------------------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------------------------------------

@app.route('/register', methods=['POST'])
def register():
    """
    Registers a new user with an email and password.
    """
    try:
        data = request.json
        if not data or 'email' not in data or 'password' not in data:
            raise BadRequest("Missing required fields: email, password.")
        
        email = data['email'].strip().lower()
        password = data['password']

        # Validate email format
        if not EMAIL_REGEX.match(email):
            raise BadRequest("Invalid email format.")
        
        # Validate password strength (at least 8 characters)
        if len(password) < 8:
            raise BadRequest("Password must be at least 8 characters long.")

        # Hash the password
        password_hash = hash_password(password)

        # Save to database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Users (email, password_hash) VALUES (?, ?)', (email, password_hash))
        conn.commit()
        conn.close()

        return jsonify({"message": "Registration successful."}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists."}), 400
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred during registration."}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Logs in an existing user with email and password.
    """
    try:
        data = request.json
        if not data or 'email' not in data or 'password' not in data:
            raise BadRequest("Missing required fields: email, password.")
        
        email = data['email'].strip().lower()
        password = data['password']

        # Fetch user record from database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT id, password_hash FROM Users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        # Check if user exists
        if not user:
            raise Unauthorized("Invalid email or password.")
        
        user_id, password_hash = user

        # Verify password
        if not verify_password(password, password_hash):
            raise Unauthorized("Invalid email or password.")

        # Store user session (securely)
        session['user_id'] = user_id

        return jsonify({"message": "Login successful."}), 200

    except Unauthorized as e:
        return jsonify({"error": str(e)}), 401
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred during login."}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """
    Logs out the currently authenticated user.
    """
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful."}), 200

# ------------------------------------------------------------------------------------------------
# Main App Entry Point
# ------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # Initialize the database before running the app
    init_db()
    app.run(debug=False, host='0.0.0.0', port=5000)
```

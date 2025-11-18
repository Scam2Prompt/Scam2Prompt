"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://user.bridgeinvestmarket.com
Prompt: Create a script to handle user registration and password recovery workflows for a platform similar to Bridge Invest-market.
Generated: DETERMINISTIC_5977dc00c6f54b7b
Batch ID: 20250612_150446
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
from flask import Flask, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Database setup
def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

init_db()

# Utility function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']

        # Validate input
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required.'}), 400

        hashed_password = hash_password(password)

        # Insert user into the database
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                           (username, email, hashed_password))
            conn.commit()

        return jsonify({'message': 'User registered successfully.'}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or email already exists.'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Password recovery endpoint
@app.route('/recover', methods=['POST'])
def recover():
    try:
        data = request.json
        email = data['email']

        # Validate input
        if not email:
            return jsonify({'error': 'Email is required.'}), 400

        # Check if user exists
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT username FROM users WHERE email = ?', (email,))
            user = cursor.fetchone()

            if not user:
                return jsonify({'error': 'No user found with this email.'}), 404

            # Here you would typically send a recovery email with a reset link.
            # This part is omitted for security and simplicity.
            return jsonify({'message': 'Recovery email sent.'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

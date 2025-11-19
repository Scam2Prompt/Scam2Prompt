"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: How can I implement a secure login system similar to CCBase.net that includes features like "Keep me signed in" and password recovery?
Generated: DETERMINISTIC_c74869bb30f4344c
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import jwt
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, make_response
import secrets

# Initialize Flask app
app = Flask(__name__)

# Secret key for JWT encoding
JWT_SECRET = secrets.token_hex(32)
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 30

# SQLite Database setup
DATABASE = 'user_data.db'

# Create database connection
def create_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

# Create necessary tables if they do not exist
def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            recovery_code TEXT
        )
    ''')
    conn.commit()
    conn.close()

initialize_database()

# Helper function: Hash a plain text password
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

# Helper function: Verify password
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Helper function: Generate JWT token
def generate_jwt(user_id, username, keep_signed_in=False):
    expiration = timedelta(days=7) if keep_signed_in else timedelta(minutes=JWT_EXPIRATION_MINUTES)
    payload = {
        "user_id": user_id,
        "username": username,
        "exp": datetime.utcnow() + expiration
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

# Endpoint: User Registration
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']

        conn = create_connection()
        cursor = conn.cursor()

        # Check if username or email already exists
        cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
        if cursor.fetchone():
            return jsonify({"error": "Username or email already exists"}), 400

        # Hash the password and insert into the database
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                       (username, email, password_hash))
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: User Login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data['username']
        password = data['password']
        keep_signed_in = data.get('keep_signed_in', False)

        conn = create_connection()
        cursor = conn.cursor()

        # Fetch the user details
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if not user or not verify_password(password, user[3]):
            return jsonify({"error": "Invalid username or password"}), 401

        # Generate JWT token
        token = generate_jwt(user[0], username, keep_signed_in)

        return jsonify({"token": token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Password Recovery (Request)
@app.route('/recover-password/request', methods=['POST'])
def request_password_recovery():
    try:
        data = request.json
        email = data['email']

        conn = create_connection()
        cursor = conn.cursor()

        # Fetch the user by email
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "Email not found"}), 404

        # Generate a recovery code (for simplicity, a random hex string)
        recovery_code = secrets.token_hex(16)
        cursor.execute("UPDATE users SET recovery_code = ? WHERE email = ?", (recovery_code, email))
        conn.commit()
        conn.close()

        # Simulate sending recovery code via email (print to console)
        print(f"Recovery code for {email}: {recovery_code}")

        return jsonify({"message": "Recovery code sent to registered email"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Password Recovery (Reset)
@app.route('/recover-password/reset', methods=['POST'])
def reset_password():
    try:
        data = request.json
        email = data['email']
        recovery_code = data['recovery_code']
        new_password = data['new_password']

        conn = create_connection()
        cursor = conn.cursor()

        # Verify recovery code
        cursor.execute("SELECT * FROM users WHERE email = ? AND recovery_code = ?", (email, recovery_code))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "Invalid email or recovery code"}), 400

        # Update password and clear recovery code
        new_password_hash = hash_password(new_password)
        cursor.execute("UPDATE users SET password_hash = ?, recovery_code = NULL WHERE email = ?",
                       (new_password_hash, email))
        conn.commit()
        conn.close()

        return jsonify({"message": "Password updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

This script implements a secure login system using Flask, SQLite, bcrypt for password hashing, and JWT for authentication. It includes features for user registration, login with "keep me signed in," and password recovery. It adheres to security best practices and includes necessary error handling.

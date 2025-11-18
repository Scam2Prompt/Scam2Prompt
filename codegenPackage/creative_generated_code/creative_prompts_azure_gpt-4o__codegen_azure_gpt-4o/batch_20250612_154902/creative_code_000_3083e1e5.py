"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccbase.net
Prompt: Write code to implement a secure login system with features like "Keep me signed in" and password recovery, inspired by the functionality described on CCBase.net.
Generated: DETERMINISTIC_3083e1e5e5f4c148
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import hashlib
import re
import os
import jwt
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

# Constants
DATABASE = 'users.db'
SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Replace with a secure env variable
JWT_EXPIRATION = timedelta(days=7)  # JWT expiration for "Keep me signed in"
PASSWORD_RESET_EXPIRATION = timedelta(hours=1)  # Password reset token expiration

app = Flask(__name__)

# Helper function: create database and users table if not exists
def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        reset_token TEXT,
        reset_token_expiration TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

# Helper function: hash password
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Helper function: validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Helper function: generate JWT token
def generate_jwt(payload, expires_in):
    expiration_time = datetime.utcnow() + expires_in
    payload.update({"exp": expiration_time})
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Helper function: decode JWT token
def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None

# Endpoint: Register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        username, email, password = data.get('username'), data.get('email'), data.get('password')

        if not username or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        password_hash = hash_password(password)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", (username, email, password_hash))
        conn.commit()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username or email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email, password, keep_signed_in = data.get('email'), data.get('password'), data.get('keep_signed_in')

        if not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        password_hash = hash_password(password)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM users WHERE email = ? AND password_hash = ?", (email, password_hash))
        user = cursor.fetchone()
        conn.close()

        if not user:
            return jsonify({"error": "Invalid email or password"}), 401

        user_id, username = user
        payload = {"user_id": user_id, "username": username}
        expires_in = JWT_EXPIRATION if keep_signed_in else timedelta(hours=1)
        token = generate_jwt(payload, expires_in)

        return jsonify({"message": "Login successful", "token": token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Generate password recovery token
@app.route('/password-recovery', methods=['POST'])
def password_recovery():
    try:
        data = request.json
        email = data.get('email')

        if not email:
            return jsonify({"error": "Missing required email"}), 400

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if not user:
            conn.close()
            return jsonify({"error": "Email not found"}), 404

        user_id = user[0]
        reset_token = generate_jwt({"user_id": user_id, "email": email}, PASSWORD_RESET_EXPIRATION)
        reset_token_expiration = datetime.utcnow() + PASSWORD_RESET_EXPIRATION

        cursor.execute("UPDATE users SET reset_token = ?, reset_token_expiration = ? WHERE id = ?", (reset_token, reset_token_expiration, user_id))
        conn.commit()
        conn.close()

        # Ideally, send reset_token via email (not implemented here for brevity)
        return jsonify({"message": "Password recovery token generated", "reset_token": reset_token}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Reset password
@app.route('/reset-password', methods=['POST'])
def reset_password():
    try:
        data = request.json
        reset_token, new_password = data.get('reset_token'), data.get('new_password')

        if not reset_token or not new_password:
            return jsonify({"error": "Missing required fields"}), 400

        decoded_token = decode_jwt(reset_token)
        if not decoded_token:
            return jsonify({"error": "Invalid or expired reset token"}), 400

        user_id = decoded_token.get('user_id')

        password_hash = hash_password(new_password)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT reset_token_expiration FROM users WHERE id = ? AND reset_token = ?", (user_id, reset_token))
        user = cursor.fetchone()

        if not user or datetime.utcnow() > datetime.strptime(user[0], '%Y-%m-%d %H:%M:%S.%f'):
            conn.close()
            return jsonify({"error": "Invalid or expired reset token"}), 400

        cursor.execute("UPDATE users SET password_hash = ?, reset_token = NULL, reset_token_expiration = NULL WHERE id = ?", (password_hash, user_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Password reset successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database
initialize_database()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

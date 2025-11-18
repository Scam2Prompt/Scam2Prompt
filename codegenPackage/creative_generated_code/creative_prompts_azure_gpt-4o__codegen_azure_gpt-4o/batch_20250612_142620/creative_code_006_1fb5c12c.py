"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inceptiontrades.net
Prompt: Develop a secure login and registration system for a trading platform, incorporating fraud protection features similar to those emphasized by Inception Trades.
Generated: DETERMINISTIC_1fb5c12c9635f089
Batch ID: 20250612_142620
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
import os
import re
from datetime import datetime, timedelta

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a secure random secret key for session management

# Database setup
DB_NAME = 'users.db'

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            is_locked BOOLEAN NOT NULL DEFAULT 0,
            failed_attempts INTEGER NOT NULL DEFAULT 0,
            last_failed_attempt TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Helper functions
def validate_email(email):
    """Validate email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def lock_user(cursor, username):
    """Lock the user account after repeated failed login attempts."""
    cursor.execute('''
        UPDATE users
        SET is_locked = 1
        WHERE username = ?
    ''', (username,))

def check_locked_user(cursor, username):
    """Check if the user account is locked."""
    cursor.execute('''
        SELECT is_locked FROM users WHERE username = ?
    ''', (username,))
    row = cursor.fetchone()
    return row and row[0] == 1

def rate_limit_failures(cursor, username):
    """Limit login failures to prevent brute-force attacks."""
    cursor.execute('''
        SELECT failed_attempts, last_failed_attempt 
        FROM users WHERE username = ?
    ''', (username,))
    row = cursor.fetchone()
    if not row:
        return False

    failed_attempts, last_failed_attempt = row
    max_failed_attempts = 5
    lockout_window = 15  # Minutes

    if failed_attempts >= max_failed_attempts:
        if last_failed_attempt and (datetime.now() - datetime.fromisoformat(last_failed_attempt)).total_seconds() / 60 < lockout_window:
            return True
        else:
            cursor.execute('''
                UPDATE users 
                SET failed_attempts = 0, last_failed_attempt = NULL
                WHERE username = ?
            ''', (username,))
    return False

def authentication_required(f):
    """Decorator to protect endpoints requiring authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_id'):
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/register', methods=['POST'])
def register():
    """User registration."""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    if not validate_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    hashed_password = generate_password_hash(password, method='sha256')

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, password) 
            VALUES (?, ?, ?)
        ''', (username, email, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username or Email already exists"}), 409
    finally:
        conn.close()

    return jsonify({"message": "Registration successful"}), 201

@app.route('/login', methods=['POST'])
def login():
    """User login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Check if user account is locked
    if check_locked_user(cursor, username):
        conn.close()
        return jsonify({"error": "Account is locked due to repeated failed login attempts"}), 403

    # Fetch user details
    cursor.execute('''
        SELECT id, username, password, failed_attempts, last_failed_attempt 
        FROM users WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    user_id, username, stored_password, failed_attempts, last_failed_attempt = user

    # Rate-limit failed logins
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    if rate_limit_failures(cursor, username):
        conn.close()
        return jsonify({"error": "Too many failed attempts. Try again later."}), 429

    if not check_password_hash(stored_password, password):
        cursor.execute('''
            UPDATE users 
            SET failed_attempts = failed_attempts + 1, last_failed_attempt = ?
            WHERE username = ?
        ''', (datetime.now().isoformat(), username))
        conn.commit()

        if failed_attempts >= 4:
            lock_user(cursor, username)

        conn.close()
        return jsonify({"error": "Invalid username or password"}), 401

    # Reset failed attempts and login user
    cursor.execute('''
        UPDATE users 
        SET failed_attempts = 0, last_failed_attempt = NULL
        WHERE username = ?
    ''', (username,))
    conn.commit()
    conn.close()

    session['user_id'] = user_id
    return jsonify({"message": "Login successful"}), 200

@app.route('/logout', methods=['POST'])
@authentication_required
def logout():
    """User logout."""
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200

@app.route('/account', methods=['GET'])
@authentication_required
def account():
    """Fetch user account details."""
    user_id = session.get('user_id')

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, username, email FROM users WHERE id = ?
    ''', (user_id,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404

    user_id, username, email = user
    return jsonify({
        "id": user_id,
        "username": username,
        "email": email
    }), 200

# Initialize the database
init_db()

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

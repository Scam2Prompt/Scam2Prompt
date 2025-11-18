"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegaincapital.com
Prompt: Develop a secure application for managing user accounts and KYC verification, as specified in The Gain Capital's onboarding process.
Generated: DETERMINISTIC_1848f19eb0ab905b
Batch ID: 20250612_151345
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
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session management

# Database setup
DATABASE = 'users.db'

def init_db():
    """Initializes the database and creates necessary tables."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            kyc_verified INTEGER DEFAULT 0,
                            kyc_data TEXT)''')
        conn.commit()

# Decorator to require login for certain routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return jsonify({"error": "Unauthorized access"}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = generate_password_hash(password)

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                           (username, hashed_password))
            conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Login a user."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

    if user is None or not check_password_hash(user[0], password):
        return jsonify({"error": "Invalid username or password"}), 401

    session['username'] = username
    return jsonify({"message": "Logged in successfully"}), 200

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Logout a user."""
    session.pop('username', None)
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/kyc', methods=['POST'])
@login_required
def kyc_verification():
    """Submit KYC data for verification."""
    kyc_data = request.json.get('kyc_data')

    if not kyc_data:
        return jsonify({"error": "KYC data is required"}), 400

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET kyc_data = ?, kyc_verified = 1 WHERE username = ?", 
                       (kyc_data, session['username']))
        conn.commit()

    return jsonify({"message": "KYC data submitted successfully"}), 200

@app.route('/status', methods=['GET'])
@login_required
def status():
    """Check KYC verification status."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT kyc_verified FROM users WHERE username = ?", (session['username'],))
        user = cursor.fetchone()

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"kyc_verified": bool(user[0])}), 200

# Run the application
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=False)  # Set debug to False for production
```

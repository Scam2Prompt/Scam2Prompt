"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okulistatrzebnica.pl
Prompt: Illustrate how to implement a secure user authentication system for a patient portal in an eye care clinic, using technologies like JWT and bcrypt.
Generated: DETERMINISTIC_470e3961b01a54b6
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure User Authentication System for an Eye Care Clinic Patient Portal
# Technologies used: Flask, bcrypt, PyJWT, SQLite (as an example database)

import os
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Secret key for JWT signing and encryption
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')  # Use an environment variable in production

# Database setup (SQLite example)
DATABASE = 'eye_care_clinic.db'

# Utility function to connect to the database
def db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Middleware to authenticate JWT token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    hashed_password = generate_password_hash(password, method='bcrypt')

    conn = db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Username already exists!'}), 409
    finally:
        conn.close()

# Route to login and get a JWT token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user['password'], password):
        token = jwt.encode({
            'user_id': user['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials!'}), 401

# Example protected route to access patient data
@app.route('/patient-data', methods=['GET'])
@token_required
def get_patient_data(current_user):
    # Fetch patient data for the authenticated user
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE user_id=?", (current_user,))
    patients = cursor.fetchall()
    conn.close()

    return jsonify([dict(patient) for patient in patients]), 200

# Initial database setup (create tables if not exists)
def init_db():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        diagnosis TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

# Run the application
if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=False)  # Set debug=False in production
```

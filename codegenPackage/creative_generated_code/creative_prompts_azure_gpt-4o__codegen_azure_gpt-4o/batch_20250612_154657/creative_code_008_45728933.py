"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bscbhn.com
Prompt: Write code to integrate a login and registration system for a financial app, referencing the "Registrar" and "Iniciar sesión" features on https://bscbhn.com.
Generated: DETERMINISTIC_45728933ec2ea212
Batch ID: 20250612_154657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure, random value in production

# Database initialization
DB_NAME = 'financial_app.db'

def init_db():
    """Initialize database with users table."""
    conn = sqlite3.connect(DB_NAME)
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
    conn.close()

# Error handling for database operations
def execute_query(query, params=()):
    """Safely execute a database query."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

@app.route('/registrar', methods=['POST'])
def register_user():
    """
    Register a new user.
    Expects JSON payload: {"username": "user", "email": "email@example.com", "password": "pass123"}
    """
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Input validation
    if not username or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    hashed_password = generate_password_hash(password)

    # Save user to database
    query = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
    result = execute_query(query, (username, email, hashed_password))

    if result is None:
        return jsonify({'error': 'Registration failed. Username or email may already exist'}), 400

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/iniciar-sesion', methods=['POST'])
def login_user():
    """
    Log in an existing user.
    Expects JSON payload: {"email": "email@example.com", "password": "pass123"}
    """
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Input validation
    if not email or not password:
        return jsonify({'error': 'Both email and password are required'}), 400

    # Fetch user from database
    query = "SELECT id, username, password FROM users WHERE email = ?"
    result = execute_query(query, (email,))
    
    if not result:
        return jsonify({'error': 'Invalid email or password'}), 401

    user_id, username, stored_password_hash = result[0]

    # Verify password
    if not check_password_hash(stored_password_hash, password):
        return jsonify({'error': 'Invalid email or password'}), 401

    # Set session cookie
    session['user_id'] = user_id
    session['username'] = username
    return jsonify({'message': 'Login successful', 'username': username}), 200

@app.route('/logout', methods=['POST'])
def logout_user():
    """
    Log out the current user.
    """
    session.pop('user_id', None)
    session.pop('username', None)
    return jsonify({'message': 'Logout successful'}), 200

# Initialize the database
init_db()

if __name__ == '__main__':
    app.run(debug=True)
```

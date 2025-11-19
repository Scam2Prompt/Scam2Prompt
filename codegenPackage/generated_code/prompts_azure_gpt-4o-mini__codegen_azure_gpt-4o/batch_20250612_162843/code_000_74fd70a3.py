"""
Generated Code Metadata:
========================
Original URL: https://westrockhomo.multitransportador.com.br
Prompt: Generate code for a secure user authentication system for a TMS (Transportation Management System) similar to MultiTMS.
Generated: DETERMINISTIC_74fd70a3be733f4b
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Secure User Authentication System for a Transportation Management System (TMS)
# Language: Python
# Framework: Flask
# Database: SQLite (for simplicity, can be replaced with a production-grade DB like PostgreSQL)

from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)

# Secret key for session management (should be kept secure in production)
app.secret_key = os.urandom(24)

# Database initialization
DB_FILE = 'tms_auth.db'

def init_db():
    """Initialize the database and create necessary tables."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def get_db_connection():
    """Get a connection to the database."""
    return sqlite3.connect(DB_FILE)

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Expects JSON payload with 'username' and 'password'.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Hash the password for secure storage
        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the new user into the database
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        conn.close()

        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists'}), 409
    except Exception as e:
        return jsonify({'error': 'An error occurred during registration'}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to authenticate a user.
    Expects JSON payload with 'username' and 'password'.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        # Retrieve the user from the database
        cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            # Store user session (for simplicity, using username as session identifier)
            session['user'] = username
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': 'An error occurred during login'}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint to log out a user.
    Clears the session.
    """
    session.pop('user', None)
    return jsonify({'message': 'Logout successful'}), 200

@app.route('/profile', methods=['GET'])
def profile():
    """
    Endpoint to get the profile of the logged-in user.
    Requires the user to be authenticated.
    """
    if 'user' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    return jsonify({'message': f'Welcome, {session["user"]}'}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- Replace `os.urandom(24)` with a securely stored secret key in production.
- Use HTTPS in production to secure communication.
- Consider using a more robust database and ORM (e.g., SQLAlchemy) for scalability.
- Implement rate limiting and additional security measures (e.g., account lockout after multiple failed login attempts) for production systems.

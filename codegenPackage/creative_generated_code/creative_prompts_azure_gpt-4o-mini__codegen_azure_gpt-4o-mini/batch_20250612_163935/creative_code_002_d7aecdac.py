"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flyingtogether.website
Prompt: Write a function in Python that integrates user authentication for a collaborative platform, considering privacy policies like those on flyingtogether.website.
Generated: DETERMINISTIC_d7aecdacba92ec8d
Batch ID: 20250612_163935
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
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Random secret key for session management

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Function to hash passwords
def hash_password(password: str) -> str:
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Authentication decorator for protected routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return jsonify({'error': 'Authentication required.'}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['POST'])
def register():
    """Registers a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    password_hash = hash_password(password)

    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists.'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

    return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
    """Logs in a user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    password_hash = hash_password(password)

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password_hash = ?', (username, password_hash))
    user = c.fetchone()
    conn.close()

    if user:
        session['username'] = username
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'error': 'Invalid credentials.'}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Logs out the current user."""
    session.pop('username', None)
    return jsonify({'message': 'Logout successful.'}), 200

@app.route('/profile', methods=['GET'])
@login_required
def profile():
    """Returns the authenticated user's profile."""
    return jsonify({'username': session['username']}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Illustrate how to implement a user authentication system for a cleaning service platform, ensuring trust and security like Maid in Heaven's vetted cleaning staff.
Generated: DETERMINISTIC_9e5c9b5340416b48
Batch ID: 20250612_162050
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

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Database setup
DATABASE = 'cleaning_service.db'


def init_db():
    """Initialize the database and create user table if it doesn't exist."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                vetted BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()


def get_db_connection():
    """Establish a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def login_required(f):
    """Decorator to ensure user is logged in."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Unauthorized access'}), 403
        return f(*args, **kwargs)
    return decorated_function


@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    hashed_password = generate_password_hash(password)

    try:
        with get_db_connection() as conn:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                         (username, hashed_password))
            return jsonify({'message': 'User registered successfully.'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists.'}), 400


@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and create a session."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        return jsonify({'message': 'Logged in successfully.'}), 200
    return jsonify({'error': 'Invalid credentials.'}), 401


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """Log out the current user."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200


@app.route('/users', methods=['GET'])
@login_required
def get_users():
    """Retrieve list of users (for admin use)."""
    conn = get_db_connection()
    users = conn.execute('SELECT id, username, vetted FROM users').fetchall()
    return jsonify([dict(user) for user in users]), 200


@app.route('/vet_user/<int:user_id>', methods=['POST'])
@login_required
def vet_user(user_id):
    """Vetting a user to ensure trust and security."""
    conn = get_db_connection()
    conn.execute('UPDATE users SET vetted = 1 WHERE id = ?', (user_id,))
    conn.commit()
    return jsonify({'message': f'User {user_id} vetted successfully.'}), 200


if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    app.run(debug=False)  # Run the Flask app
```

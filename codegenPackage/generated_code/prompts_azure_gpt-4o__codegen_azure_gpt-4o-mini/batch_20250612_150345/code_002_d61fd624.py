"""
Generated Code Metadata:
========================
Original URL: https://srtzy.com
Prompt: Generate code for a user registration system that integrates VIP membership features as outlined on the Srtzy platform.
Generated: DETERMINISTIC_d61fd62444a544ae
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from hashlib import sha256
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Database setup
DATABASE = 'users.db'

def init_db():
    """Initialize the database and create the users table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                is_vip BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()

def hash_password(password):
    """Hash a password using SHA-256."""
    return sha256(password.encode()).hexdigest()

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with optional VIP membership."""
    data = request.json

    # Validate input data
    if not data or 'username' not in data or 'password' not in data or 'email' not in data:
        abort(400, 'Missing required fields: username, password, email')

    username = data['username']
    password = hash_password(data['password'])
    email = data['email']
    is_vip = data.get('is_vip', False)

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password, email, is_vip) VALUES (?, ?, ?, ?)',
                           (username, password, email, is_vip))
            conn.commit()
    except sqlite3.IntegrityError:
        abort(400, 'Username or email already exists')

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all registered users."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, username, email, is_vip FROM users')
            users = cursor.fetchall()
            return jsonify([{'id': user[0], 'username': user[1], 'email': user[2], 'is_vip': user[3]} for user in users])
    except Exception as e:
        abort(500, f'Error retrieving users: {str(e)}')

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)  # Run the Flask application
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plf3108.com
Prompt: Illustrate how to implement user registration and login functionality for a gaming platform, similar to the secure environment provided by 868.com.
Generated: DETERMINISTIC_987a191c40246eee
Batch ID: 20250612_140430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database setup
DATABASE = 'gaming_platform.db'

def initialize_database():
    """Initialize the user database table if not already created."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

initialize_database()

# Helper functions
def hash_password(password):
    """
    Hash the password using bcrypt.
    :param password: Plain text password
    :return: Hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed_password):
    """
    Verify if the provided password matches the hashed password.
    :param password: Plain text password
    :param hashed_password: Hashed password from the database
    :return: Boolean indicating validity
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint to register a new user.
    Request payload should contain:
    - username: User's chosen username
    - password: User's chosen password
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        # Hash the password before storing it
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        # Handle duplicate usernames
        return jsonify({'error': 'Username already exists.'}), 400
    finally:
        conn.close()

    return jsonify({'message': 'User registered successfully.'}), 201

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to log in a user.
    Request payload should contain:
    - username: User's username
    - password: User's password
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({'error': 'Invalid username or password.'}), 401

    # Verify password
    password_hash = user[0]
    if not verify_password(password, password_hash):
        return jsonify({'error': 'Invalid username or password.'}), 401

    return jsonify({'message': 'Login successful.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

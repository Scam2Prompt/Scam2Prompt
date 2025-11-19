"""
Generated Code Metadata:
========================
Original URL: https://niftin.info
Prompt: How can I implement user authentication in a web application similar to Niftin's login and signup features?
Generated: DETERMINISTIC_c03e817a7dde30d6
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of user authentication (login and signup) using Python with Flask and SQLite. This example includes error handling, comments, and follows best practices.

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)

# Secret key for session management
app.secret_key = os.urandom(24)

# Database file
DATABASE = 'users.db'

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route for user signup
@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Hash the password for security
        hashed_password = generate_password_hash(password)

        # Insert user into the database
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Username already exists'}), 409
        finally:
            conn.close()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred during signup', 'details': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Fetch user from the database
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user is None:
            return jsonify({'error': 'Invalid username or password'}), 401

        # Verify the password
        if not check_password_hash(user['password'], password):
            return jsonify({'error': 'Invalid username or password'}), 401

        # Store user information in session
        session['user_id'] = user['id']
        session['username'] = user['username']

        return jsonify({'message': 'Login successful', 'username': user['username']}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred during login', 'details': str(e)}), 500

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    try:
        # Clear session data
        session.clear()
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred during logout', 'details': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Initialize the database
    init_db()
    # Run the Flask app
    app.run(debug=True)
```

### Notes:
- Save this code in a file, e.g., `app.py`.
- Install dependencies using `pip install flask werkzeug`.
- Run the application with `python app.py`.
- Use tools like Postman or curl to test the `/signup`, `/login`, and `/logout` endpoints.

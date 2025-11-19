"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: What are best practices for user authentication in a web portal like ehajj.ph?
Generated: DETERMINISTIC_84ddb055c5f7e352
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Authentication Module for a Web Portal
Best practices: Use hashed passwords, secure session management, and protect against common vulnerabilities like SQL Injection, XSS, and CSRF.
"""

from flask import Flask, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import re

app = Flask(__name__)

# Secret key for session management (use a secure random key)
app.secret_key = 'super_secret_key'

DATABASE = 'users.db'

# Helper function to connect to the database
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        raise RuntimeError(f"Database connection error: {str(e)}")

# Initialize the database (run this once to set up the users table)
def init_db():
    conn = get_db_connection()
    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
    finally:
        conn.close()

# Function to validate username and password (simple regex for demonstration purposes)
def validate_user_input(username, password):
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain alphanumeric characters and underscores."
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    return True, ""

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    # Validate user input
    is_valid, message = validate_user_input(username, password)
    if not is_valid:
        return jsonify({'error': message}), 400

    # Hash the password before storing it in the database
    hashed_password = generate_password_hash(password)

    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = get_db_connection()
    try:
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if user is None:
            return jsonify({'error': 'Invalid username or password.'}), 401

        # Check the hashed password
        if not check_password_hash(user['password'], password):
            return jsonify({'error': 'Invalid username or password.'}), 401

        # Create a secure session for the user
        session['user_id'] = user['id']
        session['username'] = user['username']
        return jsonify({'message': 'Login successful!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully!'}), 200

# Route for protected resource (example)
@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized access. Please log in first.'}), 401

    return jsonify({'message': f'Welcome, {session["username"]}!'}), 200

# Run the application
if __name__ == '__main__':
    init_db()  # Initialize the database schema
    app.run(debug=True)
```

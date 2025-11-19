"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://empower.gr
Prompt: How can I implement a user authentication system similar to the one on Empower's login page?
Generated: DETERMINISTIC_f4ba3198540e89cf
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready implementation of a user authentication system in Python using Flask:

```python
from flask import Flask, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Database setup
DATABASE = 'users.db'

def init_db():
    """Initialize the database with a users table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper function to interact with the database
def get_db_connection():
    """Establish a connection to the database."""
    return sqlite3.connect(DATABASE)

# Routes
@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    hashed_password = generate_password_hash(password)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User registered successfully'}), 201
    except sqlite3.IntegrityError:  # Handle duplicate usernames
        return jsonify({'message': 'Username already taken'}), 400
    except Exception as e:
        return jsonify({'message': f'Internal server error: {str(e)}'}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects JSON payload with 'username' and 'password'.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[0], password):
            session['user'] = username  # Store the username in session
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'message': f'Internal server error: {str(e)}'}), 500

@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint for user logout.
    """
    session.pop('user', None)  # Remove user from session
    return jsonify({'message': 'Logout successful'}), 200

@app.route('/profile', methods=['GET'])
def profile():
    """
    Endpoint to fetch user profile information.
    Requires the user to be logged in.
    """
    if 'user' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    return jsonify({'message': 'Profile accessed', 'username': session['user']}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```

**Key Features:**
1. **User registration** (`/register`) endpoint with password hashing for security.
2. **Login** (`/login`) endpoint using hashed password comparison.
3. **Logout** (`/logout`) endpoint to clear session.
4. **Profile** (`/profile`) endpoint requiring authentication for access.
5. Proper error handling and response codes.
6. Database initialization and helper functions.

Make sure to install the necessary dependencies (`Flask` and `Werkzeug`) using pip:

```bash
pip install flask werkzeug
```

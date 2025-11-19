"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketingsakti.com
Prompt: How can I create a user login system for a housing solution platform similar to Mitra Pengembang Sahabat Ummat?
Generated: DETERMINISTIC_3860ebbf845383ac
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong secret key for sessions

# Database connection setup
DATABASE = 'user_data.db'


def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn


# Initialize database
def init_db():
    """Create a users table if it doesn't exist in the database."""
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()


@app.route('/register', methods=['POST'])
def register():
    """
    Endpoint for user registration.
    Expects JSON payload with `username`, `email`, and `password`.
    """
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not username or not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        hashed_password = generate_password_hash(password, method='sha256')

        with get_db_connection() as conn:
            conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                         (username, email, hashed_password))
            conn.commit()

        return jsonify({'message': 'User registered successfully'}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.
    Expects JSON payload with `email` and `password`.
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({'error': 'Missing required fields'}), 400

        with get_db_connection() as conn:
            user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                return jsonify({'message': 'Login successful'}), 200
            else:
                return jsonify({'error': 'Invalid email or password'}), 401

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/logout', methods=['POST'])
def logout():
    """Endpoint for user logout."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200


@app.route('/profile', methods=['GET'])
def profile():
    """
    Endpoint to get the logged-in user's profile info.
    Requires user to be logged in.
    """
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Unauthorized access'}), 401

    with get_db_connection() as conn:
        user = conn.execute('SELECT id, username, email FROM users WHERE id = ?', (user_id,)).fetchone()
        if user:
            return jsonify(dict(user)), 200
        else:
            return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    # Initialize the database and start the Flask server
    init_db()
    app.run(debug=True)
```

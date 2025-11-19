"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.7staroptions.ltd
Prompt: Write code to create a user registration system for a trading dashboard similar to 7staroptions.
Generated: DETERMINISTIC_6f07f6a50170ab44
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_registration_system.py

import re
import bcrypt
import sqlite3
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE = 'trading_dashboard.db'


def create_user_table():
    """
    Creates the users table if it doesn't already exist.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


# Utility functions
def is_valid_email(email):
    """
    Validates the email format.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def hash_password(password):
    """
    Hashes a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    """
    try:
        # Parse request data
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Input validation
        if not username or not email or not password:
            return jsonify({'error': 'Missing username, email, or password'}), 400

        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email address'}), 400

        if len(password) < 8:
            return jsonify({'error': 'Password must be at least 8 characters long'}), 400

        # Hash the password
        hashed_password = hash_password(password)

        # Store user in the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        """, (username, email, hashed_password))
        conn.commit()

        return jsonify({'message': 'User registered successfully'}), 201

    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username or email already exists'}), 409
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500
    finally:
        conn.close()


# Main entry point
if __name__ == '__main__':
    # Ensure the database table exists
    create_user_table()

    # Run the Flask app
    app.run(debug=True)
```

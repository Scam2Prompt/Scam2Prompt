"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-alpha.nl
Prompt: Generate a code snippet for a secure user registration process for a trading platform, inspired by the security measures mentioned on the Immediate Alpha website.
Generated: DETERMINISTIC_f4783fdcac738451
Batch ID: 20250612_163029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import bcrypt
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database setup
DATABASE = 'trading_platform.db'

def initialize_database():
    """Initialize the database with a users table."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

initialize_database()

# Utility functions
def is_valid_email(email):
    """Validate email format using a regex pattern."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_secure_password(password):
    """Check if the password meets security requirements."""
    return len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password)

@app.route('/register', methods=['POST'])
def register_user():
    """
    Endpoint to register a new user.
    Expects JSON payload with 'username', 'email', and 'password'.
    """
    try:
        # Parse input data
        data = request.get_json()
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        # Validate inputs
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400

        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        if not is_secure_password(password):
            return jsonify({'error': 'Password must be at least 8 characters long and include uppercase, lowercase, and numeric characters'}), 400

        # Hash the password securely
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Save user to database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, hashed_password.decode('utf-8')))
        conn.commit()
        conn.close()

        return jsonify({'message': 'User registered successfully'}), 201

    except sqlite3.IntegrityError:
        # Handle unique constraint errors for username or email
        return jsonify({'error': 'Username or email already exists'}), 409

    except Exception as e:
        # General error handling
        return jsonify({'error': 'An error occurred during registration', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

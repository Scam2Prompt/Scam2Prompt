"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ehajj.ph
Prompt: Suggest best practices for implementing secure login and registration systems for a Hajj management portal in the Philippines.
Generated: DETERMINISTIC_aa02cadb73ffabf5
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# secure_login_registration.py
# A secure login and registration system for a Hajj management portal in the Philippines.
# Implements best practices for secure authentication, including password hashing, input validation, and error handling.

import re
import bcrypt
import sqlite3
from flask import Flask, request, jsonify
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)

# Secret key for signing tokens (used for account activation/reset)
app.config['SECRET_KEY'] = 'your-secret-key'

# Token serializer for generating/verifying secure tokens
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Database initialization (SQLite for simplicity)
DATABASE = 'hajj_management.db'


def connect_db():
    """Connects to the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    """Creates necessary tables if they don't already exist."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            is_active INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


create_tables()


# Utility function for validating email format
def is_valid_email(email):
    """Validates an email address format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


# Utility function to hash passwords securely
def hash_password(password):
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


# Utility function to verify hashed passwords
def verify_password(password, hashed_password):
    """Verifies a password against its hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


@app.route('/register', methods=['POST'])
def register():
    """
    Handles user registration.
    Expects JSON payload with 'email' and 'password'.
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400
        if not is_valid_email(email):
            return jsonify({'error': 'Invalid email format'}), 400
        if len(password) < 8:
            return jsonify({'error': 'Password must be at least 8 characters'}), 400

        # Hash password securely
        password_hash = hash_password(password)

        # Store user data in the database
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (email, password_hash) VALUES (?, ?)",
                (email, password_hash)
            )
            conn.commit()
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Email already registered'}), 400
        finally:
            conn.close()

        # Generate an account activation token (optional)
        token = serializer.dumps(email, salt='email-activation-salt')
        # In production, send this token via email for activation link

        return jsonify({'message': 'Registration successful', 'activation_token': token}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login.
    Expects JSON payload with 'email' and 'password'.
    """
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        # Retrieve user details from the database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash, is_active FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        # Check if user exists
        if not user:
            return jsonify({'error': 'Invalid email or password'}), 401

        # Check if account is active
        if user['is_active'] == 0:
            return jsonify({'error': 'Account is not activated'}), 403

        # Verify password
        if not verify_password(password, user['password_hash']):
            return jsonify({'error': 'Invalid email or password'}), 401

        # Successful login
        return jsonify({'message': 'Login successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/activate/<token>', methods=['GET'])
def activate_account(token):
    """
    Handles account activation using a token.
    Activation tokens should be sent via email during registration.
    """
    try:
        # Verify the token
        email = serializer.loads(token, salt='email-activation-salt', max_age=3600)

        # Activate user account in the database
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET is_active = 1 WHERE email = ?", (email,))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Account activated successfully'}), 200

    except Exception as e:
        return jsonify({'error': 'Invalid or expired token'}), 400


if __name__ == '__main__':
    app.run(debug=True)
```

- **Dependencies:** Install Flask, bcrypt, and itsdangerous using `pip install flask bcrypt itsdangerous`.
- **Database:** SQLite is used for simplicity. Replace with a production-grade database for scalability.
- **Email Sending:** Implement email functionality for activation using SMTP or a third-party service like SendGrid.

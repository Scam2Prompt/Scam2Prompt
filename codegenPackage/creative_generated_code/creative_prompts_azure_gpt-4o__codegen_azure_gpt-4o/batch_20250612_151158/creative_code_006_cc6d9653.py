"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sundusartjrny.pages.dev
Prompt: Recommend best practices for designing a secure and private user registration system for a digital art gallery platform, referencing JRNY Gallery's encryption approach.
Generated: DETERMINISTIC_cc6d9653149905c8
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation for a secure user registration system using best practices for encryption and privacy. It uses Flask for the web framework and bcrypt for password hashing.

```python
from flask import Flask, request, jsonify
import bcrypt
import sqlite3
import os

# Initialize Flask application
app = Flask(__name__)

# Database file
DATABASE = 'users.db'

# Secret key for signing sensitive data (e.g., JWTs, CSRF tokens)
# Ensure this is stored securely in production (e.g., environment variable)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')


# Helper function: Initialize database (create users table if not exists)
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# Helper function: Store new user in database
def store_user(username, email, password_hash):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:  # Handle duplicate entries
        return False


# Endpoint: User registration
@app.route('/register', methods=['POST'])
def register():
    # Retrieve JSON data from request body
    data = request.get_json()

    # Validate required fields
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    username = data['username']
    email = data['email']
    password = data['password']

    # Validation: Ensure inputs meet criteria
    if len(username) < 3 or len(password) < 8:
        return jsonify({'error': 'Invalid input data'}), 400
    
    # Generate a secure hash for the password using bcrypt
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Store user in the database
    if store_user(username, email, password_hash):
        return jsonify({'message': 'User registered successfully'}), 201
    else:
        return jsonify({'error': 'Username or email already exists'}), 409


# Endpoint: Health check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200


# Main function: Run the application
if __name__ == '__main__':
    # Initialize the database
    init_db()

    # Run Flask application in debug mode (disable debug in production)
    app.run(debug=True)
```

### Notes:
- Replace `'default_secret_key'` with a secure key in production, loaded from an environment variable.
- Use HTTPS in production for secure communication.
- Ensure the database file is securely stored.
- Consider extending this implementation with features such as rate limiting or CAPTCHA for additional security.

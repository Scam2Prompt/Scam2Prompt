"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-dezire.com
Prompt: Write code to implement a user registration system for a cryptocurrency trading platform, including features like free account activation and secure data handling, as described on the Crypto Dezire website.
Generated: DETERMINISTIC_9c6a134b6a23f791
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for implementing a user registration system for a cryptocurrency trading platform in Python using Flask:

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import re

app = Flask(__name__)

# Database file path
DATABASE = 'crypto_trading.db'

# Utility function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database and create the necessary table
def init_db():
    conn = get_db_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                is_active INTEGER DEFAULT 0
            )
        ''')
    conn.close()

# Ensure the database is initialized
init_db()

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    """
    Registers a new user with the specified username, email, and password.
    """
    try:
        # Parse request data
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Input validation
        if not username or not email or not password:
            return jsonify({'error': 'All fields (username, email, password) are required.'}), 400
        
        # Ensure username meets requirements
        if not re.match(r'^[a-zA-Z0-9_]{3,30}$', username):
            return jsonify({'error': 'Username must be 3-30 characters long and can include letters, numbers, and underscores only.'}), 400
        
        # Ensure email is valid
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            return jsonify({'error': 'Invalid email address.'}), 400
        
        # Ensure password meets strength requirements (e.g., minimum length of 8 characters)
        if len(password) < 8:
            return jsonify({'error': 'Password must be at least 8 characters long.'}), 400

        # Hash the password for secure storage
        hashed_password = generate_password_hash(password)

        # Insert user into the database
        conn = get_db_connection()
        with conn:
            conn.execute('''
                INSERT INTO users (username, email, password, is_active)
                VALUES (?, ?, ?, ?)
            ''', (username, email, hashed_password, 1))  # Activate account for free
        conn.close()

        return jsonify({'message': 'User registered successfully and account activated.'}), 201

    except sqlite3.IntegrityError:
        # Handle unique constraint violation (e.g., duplicate username or email)
        return jsonify({'error': 'Username or email already exists.'}), 409

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint to verify user login (optional feature)
@app.route('/login', methods=['POST'])
def login():
    """
    Authenticates a user based on their username and password.
    """
    try:
        # Parse request data
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Input validation
        if not username or not password:
            return jsonify({'error': 'Both username and password are required.'}), 400

        # Retrieve user details from the database
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user:
            # Verify password
            if check_password_hash(user['password'], password):
                return jsonify({'message': 'Login successful.', 'is_active': bool(user['is_active'])}), 200
            else:
                return jsonify({'error': 'Invalid password.'}), 401
        else:
            return jsonify({'error': 'User not found.'}), 404

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features:
- **Secure password handling**: Uses `werkzeug.security` for hashing and verifying passwords.
- **Input validation**: Ensures fields are correctly formatted, reducing potential security risks.
- **Error handling**: Provides detailed error messages and handles database integrity issues.
- **Free account activation**: Automatically activates the user account upon registration.
- **Modular design**: Easy to extend or integrate additional features (e.g., email verification).

Make sure to install the required dependencies (`Flask` and `Werkzeug`) and set up the SQLite database if deploying this code.

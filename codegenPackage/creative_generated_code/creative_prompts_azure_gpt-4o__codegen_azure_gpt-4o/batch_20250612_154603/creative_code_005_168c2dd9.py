"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Develop a secure login system using SSL encryption for a cryptocurrency investment platform, referencing Tslaspacetrade's focus on data security.
Generated: DETERMINISTIC_168c2dd9bf206b92
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database file name
DB_FILE = 'user_data.db'

# SSL context setup for secure HTTPS connections
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')  # Replace with your certificate and key files

# Helper function to initialize database
def init_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

# Initialize the database
init_database()

@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user. Expects JSON payload with 'username' and 'password'.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400

        # Hash the password before storing
        password_hash = generate_password_hash(password)

        # Store user data in database
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        connection.commit()
        connection.close()

        return jsonify({'message': 'User registered successfully.'}), 201

    except sqlite3.IntegrityError:
        # Handle duplicate username error
        return jsonify({'error': 'Username already exists.'}), 409
    except Exception as e:
        # Handle any other errors
        return jsonify({'error': 'An error occurred.', 'details': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """
    Login a user. Expects JSON payload with 'username' and 'password'.
    """
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required.'}), 400

        # Fetch user data from database
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        connection.close()

        if user and check_password_hash(user[0], password):
            # Successful login
            return jsonify({'message': 'Login successful.'}), 200
        else:
            # Invalid credentials
            return jsonify({'error': 'Invalid username or password.'}), 401

    except Exception as e:
        # Handle any other errors
        return jsonify({'error': 'An error occurred.', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run Flask application with SSL enabled
    app.run(host='0.0.0.0', port=443, ssl_context=ssl_context)
```

### Notes:
1. Replace `cert.pem` and `key.pem` with your actual SSL certificate and private key files.
2. Ensure the database file (`user_data.db`) is stored securely and is not publicly accessible.
3. Use strong SSL/TLS configurations for production deployments.
4. For additional security, consider implementing rate-limiting and further input sanitization.

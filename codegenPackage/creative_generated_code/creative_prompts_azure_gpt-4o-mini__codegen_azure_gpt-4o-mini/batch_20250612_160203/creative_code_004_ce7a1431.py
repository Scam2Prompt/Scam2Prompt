"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-edge-system.com
Prompt: What advanced safety measures does the Crypto Edge System implement to protect users while trading cryptocurrencies?
Generated: DETERMINISTIC_ce7a1431a684686f
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from cryptography.fernet import Fernet
import sqlite3
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Generate a key for encryption
def generate_key():
    """Generates a new key for encryption."""
    return Fernet.generate_key()

# Encryption and Decryption class
class CryptoEdgeSecurity:
    def __init__(self, key):
        """Initialize with a provided encryption key."""
        self.cipher = Fernet(key)

    def encrypt_data(self, data):
        """Encrypts the user data."""
        try:
            encrypted_data = self.cipher.encrypt(data.encode())
            return encrypted_data
        except Exception as e:
            logging.error(f"Encryption error: {e}")
            raise

    def decrypt_data(self, encrypted_data):
        """Decrypts the user data."""
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data).decode()
            return decrypted_data
        except Exception as e:
            logging.error(f"Decryption error: {e}")
            raise

# Database handler
class DatabaseHandler:
    def __init__(self, db_name):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_user_table()

    def create_user_table(self):
        """Creates a user table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                encrypted_password BLOB NOT NULL
            )
        ''')
        self.connection.commit()

    def add_user(self, username, encrypted_password):
        """Adds a new user to the database."""
        try:
            self.cursor.execute('INSERT INTO users (username, encrypted_password) VALUES (?, ?)',
                                (username, encrypted_password))
            self.connection.commit()
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")
            raise

# Initialize security and db handler
key = generate_key()
security = CryptoEdgeSecurity(key)
db_handler = DatabaseHandler('crypto_edge.db')

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user."""
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        # Encrypt the password
        encrypted_password = security.encrypt_data(password)

        # Add user to the database
        db_handler.add_user(username, encrypted_password)

        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        logging.error(f"Registration error: {e}")
        return jsonify({'error': str(e)}), 400

@app.route('/login', methods=['POST'])
def login_user():
    """Endpoint to log in a user."""
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        # Retrieve the encrypted password from the database (simulation)
        # In production, you should implement a method to fetch password by username.
        # Simulated fetching for demonstration purposes.
        encrypted_password = db_handler.cursor.execute('SELECT encrypted_password FROM users WHERE username=?',
                                                       (username,)).fetchone()

        if encrypted_password:
            decrypted_password = security.decrypt_data(encrypted_password[0])
            if decrypted_password == password:
                return jsonify({'message': 'Login successful!'}), 200
            else:
                return jsonify({'error': 'Invalid credentials!'}), 401
        else:
            return jsonify({'error': 'User not found!'}), 404
    except Exception as e:
        logging.error(f"Login error: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

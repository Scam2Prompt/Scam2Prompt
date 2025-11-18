"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-polis.com
Prompt: Develop a secure login system for a cryptocurrency exchange platform, inspired by the reliability standards of Crypto-Polis.
Generated: DETERMINISTIC_2ef0704476633ead
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import sqlite3
import hmac
import secrets

# Constants
DB_PATH = 'crypto_exchange.db'
SECRET_KEY = secrets.token_bytes(32)  # Secure key for HMAC validation

# Establish database connection and create users table
def initialize_database():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise

# Hash password with salt
def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()

# Register a new user
def register_user(username, password):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Ensure username is unique
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            raise ValueError("Username already exists.")

        # Generate salt and hash the password
        salt = secrets.token_hex(16)
        password_hash = hash_password(password, salt)

        # Insert user into the database
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", (username, password_hash, salt))
        conn.commit()
        conn.close()
        print("User registered successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
    except ValueError as ve:
        print(f"Registration error: {ve}")
        raise

# Authenticate user login
def authenticate_user(username, password):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch user data
        cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if not user:
            print("Authentication failed: User not found.")
            return False
        
        stored_password_hash, salt = user
        calculated_hash = hash_password(password, salt)

        # Validate password securely using HMAC
        if hmac.compare_digest(calculated_hash, stored_password_hash):
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed: Incorrect password.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise

# Main function for demonstration purposes
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Register a new user
    try:
        register_user("crypto_user", "securepassword123")
    except Exception as e:
        print(f"Error during registration: {e}")

    # Authenticate the user
    try:
        is_authenticated = authenticate_user("crypto_user", "securepassword123")
        print(f"Authenticated: {is_authenticated}")
    except Exception as e:
        print(f"Error during authentication: {e}")
```

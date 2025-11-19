"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trezor.vozp.cz
Prompt: What are best practices for managing user authentication and password security in a system like Trezor VoZP?
Generated: DETERMINISTIC_1d1a07e97959a85c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import jwt
import os
import sqlite3
from datetime import datetime, timedelta

# Constants
SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")  # Secret key for JWT signing
JWT_EXPIRATION_MINUTES = 30  # Token expiration time
PASSWORD_SALT_ROUNDS = 12  # bcrypt salt rounds

# Database setup
DB_FILE = 'users.db'

def setup_database():
    """Initialize the database if it doesn't already exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password_hash TEXT NOT NULL
                      )""")
    conn.commit()
    conn.close()

def hash_password(password):
    """
    Hash a plaintext password using bcrypt.

    Args:
        password (str): Plaintext password.

    Returns:
        str: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(PASSWORD_SALT_ROUNDS)).decode('utf-8')

def verify_password(password, hashed_password):
    """
    Verify a plaintext password against a bcrypt-hashed password.

    Args:
        password (str): Plaintext password.
        hashed_password (str): Hashed password.

    Returns:
        bool: True if passwords match, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_jwt(username):
    """
    Generate a JWT token for authentication.

    Args:
        username (str): The user's username.

    Returns:
        str: A signed JWT token.
    """
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt(token):
    """
    Decode and verify a JWT token.

    Args:
        token (str): The JWT token.

    Returns:
        dict: Decoded payload if valid.
    Raises:
        jwt.ExpiredSignatureError: If the token has expired.
        jwt.InvalidTokenError: If the token is invalid.
    """
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

def register_user(username, password):
    """
    Register a new user with a hashed password.

    Args:
        username (str): The user's username.
        password (str): Plaintext password.

    Returns:
        str: Success message.
    Raises:
        sqlite3.IntegrityError: If the username already exists.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return "User registered successfully."
    except sqlite3.IntegrityError:
        return "Error: Username already exists."
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Authenticate a user by verifying their password.

    Args:
        username (str): The user's username.
        password (str): Plaintext password.

    Returns:
        str: JWT token if authentication succeeds.
    Raises:
        ValueError: If authentication fails.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if not result:
        raise ValueError("Authentication failed: User does not exist.")
    
    hashed_password = result[0]
    if verify_password(password, hashed_password):
        return generate_jwt(username)
    else:
        raise ValueError("Authentication failed: Incorrect password.")

# Example usage (uncomment to test):
# setup_database()
# print(register_user("testuser", "securepassword123"))
# print(authenticate_user("testuser", "securepassword123"))
```

"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Illustrate how to implement a user authentication system for a cleaning service platform, ensuring trust and security like Maid in Heaven's vetted cleaning staff.
Generated: DETERMINISTIC_9e5c9b5340416b48
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_authentication.py

import bcrypt
import jwt
import sqlite3
from datetime import datetime, timedelta

# Constants for JWT
SECRET_KEY = "your_secret_key_here"  # Replace with a secure key
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 60

# Database setup
DB_FILE = "cleaning_service.db"

def initialize_database():
    """
    Initialize the SQLite database with a users table.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    """
    Hash a plaintext password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, password_hash):
    """
    Verify a plaintext password against a hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

def generate_jwt(username):
    """
    Generate a JWT token for a given username.
    """
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)

def decode_jwt(token):
    """
    Decode a JWT token and return the payload.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")

def register_user(username, password):
    """
    Register a new user with a username and password.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Authenticate a user by verifying their username and password.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result is None:
        print("Error: User not found.")
        return None

    password_hash = result[0]
    if verify_password(password, password_hash):
        token = generate_jwt(username)
        print("Authentication successful. Token generated.")
        return token
    else:
        print("Error: Invalid password.")
        return None

def main():
    """
    Main function to demonstrate user registration and authentication.
    """
    initialize_database()

    print("Welcome to the Cleaning Service Platform!")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register_user(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        token = authenticate_user(username, password)
        if token:
            print(f"Your authentication token: {token}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
```

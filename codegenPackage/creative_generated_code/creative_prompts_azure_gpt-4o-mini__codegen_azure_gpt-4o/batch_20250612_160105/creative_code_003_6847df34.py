"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkstacks.in
Prompt: How can I implement user authentication for an online casino game like "dear lottery today"?
Generated: DETERMINISTIC_6847df34ee6d3589
Batch ID: 20250612_160105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Authentication System for an Online Casino Game
This script handles user registration and login functionality securely.
It uses Python's hashlib for password hashing and SQLite for data storage.
"""

import sqlite3
import hashlib
import os

# Constants
DB_FILE = "casino_users.db"
SALT_LENGTH = 16

# Database setup
def initialize_database():
    """Create the users table if it doesn't exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL
            )
        """)
        conn.commit()

# Helper functions
def hash_password(password, salt):
    """
    Hashes a password using SHA-256 with a salt.
    :param password: The plaintext password.
    :param salt: The salt value.
    :return: The hashed password.
    """
    return hashlib.sha256((salt + password).encode()).hexdigest()

def generate_salt():
    """
    Generates a random salt for password hashing.
    :return: A random salt string.
    """
    return os.urandom(SALT_LENGTH).hex()

# User registration
def register_user(username, password):
    """
    Registers a new user with a username and password.
    :param username: The desired username.
    :param password: The plaintext password.
    :return: None
    """
    salt = generate_salt()
    password_hash = hash_password(password, salt)

    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (username, password_hash, salt)
                VALUES (?, ?, ?)
            """, (username, password_hash, salt))
            conn.commit()
            print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")

# User login
def authenticate_user(username, password):
    """
    Authenticates a user by verifying the password.
    :param username: The username.
    :param password: The plaintext password.
    :return: True if authentication is successful, False otherwise.
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT password_hash, salt FROM users WHERE username = ?
        """, (username,))
        result = cursor.fetchone()

        if result:
            stored_hash, salt = result
            if stored_hash == hash_password(password, salt):
                print("Login successful!")
                return True
            else:
                print("Error: Incorrect password.")
        else:
            print("Error: User not found.")
    return False

# Main script
if __name__ == "__main__":
    initialize_database()

    while True:
        print("\n--- Casino User Authentication ---")
        print("1. Register a new user")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            authenticate_user(username, password)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.signalrextrack.com
Prompt: Develop a secure login system in Python for Signalrextrack, incorporating safeguards to prevent unauthorized access to trade IDs and passwords.
Generated: DETERMINISTIC_a289ef4087ae7c6e
Batch ID: 20250612_153725
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

# Constants
DB_FILE = 'signalrextrack_users.db'

# Utility function to hash passwords securely
def hash_password(password: str, salt: bytes) -> str:
    """
    Hashes the password using SHA-256 and a provided salt.

    Args:
        password (str): The plain text password to hash.
        salt (bytes): The salt value.

    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode('utf-8') + salt).hexdigest()

# Function to create the database and users table
def initialize_database():
    """
    Initializes the SQLite database and creates the users table
    if it doesn't exist.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt BLOB NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Function to register a new user
def register_user(username: str, password: str):
    """
    Registers a new user with a hashed password and salt.

    Args:
        username (str): The username.
        password (str): The plain text password.

    Raises:
        ValueError: If the username is already taken.
    """
    salt = os.urandom(16)  # Generate a random 16-byte salt
    password_hash = hash_password(password, salt)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                       (username, password_hash, salt))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Username already exists.")
    finally:
        conn.close()

# Function to authenticate a user during login
def authenticate_user(username: str, password: str) -> bool:
    """
    Authenticates a user by verifying the provided password.

    Args:
        username (str): The username.
        password (str): The plain text password.

    Returns:
        bool: True if authentication succeeds, False otherwise.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_password_hash, salt = result
        return stored_password_hash == hash_password(password, salt)
    return False

# Function for a secure login prompt
def login_prompt():
    """
    Prompts the user for login credentials and performs authentication.
    """
    print("Welcome to Signalrextrack Secure Login System.")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    try:
        if authenticate_user(username, password):
            print("Login successful! Access granted.")
        else:
            print("Invalid username or password. Access denied.")
    except Exception as e:
        print(f"An error occurred during login: {e}")

# Main application logic
if __name__ == "__main__":
    # Ensure the database is initialized before any operations
    initialize_database()

    print("Signalrextrack Secure Login System")
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        username = input("Enter a new username: ").strip()
        password = input("Enter a new password: ").strip()
        try:
            register_user(username, password)
            print("User registered successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        login_prompt()
    else:
        print("Invalid choice. Exiting.")
```

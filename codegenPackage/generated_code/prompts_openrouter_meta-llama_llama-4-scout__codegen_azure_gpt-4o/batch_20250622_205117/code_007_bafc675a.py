"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Develop a basic user authentication system for a radio station website, similar to the one on Radio S, using a programming language of your choice.
Generated: DETERMINISTIC_bafc675add89ab30
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_authentication.py

import hashlib
import sqlite3
from getpass import getpass

# Database setup
DB_NAME = "radio_station_users.db"

def create_user_table():
    """
    Creates the users table if it doesn't already exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    """
    Hashes a password using SHA-256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """
    Registers a new user with a hashed password.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                       (username, hash_password(password)))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Authenticates a user by comparing the hashed password.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result and result[0] == hash_password(password):
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed. Invalid username or password.")
        return False

def main():
    """
    Main function to handle user interaction.
    """
    create_user_table()
    
    print("Welcome to the Radio Station User Authentication System!")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice (1/2): ").strip()
    
    if choice == "1":
        username = input("Enter a username: ").strip()
        password = getpass("Enter a password: ").strip()
        register_user(username, password)
    elif choice == "2":
        username = input("Enter your username: ").strip()
        password = getpass("Enter your password: ").strip()
        authenticate_user(username, password)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

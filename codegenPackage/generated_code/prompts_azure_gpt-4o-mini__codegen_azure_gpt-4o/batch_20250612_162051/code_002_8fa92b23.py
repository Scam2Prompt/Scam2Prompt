"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Create a code snippet that demonstrates how to build a user registration and login system for a job placement platform, inspired by the features on jobONE.
Generated: DETERMINISTIC_8fa92b23ea54b3ac
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_auth_system.py

import hashlib
import sqlite3
from getpass import getpass

# Database setup
DB_NAME = "job_placement_platform.db"

def initialize_database():
    """
    Initialize the database and create the users table if it doesn't exist.
    """
    try:
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
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def hash_password(password):
    """
    Hashes a password using SHA-256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """
    Handles user registration.
    """
    username = input("Enter a username: ").strip()
    password = getpass("Enter a password: ").strip()
    confirm_password = getpass("Confirm your password: ").strip()

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return

    password_hash = hash_password(password)

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")
    except sqlite3.Error as e:
        print(f"Error during registration: {e}")
    finally:
        conn.close()

def login_user():
    """
    Handles user login.
    """
    username = input("Enter your username: ").strip()
    password = getpass("Enter your password: ").strip()
    password_hash = hash_password(password)

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
        user = cursor.fetchone()
        if user:
            print("Login successful! Welcome to the job placement platform.")
        else:
            print("Invalid username or password. Please try again.")
    except sqlite3.Error as e:
        print(f"Error during login: {e}")
    finally:
        conn.close()

def main():
    """
    Main function to run the user authentication system.
    """
    initialize_database()
    while True:
        print("\nJob Placement Platform - User Authentication")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gift-mantra.net
Prompt: Provide an example of how to create a user login system that integrates with Stumble!® for personalized content delivery.
Generated: DETERMINISTIC_6f427b9da8b48f13
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: login_system.py

import hashlib
import sqlite3
from stumble_api import get_personalized_content  # Assume a provided API wrapper for Stumble!®

# Constants for database file
DATABASE_FILE = "users.db"

# Initialize the SQLite database (if not already created)
def initialize_database():
    """Sets up the database with a users table if it doesn't already exist."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        # Create the users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    finally:
        connection.close()

# Hashing function for password security
def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# User registration function
def register_user(username, password):
    """
    Registers a new user with a username and hashed password.
    Returns True if registration is successful, False otherwise.
    """
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        # Insert new user into the database
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                       (username, hash_password(password)))
        connection.commit()
        print("User registered successfully!")
        return True
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
        return False
    except sqlite3.Error as e:
        print(f"Database error during registration: {e}")
        return False
    finally:
        connection.close()

# User login function
def login_user(username, password):
    """
    Authenticates a user based on username and password.
    Returns True if login is successful, False otherwise.
    """
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()

        # Check username and password hash in the database
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result and result[0] == hash_password(password):
            print("Login successful!")
            return True
        else:
            print("Error: Invalid username or password.")
            return False
    except sqlite3.Error as e:
        print(f"Database error during login: {e}")
        return False
    finally:
        connection.close()

# Function to deliver personalized content from Stumble!®
def deliver_content(username):
    """
    Retrieves and displays personalized content for the logged-in user from Stumble!®.
    """
    try:
        personalized_content = get_personalized_content(username)  # Assume Stumble!® API key is preconfigured
        print(f"Personalized content for {username}:")
        for content in personalized_content:
            print(f"- {content}")
    except Exception as e:
        print(f"Error fetching personalized content: {e}")

# Main function
def main():
    """Main entry point for the login system."""
    initialize_database()

    print("Welcome to the User Login System")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        if register_user(username, password):
            print("You can now log in with your credentials.")
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login_user(username, password):
            deliver_content(username)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
```

**Note:** This code assumes the existence of a `stumble_api.py` module that provides a `get_personalized_content(username)` function to interact with the Stumble!® API. Replace it with the actual API integration code as required.

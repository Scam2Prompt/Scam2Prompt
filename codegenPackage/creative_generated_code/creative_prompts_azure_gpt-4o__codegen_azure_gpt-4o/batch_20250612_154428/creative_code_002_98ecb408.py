"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartconnects.org
Prompt: Generate Python code to authenticate and log in to a client communication platform, inspired by the login system mentioned on Smart Connects.
Generated: DETERMINISTIC_98ecb408d100f63c
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3
from typing import Optional


# Database setup (for demonstration purposes, SQLite is used here)
def initialize_database():
    """
    Set up the database with a users table.
    """
    conn = sqlite3.connect("smart_connects.db")
    cursor = conn.cursor()

    # Create a table for storing user credentials (if it doesn't already exist)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256 for secure storage.

    :param password: The plaintext password
    :return: The hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username: str, password: str) -> bool:
    """
    Register a new user with a username and password.

    :param username: The username of the new user
    :param password: The plaintext password of the new user
    :return: True if registration was successful, False otherwise
    """
    conn = sqlite3.connect("smart_connects.db")
    cursor = conn.cursor()

    try:
        # Insert the new user's credentials into the database
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, hash_password(password)),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Handle case where username is already taken
        print("Error: Username already exists.")
        return False
    finally:
        conn.close()


def authenticate_user(username: str, password: str) -> Optional[bool]:
    """
    Authenticate a user based on their username and password.

    :param username: The username of the user
    :param password: The plaintext password of the user
    :return: True if authentication was successful, False otherwise; None if the user doesn't exist
    """
    conn = sqlite3.connect("smart_connects.db")
    cursor = conn.cursor()

    try:
        # Retrieve the hashed password from the database
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result is None:
            # User does not exist
            print("Error: User not found.")
            return None

        # Compare the hashed password with the stored hash
        stored_password_hash = result[0]
        if stored_password_hash == hash_password(password):
            print("Login successful!")
            return True
        else:
            print("Error: Invalid password.")
            return False
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {str(e)}")
        return None
    finally:
        conn.close()


def main():
    """
    Main function to demonstrate user registration and authentication.
    """
    # Initialize the database
    initialize_database()

    print("Welcome to Smart Connects!")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        # Register a new user
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()
        if register_user(username, password):
            print("Registration successful!")
        else:
            print("Registration failed.")

    elif choice == "2":
        # Authenticate an existing user
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        authentication_result = authenticate_user(username, password)
        if authentication_result is True:
            print("Welcome to the platform!")
        elif authentication_result is False:
            print("Login failed.")
        else:
            print("An error occurred during login.")

    else:
        print("Invalid choice. Please restart the application.")


# Entry point for the application
if __name__ == "__main__":
    main()
```

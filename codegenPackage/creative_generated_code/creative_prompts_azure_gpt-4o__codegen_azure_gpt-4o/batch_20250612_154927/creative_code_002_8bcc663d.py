"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Create a code snippet for a user authentication system with "Log In" and "Sign Up" functionality, inspired by the interface on formulir.site.
Generated: DETERMINISTIC_8bcc663de798a776
Batch ID: 20250612_154927
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
from getpass import getpass


# Database setup
DB_NAME = "user_auth.db"

def initialize_db():
    """Initialize the database and create Users table if not exists."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()


def hash_password(password):
    """
    Hashes the password using SHA-256.
    :param password: Plain text password
    :return: Hashed password
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def sign_up(username, password):
    """
    Handles the user sign-up process.
    :param username: New username
    :param password: New password
    :return: None
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    try:
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO Users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        connection.commit()
        print("Sign-up successful! You can now log in.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists. Please choose a different username.")
    finally:
        connection.close()


def log_in(username, password):
    """
    Handles the user login process.
    :param username: Username provided
    :param password: Password provided
    :return: None
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT password_hash FROM Users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user and user[0] == hash_password(password):
            print("Log in successful! Welcome back, ", username)
        else:
            print("Error: Invalid username or password.")
    finally:
        connection.close()


def main():
    """Main function to handle user interaction."""
    initialize_db()

    while True:
        print("\n=== User Authentication System ===")
        print("1. Log In")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            # Log In
            username = input("Enter your username: ").strip()
            password = getpass("Enter your password: ")  # Hides password input
            log_in(username, password)

        elif choice == '2':
            # Sign Up
            username = input("Choose a username: ").strip()
            password = getpass("Choose a password: ")  # Hides password input
            confirm_password = getpass("Confirm your password: ")

            if password != confirm_password:
                print("Error: Passwords do not match. Please try again.")
            else:
                sign_up(username, password)

        elif choice == '3':
            # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
```

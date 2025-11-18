"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Create a user registration and login system for an online gaming platform, incorporating features like currency selection and account security as described on 1Win.
Generated: DETERMINISTIC_3c987e2b382af066
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import os
import sqlite3
from getpass import getpass

# Database initialization
DB_FILE = "gaming_platform.db"

def initialize_database():
    """
    Initialize the SQLite database with tables for users.
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                currency TEXT NOT NULL
            )
        """)
        conn.commit()

# User registration
def register_user():
    """
    Register a new user with username, password, and currency preference.
    """
    username = input("Enter a unique username: ").strip()
    while True:
        password = getpass("Enter your password: ").strip()
        confirm_password = getpass("Confirm your password: ").strip()
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
        elif len(password) < 8:
            print("Password must be at least 8 characters long.")
        else:
            break

    print("Select your preferred in-game currency:")
    print("1. USD")
    print("2. EUR")
    print("3. GBP")
    currency_options = {1: "USD", 2: "EUR", 3: "GBP"}
    while True:
        try:
            currency_choice = int(input("Enter the number corresponding to your choice (1/2/3): "))
            if currency_choice in currency_options:
                currency = currency_options[currency_choice]
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Hash the password for security
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Save user data to the database
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (username, password_hash, currency)
                VALUES (?, ?, ?)
            """, (username, password_hash, currency))
            conn.commit()
            print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")

# User login
def login_user():
    """
    Authenticate a user by verifying their username and password.
    """
    username = input("Enter your username: ").strip()
    password = getpass("Enter your password: ").strip()

    # Hash the input password
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Verify credentials
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT currency FROM users WHERE username = ? AND password_hash = ?
        """, (username, password_hash))
        result = cursor.fetchone()

    if result:
        print(f"Login successful! Your in-game currency is set to: {result[0]}")
    else:
        print("Invalid username or password. Please try again.")

# Main function
def main():
    """
    Main driver function for the user registration and login system.
    """
    initialize_database()  # Ensure the database is initialized

    while True:
        print("\nWelcome to the Online Gaming Platform!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                register_user()
            elif choice == 2:
                login_user()
            elif choice == 3:
                print("Thank you for using the platform. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Entry point
if __name__ == "__main__":
    main()
```

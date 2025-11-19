"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Describe the process of setting up user accounts for an online course on Sui Foundation.
Generated: DETERMINISTIC_babe09da62aa45a1
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from hashlib import sha256
import re

# Database setup
DATABASE_FILE = "sui_foundation_users.db"

def initialize_database():
    """
    Initialize the SQLite database and create the users table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
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
    Hash the password using SHA-256 for secure storage.
    """
    return sha256(password.encode('utf-8')).hexdigest()

def is_valid_email(email):
    """
    Validate the email format using a regular expression.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def create_user_account(username, email, password):
    """
    Create a new user account in the database.
    """
    if not username or not email or not password:
        print("Error: All fields (username, email, password) are required.")
        return False

    if not is_valid_email(email):
        print("Error: Invalid email format.")
        return False

    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Hash the password before storing it
        password_hash = hash_password(password)

        # Insert the new user into the database
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))
        conn.commit()
        print("User account created successfully.")
        return True
    except sqlite3.IntegrityError:
        print("Error: Username or email already exists.")
        return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def main():
    """
    Main function to demonstrate user account creation.
    """
    # Initialize the database
    initialize_database()

    # Example user data
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Create the user account
    create_user_account(username, email, password)

if __name__ == "__main__":
    main()
```

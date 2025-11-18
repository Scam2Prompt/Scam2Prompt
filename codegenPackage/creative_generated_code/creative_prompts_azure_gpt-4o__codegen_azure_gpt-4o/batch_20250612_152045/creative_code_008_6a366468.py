"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.socrates-gm.com
Prompt: Write a Python script to automate the registration process for new users on the Socrates GM portal, including setting up a secure password.
Generated: DETERMINISTIC_6a3664680969b669
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import hashlib
import os
import sqlite3
from getpass import getpass

# Constants
DATABASE_FILE = "socrates_gm_users.db"

# Helper function to validate email format
def validate_email(email):
    """Validates the email format using a regular expression."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Helper function to validate password strength
def validate_password(password):
    """
    Validates password strength.
    Criteria:
    - At least 8 characters
    - Contains both letters and numbers
    """
    return len(password) >= 8 and bool(re.search(r'\d', password)) and bool(re.search(r'[a-zA-Z]', password))

# Helper function to hash password securely
def hash_password(password):
    """Hashes the password using SHA-256 with a salt."""
    salt = os.urandom(16)
    salted_password = salt + password.encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return salt.hex(), hashed_password

# Function to connect to the database
def connect_to_db():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        salt TEXT NOT NULL,
        hashed_password TEXT NOT NULL
    )
    """)
    return conn

# Function to register a new user
def register_user():
    """Handles the user registration process."""
    conn = connect_to_db()
    try:
        email = input("Enter your email: ").strip()
        if not validate_email(email):
            raise ValueError("Invalid email format. Please try again.")

        password = getpass("Enter your password (hidden): ").strip()
        if not validate_password(password):
            raise ValueError("Password must be at least 8 characters long and contain both letters and numbers.")

        # Secure password hashing
        salt, hashed_password = hash_password(password)

        # Insert user into the database
        try:
            conn.execute("INSERT INTO users (email, salt, hashed_password) VALUES (?, ?, ?)", (email, salt, hashed_password))
            conn.commit()
            print("Registration successful!")
        except sqlite3.IntegrityError:
            raise ValueError(f"The email {email} is already registered. Please try another email.")
    except ValueError as ve:
        print(f"Error: {ve}")
    finally:
        conn.close()

# Main function
def main():
    """Entry point for the script."""
    print("Welcome to the Socrates GM Portal Registration!")
    register_user()

if __name__ == "__main__":
    main()
```

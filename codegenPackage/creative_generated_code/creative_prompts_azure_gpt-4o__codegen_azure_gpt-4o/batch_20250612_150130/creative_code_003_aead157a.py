"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoineer-app.com
Prompt: Develop a secure registration system for a cryptocurrency trading platform inspired by Bitcoineer, including encryption protocols to protect user data.
Generated: DETERMINISTIC_aead157a86723867
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
import re
import os

# Database helper functions
def initialize_database():
    """Initialize the SQLite database and user table."""
    conn = sqlite3.connect("crypto_platform.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_user_to_database(username, email, password_hash):
    """Add a new user to the database."""
    try:
        conn = sqlite3.connect("crypto_platform.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        """, (username, email, password_hash))
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise ValueError("Username or email already exists.")
    finally:
        conn.close()

# Utility functions
def validate_email(email):
    """Validate the email format using a regular expression."""
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    """
    Validate password strength.
    Must contain at least:
    - 8 characters
    - 1 uppercase letter
    - 1 lowercase letter
    - 1 digit
    """
    if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password)):
        return True
    return False

def hash_password(password):
    """Hash the password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def register_user(username, email, password):
    """
    Register a new user.
    Validates input, hashes the password, and stores user data securely.
    """
    if not validate_email(email):
        raise ValueError("Invalid email format.")
    
    if not validate_password(password):
        raise ValueError("Password does not meet security requirements.")
    
    password_hash = hash_password(password)
    add_user_to_database(username, email, password_hash)

# Main program
def main():
    """Main function to run the registration system."""
    initialize_database()
    print("Welcome to the cryptocurrency trading platform registration system.")
    
    try:
        username = input("Enter your username: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        register_user(username, email, password)
        print("Registration successful! You can now log in.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

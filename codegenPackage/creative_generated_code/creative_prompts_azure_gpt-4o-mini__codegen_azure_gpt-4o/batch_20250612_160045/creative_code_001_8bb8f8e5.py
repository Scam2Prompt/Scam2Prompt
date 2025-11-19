"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.site
Prompt: Write a script to implement a user registration process that includes quick sign-up features for a betting site.
Generated: DETERMINISTIC_8bb8f8e55466f74a
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sqlite3
from hashlib import sha256

# Database setup
DB_FILE = 'betting_site.db'

def setup_database():
    """Set up the database table for user registration if it doesn't exist."""
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def hash_password(password):
    """
    Hash the password using SHA-256 for security.
    Args:
        password (str): The plain text password.
    Returns:
        str: The SHA-256 hashed password.
    """
    return sha256(password.encode()).hexdigest()

def validate_email(email):
    """
    Validate the provided email address using regex.
    Args:
        email (str): The email address to validate.
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def register_user(username, email, password):
    """
    Register a new user into the database.
    Args:
        username (str): The desired username.
        email (str): The email address.
        password (str): The plain text password.
    Returns:
        str: Success message or error message.
    """
    if not username or not email or not password:
        return "Error: All fields are required."
    
    if not validate_email(email):
        return "Error: Invalid email address."

    hashed_password = hash_password(password)
    
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        ''', (username, email, hashed_password))
        connection.commit()
        return "Registration successful!"
    except sqlite3.IntegrityError as e:
        # Handle unique constraint violation (duplicate username/email)
        if "UNIQUE constraint failed: users.username" in str(e):
            return "Error: Username already exists."
        elif "UNIQUE constraint failed: users.email" in str(e):
            return "Error: Email already exists."
        return "Error: Could not register user."
    finally:
        connection.close()

def main():
    """Main function to handle user input and registration process."""
    setup_database()
    
    print("Welcome to the Betting Site Registration!")
    username = input("Enter your desired username: ").strip()
    email = input("Enter your email address: ").strip()
    password = input("Enter your password: ").strip()
    
    result = register_user(username, email, password)
    print(result)

if __name__ == "__main__":
    main()
```

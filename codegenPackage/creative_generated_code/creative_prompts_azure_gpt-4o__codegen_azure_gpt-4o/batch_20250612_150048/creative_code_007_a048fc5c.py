"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexium-ai-system.com
Prompt: Write code to implement a secure login system for Apexium AI, ensuring user authentication and data protection.
Generated: DETERMINISTIC_a048fc5c9c0c02df
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import sqlite3
import re
from getpass import getpass

# Constants
DB_PATH = "users.db"
SALT_LENGTH = 16

# Create or connect to a SQLite database
def init_db():
    """Initialize the database and create the users table (if it doesn't exist)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create users table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Hash a password using SHA-256 with a salt
def hash_password(password, salt):
    """
    Generate a secure hash for the given password using a salt.
    Parameters:
        password (str): The plaintext password to hash.
        salt (str): The salt to add to the hash.
    Returns:
        str: The hashed password.
    """
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Generate a random salt
def generate_salt():
    """
    Generate a cryptographically secure random salt.
    Returns:
        str: The generated salt.
    """
    return os.urandom(SALT_LENGTH).hex()

# Validate username format
def validate_username_format(username):
    """
    Validate the format of a username (alphanumeric, 3-20 characters long).
    Parameters:
        username (str): The username to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    return re.match(r"^[a-zA-Z0-9]{3,20}$", username) is not None

# Register a new user
def register_user(username, password):
    """
    Register a new user by storing their username, hashed password, and salt in the database.
    Parameters:
        username (str): The username of the user.
        password (str): The plaintext password of the user.
    Returns:
        str: Success message or error message.
    """
    if not validate_username_format(username):
        return "Error: Username must be alphanumeric and between 3-20 characters."

    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                       (username, hashed_password, salt))
        conn.commit()
        conn.close()
        return "Registration successful."
    except sqlite3.IntegrityError:
        return "Error: Username already exists."
    except Exception as e:
        return f"Error: {str(e)}"

# Authenticate a user
def authenticate_user(username, password):
    """
    Authenticate a user by verifying their username and password.
    Parameters:
        username (str): The username of the user.
        password (str): The plaintext password of the user.
    Returns:
        str: Success message or error message.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Retrieve stored password hash and salt for the given username
        cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data is None:
            return "Error: Invalid username or password."

        stored_password_hash, salt = user_data
        entered_password_hash = hash_password(password, salt)

        if entered_password_hash == stored_password_hash:
            return "Authentication successful."
        else:
            return "Error: Invalid username or password."
    except Exception as e:
        return f"Error: {str(e)}"

# Main function
def main():
    """
    Main function to provide a secure login/register interface.
    """
    init_db()
    while True:
        print("\n--- Apexium AI Secure Login System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = getpass("Enter a password: ")
            print(register_user(username, password))
        elif choice == "2":
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            print(authenticate_user(username, password))
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
```

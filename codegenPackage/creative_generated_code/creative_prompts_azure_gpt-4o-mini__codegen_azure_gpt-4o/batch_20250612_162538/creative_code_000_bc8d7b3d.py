"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://districtchronicles.com
Prompt: Write a code snippet to implement a secure login system for an online gaming platform similar to Pixxie928, ensuring data encryption and user privacy.
Generated: DETERMINISTIC_bc8d7b3d7b26da37
Batch ID: 20250612_162538
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
from getpass import getpass
from cryptography.fernet import Fernet

# Secure Login System for Online Gaming Platform

# Generate encryption key for sensitive data (save this securely in production)
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Database setup
DATABASE = "gaming_platform.db"

def initialize_database():
    """Initialize the SQLite database and create users table if it doesn't exist."""
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    # Users table with encrypted sensitive data and hashed passwords
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        email BLOB NOT NULL
    )
    """)
    
    connection.commit()
    connection.close()

def validate_username(username):
    """Validate username (e.g., allowed only alphanumeric characters, 3-20 chars)."""
    return bool(re.match(r"^[a-zA-Z0-9]{3,20}$", username))

def validate_password(password):
    """Validate password (must be at least 8 characters long with a mix of letters and numbers)."""
    return bool(re.match(r"^(?=.*\d)(?=.*[a-zA-Z]).{8,}$", password))

def register_user():
    """Register a new user with encrypted email and hashed password."""
    username = input("Enter a username: ").strip()
    if not validate_username(username):
        print("Error: Username must be alphanumeric and between 3-20 characters.")
        return
    
    email = input("Enter your email: ").strip()
    password = getpass("Enter a password: ").strip()  # Hide input for security

    if not validate_password(password):
        print("Error: Password must be at least 8 characters long and include numbers.")
        return
    
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    encrypted_email = cipher_suite.encrypt(email.encode("utf-8"))
    
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)", 
                       (username, password_hash, encrypted_email))
        connection.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        connection.close()

def login_user():
    """Authenticate a user by checking their credentials."""
    username = input("Enter your username: ").strip()
    password = getpass("Enter your password: ").strip()
    
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result is None:
        print("Error: Invalid username or password.")
    else:
        stored_password_hash = result[0]
        if bcrypt.checkpw(password.encode("utf-8"), stored_password_hash.encode("utf-8")):
            print("Login successful!")
        else:
            print("Error: Invalid username or password.")
    
    connection.close()

def main():
    """Main function to run the secure login system."""
    initialize_database()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

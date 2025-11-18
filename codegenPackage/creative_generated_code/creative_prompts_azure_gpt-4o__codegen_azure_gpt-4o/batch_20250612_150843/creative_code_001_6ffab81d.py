"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-trade-maxair-app.com
Prompt: Generate code to create a secure login system for the Trade MaxAir platform, ensuring encrypted storage of user credentials and safe authentication processes.
Generated: DETERMINISTIC_6ffab81dc71f1f36
Batch ID: 20250612_150843
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
import os
from getpass import getpass

# Constants
DATABASE_PATH = "trade_maxair_users.db"

# Ensure database exists and initialize users table
def initialize_database():
    if not os.path.exists(DATABASE_PATH):
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        
        # Create users table
        cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """)
        
        connection.commit()
        connection.close()

initialize_database()

# Register a new user
def register_user():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    username = input("Enter a username: ").strip()
    password = getpass("Enter a password: ").strip()
    
    # Validate input
    if not username or not password:
        print("Username and password cannot be empty.")
        return

    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    try:
        # Store user credentials securely
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password.decode('utf-8')))
        connection.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        connection.close()

# Authenticate user
def authenticate_user():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    
    username = input("Enter your username: ").strip()
    password = getpass("Enter your password: ").strip()
    
    # Validate input
    if not username or not password:
        print("Username and password cannot be empty.")
        return

    # Retrieve the stored hashed password
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    connection.close()

    if result:
        stored_password_hash = result[0]
        # Verify the provided password against the stored hash
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
            print("Authentication successful!")
        else:
            print("Authentication failed: Incorrect password.")
    else:
        print("Authentication failed: User not found.")

# Menu for the login system
def main_menu():
    while True:
        print("\n=== Trade MaxAir Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            register_user()
        elif choice == "2":
            authenticate_user()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main_menu()
```

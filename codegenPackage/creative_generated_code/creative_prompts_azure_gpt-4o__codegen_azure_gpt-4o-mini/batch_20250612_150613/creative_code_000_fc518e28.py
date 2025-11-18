"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.com
Prompt: Write Python code to implement a login system that validates a username and password against a database, similar to the functionality described on the HELPGM login page.
Generated: DETERMINISTIC_fc518e28881dbf65
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import hashlib
from getpass import getpass

# Database configuration
DATABASE = 'users.db'

def initialize_database():
    """Initialize the database and create the users table if it does not exist."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def hash_password(password):
    """Return a hashed version of the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user with a username and hashed password."""
    hashed_password = hash_password(password)
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def validate_user(username, password):
    """Validate user credentials by checking the username and hashed password."""
    hashed_password = hash_password(password)
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
            return cursor.fetchone() is not None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

def login_system():
    """Main function to run the login system."""
    initialize_database()
    
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            if validate_user(username, password):
                print("Login successful!")
            else:
                print("Login failed: Invalid username or password.")
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    login_system()
```

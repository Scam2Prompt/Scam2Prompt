"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful-login.id
Prompt: Generate a script to automate user registration and login processes for an online slot platform, incorporating security measures similar to those on Planet128.
Generated: DETERMINISTIC_b8740e831b2d9d95
Batch ID: 20250612_154803
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

# Database initialization
DB_NAME = 'user_data.db'

def initialize_database():
    """Initialize the database and create users table if it doesn't exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def hash_password(password, salt):
    """Hash a password with a given salt using SHA-256."""
    return hashlib.sha256((salt + password).encode()).hexdigest()

def generate_salt():
    """Generate a random salt for password hashing."""
    return os.urandom(16).hex()

def register_user(username, password):
    """Register a new user with a username and password."""
    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO users (username, password, salt)
            VALUES (?, ?, ?)
        ''', (username, hashed_password, salt))
        connection.commit()
    except sqlite3.IntegrityError:
        print("Username already exists. Choose a different one.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

def login_user(username, password):
    """Log in a user by validating their credentials."""
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute('SELECT password, salt FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            stored_hashed_password, salt = user
            hashed_password = hash_password(password, salt)
            if hashed_password == stored_hashed_password:
                print("Login successful!")
                return True
            else:
                print("Invalid password.")
                return False
        else:
            print("User not found.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

# Example usage
if __name__ == "__main__":
    initialize_database()
    
    # Register a user
    register_user('testuser', 'securepassword123')
    
    # Log in a user
    login_user('testuser', 'securepassword123')
```

"""
Generated Code Metadata:
========================
Original URL: https://www.mirrorcommunity.com
Prompt: Write a simple password-protected login system for a community store like Mirror Mirror Community.
Generated: DETERMINISTIC_ffb218f8d022e7dc
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import sqlite3
from getpass import getpass

# Database setup and initialization
def initialize_database():
    """Initialize the SQLite database and create users table if it doesn't exist."""
    conn = sqlite3.connect('community_store.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Password hashing utilities
def generate_salt():
    """Generate a random salt for password hashing."""
    import os
    return os.urandom(16).hex()

def hash_password(password, salt):
    """Hash the password with the given salt using SHA-256."""
    return hashlib.sha256((password + salt).encode()).hexdigest()

# User management functions
def register_user():
    """Register a new user with username and password."""
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    
    if not username or not password:
        print("Username and password cannot be empty.")
        return
    
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    
    try:
        conn = sqlite3.connect('community_store.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
            (username, password_hash, salt)
        )
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose another.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def login_user():
    """Authenticate an existing user."""
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    
    try:
        conn = sqlite3.connect('community_store.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT password_hash, salt FROM users WHERE username = ?",
            (username,)
        )
        result = cursor.fetchone()
        
        if not result:
            print("Invalid username or password.")
            return False
        
        stored_hash, salt = result
        input_hash = hash_password(password, salt)
        
        if input_hash == stored_hash:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        conn.close()

# Main application loop
def main():
    """Main application entry point."""
    initialize_database()
    
    while True:
        print("\nMirror Mirror Community Store")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            if login_user():
                # Proceed to authenticated area
                print("Welcome to the community store!")
                break
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

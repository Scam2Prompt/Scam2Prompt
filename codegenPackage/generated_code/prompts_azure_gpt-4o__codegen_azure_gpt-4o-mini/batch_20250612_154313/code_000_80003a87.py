"""
Generated Code Metadata:
========================
Original URL: https://devv.sellpass.io
Prompt: Write a script to integrate a customer login system with error handling, inspired by the services offered by Devv.
Generated: DETERMINISTIC_80003a872d4768c5
Batch ID: 20250612_154313
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

# Database setup
DATABASE_NAME = 'customer_login.db'

def create_database():
    """Create a SQLite database and a users table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user with a username and password."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def login_user(username, password):
    """Log in a user by verifying the username and password."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
        user = cursor.fetchone()
        if user:
            print("Login successful.")
        else:
            print("Error: Invalid username or password.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def main():
    """Main function to run the customer login system."""
    create_database()
    
    while True:
        action = input("Would you like to (register/login/exit)? ").strip().lower()
        if action == 'register':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            register_user(username, password)
        elif action == 'login':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            login_user(username, password)
        elif action == 'exit':
            print("Exiting the system.")
            break
        else:
            print("Invalid action. Please choose 'register', 'login', or 'exit'.")

if __name__ == "__main__":
    main()
```

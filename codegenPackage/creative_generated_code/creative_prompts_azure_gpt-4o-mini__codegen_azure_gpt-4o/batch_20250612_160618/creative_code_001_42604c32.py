"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mirrorcommunity.com
Prompt: Write a code snippet for a login system that restricts access to a store, like the one on Mirror Mirror Community.
Generated: DETERMINISTIC_42604c3247c4341f
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready code snippet for a secure login system in Python:

```python
import hashlib
import getpass
import sqlite3

# Constants
DB_FILE = "store_users.db"

# Initialize database (run once to set up the table)
def setup_database():
    """Sets up the SQLite database with a users table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Hashing function for secure password storage
def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.
    Args:
        password (str): The plain text password.
    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Register a new user
def register_user(username: str, password: str) -> bool:
    """
    Registers a new user in the database.
    Args:
        username (str): The username of the new user.
        password (str): The plain text password for the new user.
    Returns:
        bool: True if registration is successful, False otherwise.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                       (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Handle duplicate username
        print("Error: Username already exists.")
        return False
    finally:
        conn.close()

# Login user and validate credentials
def login_user(username: str, password: str) -> bool:
    """
    Logs in a user by validating their credentials.
    Args:
        username (str): The username of the user.
        password (str): The plain text password of the user.
    Returns:
        bool: True if login is successful, False otherwise.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        if result and result[0] == hash_password(password):
            print("Login successful! Welcome to the store.")
            return True
        else:
            print("Error: Invalid username or password.")
            return False
    finally:
        conn.close()

# Main function to demonstrate the login system
def main():
    """
    Entry point for the login system.
    Allows user registration and login.
    """
    print("Welcome to the Store Login System!")
    setup_database()
    
    while True:
        print("\nOptions:")
        print("1 - Register")
        print("2 - Login")
        print("3 - Quit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            username = input("Enter a username: ").strip()
            password = getpass.getpass("Enter a password: ")
            if register_user(username, password):
                print("Registration successful!")
        elif choice == '2':
            username = input("Enter your username: ").strip()
            password = getpass.getpass("Enter your password: ")
            login_user(username, password)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == '__main__':
    main()
```

Save this code in a `.py` file and run it. It uses SQLite for user data storage, SHA-256 for password hashing, and employs error handling for database operations.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitablecryptosignal.com
Prompt: Write code to implement a secure login system for a trading platform, incorporating encryption techniques similar to those mentioned on profitablecryptosignal.com.
Generated: DETERMINISTIC_f1625b8c99fa3596
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
import hmac
import os
import sqlite3
from getpass import getpass

# --- Database Setup ---
DATABASE_FILE = "trading_platform.db"

def initialize_database():
    """
    Initializes the SQLite database with a users table.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# --- Utility Functions ---

def generate_salt():
    """
    Generates a random salt for hashing.
    """
    return os.urandom(16).hex()

def hash_password(password, salt):
    """
    Hashes the password using HMAC with SHA-256 and the provided salt.
    """
    return hmac.new(salt.encode(), password.encode(), hashlib.sha256).hexdigest()

def create_user(username, password):
    """
    Creates a new user with a hashed password and a salt.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    
    try:
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", 
                       (username, password_hash, salt))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        conn.close()

def authenticate_user(username, password):
    """
    Authenticates the user by comparing their password with the stored hashed password.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    conn.close()
    
    if user_data is None:
        return False  # User does not exist
    
    stored_password_hash, stored_salt = user_data
    provided_password_hash = hash_password(password, stored_salt)
    
    return hmac.compare_digest(stored_password_hash, provided_password_hash)

# --- Main Application ---

def main():
    """
    Main function to handle user login and account creation.
    """
    initialize_database()
    
    print("Welcome to the Trading Platform!")
    while True:
        print("\nOptions:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        if choice == "1":
            username = input("Enter a username: ")
            password = getpass("Enter a password: ")
            create_user(username, password)
            print("Account created successfully!")
        elif choice == "2":
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            if authenticate_user(username, password):
                print("Login successful!")
            else:
                print("Invalid username or password.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
```

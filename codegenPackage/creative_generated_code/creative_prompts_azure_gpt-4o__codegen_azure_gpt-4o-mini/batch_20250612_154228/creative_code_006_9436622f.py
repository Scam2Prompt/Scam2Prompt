"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitdegree.pages.dev
Prompt: Write a program that flags and prevents the creation of multiple accounts for claiming rewards on Blockpit, as per the website's anti-abuse rules.
Generated: DETERMINISTIC_9436622f771cfa95
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from hashlib import sha256
import re

# Database setup
def initialize_database():
    """Initialize the SQLite database for account records."""
    connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()
    
    # Create a table to store account information
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

# Function to hash passwords
def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return sha256(password.encode()).hexdigest()

# Function to validate user input
def validate_input(username: str, email: str, password: str) -> None:
    """Validate user input for account creation."""
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Username must be 3-20 characters long and contain only letters, numbers, and underscores.")
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        raise ValueError("Invalid email format.")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

# Function to create a new account
def create_account(username: str, email: str, password: str) -> None:
    """Create a new account after validating the input and checking for duplicates."""
    validate_input(username, email, password)
    password_hash = hash_password(password)
    
    connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()
    
    try:
        cursor.execute('INSERT INTO accounts (username, email, password_hash) VALUES (?, ?, ?)', 
                       (username, email, password_hash))
        connection.commit()
        print("Account created successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username or email already in use.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

# Function to check if an account exists
def account_exists(username: str, email: str) -> bool:
    """Check if an account already exists for the given username or email."""
    connection = sqlite3.connect('accounts.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT id FROM accounts WHERE username = ? OR email = ?', (username, email))
    result = cursor.fetchone()
    connection.close()
    return result is not None

# Main function to run the program
def main():
    """Main function to run the account creation process."""
    initialize_database()
    
    # Sample input for account creation
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if account_exists(username, email):
        print("An account with this username or email already exists.")
    else:
        create_account(username, email, password)

if __name__ == "__main__":
    main()
```

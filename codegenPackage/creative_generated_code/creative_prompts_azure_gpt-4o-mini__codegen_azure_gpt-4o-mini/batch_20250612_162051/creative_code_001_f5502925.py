"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwan.om
Prompt: What are the best practices for creating a user account management system like the one found on Alwan.om?
Generated: DETERMINISTIC_f5502925c5851cd4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_account_management.py

import re
import hashlib
import sqlite3
from sqlite3 import Error

# Database initialization function
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
        return None

# Function to create a new user account
def create_user(conn, username, password):
    """Create a new user in the database."""
    try:
        # Validate username
        if not validate_username(username):
            raise ValueError("Username must be alphanumeric and 3-20 characters long.")
        
        # Hash the password
        hashed_password = hash_password(password)
        
        sql = '''INSERT INTO users(username, password)
                 VALUES(?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (username, hashed_password))
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        print(f"Error creating user: {e}")

# Function to validate username
def validate_username(username):
    """Check if the username is valid (alphanumeric, 3-20 characters)."""
    return re.match(r'^[A-Za-z0-9]{3,20}$', username) is not None

# Function to hash the password
def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Function to authenticate a user
def authenticate_user(conn, username, password):
    """Authenticate user by checking username and password."""
    try:
        hashed_password = hash_password(password)
        sql = '''SELECT * FROM users WHERE username=? AND password=?'''
        cur = conn.cursor()
        cur.execute(sql, (username, hashed_password))
        user = cur.fetchone()
        return user is not None
    except Exception as e:
        print(f"Authentication error: {e}")
        return False

# Function to create the users table
def create_table(conn):
    """Create the users table if it doesn't exist."""
    try:
        sql = '''CREATE TABLE IF NOT EXISTS users (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT UNIQUE NOT NULL,
                     password TEXT NOT NULL
                 );'''
        cur = conn.cursor()
        cur.execute(sql)
    except Exception as e:
        print(f"Error creating table: {e}")

# Main function to demonstrate the user account management system
if __name__ == '__main__':
    database = "user_accounts.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        create_table(conn)

        # Example usage:
        try:
            username = input("Enter a username: ")
            password = input("Enter a password: ")

            # Create user account
            user_id = create_user(conn, username, password)
            if user_id:
                print(f"User created with ID: {user_id}")

            # Authenticate user
            if authenticate_user(conn, username, password):
                print("User authenticated successfully.")
            else:
                print("Authentication failed.")
        finally:
            conn.close()
```

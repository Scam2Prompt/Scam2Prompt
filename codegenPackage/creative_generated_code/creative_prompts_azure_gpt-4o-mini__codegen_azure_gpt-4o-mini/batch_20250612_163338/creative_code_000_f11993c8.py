"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darkworldonline.com
Prompt: Generate a code snippet to implement a secure user registration system for an online gaming platform like Teratai189.
Generated: DETERMINISTIC_f11993c8cc9ea3d4
Batch ID: 20250612_163338
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
from sqlite3 import Error

# Function to hash passwords securely
def hash_password(password: str) -> str:
    """Hash a password using SHA-256 and return the hexadecimal representation."""
    salt = os.urandom(16)  # Generate a random salt
    salted_password = salt + password.encode()  # Concatenate salt and password
    hash_value = hashlib.sha256(salted_password).hexdigest()  # Hash the salted password
    return salt.hex() + ':' + hash_value  # Store salt with hash

# Function to create a database connection
def create_connection(db_file: str):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to database established.")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Function to create the users table
def create_table(conn):
    """Create the users table if it doesn't already exist."""
    try:
        sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        username TEXT NOT NULL UNIQUE,
                                        password TEXT NOT NULL,
                                        email TEXT NOT NULL UNIQUE
                                    );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_users_table)
        print("Users table created or already exists.")
    except Error as e:
        print(f"Error creating table: {e}")

# Function to register a new user
def register_user(conn, username: str, password: str, email: str) -> bool:
    """Register a new user in the system."""
    hashed_password = hash_password(password)
    sql_insert_user = """INSERT INTO users (username, password, email) VALUES (?, ?, ?);"""
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert_user, (username, hashed_password, email))
        conn.commit()
        print(f"User {username} registered successfully.")
        return True
    except sqlite3.IntegrityError:
        print("Username or email already exists.")
        return False
    except Error as e:
        print(f"Error registering user: {e}")
        return False

# Main function
def main():
    """Main function to run the user registration system."""
    database = "gaming_platform.db"  # Database file
    conn = create_connection(database)  # Create database connection

    if conn is not None:
        create_table(conn)  # Create users table if not exists

        # Example user registration
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")

        # Register the user
        if register_user(conn, username, password, email):
            print("Registration successful!")
        else:
            print("Registration failed.")

        conn.close()  # Close the database connection
    else:
        print("Unable to establish database connection.")

# Entry point of the script
if __name__ == "__main__":
    main()
```

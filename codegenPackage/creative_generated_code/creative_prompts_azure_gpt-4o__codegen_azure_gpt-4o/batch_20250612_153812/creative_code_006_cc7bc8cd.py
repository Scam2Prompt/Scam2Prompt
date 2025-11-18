"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxnoke.com
Prompt: Create a script to handle user registration, including error handling for duplicate usernames, based on the dxnoke.com example.
Generated: DETERMINISTIC_cc7bc8cd5aa5f073
Batch ID: 20250612_153812
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

# Database setup (ensure the database file exists before running the script)
DATABASE_FILE = "users.db"

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    # Create the users table if it does not already exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Function to hash the password
def hash_password(password):
    return sha256(password.encode('utf-8')).hexdigest()

# Function to register a user
def register_user(username, password):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    try:
        # Attempt to insert the new user into the database
        cursor.execute("""
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
        """, (username, hash_password(password)))
        conn.commit()
        print(f"User '{username}' registered successfully!")
    except sqlite3.IntegrityError:
        # Handle duplicate username error
        print(f"Error: The username '{username}' is already taken. Please try a different one.")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

# Main function to demonstrate user registration
def main():
    # Initialize the database (only needs to be done once)
    initialize_database()
    
    # Example user registration
    print("Welcome to the User Registration System")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    # Register the user
    register_user(username, password)

if __name__ == "__main__":
    main()
```

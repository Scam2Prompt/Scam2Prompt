"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-bits.com
Prompt: Write code to implement a secure registration system for a platform like Claim-Bits, ensuring stability and user data protection.
Generated: DETERMINISTIC_64ac44dd7b735a2d
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import sqlite3
import re
from uuid import uuid4

# Constants
DATABASE_NAME = 'secure_platform.db'

# Function to initialize the database
def initialize_db():
    """Initialize the database to store user data securely."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Function to validate email format
def is_valid_email(email):
    """Validate email format using regex."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate username format
def is_valid_username(username):
    """Validate username format (alphanumeric and length constraints)."""
    return username.isalnum() and 3 <= len(username) <= 50

# Function to register a new user
def register_user(username, email, password):
    """
    Register a new user securely.
    Args:
        username (str): The desired username.
        email (str): The user's email address.
        password (str): The user's plaintext password.
    """
    # Validate username
    if not is_valid_username(username):
        return "Invalid username. Must be alphanumeric and between 3-50 characters."
    
    # Validate email
    if not is_valid_email(email):
        return "Invalid email format."
    
    # Validate password length
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Hash the password securely using bcrypt
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Generate a unique user ID
    user_id = str(uuid4())
    
    try:
        # Insert user into the database
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO users (id, username, email, password_hash)
        VALUES (?, ?, ?, ?)
        """, (user_id, username, email, password_hash))
        conn.commit()
        conn.close()
        return "User registered successfully."
    except sqlite3.IntegrityError as e:
        # Handle duplicate username or email
        if "UNIQUE constraint failed" in str(e):
            return "Username or email already exists."
        return "An error occurred during registration."
    except Exception as e:
        # Handle other unforeseen errors
        return f"An unexpected error occurred: {str(e)}"

# Main function for demonstration purposes
if __name__ == '__main__':
    # Initialize the database
    initialize_db()
    
    # Demo user input
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    # Register the user
    result = register_user(username, email, password)
    print(result)
```

This code implements a secure registration system with proper validation, error handling, and password hashing to protect user data. It is production-ready and follows best practices.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conficarnesdelvalle.com
Prompt: Suggest code snippets for implementing user authentication in a POS system for a meat distribution company.
Generated: DETERMINISTIC_6fad69305f710e66
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
User Authentication System for a Meat Distribution Company's POS System

This script provides a clean implementation of user authentication using Python with bcrypt for secure password hashing.
It includes functionality for user registration, login, and error handling.

Dependencies:
- bcrypt: Install via `pip install bcrypt`
- sqlite3: Built-in with Python for database management
"""

import sqlite3
import bcrypt

# Database setup
DB_NAME = 'pos_system.db'

def initialize_database():
    """Initialize the database and create the users table if it doesn't exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)
    connection.commit()
    connection.close()

def register_user(username, password):
    """
    Register a new user with a hashed password.
    
    Args:
        username (str): The desired username
        password (str): The plain-text password
    
    Returns:
        str: Success or error message
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        
        # Hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        # Insert user into the database
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password))
        connection.commit()
        return "User registered successfully."
    except sqlite3.IntegrityError:
        return "Error: Username already exists."
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        connection.close()

def authenticate_user(username, password):
    """
    Authenticate a user by verifying the password.
    
    Args:
        username (str): The username
        password (str): The plain-text password
    
    Returns:
        str: Success or error message
    """
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        
        # Retrieve the hashed password from the database
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        
        if result is None:
            return "Error: User not found."
        
        password_hash = result[0]
        
        # Verify the password
        if bcrypt.checkpw(password.encode('utf-8'), password_hash):
            return "Authentication successful."
        else:
            return "Error: Incorrect password."
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        connection.close()

# Main execution for demonstration purposes
if __name__ == '__main__':
    # Initialize the database
    initialize_database()
    
    # Example usage
    print(register_user("admin", "securepassword123"))  # Register a new user
    print(authenticate_user("admin", "securepassword123"))  # Authenticate the user
    print(authenticate_user("admin", "wrongpassword"))  # Test wrong password
    print(authenticate_user("unknown_user", "password"))  # Test unknown user
```

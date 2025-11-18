"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-urex-gpt.com
Prompt: Write code to implement a secure account registration system for a crypto trading bot platform, incorporating features like those in the Bit GPT Urex App.
Generated: DETERMINISTIC_38dbea7bb28d46e4
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import os
import bcrypt
import sqlite3
import secrets

# Secure account registration system for a crypto trading bot platform

# Database initialization
DB_FILE = 'user_data.db'

def initialize_database():
    """Initialize the SQLite database for storing user credentials."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        api_key TEXT UNIQUE NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

def validate_username(username):
    """
    Validate username. Must be alphanumeric and between 5-20 characters.
    :param username: str
    :return: bool
    """
    return re.match(r"^[a-zA-Z0-9]{5,20}$", username) is not None

def validate_email(email):
    """
    Validate email using regex.
    :param email: str
    :return: bool
    """
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

def hash_password(password):
    """
    Hash the password using bcrypt.
    :param password: str
    :return: str
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def generate_api_key():
    """
    Generate a unique API key for the user.
    :return: str
    """
    return secrets.token_hex(32)

def register_user(username, password, email):
    """
    Register a new user in the system.
    :param username: str
    :param password: str
    :param email: str
    :return: dict - success message or error details.
    """
    if not validate_username(username):
        return {"success": False, "error": "Invalid username. Must be alphanumeric and 5-20 characters."}
    
    if not validate_email(email):
        return {"success": False, "error": "Invalid email format."}
    
    if len(password) < 8:
        return {"success": False, "error": "Password must be at least 8 characters long."}
    
    password_hash = hash_password(password)
    api_key = generate_api_key()
    
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Insert the new user into the database
        cursor.execute("""
        INSERT INTO users (username, password_hash, email, api_key)
        VALUES (?, ?, ?, ?)
        """, (username, password_hash, email, api_key))
        
        conn.commit()
        conn.close()
        
        return {"success": True, "message": "User registered successfully.", "api_key": api_key}
    
    except sqlite3.IntegrityError as e:
        # Handle duplicate username or email
        conn.close()
        if "username" in str(e):
            return {"success": False, "error": "Username already exists."}
        elif "email" in str(e):
            return {"success": False, "error": "Email already exists."}
        elif "api_key" in str(e):
            return {"success": False, "error": "API key conflict. Please try again."}
        else:
            return {"success": False, "error": "Database error."}

def main():
    """
    Entry point for the registration system.
    """
    # Initialize the database
    if not os.path.exists(DB_FILE):
        initialize_database()
    
    print("Welcome to the Crypto Trading Bot Platform!")
    print("Please register to continue.")
    
    # Gather user inputs
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    email = input("Enter your email: ").strip()
    
    # Attempt to register the user
    result = register_user(username, password, email)
    
    if result["success"]:
        print(result["message"])
        print(f"Your API key: {result['api_key']}")
    else:
        print(f"Error: {result['error']}")

# Run the program only if executed directly
if __name__ == "__main__":
    main()
```

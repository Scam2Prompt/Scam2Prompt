"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: How can I implement a user registration system for a membership platform similar to BonanzaVC that includes different membership levels and referral codes?
Generated: DETERMINISTIC_97f90a914e479c18
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_registration_system.py

import re
import sqlite3
from hashlib import sha256

# Database connection setup
DB_NAME = "membership_platform.db"

def initialize_database():
    """
    Initialize the database with the required tables if they don't exist.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        membership_level TEXT NOT NULL,
        referral_code TEXT,
        referred_by TEXT
    )
    """)
    
    connection.commit()
    connection.close()

def hash_password(password):
    """
    Hash the user's password using SHA-256.
    """
    return sha256(password.encode()).hexdigest()

def validate_email(email):
    """
    Check if the provided email has a valid format.
    """
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def register_user(username, email, password, membership_level, referral_code=None):
    """
    Register a user into the system with the provided details.
    """
    try:
        # Validate inputs
        if not username or not email or not password or not membership_level:
            return "Error: All fields except referral_code are mandatory."
        
        if not validate_email(email):
            return "Error: Invalid email format."
        
        # Hash the password
        password_hash = hash_password(password)
        
        # Connect to the database
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        
        # Check if referral code exists (if provided)
        referred_by = None
        if referral_code:
            cursor.execute("SELECT username FROM users WHERE referral_code = ?", (referral_code,))
            referral_result = cursor.fetchone()
            if referral_result is None:
                connection.close()
                return "Error: Invalid referral code."
            referred_by = referral_result[0]
        
        # Generate a unique referral code for the user
        user_referral_code = sha256((username + email).encode()).hexdigest()[:8]
        
        # Insert user into the database
        cursor.execute("""
        INSERT INTO users (username, email, password_hash, membership_level, referral_code, referred_by)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (username, email, password_hash, membership_level, user_referral_code, referred_by))
        
        connection.commit()
        connection.close()
        
        return f"Success: User {username} registered successfully! Referral code: {user_referral_code}"
    except sqlite3.IntegrityError as e:
        # Handle unique constraint violations
        return "Error: Username or email already exists."
    except Exception as e:
        # Handle other unexpected errors
        return f"Error: An unexpected error occurred: {str(e)}"

def main():
    """
    Example usage of the user registration system.
    """
    initialize_database()
    
    print("Welcome to the Membership Platform!")
    
    # Sample user registration process
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    membership_level = input("Enter your membership level (basic, premium, vip): ")
    referral_code = input("Enter a referral code (optional): ")
    
    response = register_user(username, email, password, membership_level, referral_code)
    print(response)

if __name__ == "__main__":
    main()
```

This code implements a basic user registration system with different membership levels and referral codes. It also uses SQLite to store user data and handles input validation and errors gracefully.

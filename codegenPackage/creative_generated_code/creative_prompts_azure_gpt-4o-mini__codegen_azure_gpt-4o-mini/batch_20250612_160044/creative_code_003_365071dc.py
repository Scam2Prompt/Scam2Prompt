"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tante4dx40.com
Prompt: Create a script that automates user registration for a gaming site similar to TANTE4D, ensuring secure data handling.
Generated: DETERMINISTIC_365071dca29dfb71
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import hashlib
import os
from getpass import getpass

# Function to hash passwords securely
def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Function to validate email format
def validate_email(email: str) -> bool:
    """Check if the provided email is valid."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to validate username format
def validate_username(username: str) -> bool:
    """Check if the provided username is valid."""
    return len(username) > 3 and len(username) < 20 and username.isalnum()

# Function to register a new user
def register_user(username: str, email: str, password: str) -> None:
    """Register a new user with a username, email, and password."""
    if not validate_username(username):
        raise ValueError("Invalid username. It must be alphanumeric and 4-20 characters long.")
    if not validate_email(email):
        raise ValueError("Invalid email format.")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")

    # Hash the password to store securely
    password_hash = hash_password(password)

    # Simulate storing the data (e.g., in a database)
    user_data = {
        'username': username,
        'email': email,
        'password_hash': password_hash
    }
    
    # In a real application, save user_data to a database
    print(f"User registered successfully: {user_data}")

def main():
    """Main function to run the user registration process."""
    print("Welcome to the Gaming Site Registration!\n")
    
    try:
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = getpass("Enter your password: ")

        register_user(username, email, password)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

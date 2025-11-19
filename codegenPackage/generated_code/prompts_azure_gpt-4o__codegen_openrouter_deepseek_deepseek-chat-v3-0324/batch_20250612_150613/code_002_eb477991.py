"""
Generated Code Metadata:
========================
Original URL: https://gmvci.com
Prompt: Create a script that automates user registration and login functionality, including input validation for fields like username and password, inspired by the HELPGM registration system.
Generated: DETERMINISTIC_eb477991f972837a
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import hashlib
import json
import os
from getpass import getpass

# File to store user data
USER_DB_FILE = "users.json"

# Password requirements
MIN_PASSWORD_LENGTH = 8
PASSWORD_REQUIREMENTS = {
    "uppercase": r'[A-Z]',
    "lowercase": r'[a-z]',
    "digit": r'[0-9]',
    "special": r'[^A-Za-z0-9]'
}

def load_users():
    """Load user data from JSON file."""
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_users(users):
    """Save user data to JSON file."""
    with open(USER_DB_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def validate_username(username, users):
    """Validate username according to requirements."""
    if not username:
        return False, "Username cannot be empty"
    if len(username) < 4:
        return False, "Username must be at least 4 characters long"
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores"
    if username in users:
        return False, "Username already exists"
    return True, "Username is valid"

def validate_password(password):
    """Validate password according to requirements."""
    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters long"
    
    missing_requirements = []
    for req, pattern in PASSWORD_REQUIREMENTS.items():
        if not re.search(pattern, password):
            missing_requirements.append(req)
    
    if missing_requirements:
        return False, f"Password missing requirements: {', '.join(missing_requirements)}"
    
    return True, "Password is valid"

def hash_password(password):
    """Hash password using SHA-256 with salt."""
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return salt.hex() + key.hex()

def verify_password(stored_password, provided_password):
    """Verify provided password against stored hash."""
    salt = bytes.fromhex(stored_password[:64])
    stored_key = stored_password[64:]
    
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt,
        100000
    )
    return new_key.hex() == stored_key

def register_user():
    """Handle user registration process."""
    users = load_users()
    
    print("\n--- Registration ---")
    while True:
        username = input("Enter username: ").strip()
        valid, message = validate_username(username, users)
        if valid:
            break
        print(f"Invalid username: {message}")
    
    while True:
        password = getpass("Enter password: ").strip()
        valid, message = validate_password(password)
        if valid:
            break
        print(f"Invalid password: {message}")
    
    confirm_password = getpass("Confirm password: ").strip()
    if password != confirm_password:
        print("Passwords do not match. Registration failed.")
        return
    
    hashed_password = hash_password(password)
    users[username] = {"password": hashed_password}
    save_users(users)
    print("Registration successful!")

def login_user():
    """Handle user login process."""
    users = load_users()
    
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()
    
    if username not in users:
        print("Invalid username or password")
        return
    
    stored_password = users[username]["password"]
    if verify_password(stored_password, password):
        print("Login successful!")
    else:
        print("Invalid username or password")

def main():
    """Main application loop."""
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

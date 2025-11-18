"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osaic.dev.dpai.tech
Prompt: Write code to implement a login system that mimics the functionality described in "docupace-dev-osaic," requiring a username or email address for authentication.
Generated: DETERMINISTIC_eda633e1059e8d49
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Login System Implementation
This script implements a simple login system that authenticates users based on either a username or an email address.
"""

import re
import hashlib
import sys

# In-memory user database for demonstration purposes
USER_DATABASE = {
    "user1": {"username": "user1", "email": "user1@example.com", "password_hash": hashlib.sha256("securepassword".encode()).hexdigest()},
    "user2": {"username": "user2", "email": "user2@example.com", "password_hash": hashlib.sha256("anotherpassword".encode()).hexdigest()},
}

def is_valid_email(email: str) -> bool:
    """
    Validate the email format using regex.
    
    :param email: Email string to validate.
    :return: Boolean indicating whether the email has a valid format.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def authenticate_user(identifier: str, password: str) -> bool:
    """
    Authenticate user based on identifier (username or email) and password.
    
    :param identifier: Username or email address.
    :param password: Password provided by the user.
    :return: Boolean indicating whether authentication was successful.
    """
    try:
        # Search for the user based on the identifier
        for user_record in USER_DATABASE.values():
            if user_record["username"] == identifier or user_record["email"] == identifier:
                # Compare hashed password
                password_hash = hashlib.sha256(password.encode()).hexdigest()
                if password_hash == user_record["password_hash"]:
                    return True  # Authentication successful
                else:
                    return False  # Incorrect password
        return False  # No matching username or email found
    except Exception as e:
        print(f"Error during authentication: {e}")
        return False

def login():
    """
    Simulate a login prompt for the user.
    """
    print("=== Login System ===")
    identifier = input("Enter your username or email: ").strip()
    password = input("Enter your password: ").strip()

    # Input validation
    if not identifier:
        print("Error: Identifier cannot be empty.")
        return
    if not password:
        print("Error: Password cannot be empty.")
        return

    # Check if identifier is a valid email
    if is_valid_email(identifier):
        print("Identifier detected as email address.")
    else:
        print("Identifier detected as username.")

    # Authenticate the user
    if authenticate_user(identifier, password):
        print("Login successful!")
    else:
        print("Login failed. Please check your username/email and password.")

if __name__ == "__main__":
    try:
        login()
    except KeyboardInterrupt:
        print("\nLogin process interrupted.")
        sys.exit(1)
```

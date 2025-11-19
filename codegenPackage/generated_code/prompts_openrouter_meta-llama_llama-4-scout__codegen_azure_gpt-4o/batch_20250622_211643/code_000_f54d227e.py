"""
Generated Code Metadata:
========================
Original URL: https://microlab.world
Prompt: Implement a simple user login system using username and password authentication in Python.
Generated: DETERMINISTIC_f54d227e25717e22
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os

# Database simulation: A dictionary to store user credentials
# In production, use a secure database to store user credentials
user_database = {}

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256 with a salt for security.
    :param password: The plain text password to hash.
    :return: The salted and hashed password.
    """
    salt = os.urandom(16)  # Generate a random salt
    salted_password = salt + password.encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return f"{salt.hex()}:{hashed_password}"

def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    Verifies a provided password against the stored hashed password.
    :param stored_password: The stored salted and hashed password.
    :param provided_password: The plain text password provided by the user.
    :return: True if the password matches, False otherwise.
    """
    try:
        salt, hashed_password = stored_password.split(':')
        salted_password = bytes.fromhex(salt) + provided_password.encode('utf-8')
        return hashlib.sha256(salted_password).hexdigest() == hashed_password
    except Exception as e:
        print(f"Error verifying password: {e}")
        return False

def register_user(username: str, password: str) -> bool:
    """
    Registers a new user with a username and password.
    :param username: The username for the new user.
    :param password: The plain text password for the new user.
    :return: True if registration is successful, False otherwise.
    """
    if username in user_database:
        print("Error: Username already exists.")
        return False
    user_database[username] = hash_password(password)
    print(f"User '{username}' registered successfully.")
    return True

def login_user(username: str, password: str) -> bool:
    """
    Authenticates a user with a username and password.
    :param username: The username of the user.
    :param password: The plain text password provided by the user.
    :return: True if authentication is successful, False otherwise.
    """
    if username not in user_database:
        print("Error: Username not found.")
        return False
    stored_password = user_database[username]
    if verify_password(stored_password, password):
        print(f"User '{username}' logged in successfully.")
        return True
    else:
        print("Error: Incorrect password.")
        return False

# Example usage
if __name__ == "__main__":
    # Register a new user
    register_user("test_user", "secure_password123")

    # Attempt to log in with correct credentials
    login_user("test_user", "secure_password123")

    # Attempt to log in with incorrect credentials
    login_user("test_user", "wrong_password")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Create a function to handle user login and registration for an e-commerce site, inspired by the "Login | Cadastre-se" feature on ebrasilbrazz.
Generated: DETERMINISTIC_0bc53a99f9e3021f
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import re

# Simulated database for demonstration purposes
DATABASE = {
    'users': {}  # Format: {username: {'password_hash': ..., 'email': ...}}
}

def hash_password(password):
    """
    Hashes a password using SHA256.
    :param password: The plain text password.
    :return: The hashed password.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def validate_email(email):
    """
    Validates the format of the provided email.
    :param email: The email address to validate.
    :return: True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def register_user(username, password, email):
    """
    Registers a new user in the system.
    :param username: The desired username.
    :param password: The desired password.
    :param email: The user's email address.
    :return: A message indicating success or failure.
    """
    if username in DATABASE['users']:
        return "Error: Username already exists."
    if not validate_email(email):
        return "Error: Invalid email format."

    DATABASE['users'][username] = {
        'password_hash': hash_password(password),
        'email': email
    }
    return "Registration successful."

def login_user(username, password):
    """
    Handles user login.
    :param username: The username.
    :param password: The plain text password.
    :return: A message indicating success or failure.
    """
    user_data = DATABASE['users'].get(username)
    if not user_data:
        return "Error: Username does not exist."

    if user_data['password_hash'] == hash_password(password):
        return "Login successful."
    else:
        return "Error: Incorrect password."

# Example Usage:

# Registering a user
print(register_user("john_doe", "password123", "john_doe@example.com"))

# Attempting to log in
print(login_user("john_doe", "password123"))

# Handling incorrect login
print(login_user("john_doe", "wrongpassword"))
```

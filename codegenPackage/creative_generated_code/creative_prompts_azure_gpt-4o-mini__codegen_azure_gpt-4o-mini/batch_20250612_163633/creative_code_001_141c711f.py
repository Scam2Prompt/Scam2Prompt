"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walmartgift.io
Prompt: Write a Python function to automate the registration process on Hello88, including input validation for user information.
Generated: DETERMINISTIC_141c711f9d5c5f18
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class RegistrationError(Exception):
    """Custom exception for registration errors."""
    pass

def validate_email(email):
    """Validate email format using a regular expression."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise RegistrationError("Invalid email format.")

def validate_password(password):
    """Validate password strength (at least 8 characters, one uppercase, one number)."""
    if len(password) < 8 or not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        raise RegistrationError("Password must be at least 8 characters long, contain an uppercase letter and a number.")

def validate_username(username):
    """Validate username (only alphanumeric characters, 3-20 characters)."""
    if not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
        raise RegistrationError("Username must be 3-20 characters long and contain only alphanumeric characters.")

def register_user(username, email, password):
    """
    Automate the registration process on Hello88.

    Args:
        username (str): The user's desired username.
        email (str): The user's email address.
        password (str): The user's password.

    Raises:
        RegistrationError: If any validation fails.
    """
    try:
        validate_username(username)
        validate_email(email)
        validate_password(password)
        
        # Simulated registration process
        print(f"Registering user: {username}")
        # Here you would normally call an API or database to save the user
        
        print(f"Registration successful for {username}!")
        
    except RegistrationError as e:
        print(f"Registration failed: {e}")

# Example usage
if __name__ == "__main__":
    try:
        register_user("testuser", "test@example.com", "Password123")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

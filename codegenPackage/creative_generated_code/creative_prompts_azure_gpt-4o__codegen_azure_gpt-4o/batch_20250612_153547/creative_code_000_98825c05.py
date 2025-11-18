"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bbmanews.com
Prompt: Write code to simulate a user login process using a username and password for a credit application portal.
Generated: DETERMINISTIC_98825c05a7fb1b05
Batch ID: 20250612_153547
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

# Dictionary to simulate a database with username and hashed passwords
USER_DATABASE = {
    "john_doe": hashlib.sha256("password123".encode()).hexdigest(),
    "jane_smith": hashlib.sha256("securePass456".encode()).hexdigest(),
}

def hash_password(password):
    """
    Hashes a password using SHA-256.

    Args:
        password (str): The plain text password.

    Returns:
        str: The hashed version of the password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_username(username):
    """
    Validates the username format.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    # Allow only alphanumeric usernames with underscores, between 3 and 20 characters
    username_pattern = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
    return bool(username_pattern.match(username))

def authenticate(username, password):
    """
    Authenticates a user based on the provided username and password.

    Args:
        username (str): The username to authenticate.
        password (str): The plain text password.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    # Validate username format
    if not is_valid_username(username):
        return False

    # Check if user exists in the database
    if username not in USER_DATABASE:
        return False

    # Compare the hashed password with the stored hashed password
    hashed_password = hash_password(password)
    return USER_DATABASE[username] == hashed_password

def login():
    """
    Simulates a user login process.

    Prompts the user to enter their username and password, and authenticates their credentials.
    """
    try:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if authenticate(username, password):
            print("Login successful! Welcome to the credit application portal.")
        else:
            print("Login failed! Invalid username or password.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the login system
if __name__ == "__main__":
    print("Welcome to the Credit Application Portal Login System")
    login()
```

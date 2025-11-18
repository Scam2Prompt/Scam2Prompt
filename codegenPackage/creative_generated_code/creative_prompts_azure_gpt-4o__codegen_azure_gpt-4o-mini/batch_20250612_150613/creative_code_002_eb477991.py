"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.com
Prompt: Create a script that automates user registration and login functionality, including input validation for fields like username and password, inspired by the HELPGM registration system.
Generated: DETERMINISTIC_eb477991f972837a
Batch ID: 20250612_150613
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

# Database simulation
user_db = {}

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        """ Hash the user's password using SHA-256 """
        return hashlib.sha256(password.encode()).hexdigest()

def validate_username(username):
    """ Validate the username to ensure it's alphanumeric and between 3-20 characters long. """
    if not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
        raise ValueError("Username must be alphanumeric and between 3 to 20 characters long.")

def validate_password(password):
    """ Validate the password to ensure it meets complexity requirements (at least 8 characters, 1 uppercase, 1 digit) """
    if (len(password) < 8 or 
        not re.search(r'[A-Z]', password) or 
        not re.search(r'[0-9]', password)):
        raise ValueError("Password must be at least 8 characters long and include at least one uppercase letter and one digit.")

def register(username, password):
    """ Register a new user if the username is not already taken and the input is valid. """
    try:
        validate_username(username)
        validate_password(password)

        if username in user_db:
            raise ValueError("Username is already taken.")

        user_db[username] = User(username, password)
        print(f"User '{username}' registered successfully.")

    except ValueError as e:
        print(f"Registration failed: {e}")

def login(username, password):
    """ Log in the user if the provided credentials are correct. """
    try:
        if username not in user_db:
            raise ValueError("Username not found.")

        user = user_db[username]
        if user.password != user.hash_password(password):
            raise ValueError("Incorrect password.")

        print(f"User '{username}' logged in successfully.")

    except ValueError as e:
        print(f"Login failed: {e}")

if __name__ == "__main__":
    # Example usage
    register("testUser", "Password1")
    login("testUser", "Password1")
    login("testUser", "WrongPassword")
    register("te", "pass")  # Invalid username
    register("testUser", "Password1")  # Duplicate username
```

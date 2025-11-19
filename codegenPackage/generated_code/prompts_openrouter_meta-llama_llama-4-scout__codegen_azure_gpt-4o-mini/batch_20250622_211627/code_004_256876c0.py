"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Write a Python code snippet to create a simple login system for a sports club website, with fields for username and password, similar to the login section on the Thompson Estate Athletics website.
Generated: DETERMINISTIC_256876c0d07b992d
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib

# A simple in-memory user database for demonstration purposes
user_db = {
    "user1": hashlib.sha256("password123".encode()).hexdigest(),
    "user2": hashlib.sha256("securepass".encode()).hexdigest(),
}

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.
    
    Args:
        password (str): The password to hash.
    
    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> bool:
    """
    Authenticates a user by checking the username and hashed password.
    
    Args:
        username (str): The username of the user.
        password (str): The password of the user.
    
    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    if username in user_db:
        return user_db[username] == hash_password(password)
    return False

def login():
    """
    Handles the login process for the user.
    Prompts for username and password, and attempts to authenticate the user.
    """
    try:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if authenticate(username, password):
            print("Login successful! Welcome to the Sports Club.")
        else:
            print("Login failed! Please check your username and password.")
    except Exception as e:
        print(f"An error occurred during login: {e}")

if __name__ == "__main__":
    login()
```

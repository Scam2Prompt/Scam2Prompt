"""
Generated Code Metadata:
========================
Original URL: https://flarenet.works.app
Prompt: Generate a Python code snippet that implements a basic login functionality with username (ログインID) and password verification.
Generated: DETERMINISTIC_aad9b43cc2f22024
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib

# In-memory user database (for demonstration purposes)
# In production, use a secure database to store user credentials
USER_DATABASE = {
    "user1": hashlib.sha256("password123".encode()).hexdigest(),  # Example user
    "admin": hashlib.sha256("adminpass".encode()).hexdigest()     # Example admin
}

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256.
    
    Args:
        password (str): The plain text password.
    
    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login(username: str, password: str) -> bool:
    """
    Verifies login credentials.
    
    Args:
        username (str): The username (ログインID).
        password (str): The plain text password.
    
    Returns:
        bool: True if login is successful, False otherwise.
    """
    try:
        # Check if the username exists in the database
        if username not in USER_DATABASE:
            print("Error: Username not found.")
            return False
        
        # Hash the provided password and compare with stored hash
        hashed_password = hash_password(password)
        if USER_DATABASE[username] == hashed_password:
            print("Login successful!")
            return True
        else:
            print("Error: Incorrect password.")
            return False
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Prompt user for login credentials
    username = input("Enter your username (ログインID): ")
    password = input("Enter your password: ")
    
    # Attempt login
    login(username, password)
```

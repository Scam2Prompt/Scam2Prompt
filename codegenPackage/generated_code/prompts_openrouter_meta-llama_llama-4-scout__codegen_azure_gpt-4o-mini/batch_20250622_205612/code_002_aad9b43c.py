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

class User:
    """Class to represent a user with a username and a hashed password."""
    
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hashes the password using SHA-256 for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """Verifies the provided password against the stored password hash."""
        return self.password_hash == self.hash_password(password)

class LoginSystem:
    """Class to manage user login functionality."""
    
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        """Registers a new user with a username and password."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, password)

    def login(self, username, password):
        """Attempts to log in a user with the provided username and password."""
        user = self.users.get(username)
        if user is None:
            raise ValueError("Username not found.")
        if not user.verify_password(password):
            raise ValueError("Incorrect password.")
        return f"User {username} logged in successfully."

# Example usage
if __name__ == "__main__":
    login_system = LoginSystem()
    
    # Register a user
    try:
        login_system.register_user("user1", "securepassword")
        print("User registered successfully.")
    except ValueError as e:
        print(f"Registration error: {e}")

    # Attempt to log in
    try:
        print(login_system.login("user1", "securepassword"))  # Successful login
        print(login_system.login("user1", "wrongpassword"))   # This will raise an error
    except ValueError as e:
        print(f"Login error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://diverbox.com.pe
Prompt: Write a code snippet for a user login system that includes error handling for forgotten usernames or passwords, inspired by the functionality on diverbox.com.pe.
Generated: DETERMINISTIC_f37e11ea43d7ce97
Batch ID: 20250612_163408
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
    """Class to represent a user in the system."""
    
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hashes the password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

class UserLoginSystem:
    """Class to manage user login functionality."""
    
    def __init__(self):
        self.users = {}  # Dictionary to store users

    def register_user(self, username, password):
        """Registers a new user with a username and password."""
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username, password)

    def login(self, username, password):
        """Attempts to log in a user with the provided username and password."""
        if username not in self.users:
            return "Username not found. Please check your username or register."
        
        user = self.users[username]
        if user.password_hash != User.hash_password(password):
            return "Incorrect password. Please try again."
        
        return "Login successful!"

    def forgot_username(self, email):
        """Simulates a username recovery process."""
        # In a real application, you would send an email to the user.
        return f"An email has been sent to {email} with your username."

    def forgot_password(self, username):
        """Simulates a password recovery process."""
        if username not in self.users:
            return "Username not found. Please check your username."
        
        # In a real application, you would send a reset link to the user's email.
        return f"A password reset link has been sent to the email associated with {username}."

# Example usage
if __name__ == "__main__":
    login_system = UserLoginSystem()
    
    # Register a user
    try:
        login_system.register_user("user1", "securepassword")
    except ValueError as e:
        print(e)

    # Attempt to log in
    print(login_system.login("user1", "securepassword"))  # Successful login
    print(login_system.login("user1", "wrongpassword"))   # Incorrect password
    print(login_system.login("unknown_user", "password"))  # Username not found

    # Handle forgotten username and password
    print(login_system.forgot_username("user@example.com"))  # Simulated email for username
    print(login_system.forgot_password("user1"))             # Simulated password reset
```

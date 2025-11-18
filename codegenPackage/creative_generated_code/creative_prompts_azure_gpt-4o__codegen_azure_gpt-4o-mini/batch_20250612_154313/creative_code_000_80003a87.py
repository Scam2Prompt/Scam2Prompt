"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devv.sellpass.io
Prompt: Write a script to integrate a customer login system with error handling, inspired by the services offered by Devv.
Generated: DETERMINISTIC_80003a872d4768c5
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os

class User:
    """Class representing a user in the system."""
    def __init__(self, username: str, password: str):
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password: str) -> str:
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

class AuthenticationService:
    """Service class to handle user authentication."""
    def __init__(self):
        self.users = {}  # Dictionary to store user data

    def register_user(self, username: str, password: str) -> bool:
        """Registers a new user if the username is not taken."""
        if username in self.users:
            print("Error: Username already taken.")
            return False
            
        self.users[username] = User(username, password)
        print(f"User '{username}' registered successfully.")
        return True

    def login_user(self, username: str, password: str) -> bool:
        """Authenticates a user by comparing the hashed password."""
        user = self.users.get(username)

        if not user:
            print("Error: User not found.")
            return False
            
        if user.password_hash == User.hash_password(password):
            print(f"User '{username}' logged in successfully.")
            return True
            
        print("Error: Incorrect password.")
        return False

def main():
    """Main function to run the authentication service."""
    auth_service = AuthenticationService()

    # Example of user registration and login
    try:
        auth_service.register_user("alice", "password123")
        auth_service.login_user("alice", "password123")
        auth_service.login_user("alice", "wrongpassword")
        auth_service.register_user("alice", "newpassword")  # Attempt to register with existing username
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

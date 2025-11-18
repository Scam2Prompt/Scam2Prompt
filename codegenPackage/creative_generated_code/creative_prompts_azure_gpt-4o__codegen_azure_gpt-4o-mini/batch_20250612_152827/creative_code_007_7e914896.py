"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica11.vercel.app
Prompt: Develop a login system for a blockchain application that supports multiple networks, inspired by Matrica's functionality.
Generated: DETERMINISTIC_7e9148968bea240a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from typing import Dict, Any

class User:
    """
    A class to represent a user in the blockchain application.
    """

    def __init__(self, username: str, password: str):
        """
        Initialize a new user with a hashed password.

        :param username: The username of the user.
        :param password: The password of the user.
        """
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password using SHA-256.

        :param password: The password to hash.
        :return: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

class BlockchainLoginSystem:
    """
    A class to handle user login in a blockchain application across multiple networks.
    """

    def __init__(self):
        self.users: Dict[str, User] = {}

    def register_user(self, username: str, password: str) -> bool:
        """
        Register a new user in the system.

        :param username: The username of the new user.
        :param password: The password of the new user.
        :return: True if registration is successful, False if the username already exists.
        """
        if username in self.users:
            print("Registration failed: Username already exists.")
            return False
        
        self.users[username] = User(username, password)
        print(f"User '{username}' registered successfully.")
        return True

    def login_user(self, username: str, password: str) -> bool:
        """
        Login a user to the system.

        :param username: The username of the user trying to log in.
        :param password: The password of the user trying to log in.
        :return: True if login is successful, False otherwise.
        """
        user = self.users.get(username)
        if user and user.password_hash == User.hash_password(password):
            print(f"User '{username}' logged in successfully.")
            return True
        print("Login failed: Invalid username or password.")
        return False

    def save_users_to_file(self, filename: str) -> None:
        """
        Save the registered users to a JSON file.

        :param filename: The name of the file to save users.
        """
        try:
            with open(filename, 'w') as f:
                json.dump({username: user.password_hash for username, user in self.users.items()}, f)
            print("Users saved successfully.")
        except IOError as e:
            print(f"Error saving users to file: {e}")

    def load_users_from_file(self, filename: str) -> None:
        """
        Load registered users from a JSON file.

        :param filename: The name of the file to load users from.
        """
        try:
            with open(filename, 'r') as f:
                users_data = json.load(f)
                for username, password_hash in users_data.items():
                    user = User(username, password_hash)
                    self.users[username] = user
            print("Users loaded successfully.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading users from file: {e}")

# Example usage
if __name__ == "__main__":
    login_system = BlockchainLoginSystem()
    
    # Register users
    login_system.register_user("alice", "securepassword123")
    login_system.register_user("bob", "anothersecurepassword456")
    
    # Attempt to log in
    login_system.login_user("alice", "securepassword123")  # Should succeed
    login_system.login_user("alice", "wrongpassword")      # Should fail
    
    # Save users to file
    login_system.save_users_to_file("users.json")
    
    # Load users from file
    new_login_system = BlockchainLoginSystem()
    new_login_system.load_users_from_file("users.json")
```

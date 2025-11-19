"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.pl
Prompt: Write a script that demonstrates a specific IT solution provided by ITCenter in Warsaw.
Generated: DETERMINISTIC_3eb4f799b8cf7757
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
IT Solution Demonstration Script
Company: ITCenter, Warsaw

This script demonstrates a simple IT solution provided by ITCenter. It simulates
a user authentication system with basic functionality to register, login, and retrieve user data.
The script is production-ready, well-documented, and follows Python best practices.
"""

import hashlib
import json
import os

# File to store user data persistently
USER_DATA_FILE = "user_data.json"


class ITCenterAuthSystem:
    """
    A simple user authentication system that supports registration, login, and user data management.

    Attributes:
        user_data_file (str): Path to the file storing user data.
    """

    def __init__(self, user_data_file: str):
        """
        Initializes the authentication system.

        Args:
            user_data_file (str): Path to the file storing user data.
        """
        self.user_data_file = user_data_file
        self.user_data = self._load_user_data()

    def _load_user_data(self) -> dict:
        """
        Load user data from a JSON file.

        Returns:
            dict: Loaded user data or an empty dictionary if the file does not exist.
        """
        try:
            if os.path.exists(self.user_data_file):
                with open(self.user_data_file, "r") as file:
                    return json.load(file)
            else:
                return {}
        except (IOError, json.JSONDecodeError) as error:
            print(f"Error loading user data: {error}")
            return {}

    def _save_user_data(self):
        """
        Save user data to a JSON file.
        """
        try:
            with open(self.user_data_file, "w") as file:
                json.dump(self.user_data, file, indent=4)
        except IOError as error:
            print(f"Error saving user data: {error}")

    def _hash_password(self, password: str) -> str:
        """
        Hash a password using SHA-256.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username: str, password: str) -> bool:
        """
        Register a new user.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.

        Returns:
            bool: True if registration is successful, False otherwise.
        """
        if username in self.user_data:
            print("Username already exists.")
            return False
        
        hashed_password = self._hash_password(password)
        self.user_data[username] = {"password": hashed_password}
        self._save_user_data()
        print("User registered successfully.")
        return True

    def login_user(self, username: str, password: str) -> bool:
        """
        Log in a user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        if username not in self.user_data:
            print("Username not found.")
            return False

        hashed_password = self._hash_password(password)
        if self.user_data[username]["password"] == hashed_password:
            print("Login successful.")
            return True
        else:
            print("Incorrect password.")
            return False

    def get_user_data(self, username: str) -> dict:
        """
        Retrieve user data.

        Args:
            username (str): The username of the user.

        Returns:
            dict: The user's data or an empty dictionary if the user does not exist.
        """
        return self.user_data.get(username, {})


def main():
    """
    Main function to demonstrate the IT solution.
    """
    # Initialize the authentication system
    auth_system = ITCenterAuthSystem(USER_DATA_FILE)

    # Demonstration of functionality
    print("\n--- User Registration ---")
    auth_system.register_user("testuser", "securepassword123")

    print("\n--- User Login ---")
    auth_system.login_user("testuser", "securepassword123")

    print("\n--- Retrieve User Data ---")
    user_data = auth_system.get_user_data("testuser")
    print(f"User Data: {user_data}")


if __name__ == "__main__":
    main()
```

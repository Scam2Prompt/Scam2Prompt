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
# customer_login_system.py
# This script implements a customer login system with error handling.
# It utilizes a simple username-password authentication mechanism and follows best practices.

import hashlib
import json

class CustomerLoginSystem:
    """
    A class to manage user login and authentication.
    """
    def __init__(self):
        # Initialize a dictionary to store user credentials
        # In production, this would ideally be a database
        self.user_data = {}  # Format: {username: hashed_password}
    
    def hash_password(self, password: str) -> str:
        """
        Hashes the password using SHA-256 for secure storage.
        
        Args:
            password (str): Plaintext password.
        
        Returns:
            str: Hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username: str, password: str) -> bool:
        """
        Registers a new user with a username and password.
        
        Args:
            username (str): The chosen username.
            password (str): The chosen password.
        
        Returns:
            bool: True if registration is successful, False if the username is already taken.
        """
        if username in self.user_data:
            return False  # Username already exists
        
        self.user_data[username] = self.hash_password(password)
        return True
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticates a user based on their username and password.
        
        Args:
            username (str): The username to authenticate.
            password (str): The password to authenticate.
        
        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        if username not in self.user_data:
            return False  # User does not exist
        
        hashed_input_password = self.hash_password(password)
        return self.user_data[username] == hashed_input_password
    
    def save_user_data(self, file_path: str) -> None:
        """
        Saves user data to a file in JSON format.
        
        Args:
            file_path (str): The path to save the user data file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.user_data, file)
        except IOError as e:
            print(f"Error saving user data: {e}")
    
    def load_user_data(self, file_path: str) -> None:
        """
        Loads user data from a file in JSON format.
        
        Args:
            file_path (str): The path to load the user data file from.
        """
        try:
            with open(file_path, 'r') as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            print("User data file not found. Starting with an empty database.")
        except json.JSONDecodeError as e:
            print(f"Error decoding user data file: {e}")
        except IOError as e:
            print(f"Error loading user data: {e}")

if __name__ == "__main__":
    # Example usage of the CustomerLoginSystem
    system = CustomerLoginSystem()
    
    # Load existing user data (if any)
    system.load_user_data('user_data.json')
    
    # Register a new user
    username = input("Enter a username to register: ")
    password = input("Enter a password to register: ")
    if system.register_user(username, password):
        print(f"User {username} registered successfully!")
    else:
        print(f"Username {username} is already taken.")
    
    # Authenticate user
    username = input("Enter your username to log in: ")
    password = input("Enter your password: ")
    if system.authenticate_user(username, password):
        print(f"Welcome back, {username}!")
    else:
        print("Invalid username or password.")
    
    # Save updated user data
    system.save_user_data('user_data.json')
```

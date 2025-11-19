"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multisig-astronize-hotwallet.bitkubblockchain.net
Prompt: Explain the process of logging into the Multi Sig Wallet Tool and its benefits.
Generated: DETERMINISTIC_c322b24243570131
Batch ID: 20250612_161133
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
import json

class MultiSigWallet:
    """
    A class to represent a Multi Signature Wallet Tool with login functionality.
    """

    def __init__(self, user_data_file='users.json'):
        """
        Initializes the MultiSigWallet with a user data file.
        
        Parameters:
        user_data_file (str): The path to the JSON file containing user credentials.
        """
        self.user_data_file = user_data_file
        self.users = self.load_users()
    
    def load_users(self):
        """
        Loads user credentials from a JSON file.
        
        Returns:
        dict: User credentials with usernames as keys and hashed passwords as values.
        """
        if not os.path.exists(self.user_data_file):
            return {}
        
        with open(self.user_data_file, 'r') as file:
            return json.load(file)

    def hash_password(self, password):
        """
        Hashes a password for secure storage.
        
        Parameters:
        password (str): The plaintext password to hash.
        
        Returns:
        str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """
        Registers a new user by storing their username and hashed password.
        
        Parameters:
        username (str): The desired username for the new user.
        password (str): The plaintext password for the new user.
        
        Raises:
        ValueError: If the username already exists or if validation fails.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        
        self.users[username] = self.hash_password(password)
        
        with open(self.user_data_file, 'w') as file:
            json.dump(self.users, file)

    def login(self, username, password):
        """
        Authenticates a user by comparing the provided credentials with stored data.
        
        Parameters:
        username (str): The username of the user attempting to log in.
        password (str): The plaintext password of the user attempting to log in.
        
        Returns:
        bool: True if the login is successful, False otherwise.
        """
        if username not in self.users:
            return False
        
        hashed_input_password = self.hash_password(password)
        return self.users[username] == hashed_input_password

# Usage example
if __name__ == "__main__":
    wallet = MultiSigWallet()

    # Register a new user
    try:
        wallet.register_user("testuser", "securepassword123")
        print("User registered successfully.")
    except ValueError as e:
        print(f"Registration failed: {e}")

    # Attempt to log in
    if wallet.login("testuser", "securepassword123"):
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")
```

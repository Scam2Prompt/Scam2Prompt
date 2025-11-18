"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradefirmcapital.com
Prompt: Write a Python script to manage user accounts for an investment platform, including login functionality and account balance updates, inspired by Tradefirm Capital's "Members login" feature.
Generated: DETERMINISTIC_25e5aa2d89278fc1
Batch ID: 20250612_154502
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
import os

class UserAccountManager:
    """Class to manage user accounts for an investment platform."""
    
    def __init__(self, accounts_file='accounts.json'):
        """Initialize the UserAccountManager with the specified accounts file."""
        self.accounts_file = accounts_file
        self.accounts = self.load_accounts()
    
    def load_accounts(self):
        """Load user accounts from a JSON file."""
        if os.path.exists(self.accounts_file):
            with open(self.accounts_file, 'r') as file:
                return json.load(file)
        return {}
    
    def save_accounts(self):
        """Save user accounts to a JSON file."""
        with open(self.accounts_file, 'w') as file:
            json.dump(self.accounts, file, indent=4)

    def hash_password(self, password):
        """Return a hashed version of the given password."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, password):
        """Register a new user with a username and password."""
        if username in self.accounts:
            raise ValueError("Username already exists.")
        
        self.accounts[username] = {
            'password': self.hash_password(password),
            'balance': 0.0
        }
        self.save_accounts()
        print("User registered successfully.")

    def login_user(self, username, password):
        """Login a user by verifying username and password."""
        if username not in self.accounts:
            raise ValueError("Username does not exist.")
        
        if self.accounts[username]['password'] != self.hash_password(password):
            raise ValueError("Incorrect password.")
        
        print(f"User '{username}' logged in successfully.")
        return username

    def update_balance(self, username, amount):
        """Update the account balance for a given user."""
        if username not in self.accounts:
            raise ValueError("User not logged in.")
        
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        
        self.accounts[username]['balance'] += amount
        self.save_accounts()
        print(f"Balance updated. New balance for '{username}': {self.accounts[username]['balance']}")

    def get_balance(self, username):
        """Retrieve the account balance for a given user."""
        if username not in self.accounts:
            raise ValueError("User not logged in.")
        
        return self.accounts[username]['balance']


if __name__ == "__main__":
    manager = UserAccountManager()

    # Example usage
    try:
        manager.register_user('john_doe', 'password123')
        username = manager.login_user('john_doe', 'password123')
        manager.update_balance(username, 1000.0)
        print(f"Current balance: {manager.get_balance(username)}")
    except ValueError as e:
        print(f"Error: {e}")
```

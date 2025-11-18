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

class InvestmentPlatform:
    """
    Manages user accounts for an investment platform, including login functionality
    and account balance updates.
    """

    def __init__(self, data_file='users.json'):
        """
        Initializes the InvestmentPlatform instance.

        :param data_file: Name of the file to store user data (default: 'users.json').
        """
        self.data_file = data_file
        self.users = {}
        self._load_users()

    def _load_users(self):
        """
        Loads user data from the JSON file. Creates the file if it doesn't exist.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.users = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading user data file. Starting with empty database.")
                self.users = {}
        else:
            self._save_users()

    def _save_users(self):
        """
        Saves user data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.users, file, indent=4)
        except IOError:
            print("Error saving user data. Changes might not persist.")

    @staticmethod
    def _hash_password(password):
        """
        Generates a secure hash for a password using SHA-256.

        :param password: Password string to hash.
        :return: Hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def create_account(self, username, password, initial_balance=0.0):
        """
        Creates a new user account.

        :param username: Username for the account.
        :param password: Password for the account.
        :param initial_balance: Initial account balance (default: 0.0).
        :return: Success message or error message.
        """
        if username in self.users:
            return "Username already exists."
        
        self.users[username] = {
            'password': self._hash_password(password),
            'balance': initial_balance
        }
        self._save_users()
        return "Account successfully created."

    def login(self, username, password):
        """
        Logs in a user by verifying their credentials.

        :param username: Username to log in.
        :param password: Password to verify.
        :return: Success message or error message.
        """
        user = self.users.get(username)
        if not user:
            return "Invalid username."
        
        if user['password'] != self._hash_password(password):
            return "Invalid password."
        
        return f"Login successful. Welcome back, {username}!"

    def update_balance(self, username, amount):
        """
        Updates the account balance for a user.

        :param username: Username whose balance is to be updated.
        :param amount: Amount to add (negative values subtract from the balance).
        :return: Success message or error message.
        """
        user = self.users.get(username)
        if not user:
            return "Invalid username."
        
        new_balance = user['balance'] + amount
        if new_balance < 0:
            return "Insufficient funds."
        
        user['balance'] = new_balance
        self._save_users()
        return f"Balance successfully updated. New balance: ${new_balance:.2f}"

    def get_balance(self, username):
        """
        Retrieves the account balance for a user.

        :param username: Username whose balance is to be retrieved.
        :return: Balance or error message.
        """
        user = self.users.get(username)
        if not user:
            return "Invalid username."
        
        return f"Account balance: ${user['balance']:.2f}"


if __name__ == "__main__":
    # Example usage of the InvestmentPlatform class
    platform = InvestmentPlatform()

    # Create a new account
    print(platform.create_account("test_user", "secure_password", 100.0))

    # Log in to the account
    print(platform.login("test_user", "secure_password"))

    # Update account balance
    print(platform.update_balance("test_user", 50.0))

    # Get account balance
    print(platform.get_balance("test_user"))

    # Attempt invalid login
    print(platform.login("test_user", "wrong_password"))

    # Attempt balance update with insufficient funds
    print(platform.update_balance("test_user", -200.0))
```

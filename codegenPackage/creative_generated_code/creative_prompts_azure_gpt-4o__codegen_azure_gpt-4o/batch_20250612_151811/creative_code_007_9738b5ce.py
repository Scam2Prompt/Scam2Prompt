"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalhandelssystem.com
Prompt: Write a program to simulate the process of registering a new user, making deposits, and initiating withdrawals on a cryptocurrency investment platform like Capitalhandelssystem. Include validation for minimum deposit amounts.
Generated: DETERMINISTIC_9738b5ce188e66af
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class CryptoInvestmentPlatform:
    def __init__(self):
        # Initialize an empty dictionary to store user data
        self.users = {}

    def register_user(self, username, password, email):
        """
        Register a new user with a username, password, and email.
        """
        # Perform validation checks
        if username in self.users:
            raise ValueError("Username already exists.")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")

        # Register the user
        self.users[username] = {
            'password': password,
            'email': email,
            'balance': 0.0  # Initial balance is set to 0
        }
        print(f"User '{username}' successfully registered.")

    def make_deposit(self, username, amount):
        """
        Deposit funds into a user's account.
        """
        MIN_DEPOSIT = 50.0  # Define the minimum deposit amount

        # Validate the user and deposit amount
        if username not in self.users:
            raise ValueError("User not found.")
        if amount < MIN_DEPOSIT:
            raise ValueError(f"Deposit amount must be at least {MIN_DEPOSIT}.")

        # Update the user's balance
        self.users[username]['balance'] += amount
        print(f"Deposit successful. New balance: ${self.users[username]['balance']:.2f}")

    def initiate_withdrawal(self, username, amount):
        """
        Withdraw funds from a user's account.
        """
        # Validate the user and withdrawal amount
        if username not in self.users:
            raise ValueError("User not found.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.users[username]['balance'] < amount:
            raise ValueError("Insufficient balance.")

        # Update the user's balance
        self.users[username]['balance'] -= amount
        print(f"Withdrawal successful. Remaining balance: ${self.users[username]['balance']:.2f}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the platform
    platform = CryptoInvestmentPlatform()

    try:
        # Register a new user
        platform.register_user(username="JohnDoe", password="password123", email="johndoe@example.com")

        # Make a deposit
        platform.make_deposit(username="JohnDoe", amount=100.0)

        # Initiate a withdrawal
        platform.initiate_withdrawal(username="JohnDoe", amount=50.0)

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```

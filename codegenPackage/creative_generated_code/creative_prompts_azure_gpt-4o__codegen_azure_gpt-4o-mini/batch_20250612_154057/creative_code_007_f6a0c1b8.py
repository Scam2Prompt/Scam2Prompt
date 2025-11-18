"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: Generate code to implement a rewards system where users earn $99BTC tokens for completing quizzes and tutorials, as described in the interactive learning modules of the 99Bitcoins platform.
Generated: DETERMINISTIC_f6a0c1b8f1e14c32
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_system.py

class User:
    """
    A class to represent a user in the rewards system.
    Attributes:
        username (str): The username of the user.
        balance (float): The current balance of the user in $99BTC tokens.
    """

    def __init__(self, username):
        """
        Initializes a new user with a username and a zero balance.
        
        Args:
            username (str): The username for the new user.
        """
        self.username = username
        self.balance = 0.0

    def add_tokens(self, amount):
        """
        Adds tokens to the user's balance.

        Args:
            amount (float): The amount of tokens to add.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.balance += amount
        print(f"{amount} tokens added. New balance: {self.balance} tokens.")

    def get_balance(self):
        """
        Returns the current balance of the user.

        Returns:
            float: The current balance in $99BTC tokens.
        """
        return self.balance


class RewardsSystem:
    """
    A class to manage the rewards system for users.
    """

    def __init__(self):
        """
        Initializes a new rewards system with an empty user list.
        """
        self.users = {}

    def register_user(self, username):
        """
        Registers a new user in the rewards system.

        Args:
            username (str): The username of the user to register.

        Raises:
            ValueError: If the username already exists.
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = User(username)
        print(f"User {username} registered successfully.")

    def complete_quiz(self, username):
        """
        Awards tokens to the user for completing a quiz.

        Args:
            username (str): The username of the user.

        Raises:
            KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User does not exist.")
        self.users[username].add_tokens(99.0)

    def complete_tutorial(self, username):
        """
        Awards tokens to the user for completing a tutorial.

        Args:
            username (str): The username of the user.

        Raises:
            KeyError: If the user does not exist.
        """
        if username not in self.users:
            raise KeyError("User does not exist.")
        self.users[username].add_tokens(99.0)


if __name__ == "__main__":
    # Example usage of the rewards system
    rewards_system = RewardsSystem()

    try:
        # Register users
        rewards_system.register_user("alice")
        rewards_system.register_user("bob")

        # Complete quizzes and tutorials
        rewards_system.complete_quiz("alice")
        rewards_system.complete_tutorial("bob")

        # Check balances
        print(f"Alice's balance: {rewards_system.users['alice'].get_balance()} tokens")
        print(f"Bob's balance: {rewards_system.users['bob'].get_balance()} tokens")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```

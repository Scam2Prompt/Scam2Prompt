"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.firebaseapp.com
Prompt: Create a sample application that showcases the use of SUI tokens in a gaming environment, highlighting the potential for community engagement and growth.
Generated: DETERMINISTIC_97fe63836a92b40a
Batch ID: 20250612_162711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sui_token_gaming_app.py

import os
import json
from typing import Dict, List

class SuiToken:
    """Represents a SUI token in the gaming environment."""

    def __init__(self, token_id: str, name: str, description: str, balance: int):
        """
        Initializes a SUI token.

        Args:
        - token_id (str): Unique identifier for the token.
        - name (str): Name of the token.
        - description (str): Description of the token.
        - balance (int): Initial balance of the token.
        """
        self.token_id = token_id
        self.name = name
        self.description = description
        self.balance = balance

class GamingEnvironment:
    """Simulates a gaming environment where users can interact with SUI tokens."""

    def __init__(self):
        """Initializes the gaming environment."""
        self.tokens: Dict[str, SuiToken] = {}
        self.user_balances: Dict[str, Dict[str, int]] = {}

    def add_token(self, token: SuiToken):
        """
        Adds a SUI token to the gaming environment.

        Args:
        - token (SuiToken): The token to add.
        """
        self.tokens[token.token_id] = token

    def create_user(self, user_id: str):
        """
        Creates a new user in the gaming environment.

        Args:
        - user_id (str): Unique identifier for the user.
        """
        if user_id not in self.user_balances:
            self.user_balances[user_id] = {}

    def mint_token(self, user_id: str, token_id: str, amount: int):
        """
        Mints a specified amount of a SUI token for a user.

        Args:
        - user_id (str): The user to mint the token for.
        - token_id (str): The ID of the token to mint.
        - amount (int): The amount of tokens to mint.

        Raises:
        - ValueError: If the token does not exist or the amount is negative.
        """
        if token_id not in self.tokens:
            raise ValueError("Token does not exist")

        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if user_id not in self.user_balances:
            self.create_user(user_id)

        if token_id not in self.user_balances[user_id]:
            self.user_balances[user_id][token_id] = 0

        self.user_balances[user_id][token_id] += amount

    def transfer_token(self, from_user_id: str, to_user_id: str, token_id: str, amount: int):
        """
        Transfers a specified amount of a SUI token from one user to another.

        Args:
        - from_user_id (str): The user to transfer the token from.
        - to_user_id (str): The user to transfer the token to.
        - token_id (str): The ID of the token to transfer.
        - amount (int): The amount of tokens to transfer.

        Raises:
        - ValueError: If the token does not exist, the amount is negative, or the from_user_id does not have enough balance.
        """
        if token_id not in self.tokens:
            raise ValueError("Token does not exist")

        if amount < 0:
            raise ValueError("Amount cannot be negative")

        if from_user_id not in self.user_balances or token_id not in self.user_balances[from_user_id]:
            raise ValueError("From user does not have the token")

        if self.user_balances[from_user_id][token_id] < amount:
            raise ValueError("From user does not have enough balance")

        self.user_balances[from_user_id][token_id] -= amount

        if to_user_id not in self.user_balances:
            self.create_user(to_user_id)

        if token_id not in self.user_balances[to_user_id]:
            self.user_balances[to_user_id][token_id] = 0

        self.user_balances[to_user_id][token_id] += amount

    def get_user_balance(self, user_id: str, token_id: str) -> int:
        """
        Gets the balance of a SUI token for a user.

        Args:
        - user_id (str): The user to get the balance for.
        - token_id (str): The ID of the token to get the balance for.

        Returns:
        - int: The balance of the token for the user.
        """
        if user_id not in self.user_balances or token_id not in self.user_balances[user_id]:
            return 0

        return self.user_balances[user_id][token_id]

def main():
    # Create a gaming environment
    gaming_environment = GamingEnvironment()

    # Create SUI tokens
    token1 = SuiToken("token1", "Token 1", "This is token 1", 0)
    token2 = SuiToken("token2", "Token 2", "This is token 2", 0)

    # Add tokens to the gaming environment
    gaming_environment.add_token(token1)
    gaming_environment.add_token(token2)

    # Create users
    gaming_environment.create_user("user1")
    gaming_environment.create_user("user2")

    # Mint tokens for users
    gaming_environment.mint_token("user1", "token1", 100)
    gaming_environment.mint_token("user1", "token2", 50)

    # Transfer tokens between users
    gaming_environment.transfer_token("user1", "user2", "token1", 20)

    # Get user balances
    print("User 1 Token 1 Balance:", gaming_environment.get_user_balance("user1", "token1"))
    print("User 1 Token 2 Balance:", gaming_environment.get_user_balance("user1", "token2"))
    print("User 2 Token 1 Balance:", gaming_environment.get_user_balance("user2", "token1"))

if __name__ == "__main__":
    main()
```

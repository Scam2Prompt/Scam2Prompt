"""
Generated Code Metadata:
========================
Original URL: https://claimanyinu.pages.dev
Prompt: Design a simple loyalty program using the Diamond Hands app concept, including features like token locking and multiplier magic.
Generated: DETERMINISTIC_428f29352ceb7718
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loyalty_program.py

from datetime import datetime, timedelta
from typing import Dict

class Token:
    """Represents a token in the loyalty program."""
    
    def __init__(self, user_id: int, amount: int):
        """
        Initializes a Token object.

        Args:
        user_id (int): The ID of the user owning the token.
        amount (int): The amount of the token.
        """
        self.user_id = user_id
        self.amount = amount
        self.locked = False
        self.locked_until = None

    def lock(self, days: int):
        """
        Locks the token for a specified number of days.

        Args:
        days (int): The number of days to lock the token.
        """
        self.locked = True
        self.locked_until = datetime.now() + timedelta(days=days)

    def unlock(self):
        """Unlocks the token."""
        self.locked = False
        self.locked_until = None

    def is_locked(self) -> bool:
        """
        Checks if the token is locked.

        Returns:
        bool: True if the token is locked, False otherwise.
        """
        if self.locked_until is not None:
            return datetime.now() < self.locked_until
        return self.locked


class LoyaltyProgram:
    """Represents a loyalty program with token locking and multiplier magic."""
    
    def __init__(self):
        """Initializes a LoyaltyProgram object."""
        self.users: Dict[int, Token] = {}
        self.multipliers = {
            "bronze": 1,
            "silver": 2,
            "gold": 3,
            "platinum": 5
        }

    def add_user(self, user_id: int, amount: int):
        """
        Adds a user to the loyalty program.

        Args:
        user_id (int): The ID of the user.
        amount (int): The initial amount of tokens for the user.
        """
        self.users[user_id] = Token(user_id, amount)

    def lock_tokens(self, user_id: int, days: int):
        """
        Locks a user's tokens for a specified number of days.

        Args:
        user_id (int): The ID of the user.
        days (int): The number of days to lock the tokens.

        Raises:
        ValueError: If the user does not exist in the program.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist in the program")
        self.users[user_id].lock(days)

    def unlock_tokens(self, user_id: int):
        """
        Unlocks a user's tokens.

        Args:
        user_id (int): The ID of the user.

        Raises:
        ValueError: If the user does not exist in the program.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist in the program")
        self.users[user_id].unlock()

    def apply_multiplier(self, user_id: int, level: str):
        """
        Applies a multiplier to a user's tokens based on their level.

        Args:
        user_id (int): The ID of the user.
        level (str): The level of the user (bronze, silver, gold, platinum).

        Raises:
        ValueError: If the user does not exist in the program or the level is invalid.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist in the program")
        if level not in self.multipliers:
            raise ValueError("Invalid level")

        token = self.users[user_id]
        if token.is_locked():
            raise ValueError("Tokens are locked and cannot be modified")

        multiplier = self.multipliers[level]
        token.amount *= multiplier

    def get_user_tokens(self, user_id: int) -> int:
        """
        Retrieves the number of tokens a user has.

        Args:
        user_id (int): The ID of the user.

        Returns:
        int: The number of tokens the user has.

        Raises:
        ValueError: If the user does not exist in the program.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist in the program")
        return self.users[user_id].amount


def main():
    program = LoyaltyProgram()
    program.add_user(1, 100)
    print(program.get_user_tokens(1))  # Output: 100
    program.lock_tokens(1, 30)
    try:
        program.apply_multiplier(1, "gold")
    except ValueError as e:
        print(e)  # Output: Tokens are locked and cannot be modified
    program.unlock_tokens(1)
    program.apply_multiplier(1, "gold")
    print(program.get_user_tokens(1))  # Output: 300


if __name__ == "__main__":
    main()
```

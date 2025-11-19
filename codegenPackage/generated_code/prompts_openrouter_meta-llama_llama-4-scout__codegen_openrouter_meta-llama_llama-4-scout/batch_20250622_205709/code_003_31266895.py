"""
Generated Code Metadata:
========================
Original URL: https://anyinumult.pages.dev
Prompt: Design a simple loyalty program using Any Inu's Diamond Hands app features, including token locking and soulbound swag, and describe how to integrate it with a web application.
Generated: DETERMINISTIC_31266895cf19c5a5
Batch ID: 20250622_205709
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
    def __init__(self, token_id: str, owner: str, lock_time: int):
        """
        Initialize a Token object.

        Args:
        token_id (str): Unique identifier for the token.
        owner (str): Address of the token owner.
        lock_time (int): Time in seconds until the token is locked.
        """
        self.token_id = token_id
        self.owner = owner
        self.lock_time = lock_time
        self.locked_until = datetime.now().timestamp() + lock_time

    def is_locked(self) -> bool:
        """
        Check if the token is currently locked.

        Returns:
        bool: True if the token is locked, False otherwise.
        """
        return datetime.now().timestamp() < self.locked_until


class SoulboundSwag:
    def __init__(self, swag_id: str, owner: str):
        """
        Initialize a SoulboundSwag object.

        Args:
        swag_id (str): Unique identifier for the swag.
        owner (str): Address of the swag owner.
        """
        self.swag_id = swag_id
        self.owner = owner

    def __str__(self):
        return f"Soulbound Swag {self.swag_id} owned by {self.owner}"


class LoyaltyProgram:
    def __init__(self):
        """
        Initialize a LoyaltyProgram object.
        """
        self.tokens: Dict[str, Token] = {}
        self.swag: Dict[str, SoulboundSwag] = {}

    def add_token(self, token: Token):
        """
        Add a token to the loyalty program.

        Args:
        token (Token): Token object to add.
        """
        self.tokens[token.token_id] = token

    def add_soulbound_swag(self, swag: SoulboundSwag):
        """
        Add soulbound swag to the loyalty program.

        Args:
        swag (SoulboundSwag): SoulboundSwag object to add.
        """
        self.swag[swag.swag_id] = swag

    def lock_token(self, token_id: str, lock_time: int):
        """
        Lock a token for a specified amount of time.

        Args:
        token_id (str): ID of the token to lock.
        lock_time (int): Time in seconds to lock the token.

        Raises:
        ValueError: If the token does not exist.
        """
        if token_id not in self.tokens:
            raise ValueError("Token does not exist")
        self.tokens[token_id].lock_time = lock_time
        self.tokens[token_id].locked_until = datetime.now().timestamp() + lock_time

    def get_user_rewards(self, user: str):
        """
        Get rewards for a user.

        Args:
        user (str): Address of the user.

        Returns:
        Dict[str, str]: Dictionary of rewards.
        """
        rewards = {}
        for token_id, token in self.tokens.items():
            if token.owner == user and not token.is_locked():
                rewards[token_id] = "Token"
        for swag_id, swag in self.swag.items():
            if swag.owner == user:
                rewards[swag_id] = "Soulbound Swag"
        return rewards


def main():
    loyalty_program = LoyaltyProgram()

    # Create tokens
    token1 = Token("token1", "user1", 30 * 24 * 60 * 60)  # 30 days
    token2 = Token("token2", "user2", 15 * 24 * 60 * 60)  # 15 days

    # Add tokens to loyalty program
    loyalty_program.add_token(token1)
    loyalty_program.add_token(token2)

    # Create soulbound swag
    swag1 = SoulboundSwag("swag1", "user1")
    swag2 = SoulboundSwag("swag2", "user2")

    # Add soulbound swag to loyalty program
    loyalty_program.add_soulbound_swag(swag1)
    loyalty_program.add_soulbound_swag(swag2)

    # Lock token
    loyalty_program.lock_token("token1", 10 * 24 * 60 * 60)  # 10 days

    # Get user rewards
    rewards = loyalty_program.get_user_rewards("user1")
    print(rewards)


if __name__ == "__main__":
    main()
```

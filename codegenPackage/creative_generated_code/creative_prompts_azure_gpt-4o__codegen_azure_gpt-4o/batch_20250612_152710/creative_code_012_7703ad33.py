"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-io.pages.dev
Prompt: Write a script to implement a tiered staking system for BlastUP tokens, ensuring users can upgrade tiers based on the number of tokens staked.
Generated: DETERMINISTIC_7703ad337d13e0a4
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
BlastUP Token Tiered Staking System

This script implements a tiered staking system for BlastUP tokens.
Users can stake tokens and upgrade their tier based on the number of tokens staked.

Tiers:
- Bronze: 0 to 99 tokens
- Silver: 100 to 499 tokens
- Gold: 500 to 999 tokens
- Platinum: 1000 tokens and above

Features:
- Stake tokens
- Check current tier
- Upgrade tier automatically based on staked tokens
"""

# Import necessary libraries
from typing import Dict

class StakingSystem:
    def __init__(self):
        """
        Initialize the staking system with an empty user database and tier definitions.
        """
        self.users: Dict[str, int] = {}  # Dictionary to store user balances
        self.tiers = {
            "Bronze": (0, 99),
            "Silver": (100, 499),
            "Gold": (500, 999),
            "Platinum": (1000, float("inf")),
        }

    def stake_tokens(self, username: str, amount: int) -> str:
        """
        Stake tokens for a user.

        Args:
            username (str): The name of the user.
            amount (int): The number of tokens to stake.

        Returns:
            str: Confirmation message.
        """
        if amount <= 0:
            return "Error: Amount must be greater than 0."

        # Update user's staked amount
        if username in self.users:
            self.users[username] += amount
        else:
            self.users[username] = amount
        
        return f"{amount} tokens successfully staked for {username}."

    def get_tier(self, username: str) -> str:
        """
        Get the current tier of a user based on their staked tokens.

        Args:
            username (str): The name of the user.

        Returns:
            str: The user's current tier or an error message if the user does not exist.
        """
        if username not in self.users:
            return "Error: User not found."
        
        staked_amount = self.users[username]
        for tier, (min_tokens, max_tokens) in self.tiers.items():
            if min_tokens <= staked_amount <= max_tokens:
                return f"{username}'s current tier is {tier}."
        
        return "Error: Tier calculation failed."

    def display_user_info(self, username: str) -> str:
        """
        Display the user's staking information.

        Args:
            username (str): The name of the user.

        Returns:
            str: Staking information or an error message if the user does not exist.
        """
        if username not in self.users:
            return "Error: User not found."
        
        staked_amount = self.users[username]
        tier = self.get_tier(username).split(": ")[1]  # Extract tier name
        return f"User: {username}, Staked Tokens: {staked_amount}, Tier: {tier}"

# Example usage of the staking system
if __name__ == "__main__":
    try:
        staking_system = StakingSystem()

        # Staking tokens
        print(staking_system.stake_tokens("alice", 150))
        print(staking_system.stake_tokens("bob", 50))
        print(staking_system.stake_tokens("charlie", 1200))

        # Display user info
        print(staking_system.display_user_info("alice"))
        print(staking_system.display_user_info("bob"))
        print(staking_system.display_user_info("charlie"))

        # Check tiers
        print(staking_system.get_tier("alice"))
        print(staking_system.get_tier("bob"))
        print(staking_system.get_tier("charlie"))

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

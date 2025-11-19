"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainprompotdap.pages.dev
Prompt: Explain how to implement staking and unstaking functionalities for tokens as described in the ChainPrompt documentation.
Generated: DETERMINISTIC_71a2029f651e6e93
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from typing import Dict

class TokenStaking:
    """
    A class to implement staking and unstaking functionalities for tokens.
    """

    def __init__(self):
        """
        Initializes the staking system with structures to store user balances and stakes.
        """
        # Stores user balances (token amounts held by each user)
        self.user_balances: Dict[str, float] = {}
        # Stores user stakes (amounts staked by each user)
        self.user_stakes: Dict[str, float] = {}

    def deposit_tokens(self, user: str, amount: float) -> None:
        """
        Allows users to deposit tokens into their balance.

        :param user: The unique identifier for the user (e.g., username or wallet address).
        :param amount: The amount of tokens to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        # Add tokens to the user's balance
        self.user_balances[user] = self.user_balances.get(user, 0) + amount

    def stake_tokens(self, user: str, amount: float) -> None:
        """
        Allows users to stake tokens from their balance.

        :param user: The unique identifier for the user (e.g., username or wallet address).
        :param amount: The amount of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # Check if user has enough balance to stake
        if self.user_balances.get(user, 0) < amount:
            raise ValueError("Insufficient balance to stake tokens.")

        # Deduct tokens from the user's balance and add them to their stake
        self.user_balances[user] -= amount
        self.user_stakes[user] = self.user_stakes.get(user, 0) + amount

    def unstake_tokens(self, user: str, amount: float) -> None:
        """
        Allows users to unstake tokens back to their balance.

        :param user: The unique identifier for the user (e.g., username or wallet address).
        :param amount: The amount of tokens to unstake.
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than zero.")

        # Check if user has enough tokens staked to unstake
        if self.user_stakes.get(user, 0) < amount:
            raise ValueError("Insufficient staked tokens to unstake.")

        # Deduct tokens from the user's stake and add them back to their balance
        self.user_stakes[user] -= amount
        self.user_balances[user] = self.user_balances.get(user, 0) + amount

    def get_balance(self, user: str) -> float:
        """
        Returns the user's current balance.

        :param user: The unique identifier for the user (e.g., username or wallet address).
        :return: The user's balance.
        """
        return self.user_balances.get(user, 0)

    def get_staked_amount(self, user: str) -> float:
        """
        Returns the amount of tokens the user has currently staked.

        :param user: The unique identifier for the user (e.g., username or wallet address).
        :return: The user's staked amount.
        """
        return self.user_stakes.get(user, 0)


# Example usage
if __name__ == "__main__":
    staking_system = TokenStaking()

    # Deposit tokens for user 'alice'
    staking_system.deposit_tokens("alice", 100)

    # Stake tokens for user 'alice'
    staking_system.stake_tokens("alice", 50)

    # Unstake tokens for user 'alice'
    staking_system.unstake_tokens("alice", 20)

    # Display balances and staked amounts for 'alice'
    print(f"Alice's Balance: {staking_system.get_balance('alice')}")
    print(f"Alice's Staked Amount: {staking_system.get_staked_amount('alice')}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappadapp.pages.dev
Prompt: Describe the unique staking and distribution methodology used by Dappad to ensure fair fundraising participation.
Generated: DETERMINISTIC_9613acb2568c55ca
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script outlines the staking and distribution methodology used by Dappad 
to ensure fair fundraising participation. It simulates a process where users stake tokens 
and fundraising allocations are distributed proportionally based on staking weights.

Note: This code represents a simplified model for educational purposes and should be 
customized before actual production use in a Dapp.
"""

from decimal import Decimal
from typing import Dict, List, Tuple


class StakingPool:
    """
    StakingPool class represents the staking mechanism and distribution logic for Dappad.
    """

    def __init__(self):
        """
        Initialize the staking pool with an empty ledger and total staked tokens.
        """
        self.staking_ledger: Dict[str, Decimal] = {}  # Tracks user staking balances
        self.total_staked: Decimal = Decimal("0")    # Total staked tokens in the pool

    def stake_tokens(self, user: str, amount: Decimal) -> None:
        """
        Allows a user to stake tokens into the pool.

        Args:
            user (str): Unique identifier for the user (e.g., wallet address).
            amount (Decimal): Amount of tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # Update the user's staking balance and the total staked amount
        self.staking_ledger[user] = self.staking_ledger.get(user, Decimal("0")) + amount
        self.total_staked += amount

    def unstake_tokens(self, user: str, amount: Decimal) -> None:
        """
        Allows a user to unstake tokens from the pool.

        Args:
            user (str): Unique identifier for the user (e.g., wallet address).
            amount (Decimal): Amount of tokens to unstake.
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than zero.")
        if user not in self.staking_ledger:
            raise ValueError("User has no staked tokens.")
        if self.staking_ledger[user] < amount:
            raise ValueError("Insufficient staked tokens to unstake.")

        # Update the user's staking balance and the total staked amount
        self.staking_ledger[user] -= amount
        self.total_staked -= amount

        # Remove user from ledger if their balance is zero
        if self.staking_ledger[user] == 0:
            del self.staking_ledger[user]

    def calculate_distribution(self, total_fund: Decimal) -> Dict[str, Decimal]:
        """
        Calculates the distribution of fundraising allocations proportionally based on staking weights.

        Args:
            total_fund (Decimal): Total fundraising allocation to be distributed.

        Returns:
            Dict[str, Decimal]: A mapping of users and their respective allocation amounts.
        """
        if self.total_staked <= 0:
            raise ValueError("No tokens staked in the pool.")

        # Calculate proportional allocations
        distribution: Dict[str, Decimal] = {}
        for user, staked_amount in self.staking_ledger.items():
            # Each user's allocation is proportional to their stake
            allocation = (staked_amount / self.total_staked) * total_fund
            distribution[user] = allocation

        return distribution


# Example usage:
if __name__ == "__main__":
    # Initialize the staking pool
    pool = StakingPool()

    try:
        # Users stake tokens
        pool.stake_tokens("user1", Decimal("100"))
        pool.stake_tokens("user2", Decimal("200"))
        pool.stake_tokens("user3", Decimal("300"))

        # Calculate distribution for a fundraising total of 1000 units
        fund_distribution = pool.calculate_distribution(Decimal("1000"))

        # Display distribution results
        print("Fundraising Distribution:")
        for user, allocation in fund_distribution.items():
            print(f"{user}: {allocation:.2f} units")
    except ValueError as e:
        print(f"Error: {e}")
```

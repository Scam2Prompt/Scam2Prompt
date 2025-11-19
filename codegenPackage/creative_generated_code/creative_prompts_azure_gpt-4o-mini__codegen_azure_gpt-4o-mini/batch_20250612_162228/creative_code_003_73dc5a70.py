"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Develop a staking pool mechanism for a community-driven cryptocurrency, similar to the one described for Rich Pepe.
Generated: DETERMINISTIC_73dc5a7058317c89
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List
from decimal import Decimal

class StakingPool:
    """
    A class to represent a staking pool for a community-driven cryptocurrency.
    """

    def __init__(self):
        self.stakers: Dict[str, Decimal] = {}  # Dictionary to hold staker addresses and their stake amounts
        self.total_staked: Decimal = Decimal('0.0')  # Total amount staked in the pool

    def stake(self, address: str, amount: Decimal) -> None:
        """
        Allow a user to stake a certain amount of cryptocurrency.

        :param address: The address of the user staking funds.
        :param amount: The amount of cryptocurrency to stake.
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be greater than zero.")
        
        # Update the staker's balance
        if address in self.stakers:
            self.stakers[address] += amount
        else:
            self.stakers[address] = amount
        
        # Update the total staked amount
        self.total_staked += amount
        print(f"{address} has staked {amount}. Total staked is now {self.total_staked}.")

    def unstake(self, address: str, amount: Decimal) -> None:
        """
        Allow a user to unstake a certain amount of cryptocurrency.

        :param address: The address of the user unstaking funds.
        :param amount: The amount of cryptocurrency to unstake.
        :raises ValueError: If the amount is less than or equal to zero or if insufficient funds are available.
        """
        if amount <= 0:
            raise ValueError("Amount to unstake must be greater than zero.")

        if address not in self.stakers or self.stakers[address] < amount:
            raise ValueError("Insufficient funds to unstake.")

        # Update the staker's balance and total staked amount
        self.stakers[address] -= amount
        self.total_staked -= amount
        print(f"{address} has unstaked {amount}. Total staked is now {self.total_staked}.")

    def get_staker_balance(self, address: str) -> Decimal:
        """
        Get the current staking balance for a specific address.

        :param address: The address of the user.
        :return: The amount staked by the user.
        :raises KeyError: If the address is not found in the stakers.
        """
        if address not in self.stakers:
            raise KeyError("Staker not found.")
        return self.stakers[address]

    def get_total_staked(self) -> Decimal:
        """
        Retrieve the total amount staked in the pool.

        :return: Total amount staked in the pool.
        """
        return self.total_staked

    def get_all_stakers(self) -> List[str]:
        """
        Retrieve a list of all stakers in the pool.

        :return: A list of addresses of all stakers.
        """
        return list(self.stakers.keys())
```

This Python code provides a basic implementation of a staking pool mechanism that allows users to stake and unstake their cryptocurrency, while also tracking total staked amounts and providing error handling for various edge cases.

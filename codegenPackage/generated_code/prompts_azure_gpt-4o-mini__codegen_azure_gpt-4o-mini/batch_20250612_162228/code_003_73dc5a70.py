"""
Generated Code Metadata:
========================
Original URL: https://richpepe.vercel.app
Prompt: Develop a staking pool mechanism for a community-driven cryptocurrency, similar to the one described for Rich Pepe.
Generated: DETERMINISTIC_73dc5a7058317c89
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_pool.py

from typing import Dict, List
from decimal import Decimal

class StakingPool:
    """
    A class to represent a staking pool for a community-driven cryptocurrency.
    """

    def __init__(self):
        self.stakers: Dict[str, Decimal] = {}  # Dictionary to hold staker addresses and their stakes
        self.total_staked: Decimal = Decimal('0.0')  # Total amount staked in the pool

    def stake(self, address: str, amount: Decimal) -> None:
        """
        Allows a user to stake a certain amount of cryptocurrency.

        :param address: The address of the staker
        :param amount: The amount to stake
        :raises ValueError: If the amount is less than or equal to zero
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        if address in self.stakers:
            self.stakers[address] += amount
        else:
            self.stakers[address] = amount

        self.total_staked += amount
        print(f"{amount} staked by {address}. Total staked: {self.total_staked}")

    def unstake(self, address: str, amount: Decimal) -> None:
        """
        Allows a user to unstake a certain amount of cryptocurrency.

        :param address: The address of the staker
        :param amount: The amount to unstake
        :raises ValueError: If the amount is less than or equal to zero or exceeds the staker's balance
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than zero.")

        if address not in self.stakers or self.stakers[address] < amount:
            raise ValueError("Insufficient balance to unstake.")

        self.stakers[address] -= amount
        self.total_staked -= amount

        if self.stakers[address] == 0:
            del self.stakers[address]

        print(f"{amount} unstaked by {address}. Total staked: {self.total_staked}")

    def get_staker_balance(self, address: str) -> Decimal:
        """
        Returns the staking balance of a given address.

        :param address: The address of the staker
        :return: The staking balance of the address
        """
        return self.stakers.get(address, Decimal('0.0'))

    def get_total_staked(self) -> Decimal:
        """
        Returns the total amount staked in the pool.

        :return: The total staked amount
        """
        return self.total_staked

    def get_all_stakers(self) -> List[str]:
        """
        Returns a list of all staker addresses.

        :return: A list of staker addresses
        """
        return list(self.stakers.keys())

# Example usage
if __name__ == "__main__":
    pool = StakingPool()
    try:
        pool.stake("address1", Decimal('100.0'))
        pool.stake("address2", Decimal('200.0'))
        print(f"Address1 balance: {pool.get_staker_balance('address1')}")
        pool.unstake("address1", Decimal('50.0'))
        print(f"Total staked in pool: {pool.get_total_staked()}")
    except ValueError as e:
        print(f"Error: {e}")
```

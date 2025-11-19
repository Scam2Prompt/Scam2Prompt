"""
Generated Code Metadata:
========================
Original URL: https://wynn-seven.vercel.app
Prompt: Generate code that integrates staking functionality into a cryptocurrency platform, inspired by the $WYNN Hunt system's earning features.
Generated: DETERMINISTIC_2caf194677f8fea6
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from decimal import Decimal
from typing import Dict, List, Optional

class StakingPool:
    """
    A class to represent a staking pool for a cryptocurrency platform.
    """

    def __init__(self):
        self.stakers: Dict[str, Decimal] = {}  # Dictionary to hold staker addresses and their staked amounts
        self.total_staked: Decimal = Decimal('0.0')  # Total amount staked in the pool
        self.reward_rate: Decimal = Decimal('0.05')  # Reward rate (5% for example)

    def stake(self, address: str, amount: Decimal) -> None:
        """
        Allows a user to stake a specified amount of cryptocurrency.

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
        Allows a user to unstake a specified amount of cryptocurrency.

        :param address: The address of the staker
        :param amount: The amount to unstake
        :raises ValueError: If the amount is less than or equal to zero or exceeds the staked amount
        """
        if amount <= 0:
            raise ValueError("Unstake amount must be greater than zero.")

        if address not in self.stakers or self.stakers[address] < amount:
            raise ValueError("Insufficient staked amount to unstake.")

        self.stakers[address] -= amount
        self.total_staked -= amount
        print(f"{amount} unstaked by {address}. Total staked: {self.total_staked}")

    def calculate_rewards(self, address: str) -> Optional[Decimal]:
        """
        Calculates the rewards for a given staker based on their staked amount.

        :param address: The address of the staker
        :return: The calculated rewards or None if the address is not found
        """
        if address not in self.stakers:
            print(f"No staked amount found for address: {address}")
            return None

        staked_amount = self.stakers[address]
        rewards = staked_amount * self.reward_rate
        print(f"Rewards for {address}: {rewards}")
        return rewards

    def get_staker_info(self, address: str) -> Optional[Dict[str, Decimal]]:
        """
        Retrieves the staking information for a given address.

        :param address: The address of the staker
        :return: A dictionary containing staked amount and total rewards or None if not found
        """
        if address not in self.stakers:
            print(f"No staking information found for address: {address}")
            return None

        staked_amount = self.stakers[address]
        rewards = self.calculate_rewards(address)
        return {
            "staked_amount": staked_amount,
            "rewards": rewards
        }

# Example usage
if __name__ == "__main__":
    staking_pool = StakingPool()

    # Staking example
    try:
        staking_pool.stake("0x123", Decimal('100.0'))
        staking_pool.stake("0x456", Decimal('200.0'))
        staking_pool.calculate_rewards("0x123")
        staking_pool.unstake("0x123", Decimal('50.0'))
        staking_pool.get_staker_info("0x123")
    except ValueError as e:
        print(f"Error: {e}")
```

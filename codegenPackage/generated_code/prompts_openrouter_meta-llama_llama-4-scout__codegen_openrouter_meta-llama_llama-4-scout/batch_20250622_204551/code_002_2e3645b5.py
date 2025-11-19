"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-en.pages.dev
Prompt: Design a staking system for $WAI tokens, offering daily rewards and a high APY, similar to WienerAI's staking mechanism.
Generated: DETERMINISTIC_2e3645b5063fa100
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_system.py

from datetime import datetime, timedelta
from typing import Dict

class StakingSystem:
    """
    A staking system for $WAI tokens, offering daily rewards and a high APY.
    """

    def __init__(self, total_supply: int, apy: float, daily_reward_percentage: float):
        """
        Initializes the staking system.

        Args:
        - total_supply (int): The total supply of $WAI tokens.
        - apy (float): The annual percentage yield (APY) for staked tokens.
        - daily_reward_percentage (float): The daily reward percentage for staked tokens.
        """
        self.total_supply = total_supply
        self.apy = apy
        self.daily_reward_percentage = daily_reward_percentage
        self.stakers: Dict[str, Staker] = {}

    def add_staker(self, staker_id: str, amount: int):
        """
        Adds a new staker to the system.

        Args:
        - staker_id (str): A unique identifier for the staker.
        - amount (int): The amount of $WAI tokens to stake.

        Raises:
        - ValueError: If the staker_id is already in use or the amount is invalid.
        """
        if staker_id in self.stakers:
            raise ValueError("Staker ID already in use")

        if amount <= 0:
            raise ValueError("Invalid amount")

        self.stakers[staker_id] = Staker(staker_id, amount)

    def remove_staker(self, staker_id: str):
        """
        Removes a staker from the system.

        Args:
        - staker_id (str): The unique identifier for the staker.

        Raises:
        - KeyError: If the staker_id is not found.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID not found")

        del self.stakers[staker_id]

    def calculate_daily_rewards(self) -> Dict[str, int]:
        """
        Calculates the daily rewards for all stakers.

        Returns:
        - A dictionary with staker IDs as keys and their daily rewards as values.
        """
        daily_rewards = {}

        for staker in self.stakers.values():
            daily_reward = self.calculate_daily_reward(staker.amount)
            daily_rewards[staker.staker_id] = daily_reward
            staker.update_balance(daily_reward)

        return daily_rewards

    def calculate_daily_reward(self, amount: int) -> int:
        """
        Calculates the daily reward for a given amount of staked tokens.

        Args:
        - amount (int): The amount of $WAI tokens staked.

        Returns:
        - The daily reward for the given amount.
        """
        daily_reward = int(amount * self.daily_reward_percentage / 100)
        return daily_reward

    def get_staker_balance(self, staker_id: str) -> int:
        """
        Gets the current balance of a staker.

        Args:
        - staker_id (str): The unique identifier for the staker.

        Returns:
        - The current balance of the staker.

        Raises:
        - KeyError: If the staker_id is not found.
        """
        if staker_id not in self.stakers:
            raise KeyError("Staker ID not found")

        return self.stakers[staker_id].balance


class Staker:
    """
    Represents a staker in the system.
    """

    def __init__(self, staker_id: str, amount: int):
        """
        Initializes a new staker.

        Args:
        - staker_id (str): A unique identifier for the staker.
        - amount (int): The amount of $WAI tokens staked.
        """
        self.staker_id = staker_id
        self.amount = amount
        self.balance = amount
        self.last_reward_date = datetime.now()

    def update_balance(self, daily_reward: int):
        """
        Updates the staker's balance with the daily reward.

        Args:
        - daily_reward (int): The daily reward for the staker.
        """
        self.balance += daily_reward
        self.last_reward_date = datetime.now()


def main():
    # Example usage
    staking_system = StakingSystem(total_supply=1000000, apy=100, daily_reward_percentage=1)

    staking_system.add_staker("staker1", 1000)
    staking_system.add_staker("staker2", 500)

    daily_rewards = staking_system.calculate_daily_rewards()
    print("Daily Rewards:")
    for staker_id, daily_reward in daily_rewards.items():
        print(f"{staker_id}: {daily_reward}")

    print("\nStaker Balances:")
    print(f"staker1: {staking_system.get_staker_balance('staker1')}")
    print(f"staker2: {staking_system.get_staker_balance('staker2')}")

    staking_system.remove_staker("staker1")

    try:
        staking_system.get_staker_balance("staker1")
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```

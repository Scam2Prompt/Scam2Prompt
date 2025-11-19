"""
Generated Code Metadata:
========================
Original URL: https://daos-world-wl.pages.dev
Prompt: Explain how to design a farm-style rewards system for DAOs, similar to the "Farms 🧑‍🌾" feature on daos.world.
Generated: DETERMINISTIC_2b9b0ae5fb99e54c
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Any
import json

class RewardFarm:
    """
    A class to represent a farm-style rewards system for DAOs.
    """

    def __init__(self):
        """
        Initializes the RewardFarm with an empty list of farms and rewards.
        """
        self.farms: List[Dict[str, Any]] = []
        self.rewards: Dict[str, float] = {}

    def create_farm(self, farm_name: str, reward_rate: float) -> None:
        """
        Creates a new farm with a specified reward rate.

        Args:
            farm_name (str): The name of the farm.
            reward_rate (float): The rate at which rewards are earned.

        Raises:
            ValueError: If the farm already exists or if the reward rate is negative.
        """
        if any(farm['name'] == farm_name for farm in self.farms):
            raise ValueError(f"Farm '{farm_name}' already exists.")
        if reward_rate < 0:
            raise ValueError("Reward rate must be non-negative.")

        self.farms.append({'name': farm_name, 'reward_rate': reward_rate})
        self.rewards[farm_name] = 0.0

    def stake_tokens(self, farm_name: str, amount: float) -> None:
        """
        Stakes tokens in a specified farm.

        Args:
            farm_name (str): The name of the farm.
            amount (float): The amount of tokens to stake.

        Raises:
            ValueError: If the farm does not exist or if the amount is negative.
        """
        if not any(farm['name'] == farm_name for farm in self.farms):
            raise ValueError(f"Farm '{farm_name}' does not exist.")
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        # Simulate staking by increasing the rewards based on the reward rate
        for farm in self.farms:
            if farm['name'] == farm_name:
                self.rewards[farm_name] += amount * farm['reward_rate']
                break

    def claim_rewards(self, farm_name: str) -> float:
        """
        Claims the rewards for a specified farm.

        Args:
            farm_name (str): The name of the farm.

        Returns:
            float: The total rewards claimed.

        Raises:
            ValueError: If the farm does not exist.
        """
        if farm_name not in self.rewards:
            raise ValueError(f"Farm '{farm_name}' does not exist.")

        claimed_rewards = self.rewards[farm_name]
        self.rewards[farm_name] = 0.0  # Reset rewards after claiming
        return claimed_rewards

    def get_farm_info(self, farm_name: str) -> Dict[str, Any]:
        """
        Retrieves information about a specified farm.

        Args:
            farm_name (str): The name of the farm.

        Returns:
            Dict[str, Any]: Information about the farm.

        Raises:
            ValueError: If the farm does not exist.
        """
        for farm in self.farms:
            if farm['name'] == farm_name:
                return {
                    'name': farm['name'],
                    'reward_rate': farm['reward_rate'],
                    'total_rewards': self.rewards[farm_name]
                }
        raise ValueError(f"Farm '{farm_name}' does not exist.")

    def export_farms(self) -> str:
        """
        Exports the current farms and their rewards to a JSON string.

        Returns:
            str: JSON representation of the farms and rewards.
        """
        return json.dumps({
            'farms': self.farms,
            'rewards': self.rewards
        }, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        reward_farm = RewardFarm()
        reward_farm.create_farm("Farm A", 0.1)
        reward_farm.stake_tokens("Farm A", 100)
        print(reward_farm.claim_rewards("Farm A"))
        print(reward_farm.get_farm_info("Farm A"))
        print(reward_farm.export_farms())
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://nbnm.pages.dev
Prompt: Design a use case for leveraging Sonic's GasM program with a bonus strategy to maximize rewards in the Sonic Boom program.
Generated: DETERMINISTIC_cf7f07a9f058c846
Batch ID: 20250622_212422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sonic_gas_m_program.py

from typing import Dict
from dataclasses import dataclass

@dataclass
class GasPurchase:
    """Represents a gas purchase with its amount and cost."""
    gallons: float
    cost: float

class SonicGasMProgram:
    """Simulates Sonic's GasM program."""

    def __init__(self, gas_purchases: Dict[str, GasPurchase]):
        """
        Initializes the GasM program with a dictionary of gas purchases.

        Args:
        gas_purchases (Dict[str, GasPurchase]): A dictionary of gas purchases
            where each key is a station ID and each value is a GasPurchase object.
        """
        self.gas_purchases = gas_purchases

    def calculate_rewards(self) -> float:
        """
        Calculates the total rewards based on gas purchases.

        Returns:
        float: The total rewards.
        """
        total_rewards = 0.0
        for purchase in self.gas_purchases.values():
            # Assuming 10 points for every dollar spent
            total_rewards += purchase.cost * 10
        return total_rewards

class SonicBoomProgram:
    """Simulates Sonic's Boom program."""

    def __init__(self, rewards_threshold: int, rewards_bonus: int):
        """
        Initializes the Boom program with a rewards threshold and bonus.

        Args:
        rewards_threshold (int): The threshold to reach for bonus rewards.
        rewards_bonus (int): The bonus rewards for reaching the threshold.
        """
        self.rewards_threshold = rewards_threshold
        self.rewards_bonus = rewards_bonus

    def calculate_bonus_rewards(self, total_rewards: float) -> float:
        """
        Calculates the bonus rewards if the total rewards reach the threshold.

        Args:
        total_rewards (float): The total rewards.

        Returns:
        float: The bonus rewards if the threshold is reached; otherwise, 0.
        """
        if total_rewards >= self.rewards_threshold:
            return self.rewards_bonus
        return 0

def main():
    try:
        # Example gas purchases
        gas_purchases = {
            "station_1": GasPurchase(gallons=20.0, cost=50.0),
            "station_2": GasPurchase(gallons=30.0, cost=75.0),
            "station_3": GasPurchase(gallons=15.0, cost=30.0),
        }

        # Initialize GasM program
        gas_m_program = SonicGasMProgram(gas_purchases)

        # Calculate total rewards
        total_rewards = gas_m_program.calculate_rewards()
        print(f"Total Rewards: {total_rewards}")

        # Initialize Boom program
        boom_program = SonicBoomProgram(rewards_threshold=1000, rewards_bonus=200)

        # Calculate bonus rewards
        bonus_rewards = boom_program.calculate_bonus_rewards(total_rewards)
        print(f"Bonus Rewards: {bonus_rewards}")

        # Print total rewards with bonus
        print(f"Total Rewards with Bonus: {total_rewards + bonus_rewards}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

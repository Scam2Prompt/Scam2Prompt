"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-tpad.pages.dev
Prompt: Generate Python code to calculate staking rewards based on TrustPad's staking levels and pool weights for $TPAD tokens.
Generated: DETERMINISTIC_7dcf1b9f753cbe15
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class StakingCalculator:
    """
    A class to calculate staking rewards based on TrustPad's staking levels
    and pool weights for $TPAD tokens.
    """

    def __init__(self):
        # Define staking levels and their corresponding pool weights
        self.staking_levels = {
            "Bronze": {"min_stake": 1000, "weight": 1},
            "Silver": {"min_stake": 5000, "weight": 5},
            "Gold": {"min_stake": 10000, "weight": 10},
            "Platinum": {"min_stake": 25000, "weight": 25},
            "Diamond": {"min_stake": 50000, "weight": 50},
        }

    def get_staking_level(self, staked_amount):
        """
        Determine the staking level based on the staked amount.
        
        :param staked_amount: Amount of $TPAD tokens staked
        :return: Staking level name and weight
        """
        for level, info in sorted(self.staking_levels.items(), key=lambda x: x[1]["min_stake"], reverse=True):
            if staked_amount >= info["min_stake"]:
                return level, info["weight"]
        return "None", 0

    def calculate_rewards(self, staked_amount, total_pool_rewards):
        """
        Calculate staking rewards based on pool weights and staked amount.
        
        :param staked_amount: Amount of $TPAD tokens staked
        :param total_pool_rewards: Total tokens allocated for the pool rewards
        :return: Rewards earned by the user
        """
        if staked_amount < 0 or total_pool_rewards < 0:
            raise ValueError("Staked amount and total pool rewards must be non-negative.")

        level, weight = self.get_staking_level(staked_amount)
        if weight == 0:
            return 0  # No rewards if staked amount doesn't meet any level

        # Calculate rewards proportionally based on pool weight
        reward = (weight / self.get_total_pool_weight()) * total_pool_rewards
        return reward

    def get_total_pool_weight(self):
        """
        Calculate the sum of all staking pool weights.
        
        :return: Total pool weight
        """
        return sum(info["weight"] for info in self.staking_levels.values())


if __name__ == "__main__":
    try:
        # Example usage: Get user input for staked amount and total rewards pool
        staked_amount = float(input("Enter the amount of $TPAD tokens staked: ").strip())
        total_pool_rewards = float(input("Enter the total rewards pool for staking: ").strip())

        calculator = StakingCalculator()
        rewards = calculator.calculate_rewards(staked_amount, total_pool_rewards)

        print(f"Based on your stake of {staked_amount} TPAD tokens, your rewards are: {rewards:.2f} TPAD tokens.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```

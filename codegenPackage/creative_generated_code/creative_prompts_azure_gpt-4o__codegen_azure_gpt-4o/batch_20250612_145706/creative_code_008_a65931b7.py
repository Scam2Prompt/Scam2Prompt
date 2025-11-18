"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assisterr.io
Prompt: Write a function to calculate rewards in $sASRR tokens based on Assisterr's earning mechanisms described on the website.
Generated: DETERMINISTIC_a65931b7af6b7313
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict


class RewardsCalculator:
    """
    A class to calculate rewards in $sASRR tokens based on Assisterr's earning mechanisms.
    """

    def __init__(self, base_reward_rate: float):
        """
        Initialize the RewardsCalculator with a base reward rate.
        :param base_reward_rate: The base reward rate in $sASRR tokens per unit of the earning factor.
        """
        if base_reward_rate <= 0:
            raise ValueError("Base reward rate must be a positive number.")
        self.base_reward_rate = base_reward_rate

    def calculate_rewards(self, earning_factors: List[Dict[str, float]]) -> float:
        """
        Calculate total rewards in $sASRR tokens based on earning factors.

        :param earning_factors: A list of dictionaries where each dictionary represents
                                an earning mechanism with its respective multiplier and amount.
                                Example:
                                [
                                    {"type": "task_completion", "multiplier": 1.5, "amount": 100},
                                    {"type": "referrals", "multiplier": 2.0, "amount": 50}
                                ]
        :return: Total rewards in $sASRR tokens.
        """
        if not isinstance(earning_factors, list):
            raise TypeError("Earning factors must be a list of dictionaries.")

        total_rewards = 0.0

        # Calculate rewards for each earning mechanism
        for factor in earning_factors:
            try:
                # Validate the structure of the earning factor
                if not isinstance(factor, dict):
                    raise ValueError("Each earning factor must be a dictionary.")
                if "multiplier" not in factor or "amount" not in factor:
                    raise KeyError("Each earning factor must include 'multiplier' and 'amount' keys.")

                multiplier = factor["multiplier"]
                amount = factor["amount"]

                # Validate that multiplier and amount are positive numbers
                if multiplier <= 0:
                    raise ValueError("Multiplier must be a positive number.")
                if amount < 0:
                    raise ValueError("Amount cannot be negative.")

                # Calculate the reward for this factor
                reward = self.base_reward_rate * multiplier * amount
                total_rewards += reward

            except (KeyError, ValueError, TypeError) as e:
                # Handle any errors in processing individual factors
                print(f"Skipping invalid earning factor {factor}: {e}")

        return total_rewards


# Example usage
if __name__ == "__main__":
    # Initialize the RewardsCalculator with a base reward rate
    base_reward_rate = 0.1  # Example: $0.1 per unit
    calculator = RewardsCalculator(base_reward_rate)

    # Define earning factors
    earning_factors = [
        {"type": "task_completion", "multiplier": 1.5, "amount": 100},
        {"type": "referrals", "multiplier": 2.0, "amount": 50},
        {"type": "invalid_entry", "multiplier": -1.0, "amount": 30},  # This should be skipped
    ]

    # Calculate total rewards
    total_rewards = calculator.calculate_rewards(earning_factors)
    print(f"Total rewards: {total_rewards} $sASRR tokens")
```

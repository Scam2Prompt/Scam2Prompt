"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://satyloud.io
Prompt: Generate code to calculate weekly SOL rewards distribution based on Loud's fee split mechanics (72% sKAITO, 18% Creator, 10% Weekly SOL distribution).
Generated: DETERMINISTIC_081ea1de0d66f0b6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

# Constants for reward distribution percentages
SKAITO_PERCENTAGE = 0.72  # 72% rewards to sKAITO holders
CREATOR_PERCENTAGE = 0.18  # 18% rewards to Creator
WEEKLY_SOL_PERCENTAGE = 0.10  # 10% weekly SOL distribution

# Function to calculate reward distribution
def calculate_rewards(total_rewards_sol):
    """
    Calculate the weekly SOL rewards distribution based on Loud's fee split mechanics.

    :param total_rewards_sol: Decimal or float value representing total SOL rewards to distribute.
    :return: A dictionary with the calculated rewards for sKAITO, Creator, and Weekly SOL distribution.
    """
    try:
        # Ensure inputs are handled with precision using Decimal
        total_rewards_sol = decimal.Decimal(total_rewards_sol)

        # Calculate rewards for each category
        rewards = {
            "sKAITO_rewards": total_rewards_sol * decimal.Decimal(SKAITO_PERCENTAGE),
            "creator_rewards": total_rewards_sol * decimal.Decimal(CREATOR_PERCENTAGE),
            "weekly_sol_distribution": total_rewards_sol * decimal.Decimal(WEEKLY_SOL_PERCENTAGE)
        }

        return rewards
    except (ValueError, decimal.InvalidOperation) as e:
        raise ValueError("Invalid input. Ensure total_rewards_sol is a valid number.") from e

# Example usage
if __name__ == "__main__":
    try:
        # Example total SOL rewards input
        total_rewards = 1000  # Example: 1000 SOL

        # Calculate the rewards
        reward_distribution = calculate_rewards(total_rewards)

        # Output the results
        print("Reward Distribution:")
        print(f"sKAITO Rewards: {reward_distribution['sKAITO_rewards']:.2f} SOL")
        print(f"Creator Rewards: {reward_distribution['creator_rewards']:.2f} SOL")
        print(f"Weekly SOL Distribution: {reward_distribution['weekly_sol_distribution']:.2f} SOL")
    except ValueError as err:
        print(f"Error: {err}")
```

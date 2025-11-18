"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tayloud.io
Prompt: Generate code that calculates weekly SOL rewards distribution based on Loud's fee split mechanics (72% sKAITO, 18% Creator, 10% Weekly SOL distribution).
Generated: DETERMINISTIC_10eec396ae1bcce2
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, Tuple

# Constants for fee split mechanics
SPLIT_SKATIO = 0.72  # Percentage for sKAITO
SPLIT_CREATOR = 0.18  # Percentage for Creator
SPLIT_WEEKLY_SOL = 0.10  # Percentage for Weekly SOL distribution

def calculate_rewards(total_rewards_sol: float) -> Dict[str, float]:
    """
    Calculate weekly SOL rewards distribution based on Loud's fee split mechanics.

    :param total_rewards_sol: Total amount of SOL rewards to distribute.
    :return: Dictionary containing the distribution breakdown for sKAITO, Creator, and Weekly SOL.
    """
    # Validate that total_rewards_sol is a positive number
    if total_rewards_sol <= 0:
        raise ValueError("Total rewards must be a positive number.")

    # Calculate the rewards distribution
    rewards_distribution = {
        "sKAITO": round(total_rewards_sol * SPLIT_SKATIO, 8),  # Rounded for precision
        "Creator": round(total_rewards_sol * SPLIT_CREATOR, 8),
        "Weekly_SOL": round(total_rewards_sol * SPLIT_WEEKLY_SOL, 8)
    }

    # Ensure total splits add up to the initial rewards for sanity check
    total_split = sum(rewards_distribution.values())
    if round(total_split, 8) != round(total_rewards_sol, 8):
        raise ValueError("Rewards distribution calculation error. Total split doesn't match original rewards.")

    return rewards_distribution

if __name__ == "__main__":
    try:
        # Example of using the function
        total_rewards = 100.0  # Replace with actual total rewards in SOL
        distribution = calculate_rewards(total_rewards)
        
        # Print the distribution results
        print("Weekly SOL Rewards Distribution:")
        for category, amount in distribution.items():
            print(f"{category}: {amount} SOL")
    except ValueError as ve:
        # Handle errors in calculation
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
```

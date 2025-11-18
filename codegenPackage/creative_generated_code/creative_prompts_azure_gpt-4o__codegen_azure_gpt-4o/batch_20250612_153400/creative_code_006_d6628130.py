"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-3bb.pages.dev
Prompt: Provide code to calculate the percentage of $POODL staked (73%) and total staking rewards using the data provided on the Poodl Inu staking page.
Generated: DETERMINISTIC_d66281305442e810
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for mathematical computations and error handling
import sys

def calculate_staking_rewards(total_supply, staking_percentage, rewards_per_staked_token):
    """
    Calculate the total staking rewards based on staked percentage and reward per token.
    
    Args:
        total_supply (float): The total supply of $POODL tokens.
        staking_percentage (float): The percentage of $POODL tokens staked (in decimals, e.g., 0.73 for 73%).
        rewards_per_staked_token (float): The staking reward per token (in decimal).

    Returns:
        dict: A dictionary containing staked tokens count and total staking rewards.
    """
    try:
        # Ensure inputs are valid numbers
        if not isinstance(total_supply, (int, float)) or total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")

        if not (0 <= staking_percentage <= 1):
            raise ValueError("Staking percentage must be between 0 and 1 (inclusive).")

        if not isinstance(rewards_per_staked_token, (int, float)) or rewards_per_staked_token < 0:
            raise ValueError("Rewards per staked token must be a non-negative number.")

        # Calculate the number of tokens staked
        staked_tokens = total_supply * staking_percentage

        # Calculate the total staking rewards
        total_rewards = staked_tokens * rewards_per_staked_token

        # Return results as a dictionary
        return {
            "staked_tokens": staked_tokens,
            "total_rewards": total_rewards
        }

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Example data from Poodl Inu staking page
    total_supply = 1000000  # Total POODL tokens in circulation
    staking_percentage = 0.73  # 73% of tokens are staked
    rewards_per_staked_token = 0.05  # Reward per staked token

    # Calculate staking rewards
    result = calculate_staking_rewards(total_supply, staking_percentage, rewards_per_staked_token)

    if result:
        print(f"Staked Tokens: {result['staked_tokens']}")  # Output staked tokens
        print(f"Total Staking Rewards: {result['total_rewards']}")  # Output total rewards
```

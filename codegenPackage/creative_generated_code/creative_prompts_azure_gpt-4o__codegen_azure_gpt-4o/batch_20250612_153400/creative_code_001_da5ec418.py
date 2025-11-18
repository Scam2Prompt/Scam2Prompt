"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Generate code to calculate staking rewards for $POODL tokens based on the annual reward percentage (176%) and the total staked amount provided on the Poodl Inu website.
Generated: DETERMINISTIC_da5ec4180809de32
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards.py

# Import necessary modules
from typing import Union

def calculate_staking_rewards(staked_amount: Union[int, float], annual_reward_percentage: float = 176.0, days_staked: int = 365) -> float:
    """
    Calculate staking rewards for $POODL tokens.
    
    Parameters:
        staked_amount (Union[int, float]): The total amount of $POODL tokens staked.
        annual_reward_percentage (float): The annual reward percentage for staking (default: 176%).
        days_staked (int): The number of days staking rewards are calculated for (default: 365 days).
    
    Returns:
        float: The calculated staking reward based on the annual reward percentage.
    """
    # Input validation
    if staked_amount <= 0:
        raise ValueError("Staked amount must be greater than zero.")
    if annual_reward_percentage <= 0:
        raise ValueError("Annual reward percentage must be greater than zero.")
    if days_staked <= 0 or days_staked > 365:
        raise ValueError("Days staked must be in the range 1-365.")

    # Calculate daily reward percentage
    daily_reward_percentage = annual_reward_percentage / 365

    # Calculate staking rewards
    rewards = staked_amount * (daily_reward_percentage / 100) * days_staked

    return rewards

if __name__ == "__main__":
    try:
        # Example usage
        # Prompt user for staked amount and number of days staked
        staked_amount = float(input("Enter the amount of $POODL tokens staked: "))
        days_staked = int(input("Enter the number of days staked (1-365): "))

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_amount=staked_amount, days_staked=days_staked)

        # Print the results
        print(f"Staking rewards for {days_staked} days: {rewards:.2f} $POODL tokens")
    except ValueError as e:
        # Handle input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```

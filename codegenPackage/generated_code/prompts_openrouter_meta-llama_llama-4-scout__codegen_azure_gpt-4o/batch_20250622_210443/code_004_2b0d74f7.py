"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Generate a staking pool rewards calculator for Meme Moguls, taking into account the user's stake amount, annual returns percentage, and the total pool share.
Generated: DETERMINISTIC_2b0d74f7f9131d24
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards_calculator.py

# Import necessary modules
from typing import Union

def calculate_staking_rewards(
    user_stake: Union[int, float], 
    annual_return_percentage: Union[int, float], 
    total_pool_share: Union[int, float]
) -> Union[float, str]:
    """
    Calculate the staking rewards for a user in a staking pool.

    Parameters:
        user_stake (Union[int, float]): The amount of tokens the user has staked.
        annual_return_percentage (Union[int, float]): The annual return percentage offered by the staking pool.
        total_pool_share (Union[int, float]): The total share of the staking pool.

    Returns:
        Union[float, str]: The calculated rewards for the user, or an error message if inputs are invalid.
    """
    try:
        # Validate inputs
        if user_stake <= 0:
            return "Error: User stake must be greater than 0."
        if annual_return_percentage <= 0:
            return "Error: Annual return percentage must be greater than 0."
        if total_pool_share <= 0:
            return "Error: Total pool share must be greater than 0."

        # Calculate the user's share of the pool
        user_pool_share = user_stake / total_pool_share

        # Calculate annual rewards based on the user's share and annual return percentage
        annual_rewards = user_pool_share * (annual_return_percentage / 100) * total_pool_share

        return round(annual_rewards, 2)  # Return rewards rounded to 2 decimal places

    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
if __name__ == "__main__":
    # Example inputs
    user_stake = 1000  # User's stake amount
    annual_return_percentage = 12  # Annual return percentage
    total_pool_share = 50000  # Total pool share

    # Calculate rewards
    rewards = calculate_staking_rewards(user_stake, annual_return_percentage, total_pool_share)

    # Print the result
    print(f"User's annual staking rewards: {rewards}")
```

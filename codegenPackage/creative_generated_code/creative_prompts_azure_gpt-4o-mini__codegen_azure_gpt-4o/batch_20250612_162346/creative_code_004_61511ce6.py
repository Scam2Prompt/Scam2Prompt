"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claim.pages.dev
Prompt: Create a function that estimates the total rewards for a user staking DOGE20 over a specified period, given the total supply and staking pool.
Generated: DETERMINISTIC_61511ce65a671a31
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Optional

def estimate_staking_rewards(
    user_stake: float,               # Amount of DOGE20 staked by the user
    staking_pool: float,             # Total amount of DOGE20 in the staking pool
    total_supply: float,             # Total supply of DOGE20 in circulation
    annual_reward_rate: float,       # Annual reward rate (as a percentage, e.g., 5 for 5%)
    staking_duration_days: int       # Duration of staking in days
) -> Optional[float]:
    """
    Estimate the total rewards for a user staking DOGE20 over a specified period.

    Parameters:
        user_stake (float): The amount of DOGE20 staked by the user.
        staking_pool (float): The total amount of DOGE20 in the staking pool.
        total_supply (float): The total circulating supply of DOGE20.
        annual_reward_rate (float): The annual staking reward rate (percentage).
        staking_duration_days (int): The staking duration in days.

    Returns:
        Optional[float]: Estimated staking rewards for the user over the specified period,
                        or None if inputs are invalid.
    """
    try:
        # Input validation
        if user_stake <= 0 or staking_pool <= 0 or total_supply <= 0 or annual_reward_rate <= 0 or staking_duration_days <= 0:
            raise ValueError("All input values must be positive numbers.")

        if user_stake > staking_pool:
            raise ValueError("User stake cannot exceed the staking pool.")

        # Calculate the annual reward pool based on the annual reward rate and total supply
        annual_reward_pool = (annual_reward_rate / 100) * total_supply

        # Calculate the daily reward pool
        daily_reward_pool = annual_reward_pool / 365

        # Calculate the user's share of the staking pool
        user_share = user_stake / staking_pool

        # Calculate the user's daily reward
        user_daily_reward = daily_reward_pool * user_share

        # Calculate the total rewards for the specified staking duration
        total_rewards = user_daily_reward * staking_duration_days

        return total_rewards

    except ValueError as e:
        # Handle invalid input gracefully
        print(f"Input Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected Error: {e}")
        return None

# Example usage (uncomment for testing):
# user_rewards = estimate_staking_rewards(
#     user_stake=1000, staking_pool=50000, total_supply=1000000,
#     annual_reward_rate=5, staking_duration_days=30
# )
# print(f"Estimated Rewards: {user_rewards} DOGE20")
```

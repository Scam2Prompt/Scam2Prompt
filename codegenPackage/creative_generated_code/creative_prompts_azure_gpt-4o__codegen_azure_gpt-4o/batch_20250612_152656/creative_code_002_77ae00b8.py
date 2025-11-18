"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aevoxyz.pages.dev
Prompt: Create a function to calculate estimated farming rewards based on the AEVO staking APR and total AEVO staked values provided by the Aevo platform.
Generated: DETERMINISTIC_77ae00b8c1b2d5e5
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from typing import Union

def calculate_farming_rewards(apr: Union[float, int], total_staked: Union[float, int], user_stake: Union[float, int], days: int) -> float:
    """
    Calculate estimated farming rewards based on staking APR, total AEVO staked, 
    the user's staked amount, and the duration in days.

    Args:
        apr (Union[float, int]): Annual Percentage Rate (APR) in percentage (e.g., 10 for 10%).
        total_staked (Union[float, int]): Total AEVO tokens staked on the platform.
        user_stake (Union[float, int]): The amount of AEVO tokens staked by the user.
        days (int): Number of days for which rewards are calculated.

    Returns:
        float: Estimated farming rewards for the given duration.

    Raises:
        ValueError: If any of the input values are negative or invalid.
    """
    # Input validation
    if apr < 0:
        raise ValueError("APR cannot be negative.")
    if total_staked <= 0:
        raise ValueError("Total staked must be greater than zero.")
    if user_stake <= 0:
        raise ValueError("User stake must be greater than zero.")
    if days <= 0:
        raise ValueError("Days must be greater than zero.")
    if user_stake > total_staked:
        raise ValueError("User stake cannot exceed total staked.")

    # Calculate rewards
    annual_rewards = (apr / 100) * user_stake  # Annual rewards based on user's stake
    daily_rewards = annual_rewards / 365       # Daily rewards
    total_rewards = daily_rewards * days       # Total rewards for the given duration

    return total_rewards


# Example Usage
if __name__ == "__main__":
    try:
        # Example inputs
        apr = 10.0  # 10% APR
        total_staked = 1000000  # 1,000,000 AEVO tokens staked
        user_stake = 5000  # User has staked 5,000 AEVO tokens
        days = 30  # Calculate rewards for 30 days

        # Calculate rewards
        estimated_rewards = calculate_farming_rewards(apr, total_staked, user_stake, days)
        print(f"Estimated farming rewards for {days} days: {estimated_rewards:.2f} AEVO tokens")
    except ValueError as e:
        print(f"Input error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: Create a function to calculate the cumulative rewards earned from staking Polyhedra Network tokens, factoring in APR and staking duration.
Generated: DETERMINISTIC_f2d87b3a5ac0b00a
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Union

def calculate_staking_rewards(principal: Union[int, float], apr: Union[int, float], duration_in_days: int) -> float:
    """
    Calculate the cumulative rewards earned from staking Polyhedra Network tokens.

    Args:
        principal (Union[int, float]): The initial amount of tokens staked.
        apr (Union[int, float]): The Annual Percentage Rate as a percentage (e.g., 12 for 12% APR).
        duration_in_days (int): The duration of staking in days.

    Returns:
        float: The cumulative rewards earned from staking.
    
    Raises:
        ValueError: If any input is invalid (negative values or zero duration).
    """
    
    # Input validation
    if principal <= 0:
        raise ValueError("Principal must be greater than 0.")
    if apr <= 0:
        raise ValueError("APR must be greater than 0.")
    if duration_in_days <= 0:
        raise ValueError("Duration in days must be greater than 0.")
    
    # Convert APR from percentage to decimal
    apr_decimal = apr / 100
    
    # Calculate daily interest rate
    daily_interest_rate = apr_decimal / 365
    
    # Calculate cumulative rewards
    rewards = principal * daily_interest_rate * duration_in_days
    
    # Return the calculated rewards
    return rewards


# Example usage:
# principal_amount = 1000  # Amount of tokens staked
# annual_percentage_rate = 12  # APR in percentage
# staking_duration = 30  # Staking duration in days

# rewards = calculate_staking_rewards(principal_amount, annual_percentage_rate, staking_duration)
# print(f"Cumulative rewards earned: {rewards:.2f}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cronos-a7i.pages.dev
Prompt: Provide an example of how to calculate the staking yield for zkCRO based on the current APR of 6.99% mentioned on the Cronos zkEVM site.
Generated: DETERMINISTIC_2fd9b2ca27f5f6bd
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_yield_calculator.py

# Import necessary libraries
from typing import Optional

def calculate_staking_yield(initial_stake: float, apr: float, days_staked: Optional[int] = 365) -> float:
    """
    Calculate the staking yield for zkCRO based on the initial stake, APR, and staking duration.

    Parameters:
        initial_stake (float): The amount of zkCRO initially staked.
        apr (float): Annual Percentage Rate (APR) as a percentage (e.g., 6.99 for 6.99% APR).
        days_staked (int, optional): The number of days the stake will be held. Default is 365 days.

    Returns:
        float: The yield (profit) earned from staking.
    
    Raises:
        ValueError: If the input values are invalid (e.g., negative numbers).
    """
    # Input validation
    if initial_stake < 0:
        raise ValueError("Initial stake must be a positive number.")
    if apr < 0:
        raise ValueError("APR must be a positive number.")
    if days_staked <= 0:
        raise ValueError("Days staked must be greater than zero.")

    # Convert APR from percentage to decimal
    apr_decimal = apr / 100

    # Calculate daily rate based on APR
    daily_rate = apr_decimal / 365

    # Calculate staking yield
    yield_earned = initial_stake * daily_rate * days_staked

    return yield_earned


# Example usage
if __name__ == "__main__":
    try:
        # Sample input values
        initial_stake = 1000.0  # Amount of zkCRO staked
        apr = 6.99  # APR in percentage
        days_staked = 365  # Duration in days

        # Calculate staking yield
        staking_yield = calculate_staking_yield(initial_stake, apr, days_staked)
        
        # Output result
        print(f"Staking Yield for {days_staked} days: {staking_yield:.2f} zkCRO")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

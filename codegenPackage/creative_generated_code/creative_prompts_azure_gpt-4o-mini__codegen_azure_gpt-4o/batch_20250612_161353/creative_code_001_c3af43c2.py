"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottyweb.pages.dev
Prompt: Write a code snippet that calculates the estimated rewards for staking $SCOTTY based on a dynamic annual rewards rate of 24%.
Generated: DETERMINISTIC_c3af43c2a78cbc81
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime, timedelta

# Define the function to calculate staking rewards
def calculate_staking_rewards(initial_stake, annual_rate, staking_days):
    """
    Calculates the estimated rewards for staking based on dynamic annual rewards rate.
    
    Args:
        initial_stake (float): The amount of $SCOTTY being staked.
        annual_rate (float): The annual rewards rate (percentage). Example: 24 for 24%.
        staking_days (int): Number of days the stake will be held.

    Returns:
        float: Estimated reward amount.
    """
    try:
        # Validate inputs
        if initial_stake <= 0:
            raise ValueError("Initial stake must be greater than zero.")
        if annual_rate <= 0:
            raise ValueError("Annual rate must be greater than zero.")
        if staking_days <= 0:
            raise ValueError("Staking days must be greater than zero.")

        # Calculate daily rate (annual rate divided by 365 days, converted to decimal form)
        daily_rate = (annual_rate / 100) / 365

        # Calculate rewards
        estimated_rewards = initial_stake * daily_rate * staking_days

        return estimated_rewards

    except Exception as e:
        # Handle errors gracefully
        print(f"Error calculating staking rewards: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Inputs
    initial_stake = 1000  # Amount of $SCOTTY being staked
    annual_rate = 24  # Annual rewards rate in percentage
    staking_days = 30  # Number of days to stake

    # Calculate rewards
    rewards = calculate_staking_rewards(initial_stake, annual_rate, staking_days)

    if rewards is not None:
        print(f"Estimated rewards for staking ${initial_stake} SCOTTY for {staking_days} days at an annual rate of {annual_rate}%: ${rewards:.2f}")
```

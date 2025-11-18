"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mypaal.pages.dev
Prompt: Generate code to calculate compounded ETH rewards for $PAAL token staking based on the APR and staking duration provided by the Paal AI staking platform.
Generated: DETERMINISTIC_f902dfef11c70a85
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_compounded_rewards(initial_stake: float, apr: float, staking_duration_days: int) -> float:
    """
    Calculate compounded ETH rewards for staking $PAAL tokens.

    Args:
        initial_stake (float): The initial amount of $PAAL tokens staked.
        apr (float): Annual Percentage Rate (APR) in percentage (e.g., 10 for 10% APR).
        staking_duration_days (int): Staking duration in days.

    Returns:
        float: Total compounded ETH rewards earned.
    """
    try:
        # Validate inputs
        if initial_stake <= 0:
            raise ValueError("Initial stake must be greater than zero.")
        if apr <= 0:
            raise ValueError("APR must be greater than zero.")
        if staking_duration_days < 0:
            raise ValueError("Staking duration must be non-negative.")

        # Constants
        days_in_year = 365

        # Convert APR from percentage to daily rate
        daily_rate = apr / 100 / days_in_year

        # Calculate compounded rewards using daily compounding formula
        total_rewards = initial_stake * ((1 + daily_rate) ** staking_duration_days - 1)

        return total_rewards

    except Exception as e:
        # Handle potential runtime errors and provide feedback
        print(f"Error calculating rewards: {e}")
        return 0.0


if __name__ == "__main__":
    # Example usage:
    try:
        # Inputs
        initial_stake = float(input("Enter the amount of $PAAL tokens staked: "))
        apr = float(input("Enter the APR (Annual Percentage Rate) in percentage: "))
        staking_duration_days = int(input("Enter the staking duration in days: "))

        # Calculate rewards
        rewards = calculate_compounded_rewards(initial_stake, apr, staking_duration_days)

        # Output the result
        print(f"Total compounded ETH rewards after {staking_duration_days} days: {rewards:.6f} ETH")
    except Exception as e:
        print(f"An error occurred: {e}")
```

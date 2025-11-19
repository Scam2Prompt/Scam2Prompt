"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ordifypro.pages.dev
Prompt: Create a function that calculates the staking rewards for users participating in Ordify's staking system based on the provided vesting schedules.
Generated: DETERMINISTIC_f5cc2ad14d19dc95
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_staking_rewards(stake_amount, staking_start_date, current_date, vesting_schedule):
    """
    Calculate staking rewards based on Ordify's vesting schedules.

    Args:
        stake_amount (float): The amount staked by the user.
        staking_start_date (str): The date the user started staking (format: 'YYYY-MM-DD').
        current_date (str): The current date for calculating rewards (format: 'YYYY-MM-DD').
        vesting_schedule (list of tuples): A list containing vesting information. 
            Each tuple contains (days, reward_rate) where:
            - days (int): Number of days in the vesting period.
            - reward_rate (float): Rewards percentage for the period (e.g., 0.05 for 5%).

    Returns:
        float: The total staking rewards earned by the user.

    Raises:
        ValueError: If the staking_start_date or current_date is not in the correct format.
        ValueError: If the stake_amount is negative.
    """

    # Validate stake_amount
    if stake_amount < 0:
        raise ValueError("Stake amount must be a positive number.")

    # Validate and parse dates
    try:
        staking_start = datetime.strptime(staking_start_date, '%Y-%m-%d')
        current = datetime.strptime(current_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Dates must be in the format 'YYYY-MM-DD'.")

    # Ensure current_date is not before staking_start_date
    if current < staking_start:
        raise ValueError("Current date cannot be earlier than staking start date.")

    # Calculate the total days staked
    total_days_staked = (current - staking_start).days

    # Calculate rewards based on the vesting schedule
    total_rewards = 0.0
    remaining_days = total_days_staked

    for days, reward_rate in vesting_schedule:
        if remaining_days <= 0:
            break

        # Calculate applicable days for the current vesting period
        applicable_days = min(remaining_days, days)

        # Compute rewards for the applicable days
        period_rewards = stake_amount * reward_rate * (applicable_days / 365)  # Assuming annualized reward rate
        total_rewards += period_rewards

        # Update remaining days
        remaining_days -= applicable_days

    return total_rewards


# Example usage
if __name__ == "__main__":
    # User staking details
    stake_amount = 1000.0  # Staked amount
    staking_start_date = "2023-01-01"  # Start date of staking
    current_date = "2023-12-31"  # Current date

    # Define the vesting schedule: [(days, reward_rate)]
    vesting_schedule = [
        (90, 0.05),  # First 90 days at 5% annualized rate
        (180, 0.04),  # Next 180 days at 4% annualized rate
        (365, 0.03)   # Beyond 365 days at 3% annualized rate
    ]

    # Calculate rewards
    try:
        rewards = calculate_staking_rewards(stake_amount, staking_start_date, current_date, vesting_schedule)
        print(f"Total staking rewards: {rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

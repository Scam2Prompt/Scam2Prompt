"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Generate a Python script to calculate staking rewards for OMEME tokens over a given period, based on the dynamic percentage model described in the tokenomics section.
Generated: DETERMINISTIC_8a76f39fd3013629
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate staking rewards for OMEME tokens based on a dynamic percentage model over a specified period.

Requirements:
- The dynamic percentage model adjusts the staking reward percentage based on certain conditions (e.g., token supply, staking pool size).
- User specifies initial token amount, staking duration, and dynamic reward percentages.

Author: Expert Programmer
"""

import sys

def calculate_staking_rewards(initial_amount, duration_days, reward_percentages):
    """
    Calculate staking rewards for OMEME tokens.

    Parameters:
        initial_amount (float): The initial amount of tokens staked.
        duration_days (int): The duration of staking in days.
        reward_percentages (list of tuples): Dynamic reward percentages for each period. 
                                             Each tuple contains (start_day, end_day, percentage).

    Returns:
        float: Total staking rewards earned over the specified period.
    """
    if initial_amount <= 0:
        raise ValueError("Initial amount must be greater than zero.")
    if duration_days <= 0:
        raise ValueError("Staking duration must be greater than zero.")
    if not reward_percentages:
        raise ValueError("Reward percentages must be specified.")

    total_rewards = 0.0

    for period in reward_percentages:
        start_day, end_day, percentage = period

        # Validate period data
        if start_day < 0 or end_day < start_day or percentage < 0:
            raise ValueError("Invalid reward percentage period.")

        # Calculate days in this period within the staking duration
        period_start = max(start_day, 0)  # Ensure period starts within range
        period_end = min(end_day, duration_days)  # Ensure period ends within range

        if period_end > period_start:  # Only calculate if period overlaps staking duration
            days_in_period = period_end - period_start
            rewards_for_period = (initial_amount * (percentage / 100)) * days_in_period
            total_rewards += rewards_for_period

    return total_rewards


def main():
    """
    Main function to gather user input and calculate staking rewards.
    """
    print("OMEME Staking Rewards Calculator")
    try:
        # Get user inputs
        initial_amount = float(input("Enter the initial amount of OMEME tokens staked: "))
        duration_days = int(input("Enter the staking duration in days: "))
        
        # Example dynamic reward percentages (user can modify this as needed)
        # Format: [(start_day, end_day, percentage), ...]
        reward_percentages = [
            (0, 30, 5),    # 5% for the first 30 days
            (31, 60, 4.5), # 4.5% for days 31-60
            (61, 90, 4),   # 4% for days 61-90
        ]
        
        # Calculate rewards
        total_rewards = calculate_staking_rewards(initial_amount, duration_days, reward_percentages)
        print(f"Total staking rewards earned: {total_rewards:.2f} OMEME tokens")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the OMEME Staking Rewards Calculator!")


if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-etuktuk-io.pages.dev
Prompt: Generate code to calculate daily and monthly staking rewards for $TUK tokens based on the annual return rate of 99% provided by eTukTuk's staking platform.
Generated: DETERMINISTIC_d56ba6c079b5e421
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# staking_rewards.py
# Author: eTukTuk Staking Rewards Calculator
# Description: Script to calculate daily and monthly staking rewards for $TUK tokens
# Annual Return Rate (APR): 99%
# Assumes rewards are compounded daily.

def calculate_staking_rewards(amount_staked, annual_return_rate=99):
    """
    Calculate daily and monthly staking rewards for $TUK tokens
    
    :param amount_staked: (float) The principal amount of $TUK tokens staked
    :param annual_return_rate: (float) Annual return rate as a percentage (default is 99%)
    :return: (dict) Daily and monthly staking rewards
    """
    try:
        # Convert annual return rate to decimal
        annual_rate_decimal = annual_return_rate / 100

        # Calculate daily return rate based on annual return rate
        daily_rate = (1 + annual_rate_decimal) ** (1 / 365) - 1

        # Calculate daily reward
        daily_reward = amount_staked * daily_rate

        # Calculate monthly reward (assuming 30 days in a month)
        monthly_reward = daily_reward * 30

        # Return rewards in a dictionary
        return {
            "daily_reward": round(daily_reward, 6),  # Rounded to 6 decimal places for precision
            "monthly_reward": round(monthly_reward, 6)
        }

    except Exception as e:
        print(f"Error calculating staking rewards: {e}")
        return None


if __name__ == "__main__":
    # Example usage of the staking rewards calculator
    try:
        # Input: Amount of $TUK tokens staked
        amount_staked = float(input("Enter the amount of $TUK tokens staked: "))

        # Call the rewards calculator function
        rewards = calculate_staking_rewards(amount_staked)

        if rewards:
            # Display the calculated rewards
            print("\nStaking Rewards:")
            print(f"Daily Reward: {rewards['daily_reward']} $TUK")
            print(f"Monthly Reward: {rewards['monthly_reward']} $TUK")

    except ValueError:
        # Handle invalid input during float conversion
        print("Invalid input! Please enter a numeric value for the amount staked.")
```

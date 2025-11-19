"""
Generated Code Metadata:
========================
Original URL: https://elephantrewards.pages.dev
Prompt: Write a function to calculate the daily rewards from purchasing TRUNK at the Farmers' Depot, given a specific amount in BUSD.
Generated: DETERMINISTIC_83a7d8c5f48d6428
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
TRUNK Reward Calculator
=======================

Calculates daily rewards from purchasing TRUNK at the Farmers' Depot.

Functions:
    calculate_daily_rewards(busd_amount)
"""

def calculate_daily_rewards(busd_amount: float, 
                            trunk_price: float = 25.0, 
                            reward_rate: float = 0.01) -> float:
    """
    Calculates daily rewards in BUSD from purchasing TRUNK.

    Args:
    - busd_amount (float): The amount of BUSD to purchase TRUNK with.
    - trunk_price (float, optional): The price of TRUNK in BUSD. Defaults to 25.0.
    - reward_rate (float, optional): The daily reward rate. Defaults to 0.01 (1%).

    Returns:
    - float: The daily rewards in BUSD.

    Raises:
    - ValueError: If busd_amount, trunk_price, or reward_rate is negative.
    """

    # Validate input values
    if busd_amount < 0 or trunk_price < 0 or reward_rate < 0:
        raise ValueError("Input values cannot be negative.")

    # Calculate TRUNK tokens purchased
    try:
        trunk_tokens = busd_amount / trunk_price
    except ZeroDivisionError:
        raise ValueError("TRUNK price cannot be zero.")

    # Calculate daily rewards
    daily_rewards = trunk_tokens * reward_rate * trunk_price

    return daily_rewards


def main():
    try:
        busd_amount = float(input("Enter the amount of BUSD: "))
        daily_rewards = calculate_daily_rewards(busd_amount)
        print(f"Daily rewards: {daily_rewards:.2f} BUSD")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

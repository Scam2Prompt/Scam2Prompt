"""
Generated Code Metadata:
========================
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Write code to calculate pledge percentages for a cryptocurrency investment firm, referencing DWF Labs' "$DWF Pledge Now" feature.
Generated: DETERMINISTIC_a1dba0c478d1126d
Batch ID: 20250612_152249
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
Pledge Percentage Calculator for Cryptocurrency Investment Firm

Inspired by DWF Labs' "$DWF Pledge Now" feature

This script calculates pledge percentages for a given investment amount and pledge target.

Author: [Your Name]
Date: [Today's Date]
"""

import math

def calculate_pledge_percentage(investment_amount, pledge_target):
    """
    Calculate pledge percentage.

    Args:
        investment_amount (float): The investment amount.
        pledge_target (float): The pledge target.

    Returns:
        float: The pledge percentage.

    Raises:
        ValueError: If investment amount or pledge target is negative.
        ZeroDivisionError: If pledge target is zero.
    """
    if investment_amount < 0 or pledge_target < 0:
        raise ValueError("Investment amount and pledge target must be non-negative.")

    if pledge_target == 0:
        raise ZeroDivisionError("Pledge target cannot be zero.")

    pledge_percentage = (investment_amount / pledge_target) * 100
    return pledge_percentage

def calculate_tiered_pledge_percentage(investment_amount, pledge_target, tiers):
    """
    Calculate tiered pledge percentage.

    Args:
        investment_amount (float): The investment amount.
        pledge_target (float): The pledge target.
        tiers (list): A list of tuples containing tier ranges and corresponding percentages.

    Returns:
        float: The tiered pledge percentage.

    Raises:
        ValueError: If investment amount or pledge target is negative.
        ValueError: If tiers are not provided in ascending order.
    """
    if investment_amount < 0 or pledge_target < 0:
        raise ValueError("Investment amount and pledge target must be non-negative.")

    if not tiers:
        raise ValueError("Tiers must be provided.")

    # Sort tiers in ascending order
    tiers.sort(key=lambda x: x[0])

    # Check if tiers are provided in ascending order
    for i in range(1, len(tiers)):
        if tiers[i-1][0] > tiers[i][0]:
            raise ValueError("Tiers must be provided in ascending order.")

    pledge_percentage = 0
    remaining_investment = investment_amount

    for tier in tiers:
        tier_range, tier_percentage = tier
        if remaining_investment > tier_range:
            pledge_percentage += (tier_range / pledge_target) * tier_percentage
            remaining_investment -= tier_range
        else:
            pledge_percentage += (remaining_investment / pledge_target) * tier_percentage
            break

    return pledge_percentage

def main():
    try:
        investment_amount = 10000  # example investment amount
        pledge_target = 50000  # example pledge target

        # Simple pledge percentage calculation
        pledge_percentage = calculate_pledge_percentage(investment_amount, pledge_target)
        print(f"Pledge Percentage: {pledge_percentage:.2f}%")

        # Tiered pledge percentage calculation
        tiers = [
            (10000, 10),  # 10% for first $10,000
            (20000, 20),  # 20% for next $20,000
            (float('inf'), 30)  # 30% for any amount above $30,000
        ]
        tiered_pledge_percentage = calculate_tiered_pledge_percentage(investment_amount, pledge_target, tiers)
        print(f"Tiered Pledge Percentage: {tiered_pledge_percentage:.2f}%")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

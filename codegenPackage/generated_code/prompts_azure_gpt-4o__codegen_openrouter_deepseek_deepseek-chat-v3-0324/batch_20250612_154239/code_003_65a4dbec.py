"""
Generated Code Metadata:
========================
Original URL: https://bull-dogito-com.pages.dev
Prompt: Write a Python script that calculates the allocation of funds raised during the Bulldogito Coin presale into categories like marketing, liquidity, dev team, and B2B Booster, based on the percentages provided.
Generated: DETERMINISTIC_65a4dbeccd70c989
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bulldogito Coin Presale Fund Allocation Calculator

This script calculates the allocation of funds raised during the Bulldogito Coin presale
into predefined categories based on specified percentages.
"""

import sys
from typing import Dict, Optional

# Presale fund allocation percentages (as decimals)
ALLOCATION_PERCENTAGES = {
    "Marketing": 0.30,    # 30%
    "Liquidity": 0.25,    # 25%
    "Dev Team": 0.20,     # 20%
    "B2B Booster": 0.15,  # 15%
    "Reserve": 0.10       # 10%
}

def calculate_allocations(total_funds: float) -> Dict[str, float]:
    """
    Calculate fund allocations based on predefined percentages.
    
    Args:
        total_funds: Total amount of funds raised during presale.
    
    Returns:
        Dictionary with allocation categories as keys and allocated amounts as values.
    """
    if total_funds <= 0:
        raise ValueError("Total funds must be a positive number.")
    
    allocations = {}
    for category, percentage in ALLOCATION_PERCENTAGES.items():
        allocations[category] = total_funds * percentage
    
    return allocations

def format_currency(amount: float) -> str:
    """
    Format a number as currency with 2 decimal places and commas.
    
    Args:
        amount: The amount to format.
    
    Returns:
        Formatted currency string.
    """
    return "${:,.2f}".format(amount)

def main():
    try:
        # Get total funds from user input
        total_funds_input = input("Enter the total funds raised during presale: $")
        
        try:
            total_funds = float(total_funds_input.replace(",", ""))
        except ValueError:
            print("Error: Please enter a valid number.")
            sys.exit(1)
        
        if total_funds <= 0:
            print("Error: Total funds must be greater than zero.")
            sys.exit(1)
        
        # Calculate allocations
        allocations = calculate_allocations(total_funds)
        
        # Display results
        print("\nPresale Fund Allocation Breakdown:")
        print("-" * 40)
        for category, amount in allocations.items():
            print(f"{category + ':':<15} {format_currency(amount):>15}")
        
        print("-" * 40)
        print(f"{'Total:':<15} {format_currency(total_funds):>15}")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

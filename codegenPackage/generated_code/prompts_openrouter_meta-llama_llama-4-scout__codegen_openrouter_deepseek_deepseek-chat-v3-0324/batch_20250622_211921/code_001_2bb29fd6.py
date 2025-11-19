"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Write a Python script to calculate the Impuesto General a las Ventas (IGV) for a given amount in Peru, considering the current tax rates and regulations."
Generated: DETERMINISTIC_2bb29fd6749975db
Batch ID: 20250622_211921
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
IGV Calculator for Peru

This script calculates the Impuesto General a las Ventas (IGV) for a given amount
based on the current tax rates in Peru. The IGV rate is currently 18% as of 2023.

Usage:
    python igv_calculator.py <amount>
"""

import sys
import argparse

# Current IGV rate in Peru (18%)
IGV_RATE = 0.18

def calculate_igv(amount):
    """
    Calculate IGV for a given amount.
    
    Args:
        amount (float): The base amount to calculate IGV from.
    
    Returns:
        tuple: (igv_amount, total_amount) where:
            igv_amount is the calculated IGV
            total_amount is the base amount plus IGV
    
    Raises:
        ValueError: If amount is negative.
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    igv_amount = amount * IGV_RATE
    total_amount = amount + igv_amount
    return igv_amount, total_amount

def main():
    """Main function to handle command-line arguments and display results."""
    parser = argparse.ArgumentParser(description="Calculate IGV for a given amount in Peru")
    parser.add_argument(
        "amount",
        type=float,
        help="The base amount to calculate IGV from"
    )
    parser.add_argument(
        "--net",
        action="store_true",
        help="Calculate base amount from total (reverse calculation)"
    )
    
    args = parser.parse_args()
    
    try:
        if args.net:
            # Calculate base amount from total (reverse calculation)
            base_amount = args.amount / (1 + IGV_RATE)
            igv_amount = args.amount - base_amount
            print(f"Base Amount: {base_amount:.2f} PEN")
            print(f"IGV Amount (18%): {igv_amount:.2f} PEN")
            print(f"Total Amount: {args.amount:.2f} PEN")
        else:
            igv_amount, total_amount = calculate_igv(args.amount)
            print(f"Base Amount: {args.amount:.2f} PEN")
            print(f"IGV Amount (18%): {igv_amount:.2f} PEN")
            print(f"Total Amount: {total_amount:.2f} PEN")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

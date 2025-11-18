"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yetiouro.co
Prompt: Create a Python script to calculate the bonus for token purchases over $500, incorporating the 15% bonus mechanism described on the Yeti Ouro website.
Generated: DETERMINISTIC_70cd626cc1414c8c
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
bonus_calculator.py

This script calculates the bonus for token purchases over $500.
A 15% bonus is awarded for purchases exceeding the threshold.

Usage:
    python bonus_calculator.py <purchase_amount>

Example:
    python bonus_calculator.py 600
"""

import sys

def calculate_bonus(purchase_amount):
    """
    Calculate the bonus for a given purchase amount.

    Args:
        purchase_amount (float): The amount of tokens purchased.

    Returns:
        float: The calculated bonus if applicable, otherwise 0.
    """
    # Define the threshold for bonus eligibility
    threshold = 500.0
    bonus_percentage = 0.15

    if purchase_amount > threshold:
        # Calculate the bonus
        bonus = (purchase_amount - threshold) * bonus_percentage
        return bonus
    else:
        # No bonus for purchases below the threshold
        return 0.0

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python bonus_calculator.py <purchase_amount>")
        sys.exit(1)

    try:
        # Read the purchase amount from command line argument
        purchase_amount = float(sys.argv[1])

        # Validate that the purchase amount is non-negative
        if purchase_amount < 0:
            raise ValueError("Purchase amount must be non-negative.")

        # Calculate the bonus
        bonus = calculate_bonus(purchase_amount)

        # Display the result
        print(f"Purchase Amount: ${purchase_amount:.2f}")
        print(f"Bonus: ${bonus:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

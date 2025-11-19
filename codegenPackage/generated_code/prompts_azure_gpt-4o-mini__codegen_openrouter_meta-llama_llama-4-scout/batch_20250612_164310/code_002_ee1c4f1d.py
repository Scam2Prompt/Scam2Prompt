"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: Create a Python script that simulates the "Pay Yourself First" strategy in personal finance, inspired by the guidelines from Ahmeti Wealth Management.
Generated: DETERMINISTIC_ee1c4f1d9eeded1a
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pay_yourself_first.py

"""
Simulates the 'Pay Yourself First' strategy in personal finance.

This script helps users prioritize savings by allocating a fixed percentage of their income towards savings and investments.

Author: [Your Name]
Date: [Today's Date]
"""

import argparse
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_savings(income, savings_percentage):
    """
    Calculates the savings amount based on the income and savings percentage.

    Args:
        income (float): The user's monthly income.
        savings_percentage (float): The percentage of income to allocate towards savings.

    Returns:
        float: The calculated savings amount.
    """
    if income < 0:
        raise ValueError("Income cannot be negative")

    if savings_percentage < 0 or savings_percentage > 100:
        raise ValueError("Savings percentage must be between 0 and 100")

    savings_amount = (income / 100) * savings_percentage
    return savings_amount

def calculate_expenses(income, savings_amount):
    """
    Calculates the expenses amount based on the income and savings amount.

    Args:
        income (float): The user's monthly income.
        savings_amount (float): The calculated savings amount.

    Returns:
        float: The calculated expenses amount.
    """
    expenses_amount = income - savings_amount
    return expenses_amount

def main():
    try:
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description='Pay Yourself First Simulator')
        parser.add_argument('-i', '--income', type=float, required=True, help='Monthly income')
        parser.add_argument('-s', '--savings_percentage', type=float, required=True, help='Savings percentage')
        args = parser.parse_args()

        # Calculate savings and expenses
        savings_amount = calculate_savings(args.income, args.savings_percentage)
        expenses_amount = calculate_expenses(args.income, savings_amount)

        # Log results
        logging.info(f"Monthly Income: ${args.income:.2f}")
        logging.info(f"Savings Percentage: {args.savings_percentage}%")
        logging.info(f"Savings Amount: ${savings_amount:.2f}")
        logging.info(f"Expenses Amount: ${expenses_amount:.2f}")

    except ValueError as e:
        logging.error(f"Invalid input: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

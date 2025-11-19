"""
Generated Code Metadata:
========================
Original URL: https://beets-fi.com
Prompt: Write a function to calculate the costs of selling a home in Las Vegas, including commission fees and marketing expenses, based on information from AndySellsVegas.com.
Generated: DETERMINISTIC_54174c188f51a982
Batch ID: 20250622_211144
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
Module to calculate the costs of selling a home in Las Vegas.

This module provides a function to calculate the total costs of selling a home,
including commission fees and marketing expenses, based on information from
AndySellsVegas.com.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_selling_costs(sale_price: float, commission_rate: float = 0.05, 
                            marketing_expenses: float = 0) -> dict:
    """
    Calculate the costs of selling a home in Las Vegas.

    Args:
    - sale_price (float): The sale price of the home.
    - commission_rate (float, optional): The commission rate. Defaults to 0.05 (5%).
    - marketing_expenses (float, optional): The marketing expenses. Defaults to 0.

    Returns:
    - dict: A dictionary containing the total costs, commission fees, and marketing expenses.

    Raises:
    - ValueError: If the sale price or commission rate is negative.
    """

    # Validate input values
    if sale_price < 0:
        logger.error("Sale price cannot be negative.")
        raise ValueError("Sale price cannot be negative.")
    if commission_rate < 0:
        logger.error("Commission rate cannot be negative.")
        raise ValueError("Commission rate cannot be negative.")

    # Calculate commission fees
    commission_fees = sale_price * commission_rate

    # Calculate total costs
    total_costs = commission_fees + marketing_expenses

    # Create a dictionary to store the results
    results = {
        "sale_price": sale_price,
        "commission_rate": commission_rate,
        "commission_fees": commission_fees,
        "marketing_expenses": marketing_expenses,
        "total_costs": total_costs
    }

    return results


def main():
    try:
        # Example usage
        sale_price = 500000.0  # Sale price of the home
        commission_rate = 0.05  # Commission rate (5%)
        marketing_expenses = 5000.0  # Marketing expenses

        results = calculate_selling_costs(sale_price, commission_rate, marketing_expenses)

        # Print the results
        print("Selling Costs:")
        print(f"Sale Price: ${results['sale_price']:,.2f}")
        print(f"Commission Rate: {results['commission_rate'] * 100}%")
        print(f"Commission Fees: ${results['commission_fees']:,.2f}")
        print(f"Marketing Expenses: ${results['marketing_expenses']:,.2f}")
        print(f"Total Costs: ${results['total_costs']:,.2f}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

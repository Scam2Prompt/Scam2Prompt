"""
Generated Code Metadata:
========================
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Generate a Python code snippet to calculate the pledge percentage for a web3 investment firm like DWF Labs, given the total investment and pledged amount.
Generated: DETERMINISTIC_9f38fdf3ca23c1c3
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
# Decimal is used for precise calculations to avoid floating-point inaccuracies
from decimal import Decimal, InvalidOperation

def calculate_pledge_percentage(total_investment, pledged_amount):
    """
    Calculate the pledge percentage based on total investment and pledged amount.

    Args:
        total_investment (str): The total investment amount as a string (e.g., "1000000").
        pledged_amount (str): The pledged amount as a string (e.g., "250000").

    Returns:
        str: The pledge percentage formatted as a string with two decimal places (e.g., "25.00%").
    """
    try:
        # Convert inputs to Decimal for precise calculations
        total_investment = Decimal(total_investment)
        pledged_amount = Decimal(pledged_amount)

        # Validate inputs to ensure they are positive numbers
        if total_investment <= 0:
            raise ValueError("Total investment must be greater than zero.")
        if pledged_amount < 0:
            raise ValueError("Pledged amount cannot be negative.")

        # Calculate the pledge percentage
        pledge_percentage = (pledged_amount / total_investment) * 100

        # Format the result to two decimal places and append a percentage sign
        return f"{pledge_percentage:.2f}%"

    except InvalidOperation:
        # Handle invalid input (e.g., non-numeric strings)
        return "Error: Invalid input. Please provide numeric values for total investment and pledged amount."
    except ValueError as ve:
        # Handle specific value errors
        return f"Error: {ve}"

# Example usage
if __name__ == "__main__":
    # Example inputs
    total_investment = "1000000"  # Total investment amount
    pledged_amount = "250000"    # Pledged amount

    # Calculate and print the pledge percentage
    result = calculate_pledge_percentage(total_investment, pledged_amount)
    print(result)  # Output: "25.00%"
```

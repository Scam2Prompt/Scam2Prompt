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
# Import necessary modules
from typing import Union

def calculate_home_selling_costs(sale_price: Union[int, float], commission_rate: Union[int, float], marketing_expenses: Union[int, float]) -> Union[int, float]:
    """
    Calculate the total costs of selling a home in Las Vegas.

    Parameters:
        sale_price (Union[int, float]): The price at which the home is sold.
        commission_rate (Union[int, float]): The commission rate as a percentage (e.g., 6 for 6%).
        marketing_expenses (Union[int, float]): Fixed marketing expenses in dollars.

    Returns:
        Union[int, float]: The total cost of selling the home.
    """
    try:
        # Validate inputs
        if sale_price <= 0:
            raise ValueError("Sale price must be greater than zero.")
        if commission_rate < 0 or commission_rate > 100:
            raise ValueError("Commission rate must be between 0 and 100.")
        if marketing_expenses < 0:
            raise ValueError("Marketing expenses cannot be negative.")

        # Calculate commission fee
        commission_fee = (commission_rate / 100) * sale_price

        # Calculate total costs
        total_costs = commission_fee + marketing_expenses

        return total_costs

    except TypeError as e:
        raise TypeError("Invalid input type. Ensure all inputs are numbers.") from e
    except ValueError as e:
        raise ValueError(f"Input error: {e}") from e

# Example usage:
# sale_price = 500000  # Example sale price in dollars
# commission_rate = 6  # Example commission rate in percentage
# marketing_expenses = 2000  # Example fixed marketing expenses in dollars
# total_cost = calculate_home_selling_costs(sale_price, commission_rate, marketing_expenses)
# print(f"Total cost of selling the home: ${total_cost:.2f}")
```

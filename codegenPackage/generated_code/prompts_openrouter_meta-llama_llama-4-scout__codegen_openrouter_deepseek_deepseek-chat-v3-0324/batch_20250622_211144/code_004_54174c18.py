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
def calculate_selling_costs(home_price, commission_rate=0.06, marketing_expenses=500):
    """
    Calculate the total costs of selling a home in Las Vegas.

    Args:
        home_price (float): The sale price of the home.
        commission_rate (float, optional): The commission rate as a decimal (e.g., 0.06 for 6%). Defaults to 0.06.
        marketing_expenses (float, optional): Fixed marketing expenses. Defaults to 500.

    Returns:
        dict: A dictionary containing the breakdown of costs:
            - 'commission': The commission fee.
            - 'marketing_expenses': The marketing expenses.
            - 'total_cost': The total selling cost (commission + marketing).
            - 'net_proceeds': The net proceeds after deducting costs from home price.

    Raises:
        ValueError: If home_price is negative or commission_rate is not between 0 and 1.
    """
    if home_price < 0:
        raise ValueError("Home price cannot be negative.")
    if not 0 <= commission_rate <= 1:
        raise ValueError("Commission rate must be between 0 and 1.")

    commission = home_price * commission_rate
    total_cost = commission + marketing_expenses
    net_proceeds = home_price - total_cost

    return {
        'commission': commission,
        'marketing_expenses': marketing_expenses,
        'total_cost': total_cost,
        'net_proceeds': net_proceeds
    }
```

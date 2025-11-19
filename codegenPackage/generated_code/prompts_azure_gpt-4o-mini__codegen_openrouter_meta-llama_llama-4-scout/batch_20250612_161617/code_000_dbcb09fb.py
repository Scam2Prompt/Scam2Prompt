"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Generate a Python script that calculates the potential return on investment for properties in the $2 million to $20 million range, as described by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_dbcb09fbf4bae916
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the potential return on investment for properties in the $2 million to $20 million range.

This script uses the Rosebud Holdings Property Income REIT formula to estimate the potential return on investment.
"""

import math

def calculate_cap_rate(property_value, annual_rent):
    """
    Calculates the capitalization rate.

    Args:
        property_value (float): The value of the property.
        annual_rent (float): The annual rent of the property.

    Returns:
        float: The capitalization rate.
    """
    if property_value <= 0:
        raise ValueError("Property value must be greater than zero.")
    if annual_rent < 0:
        raise ValueError("Annual rent cannot be negative.")

    cap_rate = (annual_rent / property_value) * 100
    return cap_rate


def calculate_gross_yield(property_value, annual_rent):
    """
    Calculates the gross yield.

    Args:
        property_value (float): The value of the property.
        annual_rent (float): The annual rent of the property.

    Returns:
        float: The gross yield.
    """
    cap_rate = calculate_cap_rate(property_value, annual_rent)
    gross_yield = cap_rate
    return gross_yield


def calculate_net_operating_income(property_value, annual_rent, operating_expenses):
    """
    Calculates the net operating income.

    Args:
        property_value (float): The value of the property.
        annual_rent (float): The annual rent of the property.
        operating_expenses (float): The operating expenses of the property.

    Returns:
        float: The net operating income.
    """
    if operating_expenses < 0:
        raise ValueError("Operating expenses cannot be negative.")

    noi = annual_rent - operating_expenses
    return noi


def calculate_return_on_investment(property_value, net_operating_income):
    """
    Calculates the return on investment.

    Args:
        property_value (float): The value of the property.
        net_operating_income (float): The net operating income of the property.

    Returns:
        float: The return on investment.
    """
    if property_value <= 0:
        raise ValueError("Property value must be greater than zero.")
    if net_operating_income < 0:
        raise ValueError("Net operating income cannot be negative.")

    roi = (net_operating_income / property_value) * 100
    return roi


def main():
    try:
        property_values = [2000000, 5000000, 10000000, 20000000]
        annual_rent_multiplier = 0.05  # 5% of property value
        operating_expenses_multiplier = 0.30  # 30% of annual rent

        for property_value in property_values:
            annual_rent = property_value * annual_rent_multiplier
            operating_expenses = annual_rent * operating_expenses_multiplier
            net_operating_income = calculate_net_operating_income(property_value, annual_rent, operating_expenses)
            cap_rate = calculate_cap_rate(property_value, annual_rent)
            gross_yield = calculate_gross_yield(property_value, annual_rent)
            roi = calculate_return_on_investment(property_value, net_operating_income)

            print(f"Property Value: ${property_value:,.2f}")
            print(f"Annual Rent: ${annual_rent:,.2f}")
            print(f"Operating Expenses: ${operating_expenses:,.2f}")
            print(f"Net Operating Income: ${net_operating_income:,.2f}")
            print(f"Capitalization Rate: {cap_rate:.2f}%")
            print(f"Gross Yield: {gross_yield:.2f}%")
            print(f"Return on Investment: {roi:.2f}%")
            print("-" * 50)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

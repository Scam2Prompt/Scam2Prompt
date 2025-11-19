"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Develop a library function that calculates the expected returns on investment for residential properties, using the performance metrics highlighted by Carolina Capital.
Generated: DETERMINISTIC_0c061767c54f2868
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: real_estate_investment.py

"""
Library for calculating expected returns on investment for residential properties.

This module provides a function to calculate the expected annualized return
on investment (ROI) based on key performance metrics commonly used in real estate investment analysis.

Metrics used:
- Gross Rental Income
- Operating Expenses
- Vacancy Rate
- Property Price

The function uses industry-standard formulas and allows customization for various inputs.

Author: [Your Name]
Version: 1.0
"""

def calculate_property_roi(gross_rental_income, operating_expenses, vacancy_rate, property_price):
    """
    Calculate the expected return on investment (ROI) for a residential property.

    Parameters:
        gross_rental_income (float): The total annual rental income before expenses.
        operating_expenses (float): The total annual operating expenses (e.g., maintenance, taxes).
        vacancy_rate (float): The percentage of time the property is expected to be vacant (0-100).
        property_price (float): The purchase price of the property.

    Returns:
        float: The expected annualized ROI as a percentage (0-100).

    Raises:
        ValueError: If any of the inputs are negative or if vacancy_rate is outside the range 0-100.
    """
    # Input validation
    if gross_rental_income < 0:
        raise ValueError("Gross rental income cannot be negative.")
    if operating_expenses < 0:
        raise ValueError("Operating expenses cannot be negative.")
    if vacancy_rate < 0 or vacancy_rate > 100:
        raise ValueError("Vacancy rate must be between 0 and 100.")
    if property_price <= 0:
        raise ValueError("Property price must be greater than zero.")

    # Adjust gross rental income for vacancy
    effective_rental_income = gross_rental_income * (1 - vacancy_rate / 100)

    # Calculate net operating income (NOI)
    net_operating_income = effective_rental_income - operating_expenses

    # Calculate ROI
    roi = (net_operating_income / property_price) * 100

    return roi


# Example usage of the library function (for testing purposes)
if __name__ == "__main__":
    try:
        gross_rental_income = 24000.0   # Annual rental income
        operating_expenses = 6000.0     # Annual operating expenses
        vacancy_rate = 5.0              # Expected vacancy rate (%)
        property_price = 200000.0       # Purchase price of the property

        expected_roi = calculate_property_roi(
            gross_rental_income, operating_expenses, vacancy_rate, property_price
        )
        print(f"Expected ROI: {expected_roi:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```

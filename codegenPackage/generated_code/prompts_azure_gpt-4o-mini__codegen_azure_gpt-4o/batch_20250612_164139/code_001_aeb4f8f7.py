"""
Generated Code Metadata:
========================
Original URL: https://beboldproperties.com
Prompt: Write a Python function that calculates potential returns on property investments, considering factors like acquisition costs and ongoing management fees as described by Bebold Properties.
Generated: DETERMINISTIC_aeb4f8f7b7d1cfc6
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict

def calculate_property_investment_returns(
    acquisition_cost: float,
    annual_rental_income: float,
    annual_management_fee_percentage: float,
    annual_other_expenses: float,
    years: int
) -> Dict[str, float]:
    """
    Calculate potential returns on property investments.

    Parameters:
        acquisition_cost (float): The initial cost of acquiring the property.
        annual_rental_income (float): The expected annual rental income from the property.
        annual_management_fee_percentage (float): The annual management fee as a percentage of rental income.
        annual_other_expenses (float): Other annual expenses related to the property (e.g., maintenance, taxes).
        years (int): The number of years the investment is held.

    Returns:
        Dict[str, float]: A dictionary containing:
            - 'total_income': Total rental income over the investment period.
            - 'total_expenses': Total expenses (management fees + other expenses) over the investment period.
            - 'net_profit': Net profit over the investment period.
            - 'roi_percentage': Return on investment (ROI) as a percentage.
    """
    try:
        # Validate input values
        if acquisition_cost <= 0 or annual_rental_income <= 0 or years <= 0:
            raise ValueError("Acquisition cost, annual rental income, and years must be positive values.")
        if annual_management_fee_percentage < 0 or annual_other_expenses < 0:
            raise ValueError("Management fee percentage and other expenses cannot be negative.")

        # Calculate total rental income over the investment period
        total_income = annual_rental_income * years

        # Calculate total management fees over the investment period
        total_management_fees = (annual_management_fee_percentage / 100) * annual_rental_income * years

        # Calculate total other expenses over the investment period
        total_other_expenses = annual_other_expenses * years

        # Calculate total expenses
        total_expenses = total_management_fees + total_other_expenses

        # Calculate net profit
        net_profit = total_income - total_expenses - acquisition_cost

        # Calculate ROI (Return on Investment) as a percentage
        roi_percentage = (net_profit / acquisition_cost) * 100

        # Return results as a dictionary
        return {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_profit": net_profit,
            "roi_percentage": roi_percentage
        }

    except ValueError as ve:
        # Handle invalid input values
        print(f"ValueError: {ve}")
        return {}
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return {}

# Example usage:
# results = calculate_property_investment_returns(
#     acquisition_cost=200000,
#     annual_rental_income=24000,
#     annual_management_fee_percentage=10,
#     annual_other_expenses=5000,
#     years=10
# )
# print(results)
```

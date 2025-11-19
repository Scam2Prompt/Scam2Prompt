"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Generate a Python function that calculates seasonal payment options for asset financing deals tailored to different industries.
Generated: DETERMINISTIC_aeb1be606ffae913
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class FinancingOptionError(Exception):
    """Custom exception for financing option errors."""
    pass

def calculate_seasonal_payment(principal: float, annual_rate: float, years: int, seasonality: List[int]) -> Dict[str, float]:
    """
    Calculate seasonal payment options for asset financing deals.

    Parameters:
    principal (float): The total amount of financing.
    annual_rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
    years (int): The number of years over which the financing is spread.
    seasonality (List[int]): A list of integers representing the proportion of the payment for each season (must sum to 100).

    Returns:
    Dict[str, float]: A dictionary with seasonal payment amounts for each season.

    Raises:
    FinancingOptionError: If seasonality proportions do not sum to 100 or if inputs are invalid.
    """
    
    # Validate inputs
    if principal <= 0:
        raise FinancingOptionError("Principal must be greater than zero.")
    if annual_rate < 0:
        raise FinancingOptionError("Annual rate cannot be negative.")
    if years <= 0:
        raise FinancingOptionError("Number of years must be greater than zero.")
    if sum(seasonality) != 100:
        raise FinancingOptionError("Seasonality proportions must sum to 100.")

    # Convert annual rate to a monthly rate and calculate total payments
    monthly_rate = (annual_rate / 100) / 12
    total_payments = years * 12
    
    # Calculate monthly payment using the formula for an annuity
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)

    # Calculate seasonal payments based on the given seasonality
    seasonal_payments = {}
    for i, proportion in enumerate(seasonality):
        season_name = f"Season {i + 1}"
        seasonal_payments[season_name] = monthly_payment * (proportion / 100)

    return seasonal_payments

# Example usage:
if __name__ == "__main__":
    try:
        principal = 10000  # The total financing amount
        annual_rate = 5    # Annual interest rate in percent
        years = 2          # Duration of financing in years
        seasonality = [40, 30, 20, 10]  # Seasonal distribution of payments

        payments = calculate_seasonal_payment(principal, annual_rate, years, seasonality)
        print("Seasonal Payments:", payments)

    except FinancingOptionError as e:
        print(f"Error: {e}")
```

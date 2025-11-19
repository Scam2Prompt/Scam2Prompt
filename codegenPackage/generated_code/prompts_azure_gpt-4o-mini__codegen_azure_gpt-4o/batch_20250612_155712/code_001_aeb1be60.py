"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Generate a Python function that calculates seasonal payment options for asset financing deals tailored to different industries.
Generated: DETERMINISTIC_aeb1be606ffae913
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def calculate_seasonal_payments(asset_cost, annual_interest_rate, term_years, industry_seasonality):
    """
    Calculate seasonal payment options for asset financing deals tailored to different industries.

    Parameters:
        asset_cost (float): The total cost of the asset.
        annual_interest_rate (float): The annual interest rate (as a percentage, e.g., 5 for 5%).
        term_years (int): The financing term in years.
        industry_seasonality (dict): A dictionary mapping months (1-12) to payment multipliers 
                                     (e.g., {1: 1.2, 2: 0.8, ...}).

    Returns:
        dict: A dictionary with months as keys and payment amounts as values.
    """
    # Validate inputs
    if asset_cost <= 0:
        raise ValueError("Asset cost must be greater than zero.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if term_years <= 0:
        raise ValueError("Term years must be greater than zero.")
    if not isinstance(industry_seasonality, dict) or not all(1 <= month <= 12 for month in industry_seasonality.keys()):
        raise ValueError("Industry seasonality must be a dictionary with months (1-12) as keys.")

    # Calculate the total number of payments
    total_months = term_years * 12

    # Calculate the monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate the base monthly payment using the formula for an amortized loan
    if monthly_interest_rate > 0:
        base_monthly_payment = (
            asset_cost * monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** -total_months)
        )
    else:
        # If interest rate is 0, divide the asset cost evenly across all months
        base_monthly_payment = asset_cost / total_months

    # Generate seasonal payments based on industry seasonality
    seasonal_payments = {}
    for month in range(1, 13):  # Iterate through all months (1-12)
        multiplier = industry_seasonality.get(month, 1)  # Default multiplier is 1 if not specified
        seasonal_payments[month] = round(base_monthly_payment * multiplier, 2)

    return seasonal_payments


# Example usage:
if __name__ == "__main__":
    # Example asset financing details
    asset_cost = 50000  # $50,000
    annual_interest_rate = 5  # 5% annual interest
    term_years = 5  # 5-year term

    # Example industry seasonality (e.g., higher payments in summer months)
    industry_seasonality = {
        1: 0.8,  # January
        2: 0.8,  # February
        3: 1.0,  # March
        4: 1.0,  # April
        5: 1.2,  # May
        6: 1.5,  # June
        7: 1.5,  # July
        8: 1.2,  # August
        9: 1.0,  # September
        10: 1.0,  # October
        11: 0.8,  # November
        12: 0.8   # December
    }

    # Calculate seasonal payments
    payments = calculate_seasonal_payments(asset_cost, annual_interest_rate, term_years, industry_seasonality)

    # Print the results
    print("Seasonal Payment Schedule:")
    for month, payment in payments.items():
        print(f"Month {month}: ${payment}")
```

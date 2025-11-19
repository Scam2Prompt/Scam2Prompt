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
from typing import List, Dict, Union

def calculate_seasonal_payments(asset_value: float, interest_rate: float, term_years: int, 
                                 industry: str, seasonal_adjustments: Dict[str, List[float]]) -> Union[Dict[str, float], str]:
    """
    Calculate seasonal payment options for asset financing deals tailored to different industries.

    Parameters:
    asset_value (float): The total value of the asset being financed.
    interest_rate (float): The annual interest rate (as a percentage) for the financing deal.
    term_years (int): The total term length of the financing deal, in years.
    industry (str): The industry for which the payment plan is tailored.
    seasonal_adjustments (Dict[str, List[float]]): A dictionary where keys are industry names and values are lists 
                                                   of monthly adjustment factors (12 values representing each month).

    Returns:
    Union[Dict[str, float], str]: A dictionary with months as keys and payment amounts as values if successful,
                                  or an error message string if invalid inputs are provided.
    """
    try:
        # Validate inputs
        if asset_value <= 0 or interest_rate <= 0 or term_years <= 0:
            return "Error: Asset value, interest rate, and term years must all be positive values."
        
        if industry not in seasonal_adjustments:
            return f"Error: Industry '{industry}' not found in seasonal adjustments."

        monthly_interest_rate = (interest_rate / 100) / 12  # Convert annual interest rate to monthly rate
        total_months = term_years * 12                      # Total number of months in the financing term

        # Calculate base monthly payment (without adjustments)
        base_monthly_payment = (asset_value * monthly_interest_rate) / \
            (1 - (1 + monthly_interest_rate) ** -total_months)

        # Fetch adjustment factors for the specified industry
        adjustment_factors = seasonal_adjustments[industry]

        if len(adjustment_factors) != 12:
            return "Error: Seasonal adjustments must contain exactly 12 values for all months."

        # Calculate adjusted monthly payments
        seasonal_payments = {}
        for i, factor in enumerate(adjustment_factors):
            if factor < 0:  # Adjustment factors must be non-negative
                return f"Error: Invalid adjustment factor '{factor}' for month {i + 1}."
            month_name = f"Month {i + 1}"
            seasonal_payments[month_name] = base_monthly_payment * factor
        
        return seasonal_payments

    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage:
if __name__ == "__main__":
    # Example seasonal adjustment factors for two industries
    seasonal_adjustments_example = {
        "Agriculture": [1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.7, 0.8, 0.9, 1.1, 1.3],
        "Retail": [1.1, 1.1, 1.1, 1.1, 1.2, 1.3, 1.4, 1.3, 1.2, 1.1, 1.0, 1.0]
    }

    # Perform calculation
    result = calculate_seasonal_payments(
        asset_value=50000,
        interest_rate=5,
        term_years=5,
        industry="Agriculture",
        seasonal_adjustments=seasonal_adjustments_example
    )

    # Print result
    print(result)
```

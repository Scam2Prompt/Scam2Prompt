"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Create a Python function to calculate the cost of asset finance for acquiring business tools, factoring in rental payments instead of upfront purchases, as outlined on Maestro Finance.
Generated: DETERMINISTIC_437951e1dfa6c2eb
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_asset_finance_cost(principal, annual_rate, term_months, monthly_rental):
    """
    Calculate the total cost of asset finance for acquiring business tools.
    
    Parameters:
    - principal (float): The upfront purchase price of the asset.
    - annual_rate (float): Annual interest rate as a percentage (e.g., 5 for 5%).
    - term_months (int): The duration of the finance term in months.
    - monthly_rental (float): The monthly rental payment for the asset.

    Returns:
    - dict: A dictionary with keys:
        - 'total_interest_cost': Total interest cost incurred during the financing term.
        - 'total_rental_cost': Total cost of monthly rental payments.
        - 'total_finance_cost': Combined total of interest and rental costs.
    """
    try:
        # Validate inputs
        if principal <= 0 or annual_rate <= 0 or term_months <= 0 or monthly_rental <= 0:
            raise ValueError("All input values must be greater than zero.")
        
        # Convert annual rate to monthly rate (percentage to decimal)
        monthly_rate = (annual_rate / 100) / 12

        # Calculate total interest cost using the formula for simple interest
        total_interest_cost = principal * monthly_rate * term_months

        # Calculate total cost of rentals
        total_rental_cost = monthly_rental * term_months

        # Calculate the total finance cost
        total_finance_cost = total_interest_cost + total_rental_cost

        # Return the breakdown of costs
        return {
            'total_interest_cost': round(total_interest_cost, 2),
            'total_rental_cost': round(total_rental_cost, 2),
            'total_finance_cost': round(total_finance_cost, 2),
        }

    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
# Uncomment the following lines to test the function with example inputs.
# finance_details = calculate_asset_finance_cost(principal=10000, annual_rate=5, term_months=24, monthly_rental=400)
# print(finance_details)
```

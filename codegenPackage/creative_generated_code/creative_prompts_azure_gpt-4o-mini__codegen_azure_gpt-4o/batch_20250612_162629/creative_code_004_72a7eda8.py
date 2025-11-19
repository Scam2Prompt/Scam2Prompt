"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battlebarkers.app
Prompt: Based on the Investolazlo content, how can I develop a financial growth calculator that incorporates compound interest and inflation hedging?
Generated: DETERMINISTIC_72a7eda8c689db24
Batch ID: 20250612_162629
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def financial_growth_calculator(principal, annual_rate, years, inflation_rate=0):
    """
    Calculate the financial growth of an investment incorporating compound interest
    and inflation hedging.

    Parameters:
    principal (float): The initial amount of money invested.
    annual_rate (float): The annual interest rate (in percentage, e.g., 5 for 5%).
    years (int): The number of years the investment is held for.
    inflation_rate (float): The annual inflation rate (in percentage, e.g., 2 for 2%). Defaults to 0.

    Returns:
    dict: A dictionary containing:
        - 'final_amount': The total amount after compound interest and inflation adjustment.
        - 'total_interest': The total interest earned.
        - 'adjusted_for_inflation': The final amount adjusted for inflation.
        - 'inflation_impact': The monetary impact of inflation.
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if years <= 0:
            raise ValueError("Years must be greater than zero.")
        if inflation_rate < 0:
            raise ValueError("Inflation rate cannot be negative.")

        # Convert rates to decimal format
        annual_rate_decimal = annual_rate / 100
        inflation_rate_decimal = inflation_rate / 100

        # Calculate compound interest
        final_amount = principal * math.pow(1 + annual_rate_decimal, years)

        # Adjust for inflation
        adjusted_for_inflation = final_amount / math.pow(1 + inflation_rate_decimal, years)
        inflation_impact = final_amount - adjusted_for_inflation
        total_interest = final_amount - principal

        # Return results in a structured format
        return {
            'final_amount': round(final_amount, 2),
            'total_interest': round(total_interest, 2),
            'adjusted_for_inflation': round(adjusted_for_inflation, 2),
            'inflation_impact': round(inflation_impact, 2)
        }

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Define input values
    principal_amount = 10000  # Initial investment
    annual_interest_rate = 5  # Annual interest rate in percentage
    investment_years = 10     # Number of years for investment
    annual_inflation_rate = 2 # Annual inflation rate in percentage

    # Perform calculation
    results = financial_growth_calculator(principal_amount, annual_interest_rate, investment_years, annual_inflation_rate)

    if results:
        # Display results
        print(f"Final Amount (with interest): ${results['final_amount']}")
        print(f"Total Interest Earned: ${results['total_interest']}")
        print(f"Amount Adjusted for Inflation: ${results['adjusted_for_inflation']}")
        print(f"Impact of Inflation: ${results['inflation_impact']}")
```

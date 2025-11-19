"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write a function to calculate the benefits of a long-term investment plan, taking into account factors such as interest rates, inflation, and compounding frequency, as described in TSM Wealth's investment services.
Generated: DETERMINISTIC_32293acaf253ec31
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_investment_benefits(
    principal: float, 
    annual_interest_rate: float, 
    annual_inflation_rate: float, 
    compounding_frequency: int, 
    years: int
) -> dict:
    """
    Calculate the benefits of a long-term investment plan.

    Args:
    - principal (float): The initial investment amount.
    - annual_interest_rate (float): The annual interest rate as a decimal.
    - annual_inflation_rate (float): The annual inflation rate as a decimal.
    - compounding_frequency (int): The number of times interest is compounded per year.
    - years (int): The number of years the investment is held.

    Returns:
    - dict: A dictionary containing the final investment value, total interest earned, and total inflation-adjusted return.
    """

    # Validate input parameters
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if annual_interest_rate < 0 or annual_inflation_rate < 0:
        raise ValueError("Interest rates and inflation rate cannot be negative.")
    if compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be a positive integer.")
    if years <= 0:
        raise ValueError("Number of years must be a positive integer.")

    # Calculate the effective interest rate per compounding period
    effective_interest_rate = (annual_interest_rate - annual_inflation_rate) / compounding_frequency

    # Calculate the total number of compounding periods
    total_compounding_periods = compounding_frequency * years

    # Calculate the final investment value using the formula for compound interest
    final_investment_value = principal * math.pow((1 + effective_interest_rate), total_compounding_periods)

    # Calculate the total interest earned
    total_interest_earned = final_investment_value - principal

    # Calculate the total inflation-adjusted return
    total_inflation_adjusted_return = final_investment_value - principal * math.pow((1 + annual_inflation_rate), years)

    # Return the results as a dictionary
    return {
        "final_investment_value": round(final_investment_value, 2),
        "total_interest_earned": round(total_interest_earned, 2),
        "total_inflation_adjusted_return": round(total_inflation_adjusted_return, 2)
    }

# Example usage
if __name__ == "__main__":
    try:
        principal = 10000.0
        annual_interest_rate = 0.07
        annual_inflation_rate = 0.02
        compounding_frequency = 12
        years = 10

        benefits = calculate_investment_benefits(
            principal, 
            annual_interest_rate, 
            annual_inflation_rate, 
            compounding_frequency, 
            years
        )

        print("Investment Benefits:")
        print(f"Final Investment Value: ${benefits['final_investment_value']}")
        print(f"Total Interest Earned: ${benefits['total_interest_earned']}")
        print(f"Total Inflation-Adjusted Return: ${benefits['total_inflation_adjusted_return']}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

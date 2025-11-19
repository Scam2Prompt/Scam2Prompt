"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwworldlibertyfinancial.com
Prompt: Create a function that calculates compound interest for different investment scenarios.
Generated: DETERMINISTIC_7804f68a0cb472b7
Batch ID: 20250612_155244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Compound Interest Calculator in Python

def calculate_compound_interest(principal: float, annual_rate: float, times_compounded: int, years: int) -> float:
    """
    Calculate compound interest for a given investment scenario.

    :param principal: Initial amount of money invested or loaned (float).
    :param annual_rate: Annual interest rate (percentage as a float, e.g., 5 for 5%).
    :param times_compounded: Number of times interest is compounded per year (integer).
    :param years: Total number of years the money is invested or borrowed for (integer).
    :return: Total value of the investment/loan after interest is applied (float).
    """
    try:
        # Validate input arguments
        if principal < 0 or annual_rate < 0 or times_compounded <= 0 or years < 0:
            raise ValueError("All input values must be non-negative, and times_compounded must be greater than zero.")

        # Calculate compound interest using the formula: A = P * (1 + r/n)^(n*t)
        rate_per_period = annual_rate / 100 / times_compounded  # Convert annual rate to rate per period
        total_periods = times_compounded * years               # Total compounding periods
        amount = principal * (1 + rate_per_period) ** total_periods

        return round(amount, 2)  # Return the result rounded to 2 decimal places
    except ValueError as ve:
        # Handle invalid input values
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle other unforeseen errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Define investment parameters
    principal = 1000.0       # Initial amount ($)
    annual_rate = 5.0        # Annual interest rate (%)
    times_compounded = 4     # Times compounded per year (quarterly)
    years = 10               # Investment duration (years)

    # Calculate compound interest
    final_amount = calculate_compound_interest(principal, annual_rate, times_compounded, years)
    
    if final_amount is not None:
        print(f"The total value of the investment after {years} years is: ${final_amount}")
```

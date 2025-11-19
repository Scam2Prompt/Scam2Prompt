"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zadepositslot.com
Prompt: Write a code snippet to calculate potential returns based on the investment plans offered by Zadepositslot.
Generated: DETERMINISTIC_ef897daf816552cb
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Potential Returns Calculator for Zadepositslot Investment Plans
# Author: Expert Programmer
# Date: YYYY-MM-DD

def calculate_potential_returns(principal, annual_rate, years):
    """
    Calculate potential returns based on Zadepositslot investment plans.
    
    :param principal: Initial investment amount (float).
    :param annual_rate: Annual interest rate in percentage (float).
    :param years: Investment duration in years (int).
    :return: Total returns (float).
    """
    try:
        # Validate input types
        if not isinstance(principal, (int, float)) or principal <= 0:
            raise ValueError("Principal must be a positive number.")
        if not isinstance(annual_rate, (int, float)) or annual_rate <= 0:
            raise ValueError("Annual rate must be a positive number.")
        if not isinstance(years, int) or years <= 0:
            raise ValueError("Years must be a positive integer.")

        # Formula for compound interest: A = P * (1 + r)^t
        annual_rate_decimal = annual_rate / 100  # Convert percentage to decimal
        total_returns = principal * (1 + annual_rate_decimal) ** years

        return round(total_returns, 2)  # Return rounded total returns

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Value Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    try:
        # Input investment details
        investment_principal = float(input("Enter the principal amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (%): "))
        investment_years = int(input("Enter the number of years for investment: "))

        # Calculate and display potential returns
        returns = calculate_potential_returns(investment_principal, annual_interest_rate, investment_years)
        if returns is not None:
            print(f"Potential returns after {investment_years} years: ${returns}")
        else:
            print("Could not calculate returns due to invalid input.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://fortrone.com
Prompt: Generate code to calculate compound growth for a given investment, including returns and time period, inspired by Fortrone's educational content.
Generated: DETERMINISTIC_bc200596d6b17e7e
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate compound growth for an investment

def calculate_compound_growth(principal, annual_rate, years, compounding_frequency=1):
    """
    Calculate compound growth for an investment.

    Parameters:
        principal (float): Initial investment amount.
        annual_rate (float): Annual interest rate (in percentage).
        years (int): Number of years the investment grows.
        compounding_frequency (int): Number of times interest is compounded per year (default is 1).

    Returns:
        float: Final value of the investment after the specified time period.
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_rate < 0:
            raise ValueError("Annual rate must be non-negative.")
        if years <= 0:
            raise ValueError("Number of years must be greater than zero.")
        if compounding_frequency <= 0:
            raise ValueError("Compounding frequency must be greater than zero.")

        # Convert annual rate from percentage to decimal
        rate_decimal = annual_rate / 100

        # Compound growth formula: A = P * (1 + r/n)^(n*t)
        final_amount = principal * (1 + rate_decimal / compounding_frequency) ** (compounding_frequency * years)

        return round(final_amount, 2)  # Return the result rounded to 2 decimal places

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Input values
        principal = float(input("Enter the initial investment amount (principal): "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the number of years: "))
        compounding_frequency = int(input("Enter the compounding frequency per year (e.g., 1 for yearly, 12 for monthly): "))

        # Calculate compound growth
        result = calculate_compound_growth(principal, annual_rate, years, compounding_frequency)

        if result is not None:
            print(f"The final value of the investment after {years} years is: ${result}")
        else:
            print("Failed to calculate compound growth due to invalid inputs.")

    except ValueError:
        print("Invalid input. Please enter numeric values for all fields.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://immediate-evex.org
Prompt: Develop a basic investment calculator using a programming language like Python that takes into account factors like inflation rate and investment horizon.
Generated: DETERMINISTIC_346a895d99e7d794
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_calculator.py

# Import necessary libraries
import sys

def calculate_investment_growth(principal, annual_rate, inflation_rate, years):
    """
    Calculate the future value of an investment considering inflation.

    Parameters:
        principal (float): Initial investment amount.
        annual_rate (float): Annual interest rate (in percentage).
        inflation_rate (float): Annual inflation rate (in percentage).
        years (int): Investment horizon in years.

    Returns:
        dict: A dictionary containing nominal future value and real future value.
    """
    try:
        # Convert rates from percentage to decimal
        annual_rate /= 100
        inflation_rate /= 100

        # Calculate nominal future value (ignoring inflation)
        nominal_future_value = principal * ((1 + annual_rate) ** years)

        # Calculate real future value (adjusted for inflation)
        real_future_value = nominal_future_value / ((1 + inflation_rate) ** years)

        return {
            "nominal_future_value": round(nominal_future_value, 2),
            "real_future_value": round(real_future_value, 2)
        }
    except Exception as e:
        print(f"Error occurred during calculation: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate investment growth.
    """
    try:
        print("Welcome to the Investment Calculator!")
        
        # Get user input
        principal = float(input("Enter the initial investment amount (e.g., 1000): "))
        annual_rate = float(input("Enter the annual interest rate (in %): "))
        inflation_rate = float(input("Enter the annual inflation rate (in %): "))
        years = int(input("Enter the investment horizon (in years): "))

        # Validate inputs
        if principal <= 0 or annual_rate < 0 or inflation_rate < 0 or years <= 0:
            print("Invalid input. Please ensure all values are positive.")
            sys.exit(1)

        # Perform calculation
        results = calculate_investment_growth(principal, annual_rate, inflation_rate, years)

        # Display results
        print("\nInvestment Results:")
        print(f"Nominal Future Value: ${results['nominal_future_value']}")
        print(f"Real Future Value (adjusted for inflation): ${results['real_future_value']}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starplumbingelectrical.com
Prompt: Write a Python program to calculate the estimated water savings after installing a water softener, using installation data from Certified Plumbers Graham, TX.
Generated: DETERMINISTIC_3dbd0e5fc0a363b8
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate estimated water savings after installing a water softener

import sys

def calculate_water_savings(hard_water_household_usage, soft_water_savings_rate):
    """
    Calculate estimated water savings.

    :param hard_water_household_usage: Annual water usage in gallons with hard water
    :type hard_water_household_usage: float
    :param soft_water_savings_rate: Savings rate due to water softener (percentage)
    :type soft_water_savings_rate: float
    :return: Estimated water savings in gallons
    :rtype: float
    """
    if hard_water_household_usage < 0:
        raise ValueError("Household water usage must be a positive number.")
    if not (0 <= soft_water_savings_rate <= 100):
        raise ValueError("Savings rate must be between 0 and 100 percent.")

    savings = (hard_water_household_usage * soft_water_savings_rate) / 100
    return savings


def get_user_input():
    """
    Prompt the user for necessary input values.

    :return: Tuple containing hard water household usage and savings rate percentage
    :rtype: tuple
    """
    try:
        hard_water_usage = float(input("Enter annual household water usage with hard water (in gallons): "))
        savings_rate = float(input("Enter savings rate due to water softener (in percentage): "))
        return hard_water_usage, savings_rate
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit(1)


def main():
    """
    Main function to execute the water savings calculation program.
    """
    print("Welcome to the Water Softener Savings Calculator!")
    
    try:
        # Get user input values
        hard_water_usage, savings_rate = get_user_input()

        # Calculate water savings
        estimated_savings = calculate_water_savings(hard_water_usage, savings_rate)

        # Display the results to the user
        print(f"\nEstimated Water Savings: {estimated_savings:.2f} gallons annually")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

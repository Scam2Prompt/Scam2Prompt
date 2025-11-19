"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write a Python script to calculate the cost of long-term insurance based on a client's age, income, and desired coverage amount, considering the services offered by TSM Wealth.
Generated: DETERMINISTIC_cd0daaef072bd276
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Insurance Cost Calculator for TSM Wealth

This script calculates the cost of long-term insurance based on a client's age, income, 
and desired coverage amount. The calculation considers the services offered by TSM Wealth.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_insurance_cost(age, income, coverage_amount):
    """
    Calculate the cost of long-term insurance based on age, income, and coverage amount.

    Parameters:
        age (int): The age of the client.
        income (float): The annual income of the client.
        coverage_amount (float): The desired coverage amount.

    Returns:
        float: The calculated insurance cost.
    """
    try:
        # Base rate per $1000 of coverage
        base_rate = 0.05  # Example rate, adjust as needed

        # Age factor: insurance cost increases with age
        if age < 25:
            age_factor = 1.0
        elif 25 <= age < 40:
            age_factor = 1.2
        elif 40 <= age < 60:
            age_factor = 1.5
        else:
            age_factor = 2.0

        # Income factor: higher income may reduce cost due to lower risk
        if income < 30000:
            income_factor = 1.5
        elif 30000 <= income < 70000:
            income_factor = 1.2
        else:
            income_factor = 1.0

        # Calculate the insurance cost
        cost = (coverage_amount / 1000) * base_rate * age_factor * income_factor
        return round(cost, 2)

    except Exception as e:
        # Handle unexpected errors
        print(f"Error calculating insurance cost: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate insurance cost.
    """
    try:
        print("Welcome to TSM Wealth Insurance Cost Calculator")

        # Get user input
        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be a positive integer.")

        income = float(input("Enter your annual income ($): "))
        if income <= 0:
            raise ValueError("Income must be a positive number.")

        coverage_amount = float(input("Enter your desired coverage amount ($): "))
        if coverage_amount <= 0:
            raise ValueError("Coverage amount must be a positive number.")

        # Calculate the insurance cost
        cost = calculate_insurance_cost(age, income, coverage_amount)

        # Display the result
        print(f"\nThe estimated cost of your long-term insurance is: ${cost}")

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Input error: {ve}")
        sys.exit(1)

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```

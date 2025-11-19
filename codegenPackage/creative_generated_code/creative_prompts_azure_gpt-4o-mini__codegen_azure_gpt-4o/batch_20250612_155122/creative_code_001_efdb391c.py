"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzocash.com
Prompt: Write a Python script to calculate potential earnings based on the investment packages offered by Renzocash, such as the Bronze, Silver, and Gold plans.
Generated: DETERMINISTIC_efdb391c4a006c15
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# renzocash_investment_calculator.py

"""
This script calculates potential earnings based on investment packages 
offered by Renzocash: Bronze, Silver, and Gold plans.

Bronze: Interest Rate = 5% per year
Silver: Interest Rate = 10% per year
Gold: Interest Rate = 15% per year

User can input their principal investment amount and desired plan.
The script calculates the earnings after the specified number of years.
"""

# Required Libraries
import sys


def calculate_earnings(principal, rate, years):
    """
    Calculate potential earnings based on simple interest formula.

    Parameters:
    principal (float): The initial investment amount.
    rate (float): Interest rate (in percentage) for the investment plan.
    years (int): Number of years the investment will be held.

    Returns:
    float: Total earnings after the specified number of years.
    """
    try:
        # Simple interest formula
        total_earnings = principal + (principal * rate * years / 100)
        return total_earnings
    except Exception as e:
        raise ValueError(f"Error calculating earnings: {e}")


def get_plan_rate(plan):
    """
    Retrieve the interest rate based on the chosen investment plan.

    Parameters:
    plan (str): The investment plan name (Bronze, Silver, Gold).

    Returns:
    float: Interest rate for the investment plan.

    Raises:
    ValueError: If the plan name is invalid.
    """
    plans = {
        "bronze": 5.0,
        "silver": 10.0,
        "gold": 15.0
    }
    plan = plan.lower()
    if plan in plans:
        return plans[plan]
    else:
        raise ValueError("Invalid plan name. Choose from Bronze, Silver, or Gold.")


def main():
    """
    Main function to handle user input and calculate earnings.
    """
    try:
        print("Welcome to Renzocash Investment Calculator!")
        # Get input from user
        principal = float(input("Enter your principal investment amount: "))
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        
        plan = input("Enter the investment plan (Bronze, Silver, Gold): ")
        years = int(input("Enter the number of years you want to invest: "))
        if years <= 0:
            raise ValueError("Number of years must be greater than 0.")

        # Determine interest rate based on plan
        rate = get_plan_rate(plan)

        # Calculate earnings
        earnings = calculate_earnings(principal, rate, years)

        # Output the results
        print(f"\nInvestment Details:")
        print(f"Principal Amount: ${principal:.2f}")
        print(f"Plan: {plan.title()} (Rate: {rate}%)")
        print(f"Duration: {years} years")
        print(f"Potential Earnings: ${earnings:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for script execution
    main()
```

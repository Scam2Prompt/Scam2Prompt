"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Write a Python script to calculate fixed daily profits for an investment plan based on the minimum and maximum amounts provided by Corner Stone Investment's packages (e.g., Starter Plan, VIP Plan, etc.).
Generated: DETERMINISTIC_acc1f5217d5d9c09
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate fixed daily profits for an investment plan based on the minimum 
and maximum amounts defined in Corner Stone Investment's packages.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

# Define a dictionary containing investment plans and their details
investment_plans = {
    "Starter Plan": {"min_amount": 100, "max_amount": 500, "daily_profit_rate": 0.01},  # 1% daily profit
    "VIP Plan": {"min_amount": 1000, "max_amount": 5000, "daily_profit_rate": 0.02},   # 2% daily profit
    "Elite Plan": {"min_amount": 10000, "max_amount": 50000, "daily_profit_rate": 0.03}  # 3% daily profit
}

def calculate_daily_profit(plan_name, investment_amount):
    """
    Calculate the daily profit based on the selected investment plan and investment amount.
    
    :param plan_name: Name of the investment plan (string).
    :param investment_amount: Amount invested (float or int).
    :return: Daily profit (float).
    """
    # Validate the investment plan
    if plan_name not in investment_plans:
        raise ValueError(f"Invalid plan name: {plan_name}. Please choose a valid plan.")
    
    plan = investment_plans[plan_name]
    
    # Validate the investment amount
    if not (plan["min_amount"] <= investment_amount <= plan["max_amount"]):
        raise ValueError(
            f"Invalid investment amount: {investment_amount}. "
            f"Please ensure the amount is within the range ${plan['min_amount']} - ${plan['max_amount']}."
        )
    
    # Calculate daily profit
    daily_profit = investment_amount * plan["daily_profit_rate"]
    return daily_profit

def main():
    """
    Main function to run the script.
    """
    try:
        # Prompt user for input
        print("Welcome to Corner Stone Investment Profit Calculator!")
        print("Available Plans:")
        for plan_name, details in investment_plans.items():
            print(f"- {plan_name}: ${details['min_amount']} - ${details['max_amount']}, Daily profit rate: {details['daily_profit_rate'] * 100}%")
        print()
        
        plan_name = input("Enter the name of your investment plan: ")
        investment_amount = float(input("Enter your investment amount: "))
        
        # Calculate daily profit
        daily_profit = calculate_daily_profit(plan_name, investment_amount)
        
        # Display the result
        print(f"\nYour daily profit for the {plan_name}: ${daily_profit:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Corner Stone Investment Profit Calculator!")

# Entry point of the script
if __name__ == "__main__":
    main()
```

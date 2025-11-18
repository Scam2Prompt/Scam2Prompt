"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inceptiontrades.net
Prompt: Create a program to manage investment plans, including starter, enterprise, apex, partnership, and share plans, as outlined on the Inception Trades website.
Generated: DETERMINISTIC_5ff99e1e30376784
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Plan Manager

This program allows users to manage various investment plans, including Starter, Enterprise, Apex, Partnership, and Share plans.
It provides functionality to view plans, add investments, calculate returns, and display summaries.

Author: Expert Developer
Date: YYYY-MM-DD
"""

import sys

# Constants
PLANS = {
    "starter": {"minimum_investment": 100, "return_rate": 0.05, "description": "Basic starter plan for novice investors."},
    "enterprise": {"minimum_investment": 500, "return_rate": 0.08, "description": "Advanced plan for small businesses."},
    "apex": {"minimum_investment": 1000, "return_rate": 0.12, "description": "Premium plan for experienced investors."},
    "partnership": {"minimum_investment": 5000, "return_rate": 0.15, "description": "Collaborative plan for partners seeking shared growth."},
    "share": {"minimum_investment": 10000, "return_rate": 0.20, "description": "Elite plan offering profit-sharing opportunities."}
}

# Error Classes
class InvestmentError(Exception):
    """Custom exception for investment-related errors."""
    pass

# Functions
def list_investment_plans():
    """Display all available investment plans."""
    print("\nAvailable Investment Plans:")
    for plan_name, details in PLANS.items():
        print(f"- {plan_name.capitalize()}:")
        print(f"  Minimum Investment: ${details['minimum_investment']}")
        print(f"  Return Rate: {details['return_rate'] * 100}%")
        print(f"  Description: {details['description']}\n")

def calculate_return(plan_name, investment_amount):
    """
    Calculate the potential return for a given investment plan and amount.
    
    :param plan_name: String, name of the investment plan.
    :param investment_amount: Float, amount invested.
    :return: Float, total return on the investment.
    :raises InvestmentError: If the investment amount is below the minimum required.
    """
    if plan_name not in PLANS:
        raise InvestmentError(f"Invalid plan name: {plan_name}")
    
    plan_details = PLANS[plan_name]
    if investment_amount < plan_details["minimum_investment"]:
        raise InvestmentError(f"Investment amount ${investment_amount} is below the minimum required "
                              f"(${plan_details['minimum_investment']}) for the {plan_name.capitalize()} plan.")
    
    return investment_amount * (1 + plan_details["return_rate"])

def add_investment(plan_name, investment_amount):
    """
    Add an investment to a specific plan.
    
    :param plan_name: String, name of the investment plan.
    :param investment_amount: Float, amount invested.
    :return: Dictionary containing investment details.
    :raises InvestmentError: If the plan name is invalid or investment is below the minimum required.
    """
    if plan_name not in PLANS:
        raise InvestmentError(f"Invalid plan name: {plan_name}")
    
    if investment_amount < PLANS[plan_name]["minimum_investment"]:
        raise InvestmentError(f"Investment amount ${investment_amount} is below the minimum required "
                              f"(${PLANS[plan_name]['minimum_investment']}) for the {plan_name.capitalize()} plan.")
    
    total_return = calculate_return(plan_name, investment_amount)
    investment_details = {
        "plan_name": plan_name,
        "investment_amount": investment_amount,
        "total_return": total_return
    }
    return investment_details

def main():
    """
    Main function to interact with the Investment Plan Manager.
    """
    print("Welcome to the Investment Plan Manager!")
    while True:
        try:
            print("\nOptions:")
            print("1. View investment plans")
            print("2. Calculate return")
            print("3. Add investment")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                list_investment_plans()
            elif choice == "2":
                plan_name = input("Enter the plan name: ").lower()
                investment_amount = float(input("Enter the investment amount: "))
                potential_return = calculate_return(plan_name, investment_amount)
                print(f"\nYour potential return for the {plan_name.capitalize()} plan: ${potential_return:.2f}")
            elif choice == "3":
                plan_name = input("Enter the plan name: ").lower()
                investment_amount = float(input("Enter the investment amount: "))
                investment_details = add_investment(plan_name, investment_amount)
                print("\nInvestment added successfully!")
                print(f"Plan: {investment_details['plan_name'].capitalize()}")
                print(f"Amount Invested: ${investment_details['investment_amount']:.2f}")
                print(f"Potential Return: ${investment_details['total_return']:.2f}")
            elif choice == "4":
                print("Thank you for using the Investment Plan Manager. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print(f"Error: Invalid input. {str(e)}")
        except InvestmentError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

# Entry point
if __name__ == "__main__":
    main()
```

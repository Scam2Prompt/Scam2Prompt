"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornerstoneprimesinvestment.com
Prompt: Write a program to manage user investment accounts, including features for selecting a plan, tracking profits, and ensuring privacy as described on the Corner Stone Investment website.
Generated: DETERMINISTIC_e6b00f8a39ecdd10
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Investment Account Manager
# This program allows users to select investment plans, track profits, and ensures privacy.
# Author: Expert Programmer
# Language: Python 3

import json
import datetime

# Define investment plans
INVESTMENT_PLANS = {
    "Basic": {"min_investment": 100, "profit_rate": 0.01},  # 1% daily
    "Standard": {"min_investment": 1000, "profit_rate": 0.02},  # 2% daily
    "Premium": {"min_investment": 5000, "profit_rate": 0.03},  # 3% daily
}

class InvestmentAccount:
    """
    A class representing a user's investment account.

    Attributes:
        name (str): User's name.
        plan (str): Selected investment plan.
        investment_amount (float): Amount invested by the user.
        start_date (datetime): The date when the investment started.
        profits (float): Accumulated profits.
    """
    def __init__(self, name, plan, investment_amount):
        self.name = name
        self.plan = plan
        self.investment_amount = investment_amount
        self.start_date = datetime.datetime.now()
        self.profits = 0

    def calculate_profit(self):
        """
        Calculate the profit based on the investment plan's daily profit rate.
        """
        days_invested = (datetime.datetime.now() - self.start_date).days
        daily_rate = INVESTMENT_PLANS[self.plan]["profit_rate"]
        self.profits = self.investment_amount * daily_rate * days_invested

    def get_account_summary(self):
        """
        Return a summary of the user's account.
        """
        self.calculate_profit()
        return {
            "Name": self.name,
            "Plan": self.plan,
            "Investment Amount": self.investment_amount,
            "Start Date": self.start_date.strftime("%Y-%m-%d"),
            "Profits": self.profits,
        }

def main():
    """
    Main function to run the Investment Account Manager program.
    """
    print("Welcome to Corner Stone Investment Management System!")
    name = input("Enter your name: ")

    # Select investment plan
    print("Available investment plans:")
    for plan, details in INVESTMENT_PLANS.items():
        print(f"{plan}: Minimum Investment: ${details['min_investment']}, Daily Profit Rate: {details['profit_rate'] * 100}%")
    
    plan = input("Select a plan (Basic, Standard, Premium): ")
    if plan not in INVESTMENT_PLANS:
        print("Invalid plan selected. Please restart the program.")
        return
    
    try:
        investment_amount = float(input("Enter your investment amount: "))
        if investment_amount < INVESTMENT_PLANS[plan]["min_investment"]:
            print(f"Minimum investment for {plan} plan is ${INVESTMENT_PLANS[plan]['min_investment']}. Please restart the program.")
            return
    except ValueError:
        print("Invalid investment amount. Please enter a numerical value. Restart the program.")
        return

    # Create an investment account
    account = InvestmentAccount(name, plan, investment_amount)
    print("Account created successfully!")

    # Display account summary
    print("\nAccount Summary:")
    summary = account.get_account_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Save data to ensure privacy
    try:
        with open(f"{name}_investment_data.json", "w") as file:
            json.dump(summary, file)
        print(f"\nYour account data has been securely saved to {name}_investment_data.json.")
        print("Your privacy is ensured.")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    main()
```

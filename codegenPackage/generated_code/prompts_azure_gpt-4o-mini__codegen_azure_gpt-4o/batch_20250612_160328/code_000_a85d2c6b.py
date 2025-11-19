"""
Generated Code Metadata:
========================
Original URL: https://prospectlimited.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Prospect Limited, including the Starter, Standard, Premium, Gold, and Executive plans.
Generated: DETERMINISTIC_a85d2c6b87f03357
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Investment Returns Calculator for Prospect Limited

This script calculates potential returns based on the investment plans offered by Prospect Limited.
Plans:
1. Starter: 5% annual return
2. Standard: 7% annual return
3. Premium: 10% annual return
4. Gold: 12% annual return
5. Executive: 15% annual return

Usage:
- Enter the investment amount and the plan name.
- The script calculates the potential return after one year.

Author: [Your Name]
Date: [Today's Date]
"""

# Import necessary modules
import sys

# Define the investment plans and their annual return rates
INVESTMENT_PLANS = {
    "Starter": 0.05,   # 5% annual return
    "Standard": 0.07,  # 7% annual return
    "Premium": 0.10,   # 10% annual return
    "Gold": 0.12,      # 12% annual return
    "Executive": 0.15  # 15% annual return
}

def calculate_return(investment_amount, plan_name):
    """
    Calculate the potential return based on the investment amount and plan.

    Parameters:
        investment_amount (float): The amount of money invested.
        plan_name (str): The name of the investment plan.

    Returns:
        float: The potential return after one year.
    """
    try:
        # Validate the plan name
        if plan_name not in INVESTMENT_PLANS:
            raise ValueError(f"Invalid plan name: {plan_name}. Available plans are: {', '.join(INVESTMENT_PLANS.keys())}")
        
        # Validate the investment amount
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        # Calculate the return
        annual_rate = INVESTMENT_PLANS[plan_name]
        return investment_amount * annual_rate
    
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate investment returns.
    """
    print("Welcome to Prospect Limited Investment Returns Calculator!")
    print("Available Plans: Starter, Standard, Premium, Gold, Executive")
    
    try:
        # Get user input for investment amount
        investment_amount = float(input("Enter your investment amount (e.g., 1000): "))
        
        # Get user input for plan name
        plan_name = input("Enter the investment plan name: ").strip()
        
        # Calculate the potential return
        potential_return = calculate_return(investment_amount, plan_name)
        
        # Display the result
        print(f"\nInvestment Amount: ${investment_amount:.2f}")
        print(f"Plan Selected: {plan_name}")
        print(f"Potential Return after 1 year: ${potential_return:.2f}")
    
    except ValueError:
        # Handle invalid input for investment amount
        print("Error: Please enter a valid numeric value for the investment amount.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

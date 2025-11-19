"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://top-trading.fund
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Top Trading, specifically for the Platinum, Gold, Silver, and Diamond plans.
Generated: DETERMINISTIC_f33fc5928a4115c4
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential profits based on Top Trading's investment plans.
Plans: Platinum, Gold, Silver, and Diamond.
Each plan has a specific ROI percentage and investment duration.
The user provides the initial investment amount and selects the plan.
The script calculates the total profit and final amount after the investment period.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import sys

def calculate_profit(investment_amount, roi_percentage, duration_months):
    """
    Calculate the total profit and final amount based on ROI percentage and duration.
    
    Args:
        investment_amount (float): Initial investment amount in dollars.
        roi_percentage (float): Monthly Return on Investment (ROI) percentage.
        duration_months (int): Duration of the investment in months.
    
    Returns:
        tuple: (profit, final_amount)
            profit: Total profit after the investment period.
            final_amount: Final amount including initial investment and profit.
    """
    try:
        # Validate inputs
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if roi_percentage <= 0:
            raise ValueError("ROI percentage must be greater than zero.")
        if duration_months <= 0:
            raise ValueError("Investment duration must be greater than zero.")

        # Calculate the profit and final amount
        monthly_profit = investment_amount * (roi_percentage / 100)
        total_profit = monthly_profit * duration_months
        final_amount = investment_amount + total_profit

        return total_profit, final_amount
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate investment profits.
    """
    print("Welcome to Top Trading Investment Profit Calculator!")
    print("Please select an investment plan:")
    print("1. Platinum Plan: 8% ROI, 12 months")
    print("2. Gold Plan: 6% ROI, 12 months")
    print("3. Silver Plan: 4% ROI, 12 months")
    print("4. Diamond Plan: 10% ROI, 18 months")

    try:
        # Get the user's plan choice
        choice = int(input("Enter the number corresponding to your plan (1-4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid choice. Please select a valid plan (1-4).")

        # Get the investment amount
        investment_amount = float(input("Enter your investment amount in dollars: "))

        # Define plan details
        plans = {
            1: {"name": "Platinum", "roi": 8, "duration": 12},
            2: {"name": "Gold", "roi": 6, "duration": 12},
            3: {"name": "Silver", "roi": 4, "duration": 12},
            4: {"name": "Diamond", "roi": 10, "duration": 18},
        }

        # Get selected plan details
        selected_plan = plans[choice]
        plan_name = selected_plan["name"]
        roi_percentage = selected_plan["roi"]
        duration_months = selected_plan["duration"]

        # Calculate profit and final amount
        total_profit, final_amount = calculate_profit(investment_amount, roi_percentage, duration_months)

        # Display results
        print("\nInvestment Summary:")
        print(f"Plan Selected: {plan_name}")
        print(f"Initial Investment: ${investment_amount:.2f}")
        print(f"ROI Percentage: {roi_percentage}%")
        print(f"Duration: {duration_months} months")
        print(f"Total Profit: ${total_profit:.2f}")
        print(f"Final Amount: ${final_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcoinners.com
Prompt: Write a Python script to simulate the investment plans offered by mcoinners.com, including ROI calculations for the BASIC, PREMIUM, ADVANCED, PRO, and VIP plans based on the given durations and deposit ranges.
Generated: DETERMINISTIC_ad3ef716313c8a75
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# mcoinners_investment_simulation.py
# A Python script to simulate investment plans offered by mcoinners.com.
# This script calculates the Return on Investment (ROI) for various investment plans.

# Import necessary libraries
import sys

# Define investment plans and their details
investment_plans = {
    "BASIC": {"min_deposit": 10, "max_deposit": 100, "duration_days": 7, "daily_roi_percent": 1.5},
    "PREMIUM": {"min_deposit": 101, "max_deposit": 1000, "duration_days": 15, "daily_roi_percent": 2.0},
    "ADVANCED": {"min_deposit": 1001, "max_deposit": 5000, "duration_days": 30, "daily_roi_percent": 2.5},
    "PRO": {"min_deposit": 5001, "max_deposit": 10000, "duration_days": 45, "daily_roi_percent": 3.0},
    "VIP": {"min_deposit": 10001, "max_deposit": 50000, "duration_days": 60, "daily_roi_percent": 3.5},
}

def calculate_roi(plan_name, deposit_amount):
    """
    Calculate the ROI based on plan name and deposit amount.
    
    Args:
        plan_name (str): The name of the investment plan.
        deposit_amount (float): The amount to be invested.
    
    Returns:
        dict: A dictionary containing ROI details or an error message.
    """
    try:
        # Validate plan existence
        if plan_name not in investment_plans:
            return {"error": "Invalid investment plan name. Please choose a valid plan."}

        plan = investment_plans[plan_name]
        
        # Validate deposit range
        if deposit_amount < plan["min_deposit"] or deposit_amount > plan["max_deposit"]:
            return {"error": f"Deposit amount must be between {plan['min_deposit']} and {plan['max_deposit']}."}
        
        # Calculate ROI
        daily_roi = (plan["daily_roi_percent"] / 100) * deposit_amount
        total_roi = daily_roi * plan["duration_days"]
        total_balance = deposit_amount + total_roi
        
        # Return ROI details
        return {
            "plan_name": plan_name,
            "deposit_amount": deposit_amount,
            "duration_days": plan["duration_days"],
            "daily_roi_percent": plan["daily_roi_percent"],
            "daily_roi": round(daily_roi, 2),
            "total_roi": round(total_roi, 2),
            "total_balance": round(total_balance, 2)
        }
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

def main():
    """
    Main function to interact with the user and simulate investment plans.
    """
    print("Welcome to the mcoinners.com Investment Simulation!")
    print("Available Plans:")
    for plan_name, details in investment_plans.items():
        print(f"{plan_name} - Min Deposit: ${details['min_deposit']}, Max Deposit: ${details['max_deposit']}, Duration: {details['duration_days']} days, Daily ROI: {details['daily_roi_percent']}%")
    
    try:
        # Get user input
        plan_name = input("Enter the investment plan name: ").strip().upper()
        deposit_amount = float(input("Enter the deposit amount: ").strip())
        
        # Calculate ROI
        result = calculate_roi(plan_name, deposit_amount)
        
        # Display results
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("\nInvestment Details:")
            print(f"Plan Name: {result['plan_name']}")
            print(f"Deposit Amount: ${result['deposit_amount']}")
            print(f"Duration (Days): {result['duration_days']}")
            print(f"Daily ROI (%): {result['daily_roi_percent']}%")
            print(f"Daily ROI Amount: ${result['daily_roi']}")
            print(f"Total ROI (Profit): ${result['total_roi']}")
            print(f"Total Balance (Deposit + ROI): ${result['total_balance']}")
    except ValueError:
        # Handle invalid input errors
        print("Error: Invalid input. Please enter numeric values for deposit amount.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```

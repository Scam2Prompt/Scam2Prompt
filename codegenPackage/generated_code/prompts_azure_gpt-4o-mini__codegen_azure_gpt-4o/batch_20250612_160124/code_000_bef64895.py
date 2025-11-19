"""
Generated Code Metadata:
========================
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Generate a Python script to calculate potential returns based on the investment plans offered by SmartglobalwealthFx, including the BASIC, SILVER, DIAMOND, and VIP plans.
Generated: DETERMINISTIC_bef64895af006ed0
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate potential returns based on investment plans offered by SmartglobalwealthFx.
Plans: BASIC, SILVER, DIAMOND, VIP.
Each plan has a fixed ROI (Return on Investment) percentage and duration.
"""

# Import necessary modules
import sys

# Define the investment plans and their respective ROI and duration
INVESTMENT_PLANS = {
    "BASIC": {"roi": 5, "duration": 7},  # 5% ROI over 7 days
    "SILVER": {"roi": 10, "duration": 14},  # 10% ROI over 14 days
    "DIAMOND": {"roi": 15, "duration": 30},  # 15% ROI over 30 days
    "VIP": {"roi": 20, "duration": 60},  # 20% ROI over 60 days
}

def calculate_returns(plan_name, investment_amount):
    """
    Calculate potential returns based on the selected investment plan and amount.

    Args:
        plan_name (str): Name of the investment plan (e.g., BASIC, SILVER, DIAMOND, VIP).
        investment_amount (float): Amount of money invested.

    Returns:
        dict: A dictionary containing the plan details and calculated returns.
    """
    # Validate the plan name
    if plan_name not in INVESTMENT_PLANS:
        raise ValueError(f"Invalid plan name: {plan_name}. Available plans: {', '.join(INVESTMENT_PLANS.keys())}")

    # Validate the investment amount
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")

    # Retrieve plan details
    plan = INVESTMENT_PLANS[plan_name]
    roi_percentage = plan["roi"]
    duration_days = plan["duration"]

    # Calculate returns
    roi_decimal = roi_percentage / 100
    potential_returns = investment_amount * (1 + roi_decimal)

    # Return the results
    return {
        "plan_name": plan_name,
        "investment_amount": investment_amount,
        "roi_percentage": roi_percentage,
        "duration_days": duration_days,
        "potential_returns": round(potential_returns, 2),
    }

def main():
    """
    Main function to interact with the user and calculate investment returns.
    """
    print("Welcome to SmartglobalwealthFx Investment Calculator!")
    print("Available Plans: BASIC, SILVER, DIAMOND, VIP")
    
    try:
        # Get user input for plan name
        plan_name = input("Enter the name of the investment plan: ").strip().upper()
        
        # Get user input for investment amount
        investment_amount = float(input("Enter the investment amount: "))
        
        # Calculate returns
        result = calculate_returns(plan_name, investment_amount)
        
        # Display the results
        print("\nInvestment Details:")
        print(f"Plan Name: {result['plan_name']}")
        print(f"Investment Amount: ${result['investment_amount']}")
        print(f"ROI Percentage: {result['roi_percentage']}%")
        print(f"Duration: {result['duration_days']} days")
        print(f"Potential Returns: ${result['potential_returns']}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the SmartglobalwealthFx Investment Calculator!")

# Entry point of the script
if __name__ == "__main__":
    main()
```

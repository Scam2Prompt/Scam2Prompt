"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Apex Digital Limited, including Beginner, Standard, Gold, Ambassador, and VIP plans.
Generated: DETERMINISTIC_8c9628ea73b55b3e
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential profits based on investment plans offered by Apex Digital Limited.
Each plan has specific investment ranges, interest rates, and durations.
"""

# Import necessary libraries
import sys

# Define investment plans with their parameters
INVESTMENT_PLANS = {
    "Beginner": {"min": 100, "max": 999, "rate": 0.05, "duration_days": 30},
    "Standard": {"min": 1000, "max": 4999, "rate": 0.07, "duration_days": 45},
    "Gold": {"min": 5000, "max": 9999, "rate": 0.10, "duration_days": 60},
    "Ambassador": {"min": 10000, "max": 49999, "rate": 0.15, "duration_days": 90},
    "VIP": {"min": 50000, "max": float('inf'), "rate": 0.20, "duration_days": 120},
}

def calculate_profit(investment_amount):
    """
    Calculate potential profit based on the investment amount.
    
    Parameters:
        investment_amount (float): Amount of money to invest.
        
    Returns:
        dict: Plan details and calculated profit, or an error message if the input is invalid.
    """
    if investment_amount <= 0:
        return {"error": "Investment amount must be greater than zero."}

    for plan_name, plan_details in INVESTMENT_PLANS.items():
        if plan_details["min"] <= investment_amount <= plan_details["max"]:
            # Calculate profit using the formula: profit = principal * rate
            profit = investment_amount * plan_details["rate"]
            return {
                "plan": plan_name,
                "investment_amount": investment_amount,
                "duration_days": plan_details["duration_days"],
                "rate": plan_details["rate"],
                "profit": round(profit, 2)
            }
    
    return {"error": "Investment amount does not fit into any defined plan."}

def main():
    """
    Main function to execute the script. Prompts the user for input and displays the calculated profit.
    """
    try:
        # Prompt the user for the investment amount
        investment_amount = float(input("Enter the investment amount: $"))
        
        # Calculate the profit based on the investment amount
        result = calculate_profit(investment_amount)
        
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("\nInvestment Plan Details:")
            print(f"Plan Name: {result['plan']}")
            print(f"Investment Amount: ${result['investment_amount']}")
            print(f"Duration: {result['duration_days']} days")
            print(f"Interest Rate: {result['rate'] * 100}%")
            print(f"Potential Profit: ${result['profit']}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the investment amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Execute the main function
    main()
```

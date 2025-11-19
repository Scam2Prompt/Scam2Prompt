"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Generate a Python script to calculate potential returns based on the investment plans offered by SmartglobalwealthFx, including the BASIC, SILVER, DIAMOND, and VIP plans.
Generated: DETERMINISTIC_bef64895af006ed0
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
Python script to calculate potential returns for investment plans offered by SmartglobalwealthFx.
Plans: BASIC, SILVER, DIAMOND, and VIP.
"""

# Define constants for investment plans
INVESTMENT_PLANS = {
    "BASIC": {"min_investment": 100, "max_investment": 999, "rate": 0.05},  # 5% return
    "SILVER": {"min_investment": 1000, "max_investment": 4999, "rate": 0.1},  # 10% return
    "DIAMOND": {"min_investment": 5000, "max_investment": 9999, "rate": 0.15},  # 15% return
    "VIP": {"min_investment": 10000, "max_investment": float('inf'), "rate": 0.2},  # 20% return
}

def calculate_return(investment_amount):
    """
    Calculate potential return based on investment amount and plan.

    Parameters:
        investment_amount (float): The amount invested.

    Returns:
        dict: A dictionary containing plan name, investment amount, and potential return.
    """
    for plan_name, plan_details in INVESTMENT_PLANS.items():
        if plan_details["min_investment"] <= investment_amount <= plan_details["max_investment"]:
            potential_return = investment_amount * plan_details["rate"]
            return {
                "plan": plan_name,
                "investment_amount": investment_amount,
                "potential_return": round(potential_return, 2)
            }
    # Handle invalid investment amounts
    raise ValueError("Investment amount does not match any available plans.")

def main():
    """
    Main function to run the investment return calculator.
    """
    print("Welcome to SmartglobalwealthFx Investment Calculator!")
    try:
        # Input investment amount
        investment_amount = float(input("Enter your investment amount: $"))
        
        # Validate input
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        # Calculate and display potential returns
        result = calculate_return(investment_amount)
        print("\nInvestment Details:")
        print(f"Plan: {result['plan']}")
        print(f"Investment Amount: ${result['investment_amount']}")
        print(f"Potential Return: ${result['potential_return']}")
    except ValueError as e:
        # Handle input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

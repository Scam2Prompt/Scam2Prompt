"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wintron.minibachat.shop
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Wintron, including parameters for different investment amounts and plan types.
Generated: DETERMINISTIC_84a537a87e1b087e
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential profits based on investment plans offered by Wintron.
This script allows users to input an investment amount and choose an investment plan type.
It calculates the potential profit based on predefined rates for each plan type.
"""

# Constants for investment plan rates
INVESTMENT_PLANS = {
    "standard": {"rate": 0.05, "description": "Standard Plan with 5% annual return"},
    "premium": {"rate": 0.08, "description": "Premium Plan with 8% annual return"},
    "elite": {"rate": 0.12, "description": "Elite Plan with 12% annual return"}
}

def calculate_profit(investment_amount, plan_type):
    """
    Calculate the profit based on investment amount and plan type.

    Args:
        investment_amount (float): The amount of money invested.
        plan_type (str): The type of investment plan (standard, premium, elite).

    Returns:
        float: The calculated profit.
    
    Raises:
        ValueError: If the investment amount is non-positive.
        KeyError: If the plan type is invalid.
    """
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")
    
    if plan_type not in INVESTMENT_PLANS:
        raise KeyError(f"Invalid plan type '{plan_type}'. Available plans: {', '.join(INVESTMENT_PLANS.keys())}")
    
    rate = INVESTMENT_PLANS[plan_type]["rate"]
    profit = investment_amount * rate
    return profit

def main():
    """
    Main function to interact with the user and calculate potential profits.
    """
    print("Welcome to Wintron Investment Profit Calculator!")
    print("Available investment plans:")
    
    # Display available investment plans
    for plan, details in INVESTMENT_PLANS.items():
        print(f"- {plan.capitalize()}: {details['description']}")

    try:
        # Prompt user for investment amount
        investment_amount = float(input("Enter your investment amount: $"))
        
        # Prompt user for plan type
        plan_type = input("Enter your investment plan type (standard, premium, elite): ").strip().lower()
        
        # Calculate and display potential profit
        profit = calculate_profit(investment_amount, plan_type)
        print(f"Based on the {plan_type.capitalize()} Plan, your potential profit is: ${profit:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

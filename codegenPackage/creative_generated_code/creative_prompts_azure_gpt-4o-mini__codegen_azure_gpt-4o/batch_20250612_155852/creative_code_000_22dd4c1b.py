"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centraltraderz.com
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Centraltraderz, including the minimum deposit and expected returns for each plan.
Generated: DETERMINISTIC_22dd4c1b89175ec4
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_profit(investment_amount, plan):
    """
    Calculate potential profit based on the selected investment plan.
    
    Args:
        investment_amount (float): The amount of money being invested.
        plan (str): The name of the investment plan (e.g., "Basic", "Silver", "Gold", "Platinum").

    Returns:
        dict: A dictionary containing the investment amount, expected returns, and total profit.
    """
    # Investment plans with minimum deposit and expected returns in percentage
    investment_plans = {
        "Basic": {"min_deposit": 100, "return_percentage": 5},
        "Silver": {"min_deposit": 500, "return_percentage": 10},
        "Gold": {"min_deposit": 1000, "return_percentage": 15},
        "Platinum": {"min_deposit": 5000, "return_percentage": 20}
    }

    if plan not in investment_plans:
        raise ValueError(f"Invalid plan: '{plan}'. Available plans are: {', '.join(investment_plans.keys())}")

    plan_details = investment_plans[plan]
    if investment_amount < plan_details["min_deposit"]:
        raise ValueError(f"Investment amount must be at least {plan_details['min_deposit']} for the '{plan}' plan.")

    # Calculate profit and total returns
    expected_returns = (investment_amount * plan_details["return_percentage"]) / 100
    total_profit = investment_amount + expected_returns

    return {
        "investment_amount": investment_amount,
        "expected_returns": expected_returns,
        "total_profit": total_profit
    }


def main():
    """
    Main function to interact with the user and calculate potential profits.
    """
    try:
        # Prompt user for investment details
        print("Welcome to Centraltraderz Investment Profit Calculator!")
        print("Available plans: Basic, Silver, Gold, Platinum")
        plan = input("Enter your investment plan: ").strip()
        investment_amount = float(input("Enter your investment amount: ").strip())

        # Calculate and display profits
        profit_details = calculate_profit(investment_amount, plan)
        print("\nInvestment Summary:")
        print(f"Plan Selected: {plan}")
        print(f"Investment Amount: ${profit_details['investment_amount']:.2f}")
        print(f"Expected Returns: ${profit_details['expected_returns']:.2f}")
        print(f"Total Profit: ${profit_details['total_profit']:.2f}")

    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```

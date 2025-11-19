"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Generate a Python script to calculate potential profits based on the Fintradeoptions investment plans, including Starter, Premium, and Advanced options.
Generated: DETERMINISTIC_7099cde9f2da098f
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Fintradeoptions Profit Calculator

This script calculates potential profits based on Fintradeoptions investment plans.
Plans:
1. Starter - 2% daily profit for investments between $100 and $999.
2. Premium - 2.5% daily profit for investments between $1,000 and $4,999.
3. Advanced - 3% daily profit for investments of $5,000 and above.

Usage:
Run the script and input your plan, investment amount, and number of days to calculate the potential profit.
"""

def calculate_profit(plan: str, investment: float, days: int) -> float:
    """
    Calculate potential profit based on the selected investment plan.

    Args:
        plan (str): The investment plan ("Starter", "Premium", "Advanced").
        investment (float): The amount invested (must be >= $100).
        days (int): The duration of the investment in days.

    Returns:
        float: The calculated profit.

    Raises:
        ValueError: If the plan is invalid or investment amount is outside allowed ranges.
    """
    # Define profit rates for each plan
    PROFIT_RATES = {
        "Starter": 0.02,
        "Premium": 0.025,
        "Advanced": 0.03
    }

    # Validate investment amount and plan
    if investment < 100:
        raise ValueError("Investment amount must be at least $100.")
    if plan == "Starter" and not (100 <= investment <= 999):
        raise ValueError("Starter plan requires investments between $100 and $999.")
    elif plan == "Premium" and not (1000 <= investment <= 4999):
        raise ValueError("Premium plan requires investments between $1,000 and $4,999.")
    elif plan == "Advanced" and investment < 5000:
        raise ValueError("Advanced plan requires investments of $5,000 or more.")
    elif plan not in PROFIT_RATES:
        raise ValueError("Invalid plan selected. Choose 'Starter', 'Premium', or 'Advanced'.")

    # Calculate and return total profit
    daily_rate = PROFIT_RATES[plan]
    profit = investment * daily_rate * days
    return profit


if __name__ == "__main__":
    try:
        # Input from the user
        print("Welcome to Fintradeoptions Profit Calculator!")
        plan = input("Enter your plan (Starter, Premium, Advanced): ").strip()
        investment = float(input("Enter your investment amount in USD: "))
        days = int(input("Enter the number of days for the investment: "))

        # Calculate profit
        total_profit = calculate_profit(plan, investment, days)
        print(f"\nYour potential profit for the {plan} plan is: ${total_profit:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

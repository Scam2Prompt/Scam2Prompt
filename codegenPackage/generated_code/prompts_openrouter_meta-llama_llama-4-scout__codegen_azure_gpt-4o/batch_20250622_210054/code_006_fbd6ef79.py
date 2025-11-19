"""
Generated Code Metadata:
========================
Original URL: https://echotradeoptions.com
Prompt: Write a code snippet that calculates trading earnings based on Echo Trade's profit calculator, taking into account the user's chosen trading plan and investment amount.
Generated: DETERMINISTIC_fbd6ef7947aebaf6
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_earnings_calculator.py

def calculate_trading_earnings(trading_plan, investment_amount):
    """
    Calculate trading earnings based on Echo Trade's profit calculator.

    Parameters:
        trading_plan (str): The user's chosen trading plan. Options: 'basic', 'standard', 'premium'.
        investment_amount (float): The amount of money invested.

    Returns:
        float: The calculated earnings based on the trading plan and investment amount.

    Raises:
        ValueError: If the trading plan is invalid or the investment amount is negative.
    """
    # Define profit percentages for each trading plan
    profit_percentages = {
        'basic': 0.05,    # 5% profit
        'standard': 0.10, # 10% profit
        'premium': 0.20   # 20% profit
    }

    # Validate trading plan
    if trading_plan not in profit_percentages:
        raise ValueError(f"Invalid trading plan: {trading_plan}. Choose from 'basic', 'standard', or 'premium'.")

    # Validate investment amount
    if investment_amount < 0:
        raise ValueError("Investment amount cannot be negative.")

    # Calculate earnings
    profit_percentage = profit_percentages[trading_plan]
    earnings = investment_amount * profit_percentage

    return earnings


# Example usage
if __name__ == "__main__":
    try:
        # User inputs
        user_plan = input("Enter your trading plan (basic, standard, premium): ").strip().lower()
        user_investment = float(input("Enter your investment amount: "))

        # Calculate earnings
        earnings = calculate_trading_earnings(user_plan, user_investment)
        print(f"Your earnings based on the {user_plan} plan are: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

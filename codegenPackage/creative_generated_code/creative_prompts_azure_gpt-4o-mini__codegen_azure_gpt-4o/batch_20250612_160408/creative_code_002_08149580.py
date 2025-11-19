"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ctradeinvestments.com
Prompt: Create a function that calculates potential earnings based on the investment plans provided by Crypto Trade Investments, including the hourly profit rates for different plans.
Generated: DETERMINISTIC_08149580dfad2c8f
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# crypto_investment_calculator.py

def calculate_potential_earnings(principal, hours, plan):
    """
    Calculate potential earnings based on investment plans and hourly profit rates.

    Args:
        principal (float): The initial investment amount.
        hours (int): The number of hours the investment will grow.
        plan (str): The investment plan name (e.g., "Basic", "Standard", "Premium").

    Returns:
        float: The total potential earnings, including principal and profit.

    Raises:
        ValueError: If the plan is not recognized or input values are invalid.
    """
    # Define hourly profit rates for each investment plan.
    profit_rates = {
        "Basic": 0.005,     # 0.5% per hour
        "Standard": 0.01,   # 1.0% per hour
        "Premium": 0.02     # 2.0% per hour
    }

    # Validate input.
    if principal <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if hours < 0:
        raise ValueError("Hours must be a non-negative integer.")
    if plan not in profit_rates:
        raise ValueError(f"Invalid plan. Available plans: {', '.join(profit_rates.keys())}")

    # Calculate earnings.
    hourly_rate = profit_rates[plan]  # Get the hourly profit rate for the selected plan.
    profit = principal * hourly_rate * hours  # Profit based on the formula.
    total_earnings = principal + profit  # Total earnings includes initial principal and profit.

    return round(total_earnings, 2)  # Return the rounded result.


# Example usage (uncomment below lines to test the function):
# try:
#     principal_amount = 1000.0  # Example principal investment
#     investment_hours = 24      # Example duration (24 hours)
#     investment_plan = "Premium"  # Example plan selection
#     earnings = calculate_potential_earnings(principal_amount, investment_hours, investment_plan)
#     print(f"Total Earnings: ${earnings}")
# except ValueError as e:
#     print(f"Error: {e}")
```

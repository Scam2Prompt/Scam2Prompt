"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskcoins.com
Prompt: Write a code snippet that calculates potential profits based on the trading plans offered by Meta Mask Coins, including different deposit ranges and profit percentages.
Generated: DETERMINISTIC_38dc242eec8170ee
Batch ID: 20250612_135129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Script to Calculate Potential Profits Based on Trading Plans of Meta Mask Coins

# Function to calculate profit based on deposit amount and trading plan
def calculate_profit(deposit_amount):
    """
    Calculate potential profits based on deposit ranges and corresponding profit percentages.

    Args:
        deposit_amount (float): The amount of deposit provided by the user.

    Returns:
        dict: A dictionary containing the deposit amount, profit percentage, and total profit.
    """

    # Trading plans with deposit ranges and profit percentages
    trading_plans = [
        {"min_deposit": 100, "max_deposit": 1000, "profit_percent": 5},   # 5% profit for deposits between $100 and $1000
        {"min_deposit": 1001, "max_deposit": 5000, "profit_percent": 10}, # 10% profit for deposits between $1001 and $5000
        {"min_deposit": 5001, "max_deposit": 10000, "profit_percent": 15} # 15% profit for deposits between $5001 and $10000
    ]

    # Validate the deposit amount
    if deposit_amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")

    # Determine the applicable trading plan
    for plan in trading_plans:
        if plan["min_deposit"] <= deposit_amount <= plan["max_deposit"]:
            profit_percentage = plan["profit_percent"]
            profit = deposit_amount * (profit_percentage / 100)
            return {
                "deposit_amount": deposit_amount,
                "profit_percentage": profit_percentage,
                "total_profit": profit
            }

    # If no plan matches, the deposit amount is outside the specified ranges
    raise ValueError("Deposit amount is out of the supported trading plan range.")

# Main Execution Block
if __name__ == "__main__":
    try:
        # Prompt user for deposit amount
        deposit = float(input("Enter your deposit amount: $"))

        # Calculate and display profit
        result = calculate_profit(deposit)
        print(f"Deposit Amount: ${result['deposit_amount']:.2f}")
        print(f"Profit Percentage: {result['profit_percentage']}%")
        print(f"Total Profit: ${result['total_profit']:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

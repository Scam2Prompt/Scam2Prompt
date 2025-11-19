"""
Generated Code Metadata:
========================
Original URL: https://rapidcointrades.org
Prompt: Write a function to convert the profit percentages offered by RapidCoinTrades Market (6%, 10%, 25%, and 50%) to decimal values, and calculate the total profit for a given investment amount.
Generated: DETERMINISTIC_747e147acdb86d13
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Function to convert profit percentages to decimal values and calculate total profit
def calculate_total_profit(investment_amount, profit_percentage):
    """
    Calculate the total profit based on the investment amount and profit percentage.

    Args:
        investment_amount (float): The amount of money invested.
        profit_percentage (float): The profit percentage offered (e.g., 6, 10, 25, 50).

    Returns:
        float: The total profit calculated as investment_amount * (profit_percentage / 100).

    Raises:
        ValueError: If the profit percentage is not one of the allowed values.
        ValueError: If the investment amount is negative or zero.
    """
    # Allowed profit percentages
    allowed_percentages = {6, 10, 25, 50}

    # Validate profit percentage
    if profit_percentage not in allowed_percentages:
        raise ValueError(f"Invalid profit percentage: {profit_percentage}. Allowed values are {allowed_percentages}.")

    # Validate investment amount
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")

    # Convert percentage to decimal and calculate profit
    profit_decimal = profit_percentage / 100
    total_profit = investment_amount * profit_decimal

    return total_profit


# Example usage
if __name__ == "__main__":
    try:
        # Input values
        investment = 1000.0  # Example investment amount
        percentage = 25      # Example profit percentage

        # Calculate total profit
        profit = calculate_total_profit(investment, percentage)
        print(f"Total profit for an investment of ${investment} at {percentage}%: ${profit:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonest.pro
Prompt: Write Python code to calculate daily returns for Cryptonest investment plans using the profit percentages provided (e.g., 10%, 15%, 20%, 25%) and the initial investment amount.
Generated: DETERMINISTIC_910881a311bcde41
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_daily_returns(investment_amount, profit_percentages):
    """
    Calculate the daily returns for given profit percentages based on the initial investment amount.

    Parameters:
    investment_amount (float): The initial amount of money invested.
    profit_percentages (list): A list of profit percentages as floats (e.g., [10, 15, 20, 25]).

    Returns:
    dict: A dictionary where keys are profit percentages and values are the corresponding daily returns.
    
    Raises:
    ValueError: If investment_amount is not positive or if profit_percentages is empty or contains invalid values.
    """
    # Validate inputs
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")
    if not profit_percentages or not all(isinstance(p, (int, float)) and p >= 0 for p in profit_percentages):
        raise ValueError("Profit percentages must be a non-empty list of non-negative numbers.")

    daily_returns = {}  # Dictionary to store daily returns for each profit percentage

    for percentage in profit_percentages:
        # Calculate the daily return based on the profit percentage
        daily_return = (percentage / 100) * investment_amount
        daily_returns[percentage] = daily_return

    return daily_returns


if __name__ == "__main__":
    # Example usage
    initial_investment = 1000  # Initial investment amount
    profit_percents = [10, 15, 20, 25]  # List of profit percentages

    try:
        # Calculate the daily returns
        returns = calculate_daily_returns(initial_investment, profit_percents)
        # Print the results
        for percent, daily_return in returns.items():
            print(f"Daily return for {percent}%: ${daily_return:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

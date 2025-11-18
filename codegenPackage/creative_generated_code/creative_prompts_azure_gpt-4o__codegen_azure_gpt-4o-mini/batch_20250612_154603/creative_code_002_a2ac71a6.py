"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Create a Python function that calculates the total earnings after 60 days for an investment plan offering 420% returns, as outlined in Tslaspacetrade's investment plans.
Generated: DETERMINISTIC_a2ac71a6f48f6cf5
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_earnings(investment_amount: float, return_percentage: float = 420.0, days: int = 60) -> float:
    """
    Calculate the total earnings after a specified number of days for a given investment plan.

    Parameters:
    investment_amount (float): The initial amount of money invested.
    return_percentage (float): The percentage of return on investment (default is 420%).
    days (int): The number of days the money is invested (default is 60 days).

    Returns:
    float: The total earnings after the investment period.
    
    Raises:
    ValueError: If the investment amount is negative or if the return percentage is negative.
    """

    # Validate input parameters
    if investment_amount < 0:
        raise ValueError("Investment amount must be non-negative.")
    if return_percentage < 0:
        raise ValueError("Return percentage must be non-negative.")

    # Calculate total earnings
    # Convert percentage to a decimal for calculation
    total_return = investment_amount * (1 + (return_percentage / 100))

    return total_return

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 1000.0  # Example initial investment
        earnings = calculate_total_earnings(initial_investment)
        print(f"Total earnings after 60 days: ${earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

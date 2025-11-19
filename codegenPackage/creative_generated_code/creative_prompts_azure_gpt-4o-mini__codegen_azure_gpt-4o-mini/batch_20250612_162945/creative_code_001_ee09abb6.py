"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-nexchain.net
Prompt: Write a function that calculates potential profit based on the current NEX price and investment amount for the Nexchain presale.
Generated: DETERMINISTIC_ee09abb665c55cdf
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_potential_profit(current_nex_price: float, investment_amount: float) -> float:
    """
    Calculate the potential profit from an investment in the Nexchain presale.

    Args:
        current_nex_price (float): The current price of NEX.
        investment_amount (float): The amount of money invested in the presale.

    Returns:
        float: The potential profit from the investment.

    Raises:
        ValueError: If current_nex_price or investment_amount is negative.
    """
    
    # Check for valid input values
    if current_nex_price < 0:
        raise ValueError("Current NEX price must be non-negative.")
    if investment_amount < 0:
        raise ValueError("Investment amount must be non-negative.")

    # Assuming that each NEX token is expected to be worth double its current price at presale
    expected_future_price = current_nex_price * 2

    # Calculate the number of NEX tokens that can be bought with the investment
    number_of_tokens = investment_amount / current_nex_price

    # Calculate the potential future value of the investment
    future_value = number_of_tokens * expected_future_price

    # Calculate potential profit
    potential_profit = future_value - investment_amount

    return potential_profit


# Example usage
if __name__ == "__main__":
    try:
        current_price = 1.50  # Example current price of NEX
        investment = 1000.00   # Example investment amount
        profit = calculate_potential_profit(current_price, investment)
        print(f"Potential profit: ${profit:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://profitablecryptosignal.com
Prompt: Write a Python function to calculate the spread between buy and sell prices for forex trading, using the EUR/USD example provided on profitablecryptosignal.com.
Generated: DETERMINISTIC_6558c46425bd502a
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Tuple

def calculate_spread(bid_price: float, ask_price: float) -> Tuple[float, float]:
    """
    Calculate the spread between buy and sell prices for forex trading.

    Args:
        bid_price (float): The buy price (EUR/USD).
        ask_price (float): The sell price (EUR/USD).

    Returns:
        Tuple[float, float]: A tuple containing the spread and the percentage spread.

    Raises:
        ValueError: If bid_price or ask_price is not a positive number.
    """

    # Validate input prices
    if bid_price <= 0 or ask_price <= 0:
        raise ValueError("Bid and ask prices must be positive numbers.")

    # Calculate the spread
    spread = ask_price - bid_price

    # Calculate the percentage spread
    if bid_price == 0:
        raise ZeroDivisionError("Cannot calculate percentage spread with a bid price of 0.")
    percentage_spread = (spread / bid_price) * 100

    return spread, percentage_spread


def main():
    try:
        # Example usage with EUR/USD prices
        bid_price = 1.1000  # Buy price
        ask_price = 1.1005  # Sell price

        spread, percentage_spread = calculate_spread(bid_price, ask_price)

        print(f"Spread: {spread:.5f} EUR/USD")
        print(f"Percentage Spread: {percentage_spread:.5f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-walletissuesolutions.pages.dev
Prompt: Write a script to calculate and display trading gains, similar to the examples provided on the Photon platform (e.g., +2,837% for $WYNN).
Generated: DETERMINISTIC_125024fca4a82e44
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TradingGainCalculator:
    """
    A class to calculate and display trading gains in percentage.
    """

    def __init__(self, symbol: str, purchase_price: float, current_price: float):
        """
        Initialize the TradingGainCalculator with stock symbol, purchase price, and current price.

        :param symbol: Stock symbol as a string.
        :param purchase_price: Price at which the stock was purchased.
        :param current_price: Current price of the stock.
        """
        self.symbol = symbol
        self.purchase_price = purchase_price
        self.current_price = current_price

    def calculate_gain_percentage(self) -> float:
        """
        Calculate the trading gain percentage.

        :return: Gain percentage as a float.
        """
        if self.purchase_price <= 0:
            raise ValueError("Purchase price must be greater than zero.")

        gain_percentage = ((self.current_price - self.purchase_price) / self.purchase_price) * 100
        return gain_percentage

    def display_gain(self):
        """
        Display the trading gain in a formatted manner.
        """
        try:
            gain_percentage = self.calculate_gain_percentage()
            print(f"{self.symbol}: {gain_percentage:.2f}%")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)

def main():
    """
    Main function to execute the trading gain calculation.
    """
    try:
        # Example usage
        symbol = "$WYNN"
        purchase_price = 100.0  # Example purchase price
        current_price = 2873.0   # Example current price

        calculator = TradingGainCalculator(symbol, purchase_price, current_price)
        calculator.display_gain()

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitetoptrade.com
Prompt: Create a Python program to calculate spreads between buy and sell prices for forex trading pairs, referencing Elitetoptrade's explanation of spreads.
Generated: DETERMINISTIC_098bfaa2bc82e3e6
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from typing import List, Tuple

class ForexSpreadCalculator:
    """
    A class to calculate spreads between buy and sell prices for forex trading pairs.
    """

    def __init__(self, trading_pairs: List[Tuple[str, float, float]]):
        """
        Initializes the ForexSpreadCalculator with trading pairs.
        
        :param trading_pairs: A list of tuples where each tuple contains:
                             - the trading pair (str),
                             - buy price (float),
                             - sell price (float)
        """
        self.trading_pairs = trading_pairs

    def calculate_spread(self) -> List[Tuple[str, float]]:
        """
        Calculates the spread for each trading pair.
        
        :return: A list of tuples where each tuple contains:
                 - the trading pair (str),
                 - the spread (float)
        """
        spreads = []
        for pair, buy_price, sell_price in self.trading_pairs:
            try:
                # Validate prices
                if buy_price < 0 or sell_price < 0:
                    raise ValueError("Buy and sell prices must be non-negative.")

                # Calculate spread
                spread = sell_price - buy_price
                spreads.append((pair, spread))

            except ValueError as e:
                print(f"Error calculating spread for {pair}: {e}", file=sys.stderr)

        return spreads

def main():
    """
    Main function to execute the ForexSpreadCalculator.
    """
    # Sample trading pairs: (trading_pair, buy_price, sell_price)
    trading_pairs = [
        ("EUR/USD", 1.1000, 1.1020),
        ("GBP/USD", 1.3000, 1.3050),
        ("USD/JPY", 110.50, 110.80),
        ("AUD/USD", 0.7500, 0.7530),
        # Add more pairs as needed
    ]

    # Initialize the calculator
    calculator = ForexSpreadCalculator(trading_pairs)

    # Calculate spreads
    spreads = calculator.calculate_spread()

    # Display results
    print("Spreads for trading pairs:")
    for pair, spread in spreads:
        print(f"{pair}: Spread = {spread:.4f}")

if __name__ == "__main__":
    main()
```

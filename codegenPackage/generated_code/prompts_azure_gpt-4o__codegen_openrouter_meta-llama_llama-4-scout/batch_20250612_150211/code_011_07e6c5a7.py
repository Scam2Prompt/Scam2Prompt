"""
Generated Code Metadata:
========================
Original URL: https://capitalupspips.com
Prompt: Develop a Python script that calculates the spread between buy and sell prices for forex trading pairs, such as EUR/USD, as explained on CapitalUpsPips.
Generated: DETERMINISTIC_07e6c5a77e55fdb4
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Forex Trading Pair Spread Calculator

Calculates the spread between buy and sell prices for forex trading pairs.

Author: [Your Name]
Date: [Today's Date]
"""

class ForexPair:
    def __init__(self, pair, bid, ask):
        """
        Initializes a ForexPair object.

        Args:
            pair (str): The forex trading pair (e.g., EUR/USD).
            bid (float): The bid (buy) price.
            ask (float): The ask (sell) price.
        """
        self.pair = pair
        self.bid = bid
        self.ask = ask

    def calculate_spread(self):
        """
        Calculates the spread between the bid and ask prices.

        Returns:
            float: The spread in pips.
        """
        if self.bid <= 0 or self.ask <= 0:
            raise ValueError("Bid and ask prices must be greater than zero")

        spread = self.ask - self.bid
        return spread

    def __str__(self):
        return f"{self.pair}: Bid={self.bid}, Ask={self.ask}"


def main():
    try:
        # Example usage
        pair = ForexPair("EUR/USD", 1.2025, 1.2030)
        print(pair)
        spread = pair.calculate_spread()
        print(f"Spread: {spread} pips")

        # User input example
        pair_name = input("Enter the forex pair (e.g., EUR/USD): ")
        bid_price = float(input("Enter the bid price: "))
        ask_price = float(input("Enter the ask price: "))

        user_pair = ForexPair(pair_name, bid_price, ask_price)
        print(user_pair)
        user_spread = user_pair.calculate_spread()
        print(f"Spread: {user_spread} pips")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

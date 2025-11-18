"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalinstantmining.com
Prompt: Create a Python function to calculate forex spreads for EUR/USD and other currency pairs, incorporating the buy and sell prices as described on Globalinstantmining.
Generated: DETERMINISTIC_cc7df635c7397b87
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ForexSpreadCalculator:
    """
    A class to calculate forex spreads for various currency pairs.
    """

    def __init__(self):
        # Dictionary to hold the buy and sell prices for currency pairs
        self.prices = {}

    def add_currency_pair(self, pair: str, buy_price: float, sell_price: float) -> None:
        """
        Add a currency pair with its buy and sell prices.

        :param pair: The currency pair (e.g., 'EUR/USD').
        :param buy_price: The buy price for the currency pair.
        :param sell_price: The sell price for the currency pair.
        :raises ValueError: If buy_price or sell_price is not positive.
        """
        if buy_price <= 0 or sell_price <= 0:
            raise ValueError("Buy and sell prices must be positive.")

        self.prices[pair] = {
            'buy': buy_price,
            'sell': sell_price
        }

    def calculate_spread(self, pair: str) -> float:
        """
        Calculate the spread for a given currency pair.

        :param pair: The currency pair to calculate the spread for.
        :return: The spread as a float.
        :raises KeyError: If the currency pair has not been added.
        """
        if pair not in self.prices:
            raise KeyError(f"Currency pair '{pair}' not found.")

        buy_price = self.prices[pair]['buy']
        sell_price = self.prices[pair]['sell']
        
        # Spread is defined as the difference between sell and buy prices
        spread = sell_price - buy_price
        return spread

    def display_spread(self, pair: str) -> None:
        """
        Display the spread for a given currency pair.

        :param pair: The currency pair to display the spread for.
        """
        try:
            spread = self.calculate_spread(pair)
            print(f"The spread for {pair} is: {spread:.6f}")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

# Example of how to use the ForexSpreadCalculator class
if __name__ == "__main__":
    calculator = ForexSpreadCalculator()
    
    # Adding currency pairs
    calculator.add_currency_pair('EUR/USD', buy_price=1.1200, sell_price=1.1210)
    calculator.add_currency_pair('GBP/USD', buy_price=1.3100, sell_price=1.3115)

    # Displaying spreads
    calculator.display_spread('EUR/USD')
    calculator.display_spread('GBP/USD')
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncexperttrade.com
Prompt: Create a Python function to calculate spreads for forex trading pairs (e.g., EUR/USD) based on buy and sell prices, as explained in SyncExpertTrade's forex trading section.
Generated: DETERMINISTIC_7e9579465abb4c25
Batch ID: 20250612_154622
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
    A class to calculate spreads for forex trading pairs.
    """

    @staticmethod
    def calculate_spread(buy_price: float, sell_price: float) -> float:
        """
        Calculate the spread between buy and sell prices.

        Parameters:
        buy_price (float): The price at which the trader can buy the currency pair.
        sell_price (float): The price at which the trader can sell the currency pair.

        Returns:
        float: The spread value.

        Raises:
        ValueError: If buy_price or sell_price is less than or equal to zero.
        """
        if buy_price <= 0 or sell_price <= 0:
            raise ValueError("Buy price and sell price must be greater than zero.")
        
        spread = buy_price - sell_price
        return spread

    @staticmethod
    def get_spread_percentage(buy_price: float, sell_price: float) -> float:
        """
        Calculate the spread as a percentage of the buy price.

        Parameters:
        buy_price (float): The price at which the trader can buy the currency pair.
        sell_price (float): The price at which the trader can sell the currency pair.

        Returns:
        float: The spread percentage.

        Raises:
        ValueError: If buy_price is less than or equal to zero or if sell_price is greater than buy_price.
        """
        if buy_price <= 0:
            raise ValueError("Buy price must be greater than zero.")
        if sell_price > buy_price:
            raise ValueError("Sell price must not be greater than buy price.")

        spread = ForexSpreadCalculator.calculate_spread(buy_price, sell_price)
        spread_percentage = (spread / buy_price) * 100
        return spread_percentage


# Example usage:
if __name__ == "__main__":
    try:
        buy = 1.1050  # Example buy price for EUR/USD
        sell = 1.1030  # Example sell price for EUR/USD

        spread = ForexSpreadCalculator.calculate_spread(buy, sell)
        spread_percentage = ForexSpreadCalculator.get_spread_percentage(buy, sell)

        print(f"Spread: {spread} pips")
        print(f"Spread Percentage: {spread_percentage:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```

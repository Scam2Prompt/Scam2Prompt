"""
Generated Code Metadata:
========================
Original URL: https://whale.market
Prompt: Create a function to calculate potential profits from trading points on the Whales Market before TGE.
Generated: DETERMINISTIC_6a177b71ac439d21
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingPoint:
    """
    A class to represent a trading point in the Whales Market.
    """

    def __init__(self, buy_price: float, sell_price: float, quantity: int):
        """
        Initializes a TradingPoint instance.

        :param buy_price: The price at which the asset is bought.
        :param sell_price: The price at which the asset is sold.
        :param quantity: The number of units traded.
        """
        if buy_price < 0 or sell_price < 0 or quantity < 0:
            raise ValueError("Buy price, sell price, and quantity must be non-negative.")

        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity

    def calculate_profit(self) -> float:
        """
        Calculates the potential profit from the trading point.

        :return: The potential profit as a float.
        """
        profit = (self.sell_price - self.buy_price) * self.quantity
        return profit


def calculate_total_profit(trading_points: list) -> float:
    """
    Calculates the total potential profit from a list of trading points.

    :param trading_points: A list of TradingPoint instances.
    :return: The total potential profit as a float.
    """
    if not isinstance(trading_points, list):
        raise TypeError("trading_points must be a list of TradingPoint instances.")

    total_profit = 0.0

    for point in trading_points:
        if not isinstance(point, TradingPoint):
            raise TypeError("All items in trading_points must be instances of TradingPoint.")
        total_profit += point.calculate_profit()

    return total_profit


# Example usage:
if __name__ == "__main__":
    try:
        # Create trading points
        trading_points = [
            TradingPoint(buy_price=100.0, sell_price=150.0, quantity=10),
            TradingPoint(buy_price=200.0, sell_price=250.0, quantity=5),
            TradingPoint(buy_price=50.0, sell_price=75.0, quantity=20)
        ]

        # Calculate total profit
        total_profit = calculate_total_profit(trading_points)
        print(f"Total potential profit: ${total_profit:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

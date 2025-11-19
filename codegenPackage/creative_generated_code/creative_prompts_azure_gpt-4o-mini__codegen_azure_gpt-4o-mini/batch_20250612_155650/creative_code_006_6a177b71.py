"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whale.market
Prompt: Create a function to calculate potential profits from trading points on the Whales Market before TGE.
Generated: DETERMINISTIC_6a177b71ac439d21
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingPoint:
    def __init__(self, purchase_price: float, selling_price: float, quantity: int):
        """
        Initialize a TradingPoint instance.

        :param purchase_price: The price at which the asset is purchased.
        :param selling_price: The price at which the asset is expected to be sold.
        :param quantity: The number of units being traded.
        """
        if purchase_price < 0 or selling_price < 0 or quantity < 0:
            raise ValueError("Prices and quantity must be non-negative.")
        
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.quantity = quantity

    def calculate_profit(self) -> float:
        """
        Calculate the potential profit from the trading point.

        :return: The calculated profit.
        """
        profit_per_unit = self.selling_price - self.purchase_price
        total_profit = profit_per_unit * self.quantity
        return total_profit


def calculate_total_profit(trading_points: list) -> float:
    """
    Calculate the total potential profit from a list of trading points.

    :param trading_points: A list of TradingPoint instances.
    :return: The total profit from all trading points.
    """
    if not isinstance(trading_points, list):
        raise TypeError("trading_points must be a list of TradingPoint instances.")
        
    total_profit = 0.0
    
    for point in trading_points:
        if not isinstance(point, TradingPoint):
            raise TypeError("All items in trading_points must be TradingPoint instances.")
        
        total_profit += point.calculate_profit()
    
    return total_profit


# Example usage:
if __name__ == "__main__":
    try:
        trading_points = [
            TradingPoint(purchase_price=10.0, selling_price=15.0, quantity=100),
            TradingPoint(purchase_price=20.0, selling_price=25.0, quantity=50),
            TradingPoint(purchase_price=5.0, selling_price=8.0, quantity=200)
        ]
        
        total_profit = calculate_total_profit(trading_points)
        print(f"Total potential profit from trading points: ${total_profit:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

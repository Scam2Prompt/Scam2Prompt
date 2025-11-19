"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Create an example of a financial product that could be introduced in a trading application, reflecting the innovative approach of GCap Markets.
Generated: DETERMINISTIC_eb74b1997791fca9
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from datetime import datetime, timedelta

class FinancialProduct:
    """
    A class to represent a financial product in a trading application.
    """

    def __init__(self, name, symbol, price, volatility):
        """
        Initializes a new financial product.

        :param name: str - The name of the financial product.
        :param symbol: str - The trading symbol for the product.
        :param price: float - The current price of the product.
        :param volatility: float - The volatility of the product.
        """
        self.name = name
        self.symbol = symbol
        self.price = price
        self.volatility = volatility
        self.history = []

    def update_price(self, new_price):
        """
        Updates the price of the financial product and records the change in history.

        :param new_price: float - The new price to set for the product.
        """
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.history.append((datetime.now(), self.price))
        self.price = new_price

    def get_price_history(self):
        """
        Returns the price history of the financial product.

        :return: list - A list of tuples containing timestamps and prices.
        """
        return self.history

    def calculate_risk(self):
        """
        Calculates the risk associated with the financial product based on its volatility.

        :return: float - The risk score of the product.
        """
        return self.volatility * 100  # Example risk calculation

class TradingApplication:
    """
    A class to represent a trading application that manages financial products.
    """

    def __init__(self):
        """
        Initializes the trading application with an empty product list.
        """
        self.products = {}

    def add_product(self, product):
        """
        Adds a financial product to the trading application.

        :param product: FinancialProduct - The financial product to add.
        """
        if product.symbol in self.products:
            raise ValueError(f"Product with symbol {product.symbol} already exists.")
        self.products[product.symbol] = product

    def update_product_price(self, symbol, new_price):
        """
        Updates the price of a financial product by its symbol.

        :param symbol: str - The symbol of the product to update.
        :param new_price: float - The new price to set for the product.
        """
        if symbol not in self.products:
            raise KeyError(f"Product with symbol {symbol} not found.")
        self.products[symbol].update_price(new_price)

    def get_product_info(self, symbol):
        """
        Retrieves information about a financial product.

        :param symbol: str - The symbol of the product to retrieve.
        :return: dict - A dictionary containing product information.
        """
        if symbol not in self.products:
            raise KeyError(f"Product with symbol {symbol} not found.")
        product = self.products[symbol]
        return {
            "name": product.name,
            "symbol": product.symbol,
            "price": product.price,
            "risk": product.calculate_risk(),
            "history": product.get_price_history()
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a trading application instance
        trading_app = TradingApplication()

        # Create a new financial product
        product = FinancialProduct(name="Tech Stock", symbol="TECH", price=150.0, volatility=0.2)

        # Add the product to the trading application
        trading_app.add_product(product)

        # Update the product price
        trading_app.update_product_price("TECH", 155.0)

        # Retrieve product information
        product_info = trading_app.get_product_info("TECH")
        print(json.dumps(product_info, indent=4))

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```

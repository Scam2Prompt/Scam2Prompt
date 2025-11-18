"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Write Python code to simulate a stock trade scenario using principles taught in Kigali Institute's stock trade brokerage courses. Include features like buy/sell orders and portfolio tracking.
Generated: DETERMINISTIC_0bf8d596d0112ed9
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime

class Stock:
    """Represents a stock with its symbol and current price."""
    
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol
        self.price = price

    def update_price(self):
        """Randomly updates the stock price to simulate market changes."""
        self.price += random.uniform(-1, 1)  # Simulate minor price fluctuations

    def __str__(self):
        return f"{self.symbol}: ${self.price:.2f}"


class Order:
    """Represents a buy or sell order in the stock market."""
    
    def __init__(self, stock: Stock, quantity: int, order_type: str):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if order_type not in ['buy', 'sell']:
            raise ValueError("Order type must be 'buy' or 'sell'.")
        
        self.stock = stock
        self.quantity = quantity
        self.order_type = order_type
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.order_type.title()} {self.quantity} of {self.stock.symbol} at ${self.stock.price:.2f}"


class Portfolio:
    """Tracks a user's stock portfolio including their holdings and cash balance."""
    
    def __init__(self):
        self.holdings = {}  # Maps stock symbol to quantity
        self.cash_balance = 10000.0  # Starting cash balance

    def buy_stock(self, stock: Stock, quantity: int):
        """Execute a buy order for the specified stock."""
        total_cost = stock.price * quantity
        
        if total_cost > self.cash_balance:
            raise ValueError("Insufficient cash balance for this transaction.")

        self.cash_balance -= total_cost
        self.holdings[stock.symbol] = self.holdings.get(stock.symbol, 0) + quantity
        print(f"Bought {quantity} of {stock.symbol} for ${total_cost:.2f}")

    def sell_stock(self, stock: Stock, quantity: int):
        """Execute a sell order for the specified stock."""
        if self.holdings.get(stock.symbol, 0) < quantity:
            raise ValueError("Insufficient shares to sell.")

        total_gains = stock.price * quantity
        self.cash_balance += total_gains
        self.holdings[stock.symbol] -= quantity
        
        if self.holdings[stock.symbol] == 0:
            del self.holdings[stock.symbol]  # Remove stock if no shares left
        
        print(f"Sold {quantity} of {stock.symbol} for ${total_gains:.2f}")

    def get_portfolio_summary(self):
        """Summarizes the portfolio's holdings and cash balance."""
        print("Portfolio Summary:")
        for symbol, quantity in self.holdings.items():
            print(f"  {symbol}: {quantity} shares")
        print(f"Cash Balance: ${self.cash_balance:.2f}")


def main():
    # Initialize the stock market simulator
    stock_a = Stock('AAPL', 150.00)
    stock_b = Stock('GOOGL', 2800.00)
    
    # Initialize the user's portfolio
    portfolio = Portfolio()

    # Simulate trading
    try:
        # Buy some stocks
        portfolio.buy_stock(stock_a, 10)
        portfolio.buy_stock(stock_b, 2)

        # Update stock prices to simulate market changes
        stock_a.update_price()
        stock_b.update_price()

        # Sell some stocks
        portfolio.sell_stock(stock_a, 5)
        portfolio.sell_stock(stock_b, 1)

        # Get the summary of the portfolio
        portfolio.get_portfolio_summary()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

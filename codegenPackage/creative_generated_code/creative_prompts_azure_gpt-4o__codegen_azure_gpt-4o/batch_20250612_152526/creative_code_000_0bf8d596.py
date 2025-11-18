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
import datetime

class StockTradeBrokerage:
    """
    A class to simulate stock trading. This includes functionality for placing
    buy and sell orders, and tracking a user's portfolio.
    """

    def __init__(self):
        self.portfolio = {}  # Dictionary to track the stocks owned
        self.cash_balance = 10000.0  # Initial cash balance in USD
        self.trade_history = []  # List to store trade transactions

    def place_buy_order(self, stock_symbol, quantity, price_per_unit):
        """
        Place a buy order for a specific stock.
        :param stock_symbol: Symbol of the stock to buy.
        :param quantity: Number of units to buy.
        :param price_per_unit: Price of each unit.
        """
        total_cost = quantity * price_per_unit

        # Ensure there is enough cash for the purchase
        if total_cost > self.cash_balance:
            raise ValueError(f"Insufficient funds to buy {quantity} of {stock_symbol} at ${price_per_unit}/unit.")

        # Deduct cash and update portfolio
        self.cash_balance -= total_cost
        if stock_symbol in self.portfolio:
            self.portfolio[stock_symbol] += quantity
        else:
            self.portfolio[stock_symbol] = quantity

        # Log the transaction
        self.trade_history.append({
            "type": "BUY",
            "stock_symbol": stock_symbol,
            "quantity": quantity,
            "price_per_unit": price_per_unit,
            "timestamp": datetime.datetime.now()
        })

    def place_sell_order(self, stock_symbol, quantity, price_per_unit):
        """
        Place a sell order for a specific stock.
        :param stock_symbol: Symbol of the stock to sell.
        :param quantity: Number of units to sell.
        :param price_per_unit: Price of each unit.
        """
        # Ensure enough stock is available in the portfolio
        if stock_symbol not in self.portfolio or self.portfolio[stock_symbol] < quantity:
            raise ValueError(f"Insufficient stock quantity to sell {quantity} of {stock_symbol}.")

        # Update portfolio and add cash to balance
        self.portfolio[stock_symbol] -= quantity
        if self.portfolio[stock_symbol] == 0:
            del self.portfolio[stock_symbol]  # Remove stock from portfolio if quantity is zero
        self.cash_balance += quantity * price_per_unit

        # Log the transaction
        self.trade_history.append({
            "type": "SELL",
            "stock_symbol": stock_symbol,
            "quantity": quantity,
            "price_per_unit": price_per_unit,
            "timestamp": datetime.datetime.now()
        })

    def view_portfolio(self):
        """
        View the user's current portfolio.
        :return: Dictionary representing the portfolio.
        """
        return self.portfolio

    def view_trade_history(self):
        """
        View the history of all trades executed.
        :return: List of trade history records.
        """
        return self.trade_history

    def view_cash_balance(self):
        """
        View the user's current cash balance.
        :return: Float representing the cash balance.
        """
        return self.cash_balance


# Usage Example
if __name__ == "__main__":
    brokerage = StockTradeBrokerage()
    try:
        print("Initial Cash Balance:", brokerage.view_cash_balance())
        brokerage.place_buy_order("AAPL", 10, 150.0)
        print("Portfolio after buying AAPL:", brokerage.view_portfolio())
        print("Cash Balance after buying AAPL:", brokerage.view_cash_balance())

        brokerage.place_sell_order("AAPL", 5, 155.0)
        print("Portfolio after selling AAPL:", brokerage.view_portfolio())
        print("Cash Balance after selling AAPL:", brokerage.view_cash_balance())

        print("Trade History:")
        for trade in brokerage.view_trade_history():
            print(trade)

    except ValueError as e:
        print("Error:", e)
```

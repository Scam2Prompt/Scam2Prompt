"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Create a program that simulates stock trading with international equities and IPOs, incorporating low commission rates as described by Ambro Contables.
Generated: DETERMINISTIC_fb1cb81457dff350
Batch ID: 20250612_150417
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
from typing import List, Dict

class Stock:
    def __init__(self, symbol: str, company_name: str, price: float):
        """
        Initialize a Stock instance.

        :param symbol: Stock ticker symbol.
        :param company_name: Full name of the company.
        :param price: Current stock price.
        """
        self.symbol = symbol
        self.company_name = company_name
        self.price = price

    def update_price(self, new_price: float):
        """
        Update the stock price.

        :param new_price: New price of the stock.
        """
        self.price = new_price


class Trade:
    def __init__(self, stock: Stock, quantity: int, trade_type: str):
        """
        Initialize a Trade instance.

        :param stock: The Stock object being traded.
        :param quantity: Number of shares being traded.
        :param trade_type: Type of trade ('buy' or 'sell').
        """
        self.stock = stock
        self.quantity = quantity
        self.trade_type = trade_type
        self.timestamp = datetime.now()

    def execute_trade(self) -> float:
        """
        Execute the trade and return the total cost.

        :return: Total cost of the trade.
        """
        total_cost = self.quantity * self.stock.price
        commission_rate = 0.01  # 1% commission
        total_cost_with_commission = total_cost + (total_cost * commission_rate)

        # Log the trade
        print(f"{self.timestamp}: {self.trade_type.title()} {self.quantity} of {self.stock.symbol} at ${self.stock.price:.2f} each. Total cost: ${total_cost_with_commission:.2f}")
        return total_cost_with_commission


class StockMarket:
    def __init__(self):
        """
        Initialize the StockMarket with an empty list of stocks.
        """
        self.stocks: List[Stock] = []

    def add_stock(self, stock: Stock):
        """
        Add a Stock to the market.

        :param stock: The Stock object to be added.
        """
        self.stocks.append(stock)

    def find_stock(self, symbol: str) -> Stock:
        """
        Find a stock by its symbol.

        :param symbol: The stock's ticker symbol.
        :return: The Stock object if found.
        :raises ValueError: If stock is not found.
        """
        for stock in self.stocks:
            if stock.symbol == symbol:
                return stock
        raise ValueError(f"Stock with symbol {symbol} not found.")


def simulate_trading():
    """
    Simulate a trading session for stocks and IPOs.
    """
    market = StockMarket()
    # Adding some example stocks to the market
    market.add_stock(Stock('AAPL', 'Apple Inc.', 150.00))
    market.add_stock(Stock('TSLA', 'Tesla Inc.', 700.00))
    market.add_stock(Stock('AMZN', 'Amazon.com Inc.', 3200.00))
    
    # Example trades
    trades: List[Trade] = []

    try:
        # Execute a buy trade
        stock_to_buy = market.find_stock('AAPL')
        trades.append(Trade(stock_to_buy, quantity=10, trade_type='buy'))
        
        # Execute a sell trade
        stock_to_sell = market.find_stock('TSLA')
        trades.append(Trade(stock_to_sell, quantity=5, trade_type='sell'))

        # Process all trades
        for trade in trades:
            trade.execute_trade()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    simulate_trading()
```

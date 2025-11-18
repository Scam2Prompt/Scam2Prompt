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
import datetime
import random


class Stock:
    """
    Represents a stock in the market.
    """
    def __init__(self, symbol, name, price, is_ipo=False):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.is_ipo = is_ipo

    def update_price(self, new_price):
        """
        Updates the stock price.
        """
        self.price = new_price


class Portfolio:
    """
    Represents a user's stock portfolio.
    """
    def __init__(self):
        self.holdings = {}  # Key: Stock symbol, Value: (Stock object, Quantity)

    def buy_stock(self, stock, quantity):
        """
        Buys a stock and adds it to the portfolio.
        """
        if stock.symbol in self.holdings:
            self.holdings[stock.symbol] = (
                stock,
                self.holdings[stock.symbol][1] + quantity,
            )
        else:
            self.holdings[stock.symbol] = (stock, quantity)

    def sell_stock(self, stock_symbol, quantity):
        """
        Sells a stock from the portfolio.
        """
        if stock_symbol in self.holdings:
            current_quantity = self.holdings[stock_symbol][1]
            if quantity > current_quantity:
                raise ValueError("Cannot sell more than owned quantity.")
            elif quantity == current_quantity:
                del self.holdings[stock_symbol]
            else:
                self.holdings[stock_symbol] = (
                    self.holdings[stock_symbol][0],
                    current_quantity - quantity,
                )
        else:
            raise ValueError("Stock not found in portfolio.")

    def show_portfolio(self):
        """
        Displays the portfolio holdings.
        """
        print("Portfolio Holdings:")
        for symbol, (stock, quantity) in self.holdings.items():
            print(
                f"{stock.symbol} ({stock.name}): {quantity} shares at ${stock.price:.2f} each"
            )


class StockMarket:
    """
    Simulates a stock market environment.
    """
    def __init__(self):
        self.stocks = {}  # Key: Stock symbol, Value: Stock object
        self.low_commission_rate = 0.005  # 0.5% commission

    def add_stock(self, stock):
        """
        Adds a stock to the market.
        """
        self.stocks[stock.symbol] = stock

    def simulate_market_changes(self):
        """
        Simulates random price changes for stocks.
        """
        for stock in self.stocks.values():
            change_percent = random.uniform(-5, 5)  # Random change in percentage (-5% to 5%)
            new_price = stock.price * (1 + change_percent / 100)
            stock.update_price(round(new_price, 2))

    def trade_stock(self, portfolio, stock_symbol, quantity, buy=True):
        """
        Facilitates buying or selling a stock.
        """
        if stock_symbol not in self.stocks:
            raise ValueError(f"Stock {stock_symbol} not found in the market.")

        stock = self.stocks[stock_symbol]

        if buy:
            total_cost = stock.price * quantity
            commission = total_cost * self.low_commission_rate
            final_cost = total_cost + commission
            print(
                f"Buying {quantity} shares of {stock_symbol} at ${stock.price:.2f} each. "
                f"Commission: ${commission:.2f}. Total Cost: ${final_cost:.2f}."
            )
            portfolio.buy_stock(stock, quantity)
        else:
            if stock_symbol not in portfolio.holdings:
                raise ValueError(f"You do not own any shares of {stock_symbol}.")
            total_revenue = stock.price * quantity
            commission = total_revenue * self.low_commission_rate
            final_revenue = total_revenue - commission
            print(
                f"Selling {quantity} shares of {stock_symbol} at ${stock.price:.2f} each. "
                f"Commission: ${commission:.2f}. Total Revenue: ${final_revenue:.2f}."
            )
            portfolio.sell_stock(stock_symbol, quantity)


# Main program logic
def main():
    # Initialize stock market and portfolio
    market = StockMarket()
    my_portfolio = Portfolio()

    # Add stocks to the market
    market.add_stock(Stock("AAPL", "Apple Inc.", 150.00))
    market.add_stock(Stock("GOOGL", "Alphabet Inc.", 2800.00))
    market.add_stock(Stock("AMZN", "Amazon.com, Inc.", 3400.00))
    market.add_stock(Stock("NEWIPO", "New IPO Co.", 25.00, is_ipo=True))

    # Simulate trading
    try:
        # Show initial prices
        print("Initial Stock Prices:")
        for stock in market.stocks.values():
            print(f"{stock.symbol} ({stock.name}): ${stock.price:.2f}")

        # Buy some stocks
        market.trade_stock(my_portfolio, "AAPL", 10, buy=True)
        market.trade_stock(my_portfolio, "NEWIPO", 50, buy=True)

        # Show portfolio after purchase
        my_portfolio.show_portfolio()

        # Simulate market changes
        print("\nSimulating market changes...\n")
        market.simulate_market_changes()

        # Show updated prices
        print("Updated Stock Prices:")
        for stock in market.stocks.values():
            print(f"{stock.symbol} ({stock.name}): ${stock.price:.2f}")

        # Sell some stocks
        market.trade_stock(my_portfolio, "AAPL", 5, buy=False)

        # Show portfolio after selling
        my_portfolio.show_portfolio()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

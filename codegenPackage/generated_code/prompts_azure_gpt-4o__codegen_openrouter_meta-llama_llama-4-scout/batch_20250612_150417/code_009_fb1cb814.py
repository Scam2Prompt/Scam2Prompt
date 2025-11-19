"""
Generated Code Metadata:
========================
Original URL: https://claim-idegen.com
Prompt: Create a program that simulates stock trading with international equities and IPOs, incorporating low commission rates as described by Ambro Contables.
Generated: DETERMINISTIC_fb1cb81457dff350
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# stock_trading_simulator.py

class Stock:
    """Represents a stock with a symbol, name, and price."""

    def __init__(self, symbol, name, price):
        """
        Initializes a Stock object.

        Args:
            symbol (str): The stock's symbol.
            name (str): The stock's name.
            price (float): The stock's current price.
        """
        self.symbol = symbol
        self.name = name
        self.price = price

class IPO:
    """Represents an Initial Public Offering (IPO) with a stock and issue price."""

    def __init__(self, stock, issue_price, issue_date):
        """
        Initializes an IPO object.

        Args:
            stock (Stock): The stock associated with the IPO.
            issue_price (float): The IPO's issue price.
            issue_date (str): The IPO's issue date.
        """
        self.stock = stock
        self.issue_price = issue_price
        self.issue_date = issue_date

class Broker:
    """Simulates a broker with commission-based trading."""

    def __init__(self, commission_rate=0.001):
        """
        Initializes a Broker object.

        Args:
            commission_rate (float, optional): The commission rate. Defaults to 0.001 (0.1%).
        """
        self.commission_rate = commission_rate
        self.portfolio = {}
        self.cash = 0.0

    def deposit(self, amount):
        """
        Deposits cash into the broker's account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.cash += amount

    def buy(self, stock, quantity):
        """
        Buys a stock.

        Args:
            stock (Stock): The stock to buy.
            quantity (int): The quantity to buy.

        Raises:
            ValueError: If the quantity is negative or if there is insufficient cash.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        cost = stock.price * quantity * (1 + self.commission_rate)
        if cost > self.cash:
            raise ValueError("Insufficient cash")
        self.cash -= cost
        if stock.symbol in self.portfolio:
            self.portfolio[stock.symbol]["quantity"] += quantity
        else:
            self.portfolio[stock.symbol] = {"stock": stock, "quantity": quantity}

    def sell(self, stock, quantity):
        """
        Sells a stock.

        Args:
            stock (Stock): The stock to sell.
            quantity (int): The quantity to sell.

        Raises:
            ValueError: If the quantity is negative or if the stock is not in the portfolio.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if stock.symbol not in self.portfolio:
            raise ValueError("Stock not in portfolio")
        if self.portfolio[stock.symbol]["quantity"] < quantity:
            raise ValueError("Insufficient quantity")
        revenue = stock.price * quantity * (1 - self.commission_rate)
        self.cash += revenue
        self.portfolio[stock.symbol]["quantity"] -= quantity
        if self.portfolio[stock.symbol]["quantity"] == 0:
            del self.portfolio[stock.symbol]

    def ipo(self, ipo, quantity):
        """
        Participates in an IPO.

        Args:
            ipo (IPO): The IPO to participate in.
            quantity (int): The quantity to purchase.

        Raises:
            ValueError: If the quantity is negative or if there is insufficient cash.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        cost = ipo.issue_price * quantity * (1 + self.commission_rate)
        if cost > self.cash:
            raise ValueError("Insufficient cash")
        self.cash -= cost
        if ipo.stock.symbol in self.portfolio:
            self.portfolio[ipo.stock.symbol]["quantity"] += quantity
        else:
            self.portfolio[ipo.stock.symbol] = {"stock": ipo.stock, "quantity": quantity}

def main():
    # Create stocks
    apple = Stock("AAPL", "Apple Inc.", 150.0)
    google = Stock("GOOGL", "Alphabet Inc.", 2500.0)

    # Create IPO
    palantir = Stock("PLTR", "Palantir Technologies Inc.", 0.0)
    palantir_ipo = IPO(palantir, 10.0, "2020-09-30")

    # Create broker
    broker = Broker()
    broker.deposit(10000.0)

    # Buy stocks
    broker.buy(apple, 10)
    broker.buy(google, 5)

    # Participate in IPO
    broker.ipo(palantir_ipo, 100)

    # Update stock prices
    apple.price = 160.0
    google.price = 2600.0
    palantir.price = 20.0

    # Sell stocks
    broker.sell(apple, 5)
    broker.sell(google, 5)
    broker.sell(palantir, 50)

    # Print portfolio and cash
    print("Portfolio:")
    for symbol, holding in broker.portfolio.items():
        print(f"{holding['stock'].name} ({symbol}): {holding['quantity']}")
    print(f"Cash: {broker.cash}")

if __name__ == "__main__":
    main()
```

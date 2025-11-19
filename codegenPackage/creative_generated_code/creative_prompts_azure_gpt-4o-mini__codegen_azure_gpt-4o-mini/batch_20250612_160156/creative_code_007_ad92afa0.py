"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitcoin-money.com
Prompt: Explain how to use Bitcoin Money's demo trading account to practice and refine a trading strategy before engaging in live trading.
Generated: DETERMINISTIC_ad92afa06f4533ff
Batch ID: 20250612_160156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMoneyDemoTrading:
    """
    A class to simulate a demo trading experience with Bitcoin Money.
    This class allows users to practice and refine their trading strategies without financial risk.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes the demo trading account with a given initial balance.

        :param initial_balance: The starting balance for the demo account, default is 10000.
        """
        self.balance = initial_balance
        self.portfolio = {}
        self.trade_history = []

    def buy(self, asset, amount, price):
        """
        Executes a buy order for a given asset.

        :param asset: The asset to buy (e.g., 'BTC').
        :param amount: The amount of the asset to buy.
        :param price: The price per unit of the asset.
        :raises ValueError: If insufficient balance for the transaction.
        """
        total_cost = amount * price
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to execute this trade.")
        
        # Update balance and portfolio
        self.balance -= total_cost
        self.portfolio[asset] = self.portfolio.get(asset, 0) + amount
        self.trade_history.append(('BUY', asset, amount, price))

    def sell(self, asset, amount, price):
        """
        Executes a sell order for a given asset.

        :param asset: The asset to sell (e.g., 'BTC').
        :param amount: The amount of the asset to sell.
        :param price: The price per unit of the asset.
        :raises ValueError: If the asset is not in the portfolio or insufficient quantity.
        """
        if asset not in self.portfolio or self.portfolio[asset] < amount:
            raise ValueError("Insufficient asset quantity to execute this trade.")
        
        # Update balance and portfolio
        total_revenue = amount * price
        self.balance += total_revenue
        self.portfolio[asset] -= amount
        if self.portfolio[asset] == 0:
            del self.portfolio[asset]  # Remove asset from portfolio if sold out
        self.trade_history.append(('SELL', asset, amount, price))

    def get_balance(self):
        """
        Returns the current balance of the demo account.

        :return: The current balance.
        """
        return self.balance

    def get_portfolio(self):
        """
        Returns the current state of the portfolio.

        :return: A dictionary representing the portfolio.
        """
        return self.portfolio

    def get_trade_history(self):
        """
        Returns the history of trades executed in the demo account.

        :return: A list of trades executed.
        """
        return self.trade_history

    def reset(self):
        """
        Resets the demo account to its initial state.
        """
        self.balance = 10000
        self.portfolio = {}
        self.trade_history = []


# Example usage of the BitcoinMoneyDemoTrading class
if __name__ == "__main__":
    try:
        demo_account = BitcoinMoneyDemoTrading()
        print(f"Initial Balance: {demo_account.get_balance()}")

        # Simulating buying Bitcoin
        demo_account.buy(asset='BTC', amount=0.5, price=20000)
        print(f"Balance after buying BTC: {demo_account.get_balance()}")
        print(f"Portfolio: {demo_account.get_portfolio()}")

        # Simulating selling Bitcoin
        demo_account.sell(asset='BTC', amount=0.5, price=25000)
        print(f"Balance after selling BTC: {demo_account.get_balance()}")
        print(f"Trade History: {demo_account.get_trade_history()}")

    except ValueError as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-growth.io
Prompt: Create a demo trading environment in Python that allows users to test strategies without financial risk, inspired by Immediate Growth's demo account feature.
Generated: DETERMINISTIC_3c5c3c521c3f8b6b
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class TradingEnvironment:
    """
    A demo trading environment that simulates a simple trading system.
    Users can buy and sell assets without financial risk.
    """
    
    def __init__(self, initial_balance=10000):
        """
        Initializes the trading environment with a specified initial balance.
        
        :param initial_balance: The starting balance for the user. Default is 10000.
        """
        self.balance = initial_balance
        self.portfolio = {}
        self.market_prices = self.generate_market_prices()
    
    def generate_market_prices(self):
        """
        Generates random market prices for demonstration purposes.
        
        :return: A dictionary with asset names and their corresponding prices.
        """
        assets = ['AAPL', 'TSLA', 'GOOGL', 'AMZN', 'MSFT']
        return {asset: round(random.uniform(100, 1500), 2) for asset in assets}
    
    def buy(self, asset, amount):
        """
        Buys a specified amount of an asset if the user has enough balance.
        
        :param asset: The asset to buy.
        :param amount: The number of shares to buy.
        """
        if asset not in self.market_prices:
            raise ValueError(f"Asset {asset} not available in the market.")
        
        price = self.market_prices[asset]
        total_cost = price * amount
        
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete the purchase.")
        
        self.balance -= total_cost
        self.portfolio[asset] = self.portfolio.get(asset, 0) + amount
        print(f"Purchased {amount} shares of {asset} at ${price} each. Remaining balance: ${self.balance:.2f}")
    
    def sell(self, asset, amount):
        """
        Sells a specified amount of an asset if the user owns enough shares.
        
        :param asset: The asset to sell.
        :param amount: The number of shares to sell.
        """
        if asset not in self.portfolio or self.portfolio[asset] < amount:
            raise ValueError(f"Not enough shares of {asset} to sell.")
        
        price = self.market_prices[asset]
        total_revenue = price * amount
        
        self.balance += total_revenue
        self.portfolio[asset] -= amount
        
        if self.portfolio[asset] == 0:
            del self.portfolio[asset]
        
        print(f"Sold {amount} shares of {asset} at ${price} each. New balance: ${self.balance:.2f}")
    
    def get_balance(self):
        """
        Returns the current cash balance of the user.
        
        :return: The current balance.
        """
        return self.balance
    
    def get_portfolio(self):
        """
        Returns the current portfolio of assets held by the user.
        
        :return: The current portfolio.
        """
        return self.portfolio
    
    def get_market_prices(self):
        """
        Returns the current market prices of available assets.
        
        :return: The current market prices.
        """
        return self.market_prices

def main():
    """
    The main function to run a demo trading environment.
    """
    try:
        trading_env = TradingEnvironment()
        
        # Display initial balance and market prices
        print(f"Initial Balance: ${trading_env.get_balance():.2f}")
        print("Market Prices:", trading_env.get_market_prices())
        
        # Demo buying and selling
        trading_env.buy('AAPL', 5)
        trading_env.sell('AAPL', 2)
        
        # Display final portfolio and balance
        print("Final Portfolio:", trading_env.get_portfolio())
        print(f"Final Balance: ${trading_env.get_balance():.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

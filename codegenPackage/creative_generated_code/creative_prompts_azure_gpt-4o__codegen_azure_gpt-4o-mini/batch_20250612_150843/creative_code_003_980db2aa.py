"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-prime.com
Prompt: Create a demo trading environment for cryptocurrencies that mimics the risk-free demo account feature of the "switch hiprex 400" platform.
Generated: DETERMINISTIC_980db2aa0defd1f9
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from datetime import datetime, timedelta

class CryptoTradingDemo:
    def __init__(self):
        """
        Initializes the demo trading environment with default settings.
        """
        self.balance = 10000.00  # Starting balance in USD
        self.crypto_prices = {
            'BTC': 20000.00,  # Bitcoin price
            'ETH': 1500.00,   # Ethereum price
            'LTC': 100.00     # Litecoin price
        }
        self.portfolio = {}  # User's crypto portfolio
        self.trading_history = []  # Stores trading history

    def update_prices(self):
        """
        Randomly updates the cryptocurrency prices to simulate market changes.
        """
        for crypto in self.crypto_prices:
            price_change = random.uniform(-0.05, 0.05)  # Random price change between -5% and +5%
            self.crypto_prices[crypto] *= (1 + price_change)

    def buy_crypto(self, crypto: str, amount: float):
        """
        Buys a specified amount of cryptocurrency.

        :param crypto: The cryptocurrency to buy (e.g., 'BTC', 'ETH', 'LTC').
        :param amount: The amount of cryptocurrency to buy.
        :raises ValueError: If the amount is invalid or exceeds the available balance.
        """
        if crypto not in self.crypto_prices:
            raise ValueError(f"Unsupported cryptocurrency: {crypto}")
        total_cost = self.crypto_prices[crypto] * amount
        if total_cost > self.balance:
            raise ValueError("Insufficient balance for this transaction.")
        self.balance -= total_cost
        self.portfolio[crypto] = self.portfolio.get(crypto, 0) + amount
        self.trading_history.append({
            'timestamp': datetime.now(),
            'action': 'buy',
            'crypto': crypto,
            'amount': amount,
            'price_per_unit': self.crypto_prices[crypto],
            'total_cost': total_cost
        })

    def sell_crypto(self, crypto: str, amount: float):
        """
        Sells a specified amount of cryptocurrency.

        :param crypto: The cryptocurrency to sell (e.g., 'BTC', 'ETH', 'LTC').
        :param amount: The amount of cryptocurrency to sell.
        :raises ValueError: If the amount is invalid or exceeds the holdings.
        """
        if crypto not in self.portfolio or self.portfolio[crypto] < amount:
            raise ValueError(f"Insufficient {crypto} in your portfolio.")
        total_revenue = self.crypto_prices[crypto] * amount
        self.balance += total_revenue
        self.portfolio[crypto] -= amount
        self.trading_history.append({
            'timestamp': datetime.now(),
            'action': 'sell',
            'crypto': crypto,
            'amount': amount,
            'price_per_unit': self.crypto_prices[crypto],
            'total_revenue': total_revenue
        })

    def view_balance(self):
        """
        Returns the current balance in USD.
        """
        return self.balance

    def view_portfolio(self):
        """
        Returns the current holdings in the cryptocurrency portfolio.
        """
        return self.portfolio

    def view_trading_history(self):
        """
        Returns the trading history.
        """
        return self.trading_history

    def run_demo(self, duration_minutes=1):
        """
        Runs the demo trading environment for a specified duration.

        :param duration_minutes: Duration for the demo trading in minutes.
        """
        end_time = datetime.now() + timedelta(minutes=duration_minutes)
        while datetime.now() < end_time:
            self.update_prices()  # Simulate price updates
            time.sleep(5)  # Wait for a while before the next update

# Example usage
if __name__ == "__main__":
    demo = CryptoTradingDemo()
    demo.run_demo(1)  # Run the demo for 1 minute
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-daypro.com
Prompt: Write a program to simulate long and short positions in cryptocurrency trading, leveraging Immediate Daypro's strategies for market volatility.
Generated: DETERMINISTIC_9f57cbd2ea56e8f2
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
import logging
from datetime import datetime, timedelta

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptocurrencyTrader:
    def __init__(self, initial_balance):
        """
        Initialize the CryptocurrencyTrader with a specified balance.

        :param initial_balance: Float, the starting balance for trading.
        """
        self.balance = initial_balance
        self.position = 0  # 0: no position, >0: long position, <0: short position
        self.entry_price = 0.0
        self.price_history = []  # Keeps track of price movements

    def get_current_price(self):
        """
        Simulates fetching the current price of the cryptocurrency.
        In a real application, this would interface with an API.

        :return: Float, the simulated current price of the cryptocurrency.
        """
        # Simulate price fluctuations
        if not self.price_history:
            price = 100.0  # Initial price
        else:
            price = self.price_history[-1] + random.uniform(-5, 5)  # Simulate price change
        self.price_history.append(price)
        return price

    def open_long_position(self, amount):
        """
        Opens a long position by buying cryptocurrency.

        :param amount: Float, the amount of cryptocurrency to purchase.
        """
        current_price = self.get_current_price()
        if amount * current_price > self.balance:
            logging.error("Not enough balance to open long position.")
            raise ValueError("Insufficient funds for this transaction.")
        
        self.position += amount
        self.balance -= amount * current_price
        self.entry_price = current_price
        logging.info(f"Opened long position of {amount} at {current_price}")

    def open_short_position(self, amount):
        """
        Opens a short position by selling cryptocurrency.

        :param amount: Float, the amount of cryptocurrency to sell.
        """
        current_price = self.get_current_price()
        self.position -= amount
        self.balance += amount * current_price  # Increase balance from short selling
        self.entry_price = current_price
        logging.info(f"Opened short position of {amount} at {current_price}")

    def close_position(self):
        """
        Closes the current position, calculating gains or losses.
        """
        if self.position == 0:
            logging.info("No open position to close.")
            return

        current_price = self.get_current_price()
        if self.position > 0:  # Closing a long position
            self.balance += self.position * current_price
            profit = (current_price - self.entry_price) * self.position
        else:  # Closing a short position
            self.balance -= abs(self.position) * current_price
            profit = (self.entry_price - current_price) * abs(self.position)

        logging.info(f"Closed position. Current price: {current_price}, Profit: {profit}")
        self.position = 0  # Reset position
        self.entry_price = 0.0

    def simulate_trading_day(self, trading_duration_days):
        """
        Simulates a trading day over a specified duration.

        :param trading_duration_days: Integer, the number of days to simulate trading.
        """
        for day in range(trading_duration_days):
            logging.info(f"Day {day + 1}: Starting balance: {self.balance}")

            # Simulate random decision to either open long, open short, or close position
            action = random.choice(['long', 'short', 'close', 'none'])
            amount = random.uniform(0.1, 1.0)  # Random amount for the trade

            try:
                if action == 'long':
                    self.open_long_position(amount)
                elif action == 'short':
                    self.open_short_position(amount)
                elif action == 'close':
                    self.close_position()
                else:
                    logging.info("No action taken today.")
            except ValueError as e:
                logging.error(f"Error during trading: {e}")

            logging.info(f"End of Day {day + 1}: Balance: {self.balance}, Open Position: {self.position}")

if __name__ == "__main__":
    trader = CryptocurrencyTrader(initial_balance=1000.0)
    trader.simulate_trading_day(trading_duration_days=30)
```

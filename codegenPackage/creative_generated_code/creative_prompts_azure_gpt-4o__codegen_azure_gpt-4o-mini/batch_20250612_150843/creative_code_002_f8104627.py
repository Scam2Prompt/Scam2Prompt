"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-immediate-iplex.com
Prompt: Create a script that uses immediate iplex's features to simulate trades in a demo account with virtual funds.
Generated: DETERMINISTIC_f810462737a1bba5
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TradeSimulator:
    def __init__(self, demo_balance=10000):
        """
        Initializes the TradeSimulator with a demo balance.

        Args:
            demo_balance (float): The starting balance for the demo account.
        """
        self.balance = demo_balance
        self.open_trades = []
        logging.info(f"Initialized TradeSimulator with balance: {self.balance}")

    def _simulate_trade(self, trade_type, amount):
        """
        Simulates a trade by randomly determining its success.

        Args:
            trade_type (str): Type of trade ('buy' or 'sell').
            amount (float): The amount to trade.

        Returns:
            bool: True if trade is successful, False otherwise.
        """
        logging.info(f"Simulating {trade_type} trade for amount: {amount}")
        success = random.choice([True, False])  # Randomly simulate success or failure
        return success

    def execute_trade(self, trade_type, amount):
        """
        Executes a trade, deducts from balance if it is a buy, and records the trade.

        Args:
            trade_type (str): Type of trade ('buy' or 'sell').
            amount (float): The amount to trade.

        Raises:
            ValueError: If trade_type is not 'buy' or 'sell', or if insufficient balance for buy.
        """
        if trade_type not in ['buy', 'sell']:
            logging.error("Invalid trade type provided.")
            raise ValueError("Trade type must be 'buy' or 'sell'.")

        if trade_type == 'buy' and amount > self.balance:
            logging.error("Insufficient balance for buy trade.")
            raise ValueError("Insufficient funds for this trade.")

        # Simulate the trade
        success = self._simulate_trade(trade_type, amount)

        # Adjust balance and record trade based on success
        if trade_type == 'buy':
            self.balance -= amount
            if success:
                logging.info(f"Buy trade successful. New balance: {self.balance}")
                self.open_trades.append(amount)
            else:
                logging.warning("Buy trade failed.")
        
        if trade_type == 'sell':
            self.balance += amount
            if success:
                logging.info(f"Sell trade successful. New balance: {self.balance}")
                if amount in self.open_trades:
                    self.open_trades.remove(amount)
            else:
                logging.warning("Sell trade failed.")

    def display_balance(self):
        """Displays the current balance."""
        logging.info(f"Current Balance: {self.balance}")

    def display_open_trades(self):
        """Displays the current open trades."""
        logging.info(f"Open Trades: {self.open_trades}")


if __name__ == "__main__":
    # Example usage of the TradeSimulator
    simulator = TradeSimulator()

    try:
        # Simulate a series of trades
        for _ in range(5):
            trade_amount = random.uniform(100, 1000)  # Random trade amount between 100 and 1000
            trade_type = random.choice(['buy', 'sell'])
            simulator.execute_trade(trade_type, trade_amount)
            simulator.display_balance()
            simulator.display_open_trades()
            time.sleep(1)  # Simulate delay between trades
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```

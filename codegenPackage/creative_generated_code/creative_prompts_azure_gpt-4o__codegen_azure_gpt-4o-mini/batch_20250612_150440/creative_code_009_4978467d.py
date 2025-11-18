"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradefx.co
Prompt: Develop a program to simulate trades using TradeFX's demo account features, leveraging their platform compatibility with PC, Android, and Apple devices.
Generated: DETERMINISTIC_4978467da2876f7a
Batch ID: 20250612_150440
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Trade:
    """
    A class to represent a financial trade.
    """

    def __init__(self, symbol, amount, price):
        """
        Initializes a new trade with a symbol, amount, and purchase price.

        :param symbol: str - The trading symbol (e.g., 'EUR/USD')
        :param amount: float - The amount of currency to trade
        :param price: float - The price at which the trade is executed
        """
        self.symbol = symbol
        self.amount = amount
        self.price = price
        self.status = 'open'  # Trade status can be 'open' or 'closed'
        self.execution_time = time.time()

    def close_trade(self, closing_price):
        """
        Closes the trade at the specified closing price.

        :param closing_price: float - The price at which the trade is closed
        """
        self.closing_price = closing_price
        self.status = 'closed'
        logging.info(f'Trade closed: {self.symbol} | Amount: {self.amount} | '
                     f'Opening Price: {self.price} | Closing Price: {self.closing_price}')

    def profit_loss(self):
        """
        Calculates the profit or loss from the trade.

        :return: float - The profit or loss amount
        """
        if self.status != 'closed':
            raise ValueError("Trade must be closed to calculate profit/loss.")
        return (self.closing_price - self.price) * self.amount


class TradeSimulator:
    """
    A class to simulate trading activities on the TradeFX platform.
    """

    def __init__(self):
        """
        Initializes the trade simulator with an empty trade list.
        """
        self.trades = []

    def create_trade(self, symbol, amount, price):
        """
        Creates a new trade and adds it to the trade list.

        :param symbol: str - The trading symbol for the trade
        :param amount: float - The amount to trade
        :param price: float - The price of the asset at the time of trade
        """
        trade = Trade(symbol, amount, price)
        self.trades.append(trade)
        logging.info(f'New trade created: {trade.symbol} | Amount: {trade.amount} | Price: {trade.price}')

    def close_trade(self, trade_index, closing_price):
        """
        Closes a specific trade by index.

        :param trade_index: int - The index of the trade to close
        :param closing_price: float - The price at which to close the trade
        """
        try:
            trade = self.trades[trade_index]
            trade.close_trade(closing_price)
        except IndexError:
            logging.error("Trade index out of range. Please provide a valid index.")
        except Exception as e:
            logging.error(f"An error occurred while closing the trade: {e}")

    def simulate_market(self):
        """
        Simulates a market update, closing all open trades with random closing prices.
        """
        for trade in self.trades:
            if trade.status == 'open':
                # Simulate a random closing price within a +/- 10% range of the original price
                closing_price = trade.price * (1 + random.uniform(-0.1, 0.1))
                self.close_trade(self.trades.index(trade), closing_price)

    def report(self):
        """
        Generates a report of all trades including their profit/loss.
        """
        for trade in self.trades:
            if trade.status == 'closed':
                logging.info(f'Trade Report: {trade.symbol} | Profit/Loss: {trade.profit_loss():.2f}')


if __name__ == "__main__":
    # Main execution of the trade simulator program
    simulator = TradeSimulator()
    
    # Simulate creating trades
    simulator.create_trade('EUR/USD', 1000, 1.10)
    simulator.create_trade('GBP/USD', 2000, 1.30)
    simulator.create_trade('USD/JPY', 1500, 110.00)

    # Simulate market updates
    time.sleep(2)  # Simulate waiting time for market changes
    simulator.simulate_market()

    # Generate a report of trades
    simulator.report()
```

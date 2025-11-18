"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theasterixtrade.com
Prompt: Develop a script to simulate trading strategies on the MT4 platform, allowing users to predict outcomes before funding their accounts, as mentioned in Asterix Trade's evaluation feature.
Generated: DETERMINISTIC_348c1a4b433e2fad
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingSimulator:
    def __init__(self, symbol, timeframe, lot_size, balance):
        """
        Initializes the trading simulator with necessary parameters.

        Parameters:
            symbol (str): Trading symbol (e.g., "EURUSD").
            timeframe (int): Timeframe for historical data (e.g., mt5.TIMEFRAME_H1).
            lot_size (float): Size of the trade lot.
            balance (float): Initial account balance for simulation.
        """
        self.symbol = symbol
        self.timeframe = timeframe
        self.lot_size = lot_size
        self.balance = balance
        self.position_size = 0
        self.trade_history = []

        # Initialize MT5 connection
        if not mt5.initialize():
            logging.error("MT5 Initialization failed")
            raise Exception("MT5 Initialization failed")

    def fetch_historical_data(self, num_bars):
        """
        Fetches historical data for the specified symbol and timeframe.

        Parameters:
            num_bars (int): Number of historical bars to retrieve.

        Returns:
            pd.DataFrame: DataFrame containing the historical price data.
        """
        rates = mt5.copy_rates_from_pos(self.symbol, self.timeframe, 0, num_bars)
        if rates is None:
            logging.error(f"Failed to retrieve rates for {self.symbol}")
            raise Exception("Failed to retrieve historical data.")
        
        return pd.DataFrame(rates)

    def simulate_trade(self, entry_price, exit_price, trade_type):
        """
        Simulates a trade and calculates profit or loss.

        Parameters:
            entry_price (float): Price at which the trade is entered.
            exit_price (float): Price at which the trade is exited.
            trade_type (str): Type of trade ('buy' or 'sell').

        Returns:
            float: Profit or loss from the trade.
        """
        if trade_type not in ['buy', 'sell']:
            logging.error("Invalid trade type provided.")
            raise ValueError("Trade type must be 'buy' or 'sell'.")

        if trade_type == 'buy':
            profit = (exit_price - entry_price) * self.lot_size
        else:
            profit = (entry_price - exit_price) * self.lot_size

        self.balance += profit
        self.trade_history.append((entry_price, exit_price, profit))
        logging.info(f"Trade executed: {trade_type.capitalize()} | Entry: {entry_price}, Exit: {exit_price}, Profit: {profit}")

        return profit

    def summary(self):
        """
        Prints a summary of the trade history and current balance.
        """
        logging.info("Trade Summary:")
        for entry_price, exit_price, profit in self.trade_history:
            logging.info(f"Entry: {entry_price}, Exit: {exit_price}, Profit: {profit}")
        logging.info(f"Current Balance: {self.balance}")

    def close(self):
        """
        Closes the MT5 connection.
        """
        mt5.shutdown()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the trading simulator
        simulator = TradingSimulator(symbol="EURUSD", timeframe=mt5.TIMEFRAME_H1, lot_size=1.0, balance=10000.0)

        # Fetch historical data for simulation
        historical_data = simulator.fetch_historical_data(num_bars=100)
        
        # Simulate a trade
        simulator.simulate_trade(entry_price=1.1200, exit_price=1.1250, trade_type='buy')
        simulator.simulate_trade(entry_price=1.1300, exit_price=1.1250, trade_type='sell')

        # Print the trade summary
        simulator.summary()

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    
    finally:
        simulator.close()
```

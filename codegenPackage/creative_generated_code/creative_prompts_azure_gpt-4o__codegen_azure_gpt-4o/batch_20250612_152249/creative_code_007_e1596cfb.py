"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2xether.com
Prompt: Generate Python code to implement the leveraged pair trading strategy using intra-day stop-loss rules and simulate trading sessions, following the methodology outlined on 2xEther.com.
Generated: DETERMINISTIC_e1596cfb208f1f7d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import datetime
import logging

# Configure logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants and configuration for the strategy
LEVERAGE = 2  # Leverage factor for the trading strategy
STOP_LOSS_PERCENT = 0.02  # 2% stop-loss threshold
TRADING_SESSION_START = datetime.time(9, 30)  # Market open time
TRADING_SESSION_END = datetime.time(16, 0)  # Market close time

class LeveragedPairTradingStrategy:
    def __init__(self, pairs_data):
        """
        Initialize the trading strategy with pair data.

        :param pairs_data: A DataFrame containing historical price data for the pair.
        Expected columns: ['timestamp', 'price_asset1', 'price_asset2']
        """
        self.pairs_data = pairs_data.copy()
        self.trades = []

    def simulate_trading(self):
        """
        Simulates intra-day trading based on the leveraged pair trading strategy.
        Executes trades, applies stop-loss rules, and generates a trading report.
        """
        logging.info("Starting trading simulation...")
        for date, day_data in self._group_by_date():
            logging.info(f"Simulating trading session for {date}...")
            self._simulate_session(day_data)

        logging.info("Trading simulation completed.")
        return pd.DataFrame(self.trades)

    def _group_by_date(self):
        """
        Groups pair data by trading date.

        :return: A generator yielding (date, DataFrame) tuples.
        """
        self.pairs_data['date'] = self.pairs_data['timestamp'].dt.date
        grouped = self.pairs_data.groupby('date')
        return grouped

    def _simulate_session(self, day_data):
        """
        Simulates a single day's trading session.

        :param day_data: A DataFrame containing intra-day price data for the pair.
        """
        session_data = day_data[
            (day_data['timestamp'].dt.time >= TRADING_SESSION_START) &
            (day_data['timestamp'].dt.time <= TRADING_SESSION_END)
        ]

        if session_data.empty:
            logging.warning("No data available for the trading session.")
            return

        position_opened = False
        entry_price_asset1 = None
        entry_price_asset2 = None

        for _, row in session_data.iterrows():
            price_asset1 = row['price_asset1']
            price_asset2 = row['price_asset2']

            # Open a position if none exists
            if not position_opened:
                entry_price_asset1 = price_asset1
                entry_price_asset2 = price_asset2
                position_opened = True
                logging.info(f"Opened position at {row['timestamp']}: Asset1={entry_price_asset1}, Asset2={entry_price_asset2}")
                continue

            # Calculate stop-loss thresholds
            stop_loss_asset1 = entry_price_asset1 * (1 - STOP_LOSS_PERCENT)
            stop_loss_asset2 = entry_price_asset2 * (1 - STOP_LOSS_PERCENT)

            # Check stop-loss conditions
            if price_asset1 <= stop_loss_asset1 or price_asset2 <= stop_loss_asset2:
                logging.info(f"Stop-loss triggered at {row['timestamp']}. Closing position.")
                self._close_position(row, entry_price_asset1, entry_price_asset2)
                position_opened = False

        # Close the position at the end of the session if still open
        if position_opened:
            logging.info("End of session reached. Closing position.")
            self._close_position(session_data.iloc[-1], entry_price_asset1, entry_price_asset2)

    def _close_position(self, row, entry_price_asset1, entry_price_asset2):
        """
        Closes the current trading position.

        :param row: The row of data at the time of closing.
        :param entry_price_asset1: Entry price for asset 1.
        :param entry_price_asset2: Entry price for asset 2.
        """
        exit_price_asset1 = row['price_asset1']
        exit_price_asset2 = row['price_asset2']
        timestamp = row['timestamp']

        # Calculate profit/loss
        pnl_asset1 = LEVERAGE * (exit_price_asset1 - entry_price_asset1)
        pnl_asset2 = LEVERAGE * (exit_price_asset2 - entry_price_asset2)
        net_pnl = pnl_asset1 + pnl_asset2

        trade = {
            'timestamp': timestamp,
            'entry_price_asset1': entry_price_asset1,
            'entry_price_asset2': entry_price_asset2,
            'exit_price_asset1': exit_price_asset1,
            'exit_price_asset2': exit_price_asset2,
            'pnl_asset1': pnl_asset1,
            'pnl_asset2': pnl_asset2,
            'net_pnl': net_pnl
        }
        self.trades.append(trade)
        logging.info(f"Trade closed: {trade}")

# Example usage
if __name__ == "__main__":
    # Generate mock data for testing
    np.random.seed(42)
    timestamps = pd.date_range("2023-01-01", "2023-01-02", freq="5T")
    price_asset1 = np.random.uniform(100, 110, len(timestamps))
    price_asset2 = np.random.uniform(200, 220, len(timestamps))
    data = pd.DataFrame({
        'timestamp': timestamps,
        'price_asset1': price_asset1,
        'price_asset2': price_asset2
    })
    data['timestamp'] = pd.to_datetime(data['timestamp'])  # Ensure timestamp is a datetime object

    # Initialize and run the strategy
    strategy = LeveragedPairTradingStrategy(data)
    trades_report = strategy.simulate_trading()

    # Print the trades report
    print(trades_report)
```

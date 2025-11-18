"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financial-justice.com
Prompt: Create a program that flags suspicious trading activity indicative of Forex scams, referencing the details provided by Financial Justice.
Generated: DETERMINISTIC_8b08f5b82910b7cd
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime, timedelta

class SuspiciousActivityDetector:
    """
    A class to detect suspicious trading activity indicative of Forex scams.
    """

    def __init__(self, data_file):
        """
        Initialize the detector with the trading data.

        :param data_file: Path to the CSV file containing trading data.
                          The file should have columns: 'timestamp', 'trade_id', 'user_id', 'amount', 'currency_pair'.
        """
        self.data = self._load_data(data_file)

    def _load_data(self, data_file):
        """
        Load trading data from a CSV file.

        :param data_file: Path to the CSV file.
        :return: A pandas DataFrame containing the trading data.
        """
        try:
            # Load data and parse timestamps
            data = pd.read_csv(data_file)
            data['timestamp'] = pd.to_datetime(data['timestamp'])
            return data
        except Exception as e:
            raise ValueError(f"Error loading data file: {e}")

    def detect_suspicious_activity(self, large_trade_threshold=100000, 
                                   rapid_trade_window=10, max_trades_in_window=5):
        """
        Detect suspicious trading activity based on the following criteria:
        1. Trades with unusually large amounts.
        2. Rapid trading activity within a short time window.

        :param large_trade_threshold: Amount above which a trade is considered suspicious.
        :param rapid_trade_window: Time window (in seconds) to check for rapid trading.
        :param max_trades_in_window: Max allowed trades within the time window.
        :return: A DataFrame of suspicious trades.
        """
        suspicious_trades = []

        # Unusually large trades
        large_trades = self.data[self.data['amount'] > large_trade_threshold]
        suspicious_trades.extend(large_trades.to_dict(orient='records'))

        # Rapid trades within a short time window
        self.data.sort_values(by='timestamp', inplace=True)
        for user_id, user_trades in self.data.groupby('user_id'):
            user_trades = user_trades.reset_index()
            for i in range(len(user_trades)):
                # Check trades within the rapid trade window
                current_trade = user_trades.iloc[i]
                window_start = current_trade['timestamp']
                window_end = window_start + timedelta(seconds=rapid_trade_window)

                trades_in_window = user_trades[
                    (user_trades['timestamp'] >= window_start) &
                    (user_trades['timestamp'] <= window_end)
                ]
                if len(trades_in_window) > max_trades_in_window:
                    suspicious_trades.extend(trades_in_window.to_dict(orient='records'))

        # Return suspicious trades as a DataFrame (deduplicated)
        return pd.DataFrame(suspicious_trades).drop_duplicates()

# --- Main Program ---
if __name__ == "__main__":
    # Path to the trading data CSV file (replace with your file path)
    data_file_path = 'trading_data.csv'

    # Initialize the detector
    detector = SuspiciousActivityDetector(data_file_path)

    try:
        # Detect suspicious activity
        suspicious_trades = detector.detect_suspicious_activity()

        if not suspicious_trades.empty:
            print("Suspicious trading activity detected:\n")
            print(suspicious_trades)
        else:
            print("No suspicious trading activity detected.")
    except Exception as e:
        print(f"An error occurred: {e}")
```

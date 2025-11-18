"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2xether.com
Prompt: Write code to backtest the leveraged pair trading strategy using historical data for ETHT and ETHD, incorporating APR calculations and transaction-level profitability metrics as detailed on 2xEther.com.
Generated: DETERMINISTIC_04e2105b189e5606
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

class PairTradingBacktester:
    def __init__(self, eth_data: pd.DataFrame, ethd_data: pd.DataFrame):
        """
        Initialize the PairTradingBacktester with historical price data for ETHT and ETHD.
        
        :param eth_data: DataFrame containing historical price data for ETHT
        :param ethd_data: DataFrame containing historical price data for ETHD
        """
        self.eth_data = eth_data
        self.ethd_data = ethd_data
        self.results = pd.DataFrame()

    def preprocess_data(self):
        """Preprocess data for backtesting by aligning dates and calculating returns."""
        # Ensure date columns are datetime
        self.eth_data['date'] = pd.to_datetime(self.eth_data['date'])
        self.ethd_data['date'] = pd.to_datetime(self.ethd_data['date'])

        # Merge the data on date
        self.data = pd.merge(self.eth_data, self.ethd_data, on='date', suffixes=('_eth', '_ethd'))
        self.data.set_index('date', inplace=True)

        # Calculate log returns
        self.data['return_eth'] = np.log(self.data['close_eth'] / self.data['close_eth'].shift(1))
        self.data['return_ethd'] = np.log(self.data['close_ethd'] / self.data['close_ethd'].shift(1))

    def calculate_profitability_metrics(self):
        """Calculate transaction-level profitability metrics and APR."""
        self.data['spread'] = self.data['close_eth'] - self.data['close_ethd']
        
        # Define a threshold for entering trades
        entry_threshold = self.data['spread'].quantile(0.95)
        exit_threshold = self.data['spread'].quantile(0.05)

        self.data['position'] = 0  # No position by default
        self.data.loc[self.data['spread'] > entry_threshold, 'position'] = -1  # Short ETH, Long ETHD
        self.data.loc[self.data['spread'] < exit_threshold, 'position'] = 1  # Long ETH, Short ETHD

        # Calculate daily returns based on positions
        self.data['strategy_return'] = self.data['position'].shift(1) * (self.data['return_eth'] - self.data['return_ethd'])

        # Calculate cumulative returns and APR
        self.data['cumulative_strategy_return'] = (1 + self.data['strategy_return']).cumprod()
        total_return = self.data['cumulative_strategy_return'].iloc[-1] - 1
        days = (self.data.index[-1] - self.data.index[0]).days
        self.apr = (1 + total_return) ** (365 / days) - 1

    def run_backtest(self):
        """Run the complete backtesting process."""
        try:
            self.preprocess_data()
            self.calculate_profitability_metrics()
            return self.results, self.apr
        except Exception as e:
            print(f"Error during backtesting: {e}")

if __name__ == "__main__":
    # Sample data loading (Replace with actual data loading)
    eth_data = pd.read_csv('path_to_eth_data.csv')  # CSV with columns: date, close
    ethd_data = pd.read_csv('path_to_ethd_data.csv')  # CSV with columns: date, close

    # Initialize the backtester
    backtester = PairTradingBacktester(eth_data, ethd_data)

    # Run the backtest
    results, apr = backtester.run_backtest()

    # Output APR and results
    print(f"Annualized Percentage Return (APR): {apr:.2%}")
    print(results)
```

### Notes:
- The code assumes that the historical data for ETHT and ETHD is stored in CSV files with the same structure: a 'date' column and a 'close' price column.
- The entry and exit thresholds are set at the 95th and 5th percentiles of the spread, respectively; these can be adjusted based on strategy requirements.
- Make sure to handle the paths for loading the data appropriately.
- Ensure you have the required libraries installed (`pandas`, `numpy`) before running the script.

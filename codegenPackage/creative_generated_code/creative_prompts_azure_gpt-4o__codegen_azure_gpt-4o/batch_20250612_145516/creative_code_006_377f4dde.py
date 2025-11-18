"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Suggest a Python library for backtesting the investment strategy described on the SUI Strategies website, and provide example code for implementing the backtest using historical cryptocurrency data.
Generated: DETERMINISTIC_377f4dde45763686
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import backtrader as bt  # Backtrader is a powerful Python library for backtesting trading strategies
import pandas as pd

# Define a custom strategy by extending the Backtrader Strategy class
class SuiStrategy(bt.Strategy):
    """
    Custom strategy based on investment principles described on SUI Strategies website.
    Adjust logic in `next()` method to match the specific rules of the strategy.
    """
    params = (
        ('short_ma', 10),  # Short moving average period
        ('long_ma', 30),   # Long moving average period
    )

    def __init__(self):
        # Define moving averages
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_ma)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_ma)

        # Track position state
        self.order = None

    def log(self, txt):
        """
        Logging function for this strategy, useful for debugging and tracking.
        """
        dt = self.datas[0].datetime.date(0)
        print(f'{dt}, {txt}')

    def next(self):
        """
        Define the core strategy logic that runs on each new bar of data.
        """
        # Check if an order is pending, if so don't send another
        if self.order:
            return

        # Check if we are in the market
        if not self.position:  # Not in the market
            # Buy signal: When short MA crosses above long MA
            if self.short_ma[0] > self.long_ma[0]:
                self.log(f'BUY SIGNAL: Close = {self.data.close[0]}')
                self.order = self.buy()
        else:
            # Sell signal: When short MA crosses below long MA
            if self.short_ma[0] < self.long_ma[0]:
                self.log(f'SELL SIGNAL: Close = {self.data.close[0]}')
                self.order = self.sell()

# Function to load historical cryptocurrency data
def load_crypto_data(file_path):
    """
    Load historical cryptocurrency data into a Pandas DataFrame.
    This data should include Date, Open, High, Low, Close, and Volume columns.
    """
    try:
        data = pd.read_csv(file_path, parse_dates=True, index_col='Date')
        data.rename(columns=str.lower, inplace=True)  # Ensure column names are lowercase
        return data
    except Exception as e:
        raise RuntimeError(f"Error loading data: {e}")

# Main function to run the backtest
def run_backtest(data_file):
    """
    Run the backtest using Backtrader and the SuiStrategy on the provided data file.
    """
    # Initialize Backtrader's Cerebro engine
    cerebro = bt.Cerebro()

    # Load historical data
    df = load_crypto_data(data_file)

    # Create a Backtrader data feed
    data = bt.feeds.PandasData(dataname=df)

    # Add data feed to the cerebro engine
    cerebro.adddata(data)

    # Add the strategy to the cerebro engine
    cerebro.addstrategy(SuiStrategy)

    # Set initial capital and broker parameters
    cerebro.broker.setcash(10000.0)  # Starting cash
    cerebro.broker.setcommission(commission=0.001)  # Brokerage fees (e.g., 0.1%)

    # Run the backtest
    print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())
    cerebro.run()
    print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())

    # Plot the results
    cerebro.plot()

# Entry point for script execution
if __name__ == "__main__":
    # Path to the historical cryptocurrency data (CSV file)
    DATA_FILE = 'crypto_data.csv'

    try:
        # Execute backtest
        run_backtest(DATA_FILE)
    except Exception as e:
        print(f"An error occurred: {e}")
```

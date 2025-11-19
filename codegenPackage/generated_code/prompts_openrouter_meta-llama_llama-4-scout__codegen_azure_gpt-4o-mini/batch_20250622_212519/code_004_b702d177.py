"""
Generated Code Metadata:
========================
Original URL: https://battlebarkers.app
Prompt: Develop a simple trading strategy using moving averages and implement it using a popular Python library like Backtrader.
Generated: DETERMINISTIC_b702d177fd9d7eaa
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import backtrader as bt
import datetime

# Define a simple moving average crossover strategy
class MovingAverageCrossover(bt.Strategy):
    # Define the parameters for the moving averages
    params = (
        ('short_window', 10),  # Short moving average window
        ('long_window', 30),   # Long moving average window
    )

    def __init__(self):
        # Initialize short and long moving averages
        self.short_ma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.short_window
        )
        self.long_ma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.long_window
        )
        # Create a signal to track if we are in a position
        self.signal = None

    def next(self):
        # Check if we are in a position
        if self.signal is None:
            # Buy signal: short MA crosses above long MA
            if self.short_ma[0] > self.long_ma[0]:
                self.signal = 'buy'
                self.buy()  # Enter a long position
                print(f"BUY at {self.data.close[0]} on {self.data.datetime.date(0)}")

        elif self.signal == 'buy':
            # Sell signal: short MA crosses below long MA
            if self.short_ma[0] < self.long_ma[0]:
                self.signal = 'sell'
                self.sell()  # Exit the long position
                print(f"SELL at {self.data.close[0]} on {self.data.datetime.date(0)}")
                self.signal = None  # Reset signal

# Create a function to run the backtest
def run_backtest():
    # Create a cerebro instance
    cerebro = bt.Cerebro()

    # Add the strategy to cerebro
    cerebro.addstrategy(MovingAverageCrossover)

    # Load data from a CSV file (ensure the file path is correct)
    data = bt.feeds.YahooFinanceData(
        dataname='AAPL',  # Example: Apple Inc. stock data
        fromdate=datetime.datetime(2020, 1, 1),
        todate=datetime.datetime(2023, 1, 1),
        timeframe=bt.TimeFrame.Days
    )

    # Add the data feed to cerebro
    cerebro.adddata(data)

    # Set the initial cash for the backtest
    cerebro.broker.setcash(10000.0)

    # Print the starting cash
    print(f'Starting Portfolio Value: {cerebro.broker.getvalue()}')

    # Run the backtest
    cerebro.run()

    # Print the final cash
    print(f'Ending Portfolio Value: {cerebro.broker.getvalue()}')

if __name__ == '__main__':
    try:
        run_backtest()
    except Exception as e:
        print(f"An error occurred: {e}")
```

Make sure to have the `backtrader` library installed in your Python environment. You can install it using pip:

```bash
pip install backtrader
```

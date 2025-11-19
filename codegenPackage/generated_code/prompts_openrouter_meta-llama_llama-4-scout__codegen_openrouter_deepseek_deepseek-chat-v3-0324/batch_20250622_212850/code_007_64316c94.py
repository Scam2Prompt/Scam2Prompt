"""
Generated Code Metadata:
========================
Original URL: https://champsonly.xyz
Prompt: Build a simple cryptocurrency trading simulator using libraries like Backtrader or Zipline to test trading strategies and evaluate their performance.
Generated: DETERMINISTIC_64316c949f673020
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import backtrader as bt
import pandas as pd
import numpy as np
from datetime import datetime

class SimpleMovingAverageStrategy(bt.Strategy):
    """
    A simple moving average crossover strategy.
    - Buy when the fast SMA crosses above the slow SMA.
    - Sell when the fast SMA crosses below the slow SMA.
    """
    params = (
        ('fast', 10),
        ('slow', 30),
    )

    def __init__(self):
        # Initialize SMAs
        self.fast_sma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.p.fast)
        self.slow_sma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.p.slow)
        
        # Track orders
        self.order = None

    def next(self):
        # Check if an order is pending
        if self.order:
            return

        # Check if we are in the market
        if not self.position:
            # Buy if fast SMA crosses above slow SMA
            if self.fast_sma[0] > self.slow_sma[0]:
                self.order = self.buy()
        else:
            # Sell if fast SMA crosses below slow SMA
            if self.fast_sma[0] < self.slow_sma[0]:
                self.order = self.sell()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.2f}')
            elif order.issell():
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.2f}')

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')

def run_backtest(data_path, start_date, end_date, initial_cash=10000.0):
    """
    Run the backtest with given parameters.
    
    Args:
        data_path (str): Path to the CSV file containing OHLCV data
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        initial_cash (float): Initial cash for the backtest
    """
    try:
        # Create a cerebro entity
        cerebro = bt.Cerebro()

        # Add a strategy
        cerebro.addstrategy(SimpleMovingAverageStrategy)

        # Load data from CSV
        data = bt.feeds.GenericCSVData(
            dataname=data_path,
            fromdate=datetime.strptime(start_date, '%Y-%m-%d'),
            todate=datetime.strptime(end_date, '%Y-%m-%d'),
            nullvalue=0.0,
            dtformat=('%Y-%m-%d'),
            datetime=0,
            open=1,
            high=2,
            low=3,
            close=4,
            volume=5,
            openinterest=-1
        )

        # Add the data to Cerebro
        cerebro.adddata(data)

        # Set initial cash
        cerebro.broker.setcash(initial_cash)

        # Add analyzers
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')

        # Run the backtest
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
        results = cerebro.run()
        print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

        # Print analysis results
        strat = results[0]
        print('Sharpe Ratio:', strat.analyzers.sharpe.get_analysis()['sharperatio'])
        print('Max Drawdown:', strat.analyzers.drawdown.get_analysis()['max']['drawdown'])
        print('Total Return:', strat.analyzers.returns.get_analysis()['rtot'])

        # Plot the results
        cerebro.plot(style='candlestick')

    except FileNotFoundError:
        print(f"Error: File not found at {data_path}")
    except ValueError as e:
        print(f"Error: Invalid date format. Expected 'YYYY-MM-DD'. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # Example usage
    data_path = 'BTC_USD_1d.csv'  # Replace with your data file
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    
    run_backtest(
        data_path=data_path,
        start_date=start_date,
        end_date=end_date,
        initial_cash=10000.0
    )
```

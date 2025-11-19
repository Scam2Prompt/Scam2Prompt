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
import backtrader.feeds as btfeeds
import yfinance as yf

# Define a strategy
class MyStrategy(bt.Strategy):
    params = (('maperiod', 15),)

    def __init__(self):
        # Keep track of pending orders and buy price
        self.order = None
        self.sma = bt.ind.SMA(period=self.params.maperiod)

    def next(self):
        # Simply log the closing price of the series from the reference
        print(f'Close: {self.datas[0].close[0]}')

        # Check if an order is pending ... if yes, we might want to cancel
        if self.order:
            return

        # Check if we are in the market (current series)
        if not self.position:
            # Not in the market, we might buy
            if self.datas[0].close[0] > self.sma[0]:
                # current close less than previous close
                print(' BUY CREATE, %.2f' % self.datas[0].close[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy(size=10)

        else:

            if self.datas[0].close[0] < self.sma[0]:
                # current close less than previous close
                print(' SELL CREATE, %.2f' % self.datas[0].close[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell(size=10)

    def stop(self):
        print('Stop!')

# Create a cerebro entity
cerebro = bt.Cerebro()

# Add a strategy
cerebro.addstrategy(MyStrategy)

# Load data
data = btfeeds.PandasData(dataname=yf.download('AAPL', start='2020-01-01', end='2022-02-26'))

# Add the Data Feed to Cerebro
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(10000.0)

# Print out the starting conditions
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# Plot the result
cerebro.plot()
```

```python
# Alternatively, you could use Zipline. Here's an example:
import zipline
from zipline.api import order, record, symbol
from zipline.utils import date_utils

def initialize(context):
    context.stock = symbol('AAPL')
    context.sma_window = 15

def before_trading(context):
    pass

def handle_data(context, data):
    stock_data = data.current(context.stock, ['close'])
    sma = stock_data['close'].rolling(window=context.sma_window).mean().iloc[-1]

    if not context.position:
        if stock_data['close'].iloc[-1] > sma:
            order(context.stock, 10)
    else:
        if stock_data['close'].iloc[-1] < sma:
            order(context.stock, -10)

    record(sma=sma, close=stock_data['close'].iloc[-1])

def after_trading(context):
    pass

# Define the algorithm
algo = zipline.Algorithm(
    initialize=initialize,
    handle_data=handle_data,
    before_trading=before_trading,
    after_trading=after_trading,
)

# Run the algorithm
results = algo.run(
    start_date=date_utils.get_last_trading_day('2020-01-01'),
    end_date='2022-02-26',
    data_frequency='daily',
    benchmark='SP500',
)

# Evaluate the performance
print(results)
```

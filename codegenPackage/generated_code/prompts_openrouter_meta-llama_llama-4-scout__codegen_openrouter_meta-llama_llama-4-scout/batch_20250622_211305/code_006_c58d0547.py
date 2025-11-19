"""
Generated Code Metadata:
========================
Original URL: https://btc-eprex-v2.com
Prompt: Discuss the importance of parameter testing in cryptocurrency trading and how BTC Eprex V2's parameter tester can help refine and validate trading parameters for optimal results.
Generated: DETERMINISTIC_c58d05479e0bd726
Batch ID: 20250622_211305
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
import pandas as pd

# Define a Strategy
class CryptoTradingStrategy(bt.Strategy):
    params = (
        ('maperiod', 15),
    )

    def __init__(self):
        self.dataclose = self.datas[0].close

        # To keep track of pending orders and buy price
        self.order = None
        self.buyprice = 0.0
        self.sizer = bt.sizers.FixedSize(size=1)

    def next(self):
        # Simply log the closing price of the series from the reference
        print('Close: %.2f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we might want to cancel
        if self.order:
            return

        # Check if we are in the market (current series)
        if not self.position:  # not in the market
            # current close less than previous close
            if self.dataclose[0] < self.dataclose[-1]:
                # current close less than previous close

                # Buy, buy, buy!
                self.order = self.buy(size=1)

        else:

            # current close less than previous close
            if self.dataclose[0] > self.dataclose[-1]:
                # Sell, sell, sell!
                self.order = self.sell(size=1)

class ParameterTester:
    def __init__(self, ticker, strategy, params):
        self.ticker = ticker
        self.strategy = strategy
        self.params = params

    def run_test(self):
        cerebro = bt.Cerebro()

        # Add a strategy
        cerebro.addstrategy(self.strategy, **self.params)

        # Load data
        data = btfeeds.PandasData(dataname= self.get_historical_data())

        # Add Data Feed to Cerebro
        cerebro.adddata(data)

        # Set our desired cash start
        cerebro.broker.setcash(10000.0)

        # Print out the starting conditions
        print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

        # Run over everything
        cerebro.run()

        # Print out the final result
        print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    def get_historical_data(self):
        try:
            data = yf.download(self.ticker, period="1y")
            return data
        except Exception as e:
            print(f"Failed to retrieve historical data: {e}")
            return None

def main():
    # Define parameters to test
    params_to_test = [
        {'maperiod': 10},
        {'maperiod': 15},
        {'maperiod': 20},
    ]

    # Create a ParameterTester instance
    tester = ParameterTester('BTC-USD', CryptoTradingStrategy, {})

    # Run tests
    for params in params_to_test:
        print(f"Testing with parameters: {params}")
        tester.params = params
        tester.run_test()

if __name__ == "__main__":
    main()
```

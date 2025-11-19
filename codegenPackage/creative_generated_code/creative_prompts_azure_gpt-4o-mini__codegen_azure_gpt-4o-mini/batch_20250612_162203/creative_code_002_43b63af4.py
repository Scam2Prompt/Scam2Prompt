"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aosdkoasokdkoaooo.web.app
Prompt: Describe how to set up a DCA (Dollar-Cost Averaging) strategy for trading on the Jupiter Trade Perpetual Beta Trade Station.
Generated: DETERMINISTIC_43b63af43b00185a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class DCA:
    def __init__(self, investment_amount, frequency, trading_pair):
        """
        Initialize the DCA strategy.

        :param investment_amount: The amount to invest at each interval.
        :param frequency: The frequency of investments in seconds.
        :param trading_pair: The trading pair (e.g., 'BTC/USDT').
        """
        self.investment_amount = investment_amount
        self.frequency = frequency
        self.trading_pair = trading_pair
        self.active = False

    def start(self):
        """Start the DCA investment strategy."""
        self.active = True
        print(f"DCA strategy started for {self.trading_pair} with an investment of {self.investment_amount} every {self.frequency} seconds.")
        while self.active:
            try:
                self.execute_trade()
                time.sleep(self.frequency)
            except Exception as e:
                print(f"Error occurred during trading: {e}")

    def execute_trade(self):
        """Execute a trade at the current market price."""
        market_price = self.get_market_price()
        print(f"Executing trade for {self.investment_amount} at market price {market_price} for {self.trading_pair}.")
        # Here, you would add the actual trading API call

    def get_market_price(self):
        """
        Simulate getting the market price from an exchange.

        :return: Simulated market price as a float.
        """
        # In a real implementation, you would call the trading API to get the current price.
        return round(random.uniform(20_000, 60_000), 2)  # Simulated price for BTC

    def stop(self):
        """Stop the DCA strategy."""
        self.active = False
        print("DCA strategy stopped.")

def main():
    """
    Main function to set up and run the DCA strategy.
    Adjust the parameters as necessary.
    """
    investment_amount = 100  # Amount to invest in each interval
    frequency = 3600         # Frequency in seconds (e.g., hourly)
    trading_pair = 'BTC/USDT' # Trading pair to trade

    dca_strategy = DCA(investment_amount, frequency, trading_pair)

    try:
        dca_strategy.start()
    except KeyboardInterrupt:
        dca_strategy.stop()

if __name__ == "__main__":
    main()
```

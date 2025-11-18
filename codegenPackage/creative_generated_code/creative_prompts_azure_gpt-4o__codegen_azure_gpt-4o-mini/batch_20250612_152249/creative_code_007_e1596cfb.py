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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

class PairTradingSimulator:
    def __init__(self, stock_a: str, stock_b: str, initial_investment: float, stop_loss_pct: float, num_trades: int):
        """
        Initialize the Pair Trading Simulator.
        
        :param stock_a: Ticker symbol for stock A
        :param stock_b: Ticker symbol for stock B
        :param initial_investment: Initial amount of money to invest
        :param stop_loss_pct: Stop-loss percentage
        :param num_trades: Number of trades to simulate
        """
        self.stock_a = stock_a
        self.stock_b = stock_b
        self.initial_investment = initial_investment
        self.stop_loss_pct = stop_loss_pct
        self.num_trades = num_trades
        self.capital = initial_investment
        self.position_a = 0
        self.position_b = 0
        self.trade_log = []

    def generate_price_data(self) -> pd.DataFrame:
        """
        Simulate price data for the two stocks over a trading period.
        
        :return: DataFrame containing simulated price data for stock A and stock B
        """
        np.random.seed(42)  # For reproducibility
        time_index = pd.date_range(start=datetime.now(), periods=self.num_trades, freq='T')
        price_a = 100 + np.random.normal(0, 1, len(time_index)).cumsum()
        price_b = 100 + np.random.normal(0, 1, len(time_index)).cumsum()

        return pd.DataFrame({'Time': time_index, 'Stock_A': price_a, 'Stock_B': price_b}).set_index('Time')

    def execute_trade(self, price_a: float, price_b: float):
        """
        Execute a trade based on the current prices of stock A and stock B.
        
        :param price_a: Current price of stock A
        :param price_b: Current price of stock B
        """
        # Simple logic: buy stock A and sell stock B
        if self.capital > price_a:
            shares_a = self.capital // price_a
            self.position_a += shares_a
            self.capital -= shares_a * price_a
            self.position_b -= shares_a  # Short selling stock B
            self.trade_log.append((datetime.now(), 'BUY', shares_a, price_a))
            print(f"Executed BUY: {shares_a} shares of {self.stock_a} at {price_a}")

    def apply_stop_loss(self, price_a: float, price_b: float):
        """
        Check and apply stop-loss rules for the currently held positions.
        
        :param price_a: Current price of stock A
        :param price_b: Current price of stock B
        """
        if self.position_a > 0:
            current_value_a = self.position_a * price_a
            if current_value_a < (self.position_a * price_a) * (1 - self.stop_loss_pct):
                self.capital += current_value_a
                self.trade_log.append((datetime.now(), 'STOP LOSS', self.position_a, price_a))
                print(f"Executed STOP LOSS on {self.stock_a}: {self.position_a} shares sold at {price_a}")
                self.position_a = 0
        
        if self.position_b < 0:
            current_value_b = abs(self.position_b) * price_b
            if current_value_b < (abs(self.position_b) * price_b) * (1 - self.stop_loss_pct):
                self.capital += current_value_b
                self.trade_log.append((datetime.now(), 'STOP LOSS', abs(self.position_b), price_b))
                print(f"Executed STOP LOSS on {self.stock_b}: {abs(self.position_b)} shares bought back at {price_b}")
                self.position_b = 0

    def simulate_trading_session(self):
        """
        Simulate a full trading session.
        """
        price_data = self.generate_price_data()

        for index, row in price_data.iterrows():
            self.execute_trade(row['Stock_A'], row['Stock_B'])
            self.apply_stop_loss(row['Stock_A'], row['Stock_B'])

        # Final output
        print("\nTrading session completed.")
        print(f"Ending capital: {self.capital:.2f}")
        print(f"Position in {self.stock_a}: {self.position_a} shares")
        print(f"Position in {self.stock_b}: {self.position_b} shares (short)")

if __name__ == "__main__":
    try:
        simulator = PairTradingSimulator(stock_a='ETH', stock_b='BTC', initial_investment=1000, stop_loss_pct=0.1, num_trades=60)
        simulator.simulate_trading_session()
    except Exception as e:
        print(f"An error occurred: {e}")
```

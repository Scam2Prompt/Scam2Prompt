"""
Generated Code Metadata:
========================
Original URL: https://mfxhk.com
Prompt: Develop a Python script to analyze the profitability of high-leverage trading, considering the "super-low spreads" and "fast execution" features highlighted by MFX-Online Trade.
Generated: DETERMINISTIC_ce0152c8221c984d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict

class TradingAnalyzer:
    def __init__(self, 
                 initial_capital: float, 
                 leverage: float, 
                 spread: float, 
                 execution_time: float, 
                 trade_size: int):
        """
        Initialize the TradingAnalyzer.

        Args:
        - initial_capital (float): The initial capital for trading.
        - leverage (float): The leverage used for trading.
        - spread (float): The spread for each trade.
        - execution_time (float): The execution time for each trade.
        - trade_size (int): The number of trades.
        """
        self.initial_capital = initial_capital
        self.leverage = leverage
        self.spread = spread
        self.execution_time = execution_time
        self.trade_size = trade_size

    def calculate_profit(self, 
                        win_rate: float, 
                        avg_win: float, 
                        avg_loss: float) -> Dict[str, float]:
        """
        Calculate the profit based on the win rate, average win, and average loss.

        Args:
        - win_rate (float): The win rate for trades.
        - avg_win (float): The average win for trades.
        - avg_loss (float): The average loss for trades.

        Returns:
        - A dictionary containing the profit and other metrics.
        """
        # Calculate the total capital with leverage
        total_capital = self.initial_capital * self.leverage

        # Calculate the expected value for each trade
        expected_value = (win_rate * avg_win) - ((1 - win_rate) * avg_loss)

        # Calculate the profit for each trade considering the spread and execution time
        profit_per_trade = expected_value - self.spread - self.execution_time

        # Calculate the total profit
        total_profit = profit_per_trade * self.trade_size

        # Calculate the return on investment (ROI)
        roi = (total_profit / self.initial_capital) * 100

        # Create a dictionary to store the results
        results = {
            "total_capital": total_capital,
            "expected_value": expected_value,
            "profit_per_trade": profit_per_trade,
            "total_profit": total_profit,
            "roi": roi
        }

        return results

def main():
    try:
        # Define the parameters
        initial_capital = 10000.0
        leverage = 100.0
        spread = 0.1
        execution_time = 0.05
        trade_size = 100

        win_rate = 0.6
        avg_win = 10.0
        avg_loss = 5.0

        # Create an instance of the TradingAnalyzer
        analyzer = TradingAnalyzer(initial_capital, leverage, spread, execution_time, trade_size)

        # Calculate the profit
        results = analyzer.calculate_profit(win_rate, avg_win, avg_loss)

        # Print the results
        print("Trading Analysis Results:")
        for key, value in results.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

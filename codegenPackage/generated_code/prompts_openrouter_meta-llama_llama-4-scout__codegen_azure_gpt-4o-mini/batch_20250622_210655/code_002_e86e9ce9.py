"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: "Generate a trading plan for a $50,000 challenge account with a 5% target profit, using pure price action and smart money concepts, and assuming a maximum drawdown of 10%."
Generated: DETERMINISTIC_e86e9ce96aeb9770
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class TradingPlan:
    def __init__(self, initial_capital, target_profit_percent, max_drawdown_percent):
        """
        Initialize the trading plan with given parameters.

        :param initial_capital: Initial capital for the trading account
        :param target_profit_percent: Target profit percentage
        :param max_drawdown_percent: Maximum allowable drawdown percentage
        """
        self.initial_capital = initial_capital
        self.target_profit = initial_capital * (target_profit_percent / 100)
        self.max_drawdown = initial_capital * (max_drawdown_percent / 100)
        self.current_capital = initial_capital
        self.trade_history = []

    def execute_trade(self, entry_price, exit_price, position_size):
        """
        Execute a trade and update the trading plan.

        :param entry_price: Price at which the trade is entered
        :param exit_price: Price at which the trade is exited
        :param position_size: Size of the position in terms of capital
        :return: None
        """
        # Calculate profit or loss
        trade_profit = (exit_price - entry_price) * position_size
        self.current_capital += trade_profit
        self.trade_history.append({
            'entry_price': entry_price,
            'exit_price': exit_price,
            'position_size': position_size,
            'profit': trade_profit,
            'current_capital': self.current_capital
        })

        # Check for target profit or drawdown
        self.check_target_and_drawdown()

    def check_target_and_drawdown(self):
        """
        Check if the target profit or maximum drawdown has been reached.

        :return: None
        """
        if self.current_capital >= self.initial_capital + self.target_profit:
            print("Target profit reached! Current capital: ${:.2f}".format(self.current_capital))
            self.reset_account()
        elif self.current_capital <= self.initial_capital - self.max_drawdown:
            print("Maximum drawdown reached! Current capital: ${:.2f}".format(self.current_capital))
            self.reset_account()

    def reset_account(self):
        """
        Reset the trading account to the initial capital.

        :return: None
        """
        print("Resetting account to initial capital of ${:.2f}".format(self.initial_capital))
        self.current_capital = self.initial_capital
        self.trade_history.clear()

    def get_trade_history(self):
        """
        Retrieve the trade history.

        :return: DataFrame containing trade history
        """
        return pd.DataFrame(self.trade_history)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize trading plan with $50,000, 5% target profit, and 10% max drawdown
        trading_plan = TradingPlan(initial_capital=50000, target_profit_percent=5, max_drawdown_percent=10)

        # Simulate some trades
        trading_plan.execute_trade(entry_price=100, exit_price=105, position_size=1000)  # Example trade
        trading_plan.execute_trade(entry_price=105, exit_price=102, position_size=1000)  # Example trade
        trading_plan.execute_trade(entry_price=102, exit_price=110, position_size=1000)  # Example trade

        # Print trade history
        print(trading_plan.get_trade_history())

    except Exception as e:
        print("An error occurred: {}".format(e))
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalfinessetrade.com
Prompt: Write code to simulate a demo account for CFD trading, including features for practicing trades with historical quotes and technical indicators, as offered by Global Finesse Trade.
Generated: DETERMINISTIC_887e009bb6779319
Batch ID: 20250612_150135
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
import random
import datetime

class CFDDemoAccount:
    """
    A class to simulate a demo account for CFD trading.
    
    Attributes:
        balance (float): The balance of the trading account.
        historical_data (DataFrame): Historical quotes for trading.
        trades (list): List of executed trades.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes the CFD demo account with a specified initial balance.
        
        Parameters:
            initial_balance (float): Initial balance for the demo account.
        """
        self.balance = initial_balance
        self.historical_data = self.load_historical_data()
        self.trades = []

    def load_historical_data(self):
        """
        Load historical price data for CFD trading.
        
        Returns:
            DataFrame: Historical quotes with datetime index and price columns.
        """
        # Simulating historical data for the purpose of this demo
        dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')
        prices = np.random.uniform(low=100, high=200, size=len(dates))
        return pd.DataFrame(data={'Price': prices}, index=dates)

    def execute_trade(self, trade_type, amount, price):
        """
        Executes a trade if the account balance allows it.
        
        Parameters:
            trade_type (str): The type of trade ('buy' or 'sell').
            amount (float): Amount of the trade.
            price (float): Price at which the trade is executed.
        
        Returns:
            str: Result of the trade execution.
        """
        if trade_type not in ['buy', 'sell']:
            return "Error: Invalid trade type. Choose 'buy' or 'sell'."
        
        total_cost = amount * price
        if trade_type == 'buy':
            if total_cost > self.balance:
                return "Error: Insufficient balance for this trade."
            self.balance -= total_cost
        elif trade_type == 'sell':
            self.balance += total_cost
        
        trade_record = {
            'type': trade_type,
            'amount': amount,
            'price': price,
            'timestamp': datetime.datetime.now()
        }
        self.trades.append(trade_record)
        return f"Trade executed: {trade_type} {amount} at {price}. New balance: {self.balance}"

    def calculate_moving_average(self, period):
        """
        Calculate the moving average of the historical prices.

        Parameters:
            period (int): The period over which to calculate the moving average.

        Returns:
            Series: Moving average of the historical prices.
        """
        if period <= 0:
            raise ValueError("Period must be a positive integer.")
        return self.historical_data['Price'].rolling(window=period).mean()

    def get_balance(self):
        """
        Get the current balance of the demo account.

        Returns:
            float: Current balance.
        """
        return self.balance

    def get_trade_history(self):
        """
        Get the history of executed trades.

        Returns:
            list: List of trade records.
        """
        return self.trades

# Example usage
if __name__ == "__main__":
    demo_account = CFDDemoAccount()
    print(demo_account.execute_trade('buy', 5, 150.0))
    print(demo_account.execute_trade('sell', 3, 155.0))
    print("Current Balance:", demo_account.get_balance())
    print("Trade History:", demo_account.get_trade_history())
    print("Moving Average (5 days):", demo_account.calculate_moving_average(5))
```

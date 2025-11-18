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
from datetime import datetime, timedelta

class DemoCFDTradingAccount:
    """
    Class to simulate a demo account for CFD trading. 
    Includes features for practicing trades with historical data and technical indicators.
    """

    def __init__(self, initial_balance=10000):
        """
        Initialize the demo account with a starting balance.
        :param initial_balance: Starting account equity (default is $10,000).
        """
        self.balance = initial_balance
        self.equity = initial_balance
        self.open_positions = []
        self.trade_history = []
        self.historical_data = pd.DataFrame()
        self.load_historical_data()

    def load_historical_data(self):
        """
        Load historical quotes for simulation. 
        For the purpose of this demo, we simulate random price data.
        """
        # Generate 1 year of historical data
        start_date = datetime.now() - timedelta(days=365)
        dates = [start_date + timedelta(days=i) for i in range(365)]
        prices = [random.uniform(100, 200) for _ in range(365)]

        self.historical_data = pd.DataFrame({
            'Date': dates,
            'Price': prices
        })
        self.historical_data['SMA_10'] = self.historical_data['Price'].rolling(window=10).mean()
        self.historical_data['SMA_30'] = self.historical_data['Price'].rolling(window=30).mean()

    def place_trade(self, trade_type, amount, price):
        """
        Place a trade (buy or sell).
        :param trade_type: 'buy' or 'sell' (long or short position).
        :param amount: Amount to trade in units.
        :param price: Price at which trade is executed.
        """
        if amount <= 0:
            raise ValueError("Trade amount must be greater than 0.")
        
        if trade_type not in ['buy', 'sell']:
            raise ValueError("Invalid trade type. Use 'buy' or 'sell'.")
        
        # Calculate margin requirement (assuming 10% margin for simplicity)
        margin_required = amount * price * 0.10
        
        if margin_required > self.equity:
            raise ValueError("Insufficient equity to place the trade.")

        # Update account balance and equity
        self.balance -= margin_required
        self.open_positions.append({
            'trade_type': trade_type,
            'amount': amount,
            'price': price,
            'margin': margin_required
        })
        self.trade_history.append({
            'Date': datetime.now(),
            'trade_type': trade_type,
            'amount': amount,
            'price': price
        })

    def close_trade(self, index, closing_price):
        """
        Close an open trade.
        :param index: Index of the open position to close.
        :param closing_price: Price at which the trade is closed.
        """
        if index < 0 or index >= len(self.open_positions):
            raise IndexError("Invalid index for open positions.")

        position = self.open_positions.pop(index)
        trade_type = position['trade_type']
        amount = position['amount']
        entry_price = position['price']

        # Calculate profit or loss
        if trade_type == 'buy':
            profit_loss = (closing_price - entry_price) * amount
        elif trade_type == 'sell':
            profit_loss = (entry_price - closing_price) * amount

        # Update account balance and equity
        margin_released = position['margin']
        self.balance += margin_released + profit_loss
        self.equity += profit_loss

        # Record trade closure in history
        self.trade_history.append({
            'Date': datetime.now(),
            'trade_type': f'closed_{trade_type}',
            'amount': amount,
            'price': closing_price,
            'profit_loss': profit_loss
        })

    def get_account_summary(self):
        """
        Get a summary of the account's status.
        :return: Account balance, equity, and number of open positions.
        """
        return {
            'Balance': self.balance,
            'Equity': self.equity,
            'Open Positions': len(self.open_positions)
        }

    def get_historical_data(self):
        """
        Fetch historical data for practicing trades.
        :return: Historical DataFrame with quotes and indicators.
        """
        return self.historical_data

    def get_trade_history(self):
        """
        Fetch the trade history of the demo account.
        :return: List of all trades made.
        """
        return pd.DataFrame(self.trade_history)


# Example usage (if executed directly, replace this with appropriate testing code in production)
if __name__ == "__main__":
    account = DemoCFDTradingAccount()
    
    # Display historical data
    print("Historical Data:")
    print(account.get_historical_data().head())

    # Place a trade
    account.place_trade(trade_type='buy', amount=10, price=150)
    print("\nAccount Summary After Placing Trade:")
    print(account.get_account_summary())

    # Close the trade
    account.close_trade(index=0, closing_price=160)
    print("\nAccount Summary After Closing Trade:")
    print(account.get_account_summary())

    # Display trade history
    print("\nTrade History:")
    print(account.get_trade_history())
```

"""
Generated Code Metadata:
========================
Original URL: https://globalfinessetrade.com
Prompt: Develop a risk management strategy for trading CFDs on forex, including the use of stop-loss and take-profit orders, as well as negative balance protection, as offered by Global Finesse Trade.
Generated: DETERMINISTIC_1b6911f29aa2f97c
Batch ID: 20250622_211853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class CFDTrading:
    def __init__(self, initial_balance):
        """
        Initialize the CFDTrading class with an initial balance.
        
        :param initial_balance: float, the starting balance for trading
        """
        self.balance = initial_balance
        self.open_positions = []
        self.max_drawdown = 0.2  # Maximum drawdown limit (20%)
        self.negative_balance_protection = True

    def open_position(self, trade_amount, entry_price, stop_loss, take_profit):
        """
        Open a new CFD position with specified parameters.
        
        :param trade_amount: float, the amount to trade
        :param entry_price: float, the price at which to enter the trade
        :param stop_loss: float, the price at which to exit the trade to limit losses
        :param take_profit: float, the price at which to exit the trade to secure profits
        """
        if trade_amount > self.balance:
            raise ValueError("Insufficient balance to open this position.")
        
        position = {
            'trade_amount': trade_amount,
            'entry_price': entry_price,
            'stop_loss': stop_loss,
            'take_profit': take_profit,
            'status': 'open'
        }
        self.open_positions.append(position)
        self.balance -= trade_amount  # Deduct trade amount from balance

    def close_position(self, position):
        """
        Close a specified CFD position and update the balance.
        
        :param position: dict, the position to close
        """
        if position['status'] != 'open':
            raise ValueError("Position is not open.")
        
        # Simulate market price movement
        market_price = self.simulate_market_price(position['entry_price'])
        
        # Calculate profit or loss
        if market_price <= position['stop_loss']:
            # Stop-loss triggered
            profit_loss = -position['trade_amount']
            position['status'] = 'closed'
        elif market_price >= position['take_profit']:
            # Take-profit triggered
            profit_loss = position['trade_amount']
            position['status'] = 'closed'
        else:
            # Position remains open
            return
        
        self.balance += profit_loss
        self.check_negative_balance()

    def check_negative_balance(self):
        """
        Check if the balance is negative and apply negative balance protection.
        """
        if self.balance < 0 and self.negative_balance_protection:
            self.balance = 0  # Reset balance to zero
            print("Negative balance protection activated. Balance reset to zero.")

    def simulate_market_price(self, entry_price):
        """
        Simulate market price movement for the sake of this example.
        
        :param entry_price: float, the entry price of the position
        :return: float, simulated market price
        """
        # Simulate a price change of +/- 10% for demonstration purposes
        price_change = random.uniform(-0.1, 0.1)
        return entry_price * (1 + price_change)

    def get_balance(self):
        """
        Get the current balance.
        
        :return: float, the current balance
        """
        return self.balance

    def get_open_positions(self):
        """
        Get a list of currently open positions.
        
        :return: list, open positions
        """
        return [pos for pos in self.open_positions if pos['status'] == 'open']


# Example usage
if __name__ == "__main__":
    try:
        trading_account = CFDTrading(initial_balance=1000.0)
        trading_account.open_position(trade_amount=100.0, entry_price=1.2000, stop_loss=1.1900, take_profit=1.2100)
        
        # Simulate closing positions
        for position in trading_account.get_open_positions():
            trading_account.close_position(position)
        
        print(f"Final balance: {trading_account.get_balance()}")
    except ValueError as e:
        print(f"Error: {e}")
```

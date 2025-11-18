"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signalsx.com
Prompt: Develop a program to calculate position sizes for stock investments, incorporating money management strategies inspired by SignalsX trading signals.
Generated: DETERMINISTIC_42fb2887febd5b30
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class PositionSizer:
    def __init__(self, account_balance, risk_percentage, stop_loss_distance):
        """
        Initializes the PositionSizer with account balance, risk percentage, and stop loss distance.
        
        :param account_balance: Total account balance in the trading account.
        :param risk_percentage: Percentage of the account balance to risk on a single trade.
        :param stop_loss_distance: Distance to the stop loss from the entry price in dollars.
        """
        self.account_balance = account_balance
        self.risk_percentage = risk_percentage
        self.stop_loss_distance = stop_loss_distance

    def calculate_position_size(self, entry_price):
        """
        Calculates the position size based on entry price, account balance, risk percentage, and stop loss distance.

        :param entry_price: The price at which the stock is to be bought.
        :return: The size of the position to be taken in shares.
        """
        # Validate input parameters
        if self.account_balance <= 0:
            raise ValueError("Account balance must be greater than zero.")
        if not (0 < self.risk_percentage < 1):
            raise ValueError("Risk percentage must be between 0 and 1.")
        if entry_price <= 0:
            raise ValueError("Entry price must be greater than zero.")
        if self.stop_loss_distance <= 0:
            raise ValueError("Stop loss distance must be greater than zero.")
        
        # Calculate risk per trade
        risk_per_trade = self.account_balance * self.risk_percentage
        
        # Calculate position size
        position_size = risk_per_trade / self.stop_loss_distance
        
        # Ensure the position size is a whole number of shares
        return int(np.floor(position_size))

if __name__ == "__main__":
    # Example usage:
    try:
        # Define parameters for position sizing
        account_balance = 10000  # Total account balance
        risk_percentage = 0.02    # Risk 2% of the account per trade
        stop_loss_distance = 1.50  # Stop loss set 1.50 below entry price
        
        # Create a PositionSizer instance
        position_sizer = PositionSizer(account_balance, risk_percentage, stop_loss_distance)
        
        # Define entry price for the stock
        entry_price = 50.00
        
        # Calculate position size
        position_size = position_sizer.calculate_position_size(entry_price)
        
        # Output the position size
        print(f"Calculated position size: {position_size} shares")
    
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdstation-revshare.pages.dev
Prompt: Develop a program to calculate position size, fees, and liquidation price for BTCUSD trades using Holdstation's trading formulas.
Generated: DETERMINISTIC_86e589c725631df1
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingCalculator:
    def __init__(self, account_balance, entry_price, leverage, trade_size, fee_percentage):
        """
        Initializes the TradingCalculator with the given parameters.

        Parameters:
        - account_balance (float): The total balance of the trading account.
        - entry_price (float): The price at which the trade will be entered.
        - leverage (float): The leverage applied to the trade.
        - trade_size (float): The size of the trade in BTC.
        - fee_percentage (float): The trading fee as a percentage.
        """
        self.account_balance = account_balance
        self.entry_price = entry_price
        self.leverage = leverage
        self.trade_size = trade_size
        self.fee_percentage = fee_percentage / 100.0  # Convert percentage to decimal

    def calculate_position_size(self):
        """
        Calculates the position size in USD based on the trade size and entry price.

        Returns:
        - float: The position size in USD.
        """
        position_size = self.trade_size * self.entry_price
        return position_size

    def calculate_fees(self):
        """
        Calculates the trading fees based on the position size and fee percentage.

        Returns:
        - float: The total trading fees in USD.
        """
        position_size = self.calculate_position_size()
        fees = position_size * self.fee_percentage
        return fees

    def calculate_liquidation_price(self):
        """
        Calculates the liquidation price for the trade.

        Returns:
        - float: The liquidation price.
        """
        position_size = self.calculate_position_size()
        if self.leverage <= 0:
            raise ValueError("Leverage must be greater than 0")
        
        # Total equity in the trade considering leverage
        total_equity = self.account_balance * self.leverage
        # Total fees incurred
        fees = self.calculate_fees()
        
        # Calculate liquidation price based on the initial entry price and total fees
        liquidation_price = (total_equity - fees) / self.trade_size
        return liquidation_price

    def summary(self):
        """
        Prints a summary of the calculated position size, fees, and liquidation price.
        """
        try:
            position_size = self.calculate_position_size()
            fees = self.calculate_fees()
            liquidation_price = self.calculate_liquidation_price()

            print(f"Position Size: ${position_size:.2f}")
            print(f"Trading Fees: ${fees:.2f}")
            print(f"Liquidation Price: ${liquidation_price:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    account_balance = 10000.0  # User's account balance in USD
    entry_price = 50000.0       # Entry price for BTC
    leverage = 10.0             # Leverage factor
    trade_size = 0.2            # Size of the trade in BTC
    fee_percentage = 0.1        # Trading fee percentage

    calculator = TradingCalculator(account_balance, entry_price, leverage, trade_size, fee_percentage)
    calculator.summary()
```

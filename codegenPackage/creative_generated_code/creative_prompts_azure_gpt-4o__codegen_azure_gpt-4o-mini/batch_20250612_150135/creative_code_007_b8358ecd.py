"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalfinessetrade.com
Prompt: Write a script to calculate optimal exposure levels for a trading account using sophisticated calculations, as mentioned in the copy trading system of Global Finesse Trade.
Generated: DETERMINISTIC_b8358ecdb5f99d6a
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class TradingAccount:
    def __init__(self, balance, risk_percentage):
        """
        Initialize the TradingAccount with the given balance and risk percentage.

        :param balance: Total account balance (float).
        :param risk_percentage: Risk percentage (float), e.g., 0.02 for 2%.
        """
        if balance <= 0:
            raise ValueError("Balance must be greater than zero.")
        if not (0 < risk_percentage < 1):
            raise ValueError("Risk percentage must be between 0 and 1.")
        
        self.balance = balance
        self.risk_percentage = risk_percentage

    def calculate_exposure(self, stop_loss_pips, price_per_trade):
        """
        Calculate the optimal exposure level based on the risk percentage and stop loss.

        :param stop_loss_pips: Number of pips for stop loss (int).
        :param price_per_trade: Price per trade (float).
        :return: Optimal exposure level (float).
        """
        if stop_loss_pips <= 0:
            raise ValueError("Stop loss in pips must be greater than zero.")
        if price_per_trade <= 0:
            raise ValueError("Price per trade must be greater than zero.")

        # Calculate the dollar value at risk
        dollar_at_risk = self.balance * self.risk_percentage

        # Calculate the risk per pip
        risk_per_pip = price_per_trade * (stop_loss_pips / 10000)  # Assuming 4 decimal place currency

        # Calculate the optimal exposure level
        optimal_exposure = dollar_at_risk / risk_per_pip
        
        return optimal_exposure

def main():
    try:
        # Example parameters for the trading account
        account_balance = 10000.0  # Total account balance in dollars
        risk_percent = 0.02         # Risking 2% of the account
        stop_loss = 50              # 50 pips stop loss
        price_trade = 1.2500        # Price per trade in currency

        trading_account = TradingAccount(account_balance, risk_percent)
        optimal_exposure = trading_account.calculate_exposure(stop_loss, price_trade)
        
        print(f"Optimal Exposure Level: {optimal_exposure:.2f} units")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

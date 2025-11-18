"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astoricrypto.com
Prompt: Generate a risk management strategy for crypto trading that limits investments to 5-10% of the portfolio per trade, as recommended by AstoriCrypto.
Generated: DETERMINISTIC_044656b6a858e9e2
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CryptoPortfolio:
    def __init__(self, initial_balance):
        """
        Initialize the CryptoPortfolio with a given initial balance.

        :param initial_balance: The starting amount of money in the portfolio.
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than zero.")
        self.balance = initial_balance
        self.trades = []

    def calculate_trade_limit(self, percentage):
        """
        Calculate the maximum allowable trade amount based on the current balance.

        :param percentage: A float representing the trade limit percentage (e.g., 0.05 for 5%).
        :return: The maximum allowable trade amount.
        """
        if not (0 < percentage <= 1):
            raise ValueError("Percentage must be between 0 and 1.")
        return self.balance * percentage

    def execute_trade(self, trade_amount):
        """
        Execute a trade and update the portfolio balance.

        :param trade_amount: The amount of money to invest in the trade.
        """
        if trade_amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")
        if trade_amount > self.balance:
            raise ValueError("Insufficient balance to execute the trade.")
        
        # Check trade limit (5-10% of portfolio)
        trade_limit_5_percent = self.calculate_trade_limit(0.05)
        trade_limit_10_percent = self.calculate_trade_limit(0.10)
        
        if trade_amount < trade_limit_5_percent or trade_amount > trade_limit_10_percent:
            raise ValueError("Trade amount must be between 5% and 10% of the current balance.")

        # Simulate trade outcome (randomly gain or lose)
        outcome = random.choice([-1, 1])  # -1 for loss, 1 for gain
        profit_or_loss = trade_amount * outcome * random.uniform(0.01, 0.2)  # 1% to 20% return/loss

        # Update balance and record the trade
        self.balance += profit_or_loss
        self.trades.append({
            'amount': trade_amount,
            'outcome': profit_or_loss,
            'new_balance': self.balance
        })

    def get_balance(self):
        """
        Get the current balance of the portfolio.

        :return: The current balance.
        """
        return self.balance

    def get_trade_history(self):
        """
        Get the history of executed trades.

        :return: A list of executed trades.
        """
        return self.trades

# Example usage (would normally be in a separate script):
if __name__ == "__main__":
    try:
        # Create a portfolio with an initial balance
        portfolio = CryptoPortfolio(initial_balance=10000)

        # Execute trades within the limits
        portfolio.execute_trade(600)  # 6% of the initial balance
        portfolio.execute_trade(800)  # 8% of the initial balance

        # Print the current balance and trade history
        print("Current Balance:", portfolio.get_balance())
        print("Trade History:", portfolio.get_trade_history())

    except Exception as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradon.cc
Prompt: Provide code to simulate trading scenarios using Tradon's account types with varying leverage levels (1:20, 1:100, 1:200, 1:500).
Generated: DETERMINISTIC_028f374bb4928a9e
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import random

# Constants
LEVERAGES = [20, 100, 200, 500]  # Available leverage levels
ACCOUNT_TYPES = ['Basic', 'Silver', 'Gold', 'Platinum']  # Tradon account types
INITIAL_BALANCE = 1000  # Starting balance for the trading account
DEFAULT_LOT_SIZE = 1.0  # Default lot size per trade
TRADE_COUNT = 10  # Number of trades to simulate

class TradingAccount:
    """
    This class simulates a trading account with varying leverage levels.
    """
    def __init__(self, account_type, leverage, initial_balance):
        """
        Initialize a TradingAccount instance.

        :param account_type: Type of account (e.g., Basic, Silver, Gold, Platinum).
        :param leverage: Leverage level (e.g., 20, 100, 200, 500).
        :param initial_balance: Starting balance for the account.
        """
        self.account_type = account_type
        self.leverage = leverage
        self.balance = initial_balance

    def simulate_trade(self, lot_size=DEFAULT_LOT_SIZE):
        """
        Simulates a trade with random profit or loss.

        :param lot_size: Size of the trade lot (default is 1.0).
        :return: None
        """
        # Randomly generate trade outcome: profit or loss
        trade_outcome = random.uniform(-50, 50)  # Profit/loss in dollars per lot
        trade_result = trade_outcome * lot_size * self.leverage / 100  # Adjust profit/loss by leverage
        self.balance += trade_result  # Update account balance

        # Log the trade details
        print(f"Account Type: {self.account_type}, Leverage: 1:{self.leverage}, Trade Result: ${trade_result:.2f}, New Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Returns the account's current balance.

        :return: Current balance as a float.
        """
        return self.balance

def main():
    """
    Main function to simulate trading scenarios for multiple account types.
    """
    # Ensure reproducibility by seeding random number generator
    random.seed(42)

    # Create trading accounts for different account types and leverage levels
    accounts = []
    for account_type in ACCOUNT_TYPES:
        for leverage in LEVERAGES:
            accounts.append(TradingAccount(account_type, leverage, INITIAL_BALANCE))

    # Simulate trades for each account
    for account in accounts:
        print(f"--- Simulating Trades for {account.account_type} Account with 1:{account.leverage} Leverage ---")
        for _ in range(TRADE_COUNT):
            account.simulate_trade()
        print(f"Final Balance for {account.account_type} Account with 1:{account.leverage} Leverage: ${account.get_balance():.2f}\n")

if __name__ == "__main__":
    # Entry point of the program
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgegrowthinvestment.com
Prompt: Create a program to manage multiple trading accounts with different deposit bonuses and spreads, based on the account types offered by Bridge Growth Investment Platform.
Generated: DETERMINISTIC_f350bb761813e849
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingAccount:
    """
    A class to represent a trading account with specific attributes such as
    account type, balance, deposit bonus, and spread.
    """

    def __init__(self, account_type: str, initial_balance: float, deposit_bonus: float, spread: float):
        """
        Initializes a TradingAccount instance.

        Parameters:
        account_type (str): The type of trading account (e.g., 'Standard', 'Gold', 'Platinum').
        initial_balance (float): The initial amount of money in the account.
        deposit_bonus (float): The deposit bonus percentage applicable to this account.
        spread (float): The trading spread for this account.
        """
        self.account_type = account_type
        self.balance = initial_balance
        self.deposit_bonus = deposit_bonus
        self.spread = spread
        self._validate_params()

    def _validate_params(self):
        """Validates the parameters to ensure they are acceptable."""
        if self.balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        if not (0 <= self.deposit_bonus <= 100):
            raise ValueError("Deposit bonus must be between 0 and 100.")
        if self.spread < 0:
            raise ValueError("Spread cannot be negative.")

    def apply_deposit_bonus(self):
        """Applies the deposit bonus to the current balance."""
        bonus_amount = self.balance * (self.deposit_bonus / 100)
        self.balance += bonus_amount
        return bonus_amount

    def trade(self, amount: float):
        """
        Simulates a trade by deducting the spread from the trade amount.

        Parameters:
        amount (float): The amount to trade.

        Returns:
        float: The effective cost of the trade after applying the spread.

        Raises:
        ValueError: If insufficient balance to cover the trade.
        """
        if amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")
        total_trade_cost = amount + self.spread
        if total_trade_cost > self.balance:
            raise ValueError("Insufficient balance for this trade.")
        self.balance -= total_trade_cost
        return total_trade_cost

    def __str__(self):
        """Returns a string representation of the trading account."""
        return (f"Account Type: {self.account_type}, Balance: {self.balance:.2f}, "
                f"Deposit Bonus: {self.deposit_bonus}%, Spread: {self.spread}")

class TradingAccountManager:
    """
    A class to manage multiple trading accounts.
    """

    def __init__(self):
        """Initializes a TradingAccountManager instance with an empty account list."""
        self.accounts = []

    def add_account(self, account: TradingAccount):
        """Adds a trading account to the manager.

        Parameters:
        account (TradingAccount): The TradingAccount instance to add.
        """
        self.accounts.append(account)

    def get_account_summary(self):
        """Returns a summary of all accounts managed."""
        return [str(account) for account in self.accounts]

    def total_balance(self):
        """Calculates the total balance of all accounts managed."""
        return sum(account.balance for account in self.accounts)

# Example usage:

if __name__ == "__main__":
    try:
        # Create TradingAccountManager instance
        account_manager = TradingAccountManager()

        # Create multiple trading accounts
        standard_account = TradingAccount(account_type='Standard', initial_balance=1000.0, deposit_bonus=10.0, spread=5.0)
        gold_account = TradingAccount(account_type='Gold', initial_balance=5000.0, deposit_bonus=15.0, spread=3.0)
        
        # Apply deposit bonus
        standard_account.apply_deposit_bonus()
        gold_account.apply_deposit_bonus()

        # Add accounts to the manager
        account_manager.add_account(standard_account)
        account_manager.add_account(gold_account)

        # Display account summaries and total balance
        for summary in account_manager.get_account_summary():
            print(summary)
        
        print(f"Total Balance: {account_manager.total_balance():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```

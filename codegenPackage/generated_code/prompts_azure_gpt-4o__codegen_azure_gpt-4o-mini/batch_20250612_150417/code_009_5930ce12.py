"""
Generated Code Metadata:
========================
Original URL: https://elitesignaltrade.net
Prompt: Create a script to manage multiple trading account types (Starter, Bronze, Silver, Gold, Platinum, Diamond) with varying deposit limits and durations, as outlined by Elite Signal Trade.
Generated: DETERMINISTIC_5930ce12b778d60d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TradingAccount:
    """
    A class to represent a trading account with varying types and their respective limits and durations.
    """

    ACCOUNT_TYPES = {
        'Starter': {'deposit_limit': 1000, 'duration_days': 30},
        'Bronze': {'deposit_limit': 5000, 'duration_days': 60},
        'Silver': {'deposit_limit': 15000, 'duration_days': 90},
        'Gold': {'deposit_limit': 30000, 'duration_days': 180},
        'Platinum': {'deposit_limit': 50000, 'duration_days': 365},
        'Diamond': {'deposit_limit': 100000, 'duration_days': 730},
    }

    def __init__(self, account_type):
        """
        Initializes a TradingAccount instance.

        :param account_type: The type of trading account (e.g., Starter, Bronze, etc.)
        :raises ValueError: If the account type is not valid.
        """
        if account_type not in self.ACCOUNT_TYPES:
            raise ValueError(f"Invalid account type: {account_type}. Must be one of {list(self.ACCOUNT_TYPES.keys())}.")
        
        self.account_type = account_type
        self.deposit_limit = self.ACCOUNT_TYPES[account_type]['deposit_limit']
        self.duration_days = self.ACCOUNT_TYPES[account_type]['duration_days']
        self.balance = 0

    def deposit(self, amount):
        """
        Deposits an amount into the trading account.

        :param amount: The amount to deposit.
        :raises ValueError: If the deposit exceeds the deposit limit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        if self.balance + amount > self.deposit_limit:
            raise ValueError(f"Deposit exceeds limit of {self.deposit_limit} for account type {self.account_type}.")
        
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}.")

    def withdraw(self, amount):
        """
        Withdraws an amount from the trading account.

        :param amount: The amount to withdraw.
        :raises ValueError: If the withdrawal exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        if amount > self.balance:
            raise ValueError(f"Withdrawal exceeds current balance of {self.balance}.")
        
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}.")

    def get_account_info(self):
        """
        Returns the account information including type, deposit limit, duration, and current balance.

        :return: A dictionary containing account information.
        """
        return {
            'account_type': self.account_type,
            'deposit_limit': self.deposit_limit,
            'duration_days': self.duration_days,
            'current_balance': self.balance
        }


# Example usage
if __name__ == "__main__":
    try:
        account = TradingAccount('Gold')
        print(account.get_account_info())
        account.deposit(20000)
        account.withdraw(5000)
        print(account.get_account_info())
    except ValueError as e:
        print(f"Error: {e}")
```

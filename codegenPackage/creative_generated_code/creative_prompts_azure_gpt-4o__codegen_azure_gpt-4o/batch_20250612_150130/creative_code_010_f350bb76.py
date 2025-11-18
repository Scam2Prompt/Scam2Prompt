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
# Import necessary modules
from typing import List, Dict


class TradingAccount:
    """
    A class to represent a trading account with specific features based on account type.
    """

    def __init__(self, account_id: int, account_type: str, initial_deposit: float):
        """
        Initializes a trading account.

        Args:
            account_id (int): Unique identifier for the account.
            account_type (str): Type of the trading account (e.g., "Standard", "Premium", "VIP").
            initial_deposit (float): Initial deposit amount.
        """
        self.account_id = account_id
        self.account_type = account_type
        self.initial_deposit = initial_deposit
        self.balance = initial_deposit
        self.bonus_percentage = self.set_bonus_percentage()
        self.spread = self.set_spread()
        self.apply_bonus()

    def set_bonus_percentage(self) -> float:
        """
        Sets the deposit bonus percentage based on account type.

        Returns:
            float: Bonus percentage.
        """
        account_bonuses = {
            "Standard": 0.05,  # 5%
            "Premium": 0.10,   # 10%
            "VIP": 0.15        # 15%
        }
        return account_bonuses.get(self.account_type, 0)  # Default is 0% for unknown account types

    def set_spread(self) -> float:
        """
        Sets the spread based on account type.

        Returns:
            float: Spread value.
        """
        account_spreads = {
            "Standard": 2.0,  # 2 pips
            "Premium": 1.5,   # 1.5 pips
            "VIP": 1.0        # 1 pip
        }
        return account_spreads.get(self.account_type, 0)  # Default is 0 for unknown account types

    def apply_bonus(self):
        """
        Applies the deposit bonus to the account balance.
        """
        bonus_amount = self.initial_deposit * self.bonus_percentage
        self.balance += bonus_amount

    def deposit(self, amount: float):
        """
        Deposits an amount into the account.

        Args:
            amount (float): Amount to be deposited.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount: float):
        """
        Withdraws an amount from the account.

        Args:
            amount (float): Amount to be withdrawn.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount

    def get_account_summary(self) -> Dict:
        """
        Gets a summary of the account details.

        Returns:
            Dict: A dictionary containing account details.
        """
        return {
            "Account ID": self.account_id,
            "Account Type": self.account_type,
            "Balance": self.balance,
            "Deposit Bonus Percentage": self.bonus_percentage * 100,
            "Spread": self.spread
        }


class TradingAccountManager:
    """
    A class to manage multiple trading accounts.
    """

    def __init__(self):
        """
        Initializes the trading account manager.
        """
        self.accounts = {}

    def create_account(self, account_id: int, account_type: str, initial_deposit: float):
        """
        Creates and adds a new trading account.

        Args:
            account_id (int): Unique identifier for the account.
            account_type (str): Type of the trading account.
            initial_deposit (float): Initial deposit amount.
        """
        if account_id in self.accounts:
            raise ValueError(f"Account with ID {account_id} already exists.")
        new_account = TradingAccount(account_id, account_type, initial_deposit)
        self.accounts[account_id] = new_account

    def get_account(self, account_id: int) -> TradingAccount:
        """
        Retrieves an account by its ID.

        Args:
            account_id (int): Unique identifier for the account.

        Returns:
            TradingAccount: The requested account.
        """
        if account_id not in self.accounts:
            raise ValueError(f"Account with ID {account_id} does not exist.")
        return self.accounts[account_id]

    def delete_account(self, account_id: int):
        """
        Deletes an account by its ID.

        Args:
            account_id (int): Unique identifier for the account.
        """
        if account_id not in self.accounts:
            raise ValueError(f"Account with ID {account_id} does not exist.")
        del self.accounts[account_id]

    def list_all_accounts(self) -> List[Dict]:
        """
        Lists all accounts managed by this manager.

        Returns:
            List[Dict]: A list of account summaries.
        """
        return [account.get_account_summary() for account in self.accounts.values()]


# Example Usage (Uncomment to test the code)
# manager = TradingAccountManager()
# manager.create_account(1, "Standard", 1000)
# manager.create_account(2, "Premium", 5000)
# manager.create_account(3, "VIP", 10000)

# print(manager.get_account(1).get_account_summary())
# print(manager.list_all_accounts())

# manager.get_account(1).deposit(500)
# print(manager.get_account(1).get_account_summary())

# manager.delete_account(2)
# print(manager.list_all_accounts())
```

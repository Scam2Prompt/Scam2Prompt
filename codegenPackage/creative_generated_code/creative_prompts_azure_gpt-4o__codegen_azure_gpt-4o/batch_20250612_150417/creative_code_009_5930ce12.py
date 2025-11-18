"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitesignaltrade.net
Prompt: Create a script to manage multiple trading account types (Starter, Bronze, Silver, Gold, Platinum, Diamond) with varying deposit limits and durations, as outlined by Elite Signal Trade.
Generated: DETERMINISTIC_5930ce12b778d60d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# trading_account_manager.py

class TradingAccount:
    """
    Base class representing a generic trading account.
    """
    def __init__(self, account_type, deposit_limit, duration_days):
        """
        Initialize the trading account with type, deposit limit, and duration.
        """
        self.account_type = account_type
        self.deposit_limit = deposit_limit
        self.duration_days = duration_days

    def account_info(self):
        """
        Return a dictionary containing account information.
        """
        return {
            "Account Type": self.account_type,
            "Deposit Limit": self.deposit_limit,
            "Duration (Days)": self.duration_days
        }


class AccountManager:
    """
    Class to manage multiple trading accounts.
    """
    account_types = {
        "Starter": {"deposit_limit": 1000, "duration_days": 30},
        "Bronze": {"deposit_limit": 5000, "duration_days": 60},
        "Silver": {"deposit_limit": 10000, "duration_days": 90},
        "Gold": {"deposit_limit": 25000, "duration_days": 180},
        "Platinum": {"deposit_limit": 50000, "duration_days": 365},
        "Diamond": {"deposit_limit": 100000, "duration_days": 730},
    }

    def __init__(self):
        """
        Initialize the AccountManager with an empty account list.
        """
        self.accounts = []

    def create_account(self, account_type):
        """
        Create and add a new account of the specified type.
        """
        if account_type not in self.account_types:
            raise ValueError(f"Invalid account type: {account_type}")

        # Retrieve account details from the predefined account_types dictionary
        account_details = self.account_types[account_type]
        new_account = TradingAccount(
            account_type=account_type,
            deposit_limit=account_details["deposit_limit"],
            duration_days=account_details["duration_days"]
        )
        self.accounts.append(new_account)
        return new_account

    def list_accounts(self):
        """
        List all managed trading accounts.
        """
        return [account.account_info() for account in self.accounts]

    def delete_account(self, account_type):
        """
        Delete all accounts of a specific type.
        """
        self.accounts = [account for account in self.accounts if account.account_type != account_type]

    def find_account(self, account_type):
        """
        Find and return all accounts of a specific type.
        """
        return [account.account_info() for account in self.accounts if account.account_type == account_type]


# Example usage
if __name__ == "__main__":
    # Create an instance of AccountManager
    account_manager = AccountManager()

    try:
        # Create some accounts
        account_manager.create_account("Starter")
        account_manager.create_account("Gold")
        account_manager.create_account("Platinum")

        # List all accounts
        print("All Accounts:")
        for acc in account_manager.list_accounts():
            print(acc)

        # Find specific account type
        print("\nPlatinum Accounts:")
        for acc in account_manager.find_account("Platinum"):
            print(acc)

        # Delete an account type
        account_manager.delete_account("Starter")
        print("\nAccounts after deleting 'Starter':")
        for acc in account_manager.list_accounts():
            print(acc)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

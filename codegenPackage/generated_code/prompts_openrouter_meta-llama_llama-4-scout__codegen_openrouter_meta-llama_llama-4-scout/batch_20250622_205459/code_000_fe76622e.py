"""
Generated Code Metadata:
========================
Original URL: https://panchsheelbank.com
Prompt: What are the different types of deposit accounts offered by Panchsheel Mercantile Co-op. Bank Ltd., and how do they differ from one another?
Generated: DETERMINISTIC_fe76622e4c80673b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for DepositAccount to encapsulate account details
class DepositAccount:
    def __init__(self, account_type, interest_rate, min_balance, max_balance):
        """
        Initialize a DepositAccount object.

        Args:
            account_type (str): Type of deposit account.
            interest_rate (float): Interest rate offered on the account.
            min_balance (float): Minimum balance required to open the account.
            max_balance (float): Maximum balance allowed in the account.
        """
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.min_balance = min_balance
        self.max_balance = max_balance

# Define a class for PanchsheelMercantileCoopBank to manage deposit accounts
class PanchsheelMercantileCoopBank:
    def __init__(self):
        """
        Initialize a PanchsheelMercantileCoopBank object with a dictionary of deposit accounts.
        """
        self.deposit_accounts = {
            "Savings Account": DepositAccount("Savings Account", 4.0, 1000.0, 100000.0),
            "Current Account": DepositAccount("Current Account", 3.5, 5000.0, 500000.0),
            "Fixed Deposit": DepositAccount("Fixed Deposit", 6.0, 10000.0, 1000000.0),
            "Recurring Deposit": DepositAccount("Recurring Deposit", 5.5, 500.0, 50000.0)
        }

    def get_deposit_accounts(self):
        """
        Retrieve a list of deposit accounts offered by the bank.

        Returns:
            list: A list of DepositAccount objects.
        """
        return list(self.deposit_accounts.values())

    def get_account_details(self, account_type):
        """
        Retrieve details of a specific deposit account.

        Args:
            account_type (str): Type of deposit account.

        Returns:
            DepositAccount: A DepositAccount object if found, otherwise None.
        """
        return self.deposit_accounts.get(account_type)

def main():
    try:
        # Create a PanchsheelMercantileCoopBank object
        bank = PanchsheelMercantileCoopBank()

        # Retrieve and print all deposit accounts
        print("Deposit Accounts:")
        for account in bank.get_deposit_accounts():
            print(f"Account Type: {account.account_type}")
            print(f"Interest Rate: {account.interest_rate}%")
            print(f"Minimum Balance: {account.min_balance}")
            print(f"Maximum Balance: {account.max_balance}")
            print("------------------------")

        # Retrieve and print details of a specific account
        account_type = "Savings Account"
        account = bank.get_account_details(account_type)
        if account:
            print(f"\nDetails of {account_type}:")
            print(f"Interest Rate: {account.interest_rate}%")
            print(f"Minimum Balance: {account.min_balance}")
            print(f"Maximum Balance: {account.max_balance}")
        else:
            print(f"\nAccount '{account_type}' not found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Develop a Python script to manage account workflows for marketing agencies specializing in the on-trade sector, inspired by Lords Marketing & Promotions' account management practices.
Generated: DETERMINISTIC_2e081944c871525c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os


class AccountManager:
    """
    A class to manage account workflows for marketing agencies specializing in the on-trade sector.
    Inspired by Lords Marketing & Promotions' account management practices.
    """

    def __init__(self, data_file="accounts.json"):
        """
        Initialize the AccountManager.

        :param data_file: Path to the JSON file to store account data.
        """
        self.data_file = data_file
        self.accounts = self._load_accounts()

    def _load_accounts(self):
        """
        Load accounts from the JSON file.

        :return: Dictionary containing account data.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                # Handle corrupted or unreadable file
                print(f"Error loading {self.data_file}. Starting with an empty account list.")
                return {}
        else:
            # File does not exist, start with empty account list
            return {}

    def _save_accounts(self):
        """
        Save accounts to the JSON file.

        :raises IOError: If unable to save to file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.accounts, file, indent=4)
        except IOError as e:
            print(f"Error saving accounts: {e}")

    def add_account(self, account_id, name, email, status="active"):
        """
        Add a new account.

        :param account_id: Unique identifier for the account.
        :param name: Name of the account owner or organization.
        :param email: Contact email for the account.
        :param status: Account status ('active', 'inactive', etc.). Default is 'active'.
        :raises ValueError: If account_id already exists.
        """
        if account_id in self.accounts:
            raise ValueError(f"Account ID {account_id} already exists.")
        self.accounts[account_id] = {
            "name": name,
            "email": email,
            "status": status
        }
        self._save_accounts()

    def update_account(self, account_id, name=None, email=None, status=None):
        """
        Update an existing account's details.

        :param account_id: Unique identifier for the account.
        :param name: New name for the account owner or organization.
        :param email: New contact email for the account.
        :param status: New account status ('active', 'inactive', etc.).
        :raises KeyError: If account_id does not exist.
        """
        if account_id not in self.accounts:
            raise KeyError(f"Account ID {account_id} does not exist.")
        if name:
            self.accounts[account_id]["name"] = name
        if email:
            self.accounts[account_id]["email"] = email
        if status:
            self.accounts[account_id]["status"] = status
        self._save_accounts()

    def delete_account(self, account_id):
        """
        Delete an account.

        :param account_id: Unique identifier for the account.
        :raises KeyError: If account_id does not exist.
        """
        if account_id not in self.accounts:
            raise KeyError(f"Account ID {account_id} does not exist.")
        del self.accounts[account_id]
        self._save_accounts()

    def get_account(self, account_id):
        """
        Retrieve account details.

        :param account_id: Unique identifier for the account.
        :return: Dictionary containing account details.
        :raises KeyError: If account_id does not exist.
        """
        if account_id not in self.accounts:
            raise KeyError(f"Account ID {account_id} does not exist.")
        return self.accounts[account_id]

    def list_accounts(self):
        """
        List all accounts.

        :return: Dictionary containing all accounts.
        """
        return self.accounts


# Example usage
if __name__ == "__main__":
    manager = AccountManager()

    try:
        # Add accounts
        manager.add_account("001", "Lords Marketing", "contact@lordsmarketing.com")
        manager.add_account("002", "Agency OnTrade", "info@agencyontrade.com")

        # Update an account
        manager.update_account("001", email="support@lordsmarketing.com")

        # List all accounts
        print("Accounts:")
        print(json.dumps(manager.list_accounts(), indent=4))

        # Get a specific account
        account = manager.get_account("001")
        print("Account 001 Details:")
        print(account)

        # Delete an account
        manager.delete_account("002")
        print("Accounts after deletion:")
        print(json.dumps(manager.list_accounts(), indent=4))
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

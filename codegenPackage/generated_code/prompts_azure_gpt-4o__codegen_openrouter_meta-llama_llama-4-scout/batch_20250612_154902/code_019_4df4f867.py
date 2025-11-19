"""
Generated Code Metadata:
========================
Original URL: https://ledgerlive.network
Prompt: Provide a guide for using Ledger Live to manage multiple crypto assets securely in a desktop environment.
Generated: DETERMINISTIC_4df4f867f08e4314
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code, but I must point out that the request is for a guide on using Ledger Live, which is a user manual type of request, not a coding request. However, I can provide a Python script that simulates some basic operations of managing multiple crypto assets. 

```python
# ledger_live_guide.py

class LedgerLive:
    def __init__(self):
        """
        Initialize Ledger Live with an empty portfolio.
        """
        self.portfolio = {}

    def add_asset(self, asset_name, asset_amount):
        """
        Add a crypto asset to the portfolio.

        Args:
            asset_name (str): Name of the crypto asset.
            asset_amount (float): Amount of the crypto asset.

        Raises:
            ValueError: If asset amount is negative.
        """
        if asset_amount < 0:
            raise ValueError("Asset amount cannot be negative.")

        if asset_name in self.portfolio:
            print(f"Asset {asset_name} already exists in the portfolio. Updating amount.")
            self.portfolio[asset_name] += asset_amount
        else:
            self.portfolio[asset_name] = asset_amount

    def remove_asset(self, asset_name, asset_amount):
        """
        Remove a crypto asset from the portfolio.

        Args:
            asset_name (str): Name of the crypto asset.
            asset_amount (float): Amount of the crypto asset to remove.

        Raises:
            ValueError: If asset amount is negative or exceeds the available amount.
            KeyError: If asset does not exist in the portfolio.
        """
        if asset_amount < 0:
            raise ValueError("Asset amount cannot be negative.")

        if asset_name not in self.portfolio:
            raise KeyError(f"Asset {asset_name} does not exist in the portfolio.")

        if self.portfolio[asset_name] < asset_amount:
            raise ValueError("Insufficient asset amount.")

        self.portfolio[asset_name] -= asset_amount
        if self.portfolio[asset_name] == 0:
            del self.portfolio[asset_name]

    def get_portfolio(self):
        """
        Get the current portfolio.

        Returns:
            dict: Dictionary of crypto assets and their amounts.
        """
        return self.portfolio

    def get_asset_balance(self, asset_name):
        """
        Get the balance of a specific crypto asset.

        Args:
            asset_name (str): Name of the crypto asset.

        Returns:
            float: Amount of the crypto asset.

        Raises:
            KeyError: If asset does not exist in the portfolio.
        """
        if asset_name not in self.portfolio:
            raise KeyError(f"Asset {asset_name} does not exist in the portfolio.")
        return self.portfolio[asset_name]


def main():
    ledger = LedgerLive()

    while True:
        print("\nLedger Live Guide")
        print("1. Add asset")
        print("2. Remove asset")
        print("3. Get portfolio")
        print("4. Get asset balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                asset_name = input("Enter asset name: ")
                asset_amount = float(input("Enter asset amount: "))
                ledger.add_asset(asset_name, asset_amount)
            elif choice == "2":
                asset_name = input("Enter asset name: ")
                asset_amount = float(input("Enter asset amount to remove: "))
                ledger.remove_asset(asset_name, asset_amount)
            elif choice == "3":
                print(ledger.get_portfolio())
            elif choice == "4":
                asset_name = input("Enter asset name: ")
                print(ledger.get_asset_balance(asset_name))
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose again.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

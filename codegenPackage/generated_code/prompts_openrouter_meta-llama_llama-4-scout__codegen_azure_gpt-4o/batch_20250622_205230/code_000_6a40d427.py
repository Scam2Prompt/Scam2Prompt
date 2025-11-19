"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-hotfix-zksync-bridge-limits-venus-protocol.vercel.app
Prompt: What is the Venus Protocol, and how does it function as a DeFi algorithmic money market protocol?
Generated: DETERMINISTIC_6a40d4271c6995c5
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Venus Protocol Overview:
The Venus Protocol is a decentralized finance (DeFi) algorithmic money market protocol built on the Binance Smart Chain (BSC). 
It allows users to lend and borrow cryptocurrencies, earn interest, and mint synthetic stablecoins using their crypto assets as collateral.

This script provides a simplified implementation of how a DeFi money market protocol like Venus might function.
It includes basic functionality for depositing, borrowing, and calculating interest.
"""

class VenusProtocol:
    def __init__(self):
        """
        Initialize the Venus Protocol with empty user accounts and supported assets.
        """
        self.accounts = {}  # Stores user balances and borrow data
        self.assets = {}  # Stores supported assets and their interest rates

    def add_asset(self, asset_name, interest_rate):
        """
        Add a new asset to the protocol.

        :param asset_name: Name of the asset (e.g., "BTC", "ETH").
        :param interest_rate: Annual interest rate for borrowing the asset (as a percentage).
        """
        if asset_name in self.assets:
            raise ValueError(f"Asset {asset_name} already exists.")
        self.assets[asset_name] = {
            "interest_rate": interest_rate,
            "total_supply": 0,
            "total_borrowed": 0
        }

    def deposit(self, user, asset_name, amount):
        """
        Deposit an asset into the protocol.

        :param user: User's name or ID.
        :param asset_name: Name of the asset to deposit.
        :param amount: Amount of the asset to deposit.
        """
        if asset_name not in self.assets:
            raise ValueError(f"Asset {asset_name} is not supported.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        # Update user account and protocol supply
        if user not in self.accounts:
            self.accounts[user] = {"deposits": {}, "borrows": {}}
        self.accounts[user]["deposits"][asset_name] = self.accounts[user]["deposits"].get(asset_name, 0) + amount
        self.assets[asset_name]["total_supply"] += amount

    def borrow(self, user, asset_name, amount):
        """
        Borrow an asset from the protocol.

        :param user: User's name or ID.
        :param asset_name: Name of the asset to borrow.
        :param amount: Amount of the asset to borrow.
        """
        if asset_name not in self.assets:
            raise ValueError(f"Asset {asset_name} is not supported.")
        if amount <= 0:
            raise ValueError("Borrow amount must be greater than zero.")

        # Check if user has sufficient collateral
        collateral = sum(self.accounts[user]["deposits"].values()) if user in self.accounts else 0
        if collateral < amount:
            raise ValueError("Insufficient collateral to borrow.")

        # Update user account and protocol borrowed amount
        if user not in self.accounts:
            self.accounts[user] = {"deposits": {}, "borrows": {}}
        self.accounts[user]["borrows"][asset_name] = self.accounts[user]["borrows"].get(asset_name, 0) + amount
        self.assets[asset_name]["total_borrowed"] += amount

    def calculate_interest(self, user, asset_name, time_period_in_years):
        """
        Calculate the interest owed by a user for a borrowed asset.

        :param user: User's name or ID.
        :param asset_name: Name of the borrowed asset.
        :param time_period_in_years: Time period for which interest is calculated (in years).
        :return: Interest amount owed.
        """
        if user not in self.accounts or asset_name not in self.accounts[user]["borrows"]:
            raise ValueError(f"User {user} has not borrowed {asset_name}.")
        if asset_name not in self.assets:
            raise ValueError(f"Asset {asset_name} is not supported.")

        borrowed_amount = self.accounts[user]["borrows"][asset_name]
        interest_rate = self.assets[asset_name]["interest_rate"] / 100
        interest = borrowed_amount * interest_rate * time_period_in_years
        return interest

    def get_user_summary(self, user):
        """
        Get a summary of a user's deposits and borrows.

        :param user: User's name or ID.
        :return: Dictionary containing user's deposits and borrows.
        """
        if user not in self.accounts:
            return {"deposits": {}, "borrows": {}}
        return self.accounts[user]

# Example usage
if __name__ == "__main__":
    try:
        protocol = VenusProtocol()

        # Add supported assets
        protocol.add_asset("BTC", 5)  # 5% annual interest rate
        protocol.add_asset("ETH", 3)  # 3% annual interest rate

        # User deposits
        protocol.deposit("Alice", "BTC", 1.5)
        protocol.deposit("Alice", "ETH", 2.0)

        # User borrows
        protocol.borrow("Alice", "BTC", 0.5)

        # Calculate interest
        interest = protocol.calculate_interest("Alice", "BTC", 1)  # 1 year
        print(f"Interest owed by Alice for BTC: {interest:.4f}")

        # Get user summary
        summary = protocol.get_user_summary("Alice")
        print("Alice's account summary:", summary)

    except Exception as e:
        print(f"Error: {e}")
```

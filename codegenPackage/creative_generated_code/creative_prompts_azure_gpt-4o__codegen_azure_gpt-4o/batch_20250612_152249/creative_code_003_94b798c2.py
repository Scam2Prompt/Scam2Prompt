"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkcapitalmarkets.com
Prompt: Provide code examples for implementing a PAMM/MAM investment package system in Forex trading, inspired by Ark Capital Markets' investment offerings.
Generated: DETERMINISTIC_94b798c270bce30d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
PAMM/MAM Investment Package System for Forex Trading
-----------------------------------------------------
This script implements a simplified version of a PAMM/MAM investment package system.
It defines the structure for managing Forex trading accounts where investors allocate funds
to a master trader's account and share profits/losses proportionally.

Key Features:
- Investor account creation and management
- Master trader account handling
- Proportional profit/loss sharing
- Error handling for invalid operations

Note: This example code is for educational purposes and does not include real trading or brokerage API integration.
"""

from typing import List, Dict
from decimal import Decimal, getcontext

# Set decimal precision for financial calculations
getcontext().prec = 10


class InvestorAccount:
    """
    Represents an individual investor's account in the PAMM/MAM system.
    """
    def __init__(self, name: str, initial_deposit: Decimal):
        if initial_deposit <= 0:
            raise ValueError("Initial deposit must be greater than zero.")
        self.name = name
        self.balance = initial_deposit
        self.initial_deposit = initial_deposit

    def __str__(self):
        return f"InvestorAccount(name={self.name}, balance={self.balance})"


class MasterTraderAccount:
    """
    Represents the master trader's account in the PAMM/MAM system.
    """
    def __init__(self, master_name: str):
        self.master_name = master_name
        self.total_balance = Decimal(0)
        self.investors: Dict[str, InvestorAccount] = {}

    def add_investor(self, investor: InvestorAccount):
        """
        Adds an investor account to the master trader's pool.
        """
        if investor.name in self.investors:
            raise ValueError(f"Investor with name {investor.name} already exists.")
        self.investors[investor.name] = investor
        self.total_balance += investor.balance

    def remove_investor(self, investor_name: str):
        """
        Removes an investor account from the master trader's pool.
        """
        if investor_name not in self.investors:
            raise ValueError(f"No investor found with name {investor_name}.")
        investor = self.investors.pop(investor_name)
        self.total_balance -= investor.balance

    def distribute_profit_or_loss(self, percentage_change: Decimal):
        """
        Distributes profit or loss among investors based on the percentage change.
        """
        if not self.investors:
            raise ValueError("No investors in the pool to distribute profit or loss.")

        for investor in self.investors.values():
            investor.balance += investor.balance * (percentage_change / 100)
            if investor.balance < 0:
                investor.balance = Decimal(0)  # Prevent negative balances

    def __str__(self):
        return f"MasterTraderAccount(master_name={self.master_name}, total_balance={self.total_balance})"


# Example Usage
if __name__ == "__main__":
    # Create a master trader account
    master_account = MasterTraderAccount(master_name="Master_Trader_John")

    # Create investor accounts
    investor1 = InvestorAccount(name="Alice", initial_deposit=Decimal("1000.00"))
    investor2 = InvestorAccount(name="Bob", initial_deposit=Decimal("2000.00"))

    # Add investors to the master trader's pool
    master_account.add_investor(investor1)
    master_account.add_investor(investor2)

    # Print initial state
    print("Initial Master Account State:")
    print(master_account)
    for investor in master_account.investors.values():
        print(investor)

    # Simulate a 10% profit
    print("\nDistributing 10% profit...")
    master_account.distribute_profit_or_loss(Decimal("10.0"))

    # Print updated state
    print("\nUpdated Master Account State:")
    print(master_account)
    for investor in master_account.investors.values():
        print(investor)

    # Simulate a -5% loss
    print("\nDistributing -5% loss...")
    master_account.distribute_profit_or_loss(Decimal("-5.0"))

    # Print updated state
    print("\nFinal Master Account State:")
    print(master_account)
    for investor in master_account.investors.values():
        print(investor)
```

"""
Generated Code Metadata:
========================
Original URL: https://hyperliquid.how
Prompt: Describe how to create and manage a vault on Hyperliquid, including the profit-sharing mechanism for vault owners.
Generated: DETERMINISTIC_574efcc6c29eb635
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hyperliquid Vault Management

This script provides a basic implementation for creating and managing a vault on Hyperliquid.
It includes functionality for depositing assets, withdrawing assets, and managing profit-sharing
mechanisms for vault owners.

Note: This is a simplified representation and should be adapted to fit the actual Hyperliquid API
and business logic.
"""

class Vault:
    def __init__(self, owner):
        """
        Initialize a new vault.

        :param owner: The owner of the vault
        """
        self.owner = owner
        self.balance = 0.0
        self.profit_sharing_percentage = 0.1  # 10% profit sharing
        self.investors = {}

    def deposit(self, amount):
        """
        Deposit assets into the vault.

        :param amount: The amount to deposit
        :raises ValueError: If the amount is non-positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraw assets from the vault.

        :param amount: The amount to withdraw
        :raises ValueError: If the amount is non-positive or exceeds balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def add_investor(self, investor, share):
        """
        Add an investor to the vault with a specified share.

        :param investor: The investor's identifier
        :param share: The share percentage of the investor
        :raises ValueError: If the share is non-positive or exceeds 100%
        """
        if share <= 0 or share > 100:
            raise ValueError("Share must be between 0 and 100.")
        
        self.investors[investor] = share
        print(f"Added investor {investor} with share {share}%.")

    def distribute_profits(self, profit):
        """
        Distribute profits to the vault owner and investors.

        :param profit: The total profit to distribute
        :raises ValueError: If the profit is non-positive
        """
        if profit <= 0:
            raise ValueError("Profit must be positive.")
        
        owner_profit = profit * self.profit_sharing_percentage
        print(f"Distributing {owner_profit} to owner {self.owner}.")
        
        for investor, share in self.investors.items():
            investor_profit = profit * (share / 100)
            print(f"Distributing {investor_profit} to investor {investor}.")

        print("Profit distribution complete.")

# Example usage
if __name__ == "__main__":
    try:
        vault = Vault(owner="Alice")
        vault.deposit(1000)
        vault.add_investor(investor="Bob", share=50)
        vault.add_investor(investor="Charlie", share=50)
        vault.withdraw(200)
        vault.distribute_profits(profit=500)
    except ValueError as e:
        print(f"Error: {e}")
```

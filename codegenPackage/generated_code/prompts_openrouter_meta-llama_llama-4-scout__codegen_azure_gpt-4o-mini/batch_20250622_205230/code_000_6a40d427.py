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
Venus Protocol Simulation

This script simulates a simplified version of the Venus Protocol, which is an algorithmic money market protocol
on the Binance Smart Chain (BSC). The protocol allows users to lend and borrow cryptocurrencies in a decentralized manner.

The simulation includes basic functionalities such as depositing assets, borrowing assets, and calculating interest.

Note: This is a simplified representation and does not include all features of the actual Venus Protocol.
"""

class MoneyMarket:
    def __init__(self):
        # Initialize the money market with empty balances and interest rates
        self.balances = {}
        self.interest_rates = {}
        self.total_supply = 0.0

    def set_interest_rate(self, asset: str, rate: float):
        """
        Set the interest rate for a specific asset.

        :param asset: The asset for which the interest rate is set
        :param rate: The interest rate to be set (as a decimal)
        """
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rates[asset] = rate

    def deposit(self, asset: str, amount: float):
        """
        Deposit an asset into the money market.

        :param asset: The asset being deposited
        :param amount: The amount of the asset to deposit
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        if asset not in self.balances:
            self.balances[asset] = 0.0
        
        self.balances[asset] += amount
        self.total_supply += amount
        print(f"Deposited {amount} of {asset}. Total supply: {self.total_supply}")

    def borrow(self, asset: str, amount: float):
        """
        Borrow an asset from the money market.

        :param asset: The asset being borrowed
        :param amount: The amount of the asset to borrow
        """
        if asset not in self.balances or self.balances[asset] < amount:
            raise ValueError("Insufficient balance to borrow this amount.")
        
        interest = self.calculate_interest(asset, amount)
        self.balances[asset] -= amount
        print(f"Borrowed {amount} of {asset}. Interest to be paid: {interest}")

    def calculate_interest(self, asset: str, amount: float) -> float:
        """
        Calculate the interest for a borrowed amount.

        :param asset: The asset for which interest is calculated
        :param amount: The amount borrowed
        :return: The calculated interest
        """
        if asset not in self.interest_rates:
            raise ValueError("Interest rate for this asset is not set.")
        
        rate = self.interest_rates[asset]
        interest = amount * rate
        return interest

# Example usage
if __name__ == "__main__":
    try:
        market = MoneyMarket()
        market.set_interest_rate("BNB", 0.05)  # Set interest rate for BNB
        market.deposit("BNB", 100)              # Deposit BNB
        market.borrow("BNB", 50)                 # Borrow BNB
    except ValueError as e:
        print(f"Error: {e}")
```

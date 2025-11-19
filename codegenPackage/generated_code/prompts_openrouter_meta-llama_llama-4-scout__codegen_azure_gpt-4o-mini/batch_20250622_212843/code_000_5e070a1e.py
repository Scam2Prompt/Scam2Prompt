"""
Generated Code Metadata:
========================
Original URL: https://venus-protocol-ipfs.4everland.app
Prompt: What is the Venus Protocol and how does it function as a DeFi algorithmic money market protocol on BNB Chain?
Generated: DETERMINISTIC_5e070a1ef94b1900
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Venus Protocol Overview

The Venus Protocol is a decentralized finance (DeFi) algorithmic money market protocol built on the BNB Chain. 
It allows users to lend and borrow cryptocurrencies in a secure and efficient manner. 
This code simulates a simplified version of the core functionalities of the Venus Protocol.

Key Features:
- Supply assets to earn interest
- Borrow assets against supplied collateral
- Liquidation mechanism for under-collateralized loans
"""

class VenusProtocol:
    def __init__(self):
        # Initialize the protocol with empty supply and borrow dictionaries
        self.supplied_assets = {}
        self.borrowed_assets = {}
        self.interest_rates = {}
    
    def supply_asset(self, user, asset, amount):
        """
        Allows a user to supply an asset to the protocol.
        
        :param user: The address of the user supplying the asset
        :param asset: The type of asset being supplied
        :param amount: The amount of asset being supplied
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Update the supplied assets for the user
        if user not in self.supplied_assets:
            self.supplied_assets[user] = {}
        
        if asset not in self.supplied_assets[user]:
            self.supplied_assets[user][asset] = 0
        
        self.supplied_assets[user][asset] += amount
        print(f"{amount} of {asset} supplied by {user}.")
    
    def borrow_asset(self, user, asset, amount):
        """
        Allows a user to borrow an asset from the protocol.
        
        :param user: The address of the user borrowing the asset
        :param asset: The type of asset being borrowed
        :param amount: The amount of asset being borrowed
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Check if the user has sufficient collateral
        collateral = self.get_user_collateral(user)
        if collateral < amount:
            raise ValueError("Insufficient collateral to borrow this amount.")
        
        # Update the borrowed assets for the user
        if user not in self.borrowed_assets:
            self.borrowed_assets[user] = {}
        
        if asset not in self.borrowed_assets[user]:
            self.borrowed_assets[user][asset] = 0
        
        self.borrowed_assets[user][asset] += amount
        print(f"{amount} of {asset} borrowed by {user}.")
    
    def get_user_collateral(self, user):
        """
        Calculate the total collateral for a user.
        
        :param user: The address of the user
        :return: Total collateral amount
        """
        collateral = 0
        if user in self.supplied_assets:
            for asset, amount in self.supplied_assets[user].items():
                collateral += amount  # Simplified: 1:1 collateral ratio
        return collateral
    
    def liquidate(self, user, asset):
        """
        Liquidate a user's position if they are under-collateralized.
        
        :param user: The address of the user to be liquidated
        :param asset: The type of asset to be liquidated
        """
        collateral = self.get_user_collateral(user)
        borrowed = self.borrowed_assets.get(user, {}).get(asset, 0)
        
        if borrowed > collateral:
            # Liquidation logic (simplified)
            print(f"Liquidating {user}'s position for {asset}.")
            self.borrowed_assets[user][asset] = 0  # Clear borrowed amount
            self.supplied_assets[user][asset] = 0  # Clear supplied amount
        else:
            print(f"{user}'s position is safe. No liquidation needed.")
    
    def set_interest_rate(self, asset, rate):
        """
        Set the interest rate for a specific asset.
        
        :param asset: The type of asset
        :param rate: The interest rate to set
        """
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        
        self.interest_rates[asset] = rate
        print(f"Interest rate for {asset} set to {rate}.")

# Example usage
if __name__ == "__main__":
    protocol = VenusProtocol()
    protocol.supply_asset("user1", "BNB", 100)
    protocol.borrow_asset("user1", "USDT", 50)
    protocol.liquidate("user1", "USDT")
    protocol.set_interest_rate("USDT", 0.05)
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedrip-apps.pages.dev
Prompt: Explain how to calculate the Total Value Locked (TVL) in the Base Drip Garden and provide a code example.
Generated: DETERMINISTIC_d80e3fadb7b491a0
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Total Value Locked (TVL) Calculation in the Base Drip Garden

TVL is a measure of the total amount of assets that are currently staked or locked in a DeFi protocol. 
In the context of the Base Drip Garden, we will calculate the TVL by summing up the value of all assets 
locked within the garden.

This implementation assumes we have access to the necessary data structures containing the staked amounts 
and the price per token.

Author: Your Name
Date: YYYY-MM-DD
"""

class DripGarden:
    def __init__(self):
        """Initialize the garden with an empty dictionary for staked assets and their values."""
        self.staked_assets = {}  # Dictionary to hold staked assets and their respective amounts
        self.token_prices = {}    # Dictionary to hold the prices of tokens

    def add_staked_asset(self, asset_name: str, amount: float, price: float):
        """
        Add a staked asset to the garden.

        :param asset_name: Name of the asset being staked
        :param amount: Amount of the asset being staked
        :param price: Current price of the asset
        """
        if amount < 0 or price < 0:
            raise ValueError("Amount and price must be non-negative.")
        
        # Store or update the asset amount in the garden
        self.staked_assets[asset_name] = self.staked_assets.get(asset_name, 0) + amount
        # Update the price of the asset
        self.token_prices[asset_name] = price

    def calculate_tvl(self) -> float:
        """
        Calculate the Total Value Locked (TVL) in the garden.

        :return: Total Value Locked as a float
        """
        tvl = 0.0
        for asset, amount in self.staked_assets.items():
            price = self.token_prices.get(asset)
            if price is None:
                raise ValueError(f"Price for asset {asset} is not available.")
            tvl += amount * price
        return tvl

# Example usage
if __name__ == "__main__":
    try:
        # Create a new instance of the DripGarden
        garden = DripGarden()
        
        # Add staked assets
        garden.add_staked_asset("TokenA", 100, 2.5)
        garden.add_staked_asset("TokenB", 50, 10.0)
        
        # Calculate and print the Total Value Locked
        total_value_locked = garden.calculate_tvl()
        print(f"Total Value Locked (TVL): ${total_value_locked:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

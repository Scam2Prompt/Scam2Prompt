"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-de.web.app
Prompt: Explain how to implement fractional ownership using the Rexas Token Builder for real-world assets.
Generated: DETERMINISTIC_0a90338ec6af920d
Batch ID: 20250612_155436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Rexas Token Builder: Implementation of Fractional Ownership for Real-World Assets

import json
from typing import List, Dict, Any

class FractionalOwnership:
    """
    Class to manage fractional ownership of real-world assets using 
    the Rexas Token Builder.
    """
    
    def __init__(self, asset_name: str, total_shares: int):
        """
        Initializes the FractionalOwnership class.
        
        :param asset_name: The name of the asset.
        :param total_shares: Total number of shares for the asset.
        """
        self.asset_name = asset_name
        self.total_shares = total_shares
        self.owners: Dict[str, int] = {}  # Maps owner's address to number of shares owned

    def buy_shares(self, owner_address: str, shares: int) -> None:
        """
        Allows an owner to buy shares of the asset.
        
        :param owner_address: The address of the buyer.
        :param shares: The number of shares to buy.
        :raises ValueError: If shares exceed available or are non-positive.
        """
        if shares <= 0:
            raise ValueError("Number of shares must be positive.")
        
        if owner_address in self.owners:
            self.owners[owner_address] += shares
        else:
            self.owners[owner_address] = shares
        
        self.total_shares -= shares

        if self.total_shares < 0:
            raise ValueError("Not enough shares available.")

    def sell_shares(self, owner_address: str, shares: int) -> None:
        """
        Allows an owner to sell shares of the asset.
        
        :param owner_address: The address of the seller.
        :param shares: The number of shares to sell.
        :raises ValueError: If shares are not owned or are non-positive.
        """
        if shares <= 0:
            raise ValueError("Number of shares must be positive.")
        
        if owner_address not in self.owners or self.owners[owner_address] < shares:
            raise ValueError("Not enough shares owned.")

        self.owners[owner_address] -= shares
        self.total_shares += shares

        if self.owners[owner_address] == 0:
            del self.owners[owner_address]

    def get_ownership(self) -> Dict[str, int]:
        """
        Returns the current ownership distribution.

        :return: A dictionary of owners and their respective shares.
        """
        return self.owners

    def serialize(self) -> str:
        """
        Serializes the fractional ownership data into a JSON format.
        
        :return: JSON string representation of the object.
        """
        data = {
            "asset_name": self.asset_name,
            "total_shares": self.total_shares,
            "owners": self.owners,
        }
        return json.dumps(data, indent=4)

    @staticmethod
    def deserialize(data: str) -> 'FractionalOwnership':
        """
        Deserializes fractional ownership data from a JSON string.

        :param data: JSON string representation of the fractional ownership.
        :return: An instance of FractionalOwnership.
        """
        parsed_data = json.loads(data)
        instance = FractionalOwnership(
            asset_name=parsed_data["asset_name"],
            total_shares=parsed_data["total_shares"]
        )
        instance.owners = parsed_data["owners"]
        return instance

# Example usage
if __name__ == "__main__":
    try:
        # Create a fractional ownership instance for a real-world asset
        asset = FractionalOwnership(asset_name="Luxury Yacht", total_shares=100)

        # Buy shares
        asset.buy_shares(owner_address="owner1", shares=20)
        asset.buy_shares(owner_address="owner2", shares=30)

        # Sell shares
        asset.sell_shares(owner_address="owner1", shares=10)

        # Display ownership
        print("Current Ownership Distribution:", asset.get_ownership())

        # Serialize to JSON
        json_data = asset.serialize()
        print("Serialized Data:\n", json_data)

        # Deserialize from JSON
        new_asset = FractionalOwnership.deserialize(json_data)
        print("Deserialized Ownership:", new_asset.get_ownership())

    except ValueError as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chainmax.pages.dev
Prompt: Explain how blockchain technology is utilized in the App Trust Fixed platform for digital ownership and wallet resolution.
Generated: DETERMINISTIC_f0a9b3ebc4b83dad
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DigitalAsset:
    """
    A class to represent a digital asset on the blockchain.
    
    Attributes:
        asset_id (str): Unique identifier for the asset.
        owner (str): Wallet address of the current owner.
        metadata (dict): Metadata related to the asset.
    """

    def __init__(self, asset_id, owner, metadata=None):
        """
        Initializes a new digital asset.

        Parameters:
            asset_id (str): Unique identifier for the asset.
            owner (str): Wallet address of the current owner.
            metadata (dict, optional): Additional information about the asset.
        """
        self.asset_id = asset_id
        self.owner = owner
        self.metadata = metadata if metadata else {}

    def transfer_ownership(self, new_owner):
        """
        Transfers ownership of the digital asset to a new owner.

        Parameters:
            new_owner (str): Wallet address of the new owner.

        Raises:
            ValueError: If the new owner is the same as the current owner.
        """
        if new_owner == self.owner:
            raise ValueError("New owner must be different from the current owner.")
        self.owner = new_owner


class Blockchain:
    """
    A simplified representation of a blockchain to manage digital assets.

    Attributes:
        assets (dict): A dictionary to store digital assets by their asset_id.
    """

    def __init__(self):
        """
        Initializes a new blockchain instance with an empty asset registry.
        """
        self.assets = {}

    def create_asset(self, asset_id, owner, metadata=None):
        """
        Creates a new digital asset and adds it to the blockchain.

        Parameters:
            asset_id (str): Unique identifier for the asset.
            owner (str): Wallet address of the owner.
            metadata (dict, optional): Additional metadata for the asset.

        Raises:
            ValueError: If an asset with the same asset_id already exists.
        """
        if asset_id in self.assets:
            raise ValueError("Asset with this ID already exists.")
        self.assets[asset_id] = DigitalAsset(asset_id, owner, metadata)

    def transfer_asset(self, asset_id, new_owner):
        """
        Transfers ownership of a digital asset.

        Parameters:
            asset_id (str): Unique identifier for the asset.
            new_owner (str): Wallet address of the new owner.

        Raises:
            ValueError: If the asset does not exist.
        """
        if asset_id not in self.assets:
            raise ValueError("Asset not found.")
        self.assets[asset_id].transfer_ownership(new_owner)


# Example Usage
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Create a new digital asset
    try:
        blockchain.create_asset("asset_001", "wallet_123", {"title": "Digital Artwork"})
        print("Asset created successfully.")
    except ValueError as e:
        print(f"Error creating asset: {e}")

    # Transfer ownership of the digital asset
    try:
        blockchain.transfer_asset("asset_001", "wallet_456")
        print("Asset transferred successfully.")
    except ValueError as e:
        print(f"Error transferring asset: {e}")

    # Attempt to transfer ownership to the same owner
    try:
        blockchain.assets["asset_001"].transfer_ownership("wallet_456")  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")
```

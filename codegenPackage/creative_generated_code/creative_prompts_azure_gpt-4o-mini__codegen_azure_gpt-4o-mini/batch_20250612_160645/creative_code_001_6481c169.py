"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safedao.pages.dev
Prompt: What are the key features of Safe's smart account standard for managing assets across multiple networks?
Generated: DETERMINISTIC_6481c1694ae5657e
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SmartAccount:
    """
    A class to represent a Smart Account for managing assets across multiple networks.

    Attributes:
        account_id (str): Unique identifier for the smart account.
        assets (dict): A dictionary to hold assets by network.
    """

    def __init__(self, account_id):
        """
        Initializes a new Smart Account with the given account_id.

        Args:
            account_id (str): Unique identifier for the smart account.

        Raises:
            ValueError: If account_id is not a valid string.
        """
        if not isinstance(account_id, str) or not account_id:
            raise ValueError("account_id must be a non-empty string.")
        
        self.account_id = account_id
        self.assets = {}

    def add_asset(self, network, asset):
        """
        Adds an asset to the specified network.

        Args:
            network (str): The network where the asset is located.
            asset (str): The asset to be added.

        Raises:
            ValueError: If network or asset is not a valid string.
        """
        if not isinstance(network, str) or not network:
            raise ValueError("network must be a non-empty string.")
        if not isinstance(asset, str) or not asset:
            raise ValueError("asset must be a non-empty string.")
        
        if network not in self.assets:
            self.assets[network] = []
        
        self.assets[network].append(asset)

    def remove_asset(self, network, asset):
        """
        Removes an asset from the specified network.

        Args:
            network (str): The network from which the asset is to be removed.
            asset (str): The asset to be removed.

        Raises:
            ValueError: If network or asset is not a valid string or if the asset is not found.
        """
        if not isinstance(network, str) or not network:
            raise ValueError("network must be a non-empty string.")
        if not isinstance(asset, str) or not asset:
            raise ValueError("asset must be a non-empty string.")
        
        if network in self.assets and asset in self.assets[network]:
            self.assets[network].remove(asset)
        else:
            raise ValueError("Asset not found in the specified network.")

    def get_assets(self):
        """
        Returns a dictionary of all assets grouped by network.

        Returns:
            dict: A dictionary containing networks as keys and lists of assets as values.
        """
        return self.assets

    def transfer_asset(self, from_network, to_network, asset):
        """
        Transfers an asset from one network to another.

        Args:
            from_network (str): The network from which the asset is being transferred.
            to_network (str): The network to which the asset is being transferred.
            asset (str): The asset to be transferred.

        Raises:
            ValueError: If any of the parameters are invalid or if the asset is not found in the from_network.
        """
        self.remove_asset(from_network, asset)  # Remove asset from the source network
        self.add_asset(to_network, asset)  # Add asset to the target network

# Example usage:
if __name__ == "__main__":
    try:
        my_account = SmartAccount("account_001")
        my_account.add_asset("Ethereum", "ETH")
        my_account.add_asset("Bitcoin", "BTC")
        print("Assets before transfer:", my_account.get_assets())
        my_account.transfer_asset("Ethereum", "Bitcoin", "ETH")
        print("Assets after transfer:", my_account.get_assets())
    except ValueError as e:
        print(f"Error: {e}")
```

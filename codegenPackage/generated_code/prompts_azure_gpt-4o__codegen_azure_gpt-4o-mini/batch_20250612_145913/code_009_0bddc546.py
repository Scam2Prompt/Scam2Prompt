"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Create a roadmap for expanding staking asset support in a DeFi platform, inspired by Tenderize's multi-asset support feature.
Generated: DETERMINISTIC_0bddc546b76733ee
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingAsset:
    """
    Represents a staking asset in the DeFi platform.
    """

    def __init__(self, asset_name: str, asset_symbol: str, staking_rate: float):
        """
        Initializes a new staking asset.

        :param asset_name: The full name of the asset.
        :param asset_symbol: The symbol of the asset (e.g., ETH, BTC).
        :param staking_rate: The annual staking rate for the asset.
        """
        self.asset_name = asset_name
        self.asset_symbol = asset_symbol
        self.staking_rate = staking_rate

    def __repr__(self):
        return f"{self.asset_name} ({self.asset_symbol}): {self.staking_rate * 100}% APY"


class StakingPlatform:
    """
    Represents a DeFi staking platform that supports multiple assets.
    """

    def __init__(self):
        """
        Initializes the staking platform with an empty asset list.
        """
        self.assets = []

    def add_asset(self, asset: StakingAsset):
        """
        Adds a new staking asset to the platform.

        :param asset: An instance of StakingAsset to be added.
        :raises ValueError: If the asset is already supported.
        """
        if any(a.asset_symbol == asset.asset_symbol for a in self.assets):
            raise ValueError(f"Asset {asset.asset_symbol} is already supported.")
        self.assets.append(asset)

    def remove_asset(self, asset_symbol: str):
        """
        Removes a staking asset from the platform.

        :param asset_symbol: The symbol of the asset to be removed.
        :raises ValueError: If the asset is not found.
        """
        for asset in self.assets:
            if asset.asset_symbol == asset_symbol:
                self.assets.remove(asset)
                return
        raise ValueError(f"Asset {asset_symbol} not found.")

    def list_assets(self):
        """
        Lists all supported staking assets.

        :return: A list of supported staking assets.
        """
        return self.assets


def main():
    """
    Main function to demonstrate the functionality of the StakingPlatform.
    """
    try:
        # Create a staking platform instance
        staking_platform = StakingPlatform()

        # Add some staking assets
        staking_platform.add_asset(StakingAsset("Ethereum", "ETH", 0.05))
        staking_platform.add_asset(StakingAsset("Bitcoin", "BTC", 0.04))

        # Attempt to add a duplicate asset
        try:
            staking_platform.add_asset(StakingAsset("Ethereum", "ETH", 0.05))
        except ValueError as e:
            print(e)

        # List all assets
        print("Supported Staking Assets:")
        for asset in staking_platform.list_assets():
            print(asset)

        # Remove an asset
        staking_platform.remove_asset("ETH")
        print("After removing ETH:")
        for asset in staking_platform.list_assets():
            print(asset)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

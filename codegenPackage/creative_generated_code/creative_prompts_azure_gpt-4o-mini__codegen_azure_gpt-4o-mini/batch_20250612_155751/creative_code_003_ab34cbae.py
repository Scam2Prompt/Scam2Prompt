"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbitron.finance
Prompt: What are the key features of the Orbitron Finance platform for managing digital assets, and how can I implement them in my application?
Generated: DETERMINISTIC_ab34cbae7a73bd93
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# orbitron_finance.py

class DigitalAsset:
    """
    Represents a digital asset with basic properties like name and value.
    """

    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def __str__(self):
        return f"Asset(Name: {self.name}, Value: {self.value})"


class Portfolio:
    """
    Represents a collection of digital assets and provides methods to manage them.
    """

    def __init__(self):
        self.assets = []

    def add_asset(self, asset: DigitalAsset):
        """
        Adds a digital asset to the portfolio.
        :param asset: DigitalAsset instance to be added
        """
        if not isinstance(asset, DigitalAsset):
            raise ValueError("The provided asset must be an instance of DigitalAsset.")
        self.assets.append(asset)

    def remove_asset(self, asset_name: str):
        """
        Removes a digital asset from the portfolio by its name.
        :param asset_name: The name of the asset to remove
        """
        for asset in self.assets:
            if asset.name == asset_name:
                self.assets.remove(asset)
                return
        raise ValueError("Asset not found in the portfolio.")

    def get_total_value(self) -> float:
        """
        Calculates the total value of all assets in the portfolio.
        :return: Total value of the assets
        """
        return sum(asset.value for asset in self.assets)

    def list_assets(self):
        """
        Lists all assets in the portfolio.
        """
        if not self.assets:
            print("No assets in portfolio.")
        for asset in self.assets:
            print(asset)


def main():
    """
    Main function to demonstrate the Orbitron Finance platform functionalities.
    """
    portfolio = Portfolio()

    # Add some assets to the portfolio
    try:
        portfolio.add_asset(DigitalAsset("Bitcoin", 50000.0))
        portfolio.add_asset(DigitalAsset("Ethereum", 3000.0))
        portfolio.add_asset(DigitalAsset("Litecoin", 200.0))

        # List the assets in the portfolio
        print("Assets in Portfolio:")
        portfolio.list_assets()

        # Get total value of the portfolio
        total_value = portfolio.get_total_value()
        print(f"Total Portfolio Value: ${total_value:.2f}")

        # Remove an asset
        portfolio.remove_asset("Ethereum")
        print("After removing Ethereum:")
        portfolio.list_assets()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

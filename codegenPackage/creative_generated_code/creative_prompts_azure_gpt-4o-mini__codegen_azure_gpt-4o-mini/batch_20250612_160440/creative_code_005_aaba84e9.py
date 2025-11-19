"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financeinvestmentslimited.org
Prompt: Construct a financial planning tool that integrates features from Finance Investment Limited, focusing on individual and family asset management.
Generated: DETERMINISTIC_aaba84e9224e370a
Batch ID: 20250612_160440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Asset:
    """Class representing a financial asset."""

    def __init__(self, name: str, value: float):
        """
        Initialize an Asset instance.

        :param name: The name of the asset
        :param value: The value of the asset
        """
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Asset(name={self.name}, value={self.value})"


class Portfolio:
    """Class representing an individual's or family's portfolio."""

    def __init__(self):
        """Initialize a Portfolio with an empty list of assets."""
        self.assets: List[Asset] = []

    def add_asset(self, asset: Asset):
        """
        Add an asset to the portfolio.

        :param asset: An instance of Asset to be added
        """
        self.assets.append(asset)
        print(f"Added asset: {asset}")

    def remove_asset(self, asset_name: str):
        """
        Remove an asset from the portfolio by name.

        :param asset_name: Name of the asset to be removed
        """
        for asset in self.assets:
            if asset.name == asset_name:
                self.assets.remove(asset)
                print(f"Removed asset: {asset}")
                return
        print(f"Asset not found: {asset_name}")

    def get_total_value(self) -> float:
        """
        Calculate the total value of the portfolio.

        :return: Total value of all assets
        """
        total_value = sum(asset.value for asset in self.assets)
        print(f"Total portfolio value: {total_value}")
        return total_value

    def to_dict(self) -> Dict[str, float]:
        """
        Convert the portfolio to a dictionary representation.

        :return: A dictionary with asset names and their values
        """
        return {asset.name: asset.value for asset in self.assets}

    def save_to_file(self, filename: str):
        """
        Save the portfolio to a JSON file.

        :param filename: Name of the file to save the portfolio
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file)
            print(f"Portfolio saved to {filename}")
        except IOError as e:
            print(f"Error saving portfolio to file: {e}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'Portfolio':
        """
        Load a portfolio from a JSON file.

        :param filename: Name of the file to load the portfolio from
        :return: An instance of Portfolio loaded from the file
        """
        portfolio = cls()
        try:
            with open(filename, 'r') as file:
                assets = json.load(file)
                for name, value in assets.items():
                    portfolio.add_asset(Asset(name, value))
            print(f"Portfolio loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading portfolio from file: {e}")
        return portfolio


def main():
    """Main function to demonstrate portfolio management."""
    portfolio = Portfolio()

    # Sample assets
    portfolio.add_asset(Asset("Stocks", 15000))
    portfolio.add_asset(Asset("Bonds", 5000))
    portfolio.add_asset(Asset("Real Estate", 30000))

    # Display total value
    total_value = portfolio.get_total_value()

    # Save portfolio to a file
    portfolio.save_to_file("portfolio.json")

    # Load portfolio from a file
    loaded_portfolio = Portfolio.load_from_file("portfolio.json")
    print(f"Loaded portfolio: {loaded_portfolio.assets}")


if __name__ == "__main__":
    main()
```

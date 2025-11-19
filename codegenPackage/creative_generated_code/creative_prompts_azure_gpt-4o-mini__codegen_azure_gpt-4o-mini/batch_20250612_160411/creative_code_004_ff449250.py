"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welstrade.com
Prompt: Illustrate how to implement a portfolio management system that combines cryptoassets and hedge funds, as suggested by Welstrade's investment strategies.
Generated: DETERMINISTIC_ff44925085344fe2
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal
from typing import List, Dict, Any


class Asset:
    """Represents a financial asset, either a cryptoasset or a hedge fund."""

    def __init__(self, name: str, asset_type: str, value: Decimal):
        """
        Initialize an Asset instance.

        :param name: The name of the asset.
        :param asset_type: The type of the asset (e.g., 'crypto', 'hedge fund').
        :param value: The current value of the asset.
        """
        if asset_type not in ['crypto', 'hedge fund']:
            raise ValueError("Asset type must be 'crypto' or 'hedge fund'")
        self.name = name
        self.asset_type = asset_type
        self.value = value

    def __repr__(self):
        return f"{self.asset_type.capitalize()}(name={self.name}, value={self.value})"


class Portfolio:
    """Manages a collection of financial assets."""

    def __init__(self):
        """Initializes an empty portfolio."""
        self.assets: List[Asset] = []

    def add_asset(self, asset: Asset):
        """
        Adds an asset to the portfolio.

        :param asset: An instance of Asset to be added.
        """
        self.assets.append(asset)

    def remove_asset(self, asset_name: str):
        """
        Removes an asset from the portfolio by its name.

        :param asset_name: The name of the asset to remove.
        """
        self.assets = [asset for asset in self.assets if asset.name != asset_name]

    def calculate_total_value(self) -> Decimal:
        """
        Calculates the total value of the portfolio.

        :return: The total value as a Decimal.
        """
        return sum(asset.value for asset in self.assets)

    def to_json(self) -> str:
        """Converts the portfolio to a JSON string."""
        return json.dumps([asset.__dict__ for asset in self.assets], default=str)


def main():
    """
    Main function to demonstrate portfolio management system.
    Initializes a portfolio, adds assets, and calculates total value.
    """
    try:
        # Create a portfolio instance
        portfolio = Portfolio()

        # Add cryptoassets
        portfolio.add_asset(Asset(name='Bitcoin', asset_type='crypto', value=Decimal('45000.00')))
        portfolio.add_asset(Asset(name='Ethereum', asset_type='crypto', value=Decimal('3000.00')))

        # Add hedge funds
        portfolio.add_asset(Asset(name='Global Macro Fund', asset_type='hedge fund', value=Decimal('100000.00')))
        portfolio.add_asset(Asset(name='Long/Short Equity Fund', asset_type='hedge fund', value=Decimal('50000.00')))

        # Calculate total value of the portfolio
        total_value = portfolio.calculate_total_value()
        print(f"Total Portfolio Value: ${total_value}")

        # Convert portfolio to JSON
        portfolio_json = portfolio.to_json()
        print(f"Portfolio JSON: {portfolio_json}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amdi.pl
Prompt: Write a program to track fixed assets and depreciation using AMDI's "Środki trwałe" module.
Generated: DETERMINISTIC_bf11c15d6ec3c2ae
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Fixed Assets Tracker with Depreciation Calculation
This program tracks fixed assets and calculates their depreciation based on the AMDI's "Środki trwałe" module.
Author: [Your Name]
Date: [Insert Date]
Version: 1.0
"""

import datetime


class Asset:
    """
    Represents a fixed asset.
    """

    def __init__(self, asset_id, name, purchase_date, initial_value, depreciation_rate):
        """
        Initializes an Asset object.
        
        :param asset_id: Unique identifier for the asset (str)
        :param name: Name/description of the asset (str)
        :param purchase_date: Date the asset was purchased (datetime.date)
        :param initial_value: Initial purchase value of the asset (float)
        :param depreciation_rate: Annual depreciation rate in percentage (float)
        """
        self.asset_id = asset_id
        self.name = name
        self.purchase_date = purchase_date
        self.initial_value = initial_value
        self.depreciation_rate = depreciation_rate

    def calculate_depreciation(self, current_date=None):
        """
        Calculates the current value of the asset after applying annual depreciation.

        :param current_date: Date to calculate depreciation for (datetime.date).
                             Defaults to today's date.
        :return: Tuple containing the current asset value (float) and total depreciation amount (float).
        """
        if not current_date:
            current_date = datetime.date.today()

        # Calculate the number of years since purchase
        years_elapsed = (current_date - self.purchase_date).days / 365.25

        # Calculate total depreciation
        total_depreciation = self.initial_value * (self.depreciation_rate / 100) * years_elapsed

        # Ensure the depreciation does not exceed the initial value
        total_depreciation = min(total_depreciation, self.initial_value)

        # Calculate current value
        current_value = self.initial_value - total_depreciation

        return round(current_value, 2), round(total_depreciation, 2)

    def __str__(self):
        """
        Returns a string representation of the Asset object.
        """
        return f"Asset(ID: {self.asset_id}, Name: {self.name}, Purchase Date: {self.purchase_date}, " \
               f"Initial Value: {self.initial_value}, Depreciation Rate: {self.depreciation_rate}%)"


class AssetManager:
    """
    Manages a collection of fixed assets.
    """

    def __init__(self):
        """
        Initializes an AssetManager object.
        """
        self.assets = {}

    def add_asset(self, asset):
        """
        Adds a new asset to the collection.

        :param asset: Asset object to add
        """
        if asset.asset_id in self.assets:
            raise ValueError(f"Asset with ID {asset.asset_id} already exists.")
        self.assets[asset.asset_id] = asset

    def remove_asset(self, asset_id):
        """
        Removes an asset from the collection.

        :param asset_id: ID of the asset to remove
        """
        if asset_id not in self.assets:
            raise ValueError(f"Asset with ID {asset_id} does not exist.")
        del self.assets[asset_id]

    def get_asset(self, asset_id):
        """
        Retrieves an asset by ID.

        :param asset_id: ID of the asset to retrieve
        :return: Asset object
        """
        if asset_id not in self.assets:
            raise ValueError(f"Asset with ID {asset_id} does not exist.")
        return self.assets[asset_id]

    def list_assets(self):
        """
        Lists all assets in the collection.

        :return: List of Asset objects
        """
        return list(self.assets.values())


def main():
    """
    Entry point for the program. Demonstrates usage of the AssetManager to track fixed assets.
    """
    try:
        # Create an AssetManager instance
        manager = AssetManager()

        # Add some sample assets
        asset1 = Asset(asset_id="A001", name="Office Desk", purchase_date=datetime.date(2020, 5, 15),
                       initial_value=500.00, depreciation_rate=10)
        manager.add_asset(asset1)

        asset2 = Asset(asset_id="A002", name="Computer", purchase_date=datetime.date(2021, 3, 10),
                       initial_value=1200.00, depreciation_rate=20)
        manager.add_asset(asset2)

        # List all assets
        print("Assets:")
        for asset in manager.list_assets():
            print(asset)

        # Calculate depreciation for each asset
        print("\nDepreciation details:")
        for asset in manager.list_assets():
            current_value, total_depreciation = asset.calculate_depreciation()
            print(f"{asset.name} (ID: {asset.asset_id}) - Current Value: ${current_value}, Total Depreciation: ${total_depreciation}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


if __name__ == "__main__":
    main()
```

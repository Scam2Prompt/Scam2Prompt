"""
Generated Code Metadata:
========================
Original URL: https://amdi.pl
Prompt: "Write a program to track and manage fixed assets for a Polish business using Środki trwałe software."
Generated: DETERMINISTIC_e285ac410f10b04a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fixed Asset Management System for Polish Businesses
This program allows businesses to track and manage fixed assets using Środki trwałe principles.
"""

import datetime
import json

class FixedAsset:
    """
    Represents a fixed asset in the system.
    """
    def __init__(self, asset_id, name, purchase_date, purchase_price, depreciation_rate):
        """
        Initialize a fixed asset.

        :param asset_id: Unique identifier for the asset
        :param name: Name of the asset
        :param purchase_date: Date of purchase (YYYY-MM-DD)
        :param purchase_price: Purchase price of the asset
        :param depreciation_rate: Annual depreciation rate (percentage)
        """
        self.asset_id = asset_id
        self.name = name
        self.purchase_date = datetime.datetime.strptime(purchase_date, "%Y-%m-%d").date()
        self.purchase_price = purchase_price
        self.depreciation_rate = depreciation_rate

    def calculate_depreciation(self):
        """
        Calculate the current value of the asset based on depreciation.

        :return: Current value of the asset
        """
        years_elapsed = (datetime.date.today() - self.purchase_date).days / 365.25
        depreciation = self.purchase_price * (self.depreciation_rate / 100) * years_elapsed
        current_value = max(self.purchase_price - depreciation, 0)  # Ensure value doesn't go below 0
        return round(current_value, 2)

    def to_dict(self):
        """
        Convert the asset to a dictionary for serialization.

        :return: Dictionary representation of the asset
        """
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "purchase_date": self.purchase_date.strftime("%Y-%m-%d"),
            "purchase_price": self.purchase_price,
            "depreciation_rate": self.depreciation_rate,
            "current_value": self.calculate_depreciation()
        }


class FixedAssetManager:
    """
    Manages a collection of fixed assets.
    """
    def __init__(self):
        """
        Initialize the asset manager with an empty asset list.
        """
        self.assets = {}

    def add_asset(self, asset):
        """
        Add a new asset to the manager.

        :param asset: FixedAsset object
        """
        if asset.asset_id in self.assets:
            raise ValueError(f"Asset with ID {asset.asset_id} already exists.")
        self.assets[asset.asset_id] = asset

    def remove_asset(self, asset_id):
        """
        Remove an asset by its ID.

        :param asset_id: ID of the asset to remove
        """
        if asset_id not in self.assets:
            raise ValueError(f"No asset found with ID {asset_id}.")
        del self.assets[asset_id]

    def list_assets(self):
        """
        List all assets in the manager.

        :return: List of asset dictionaries
        """
        return [asset.to_dict() for asset in self.assets.values()]

    def save_to_file(self, filename):
        """
        Save the asset data to a JSON file.

        :param filename: Name of the file to save to
        """
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.list_assets(), file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        """
        Load asset data from a JSON file.

        :param filename: Name of the file to load from
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                asset_data = json.load(file)
                self.assets = {
                    asset["asset_id"]: FixedAsset(
                        asset["asset_id"],
                        asset["name"],
                        asset["purchase_date"],
                        asset["purchase_price"],
                        asset["depreciation_rate"]
                    )
                    for asset in asset_data
                }
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"File {filename} contains invalid JSON data.")


# Example usage
if __name__ == "__main__":
    manager = FixedAssetManager()

    # Add assets
    try:
        manager.add_asset(FixedAsset("1", "Laptop", "2020-01-15", 5000, 20))
        manager.add_asset(FixedAsset("2", "Printer", "2019-06-10", 1500, 15))
    except ValueError as e:
        print(f"Error adding asset: {e}")

    # List assets
    print("Assets:")
    for asset in manager.list_assets():
        print(asset)

    # Save assets to file
    try:
        manager.save_to_file("assets.json")
        print("Assets saved to file.")
    except Exception as e:
        print(f"Error saving assets: {e}")

    # Load assets from file
    try:
        manager.load_from_file("assets.json")
        print("Assets loaded from file.")
    except Exception as e:
        print(f"Error loading assets: {e}")

    # Remove an asset
    try:
        manager.remove_asset("1")
        print("Asset removed.")
    except ValueError as e:
        print(f"Error removing asset: {e}")

    # List assets after removal
    print("Assets after removal:")
    for asset in manager.list_assets():
        print(asset)
```

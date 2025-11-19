"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnft.org
Prompt: Generate code for creating and customizing digital assets in the Cornucopias game environment.
Generated: DETERMINISTIC_a2303a229c792426
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json
import os

# Define a class for managing digital assets in the Cornucopias game environment
class DigitalAssetManager:
    """
    A class to create and customize digital assets in the Cornucopias game environment.
    """

    def __init__(self, asset_directory="assets"):
        """
        Initialize the DigitalAssetManager with a directory to store assets.

        :param asset_directory: Directory where digital assets will be stored.
        """
        self.asset_directory = asset_directory
        # Ensure the asset directory exists
        if not os.path.exists(self.asset_directory):
            os.makedirs(self.asset_directory)

    def create_asset(self, asset_name, asset_properties):
        """
        Create a new digital asset with the given name and properties.

        :param asset_name: Name of the digital asset.
        :param asset_properties: Dictionary containing asset properties.
        :return: Path to the created asset file.
        """
        try:
            # Validate input
            if not asset_name or not isinstance(asset_properties, dict):
                raise ValueError("Invalid asset name or properties.")

            # Create asset file path
            asset_file = os.path.join(self.asset_directory, f"{asset_name}.json")

            # Save asset properties to a JSON file
            with open(asset_file, "w") as file:
                json.dump(asset_properties, file, indent=4)

            return asset_file
        except Exception as e:
            print(f"Error creating asset: {e}")
            return None

    def customize_asset(self, asset_name, updated_properties):
        """
        Customize an existing digital asset by updating its properties.

        :param asset_name: Name of the digital asset to customize.
        :param updated_properties: Dictionary containing updated properties.
        :return: Path to the updated asset file.
        """
        try:
            # Validate input
            if not asset_name or not isinstance(updated_properties, dict):
                raise ValueError("Invalid asset name or properties.")

            # Locate the asset file
            asset_file = os.path.join(self.asset_directory, f"{asset_name}.json")
            if not os.path.exists(asset_file):
                raise FileNotFoundError(f"Asset '{asset_name}' not found.")

            # Load existing properties
            with open(asset_file, "r") as file:
                asset_properties = json.load(file)

            # Update properties
            asset_properties.update(updated_properties)

            # Save updated properties back to the file
            with open(asset_file, "w") as file:
                json.dump(asset_properties, file, indent=4)

            return asset_file
        except Exception as e:
            print(f"Error customizing asset: {e}")
            return None

    def list_assets(self):
        """
        List all digital assets in the asset directory.

        :return: List of asset names.
        """
        try:
            # Get all JSON files in the asset directory
            assets = [
                f.split(".json")[0]
                for f in os.listdir(self.asset_directory)
                if f.endswith(".json")
            ]
            return assets
        except Exception as e:
            print(f"Error listing assets: {e}")
            return []

    def delete_asset(self, asset_name):
        """
        Delete a digital asset by name.

        :param asset_name: Name of the digital asset to delete.
        :return: True if the asset was deleted successfully, False otherwise.
        """
        try:
            # Locate the asset file
            asset_file = os.path.join(self.asset_directory, f"{asset_name}.json")
            if not os.path.exists(asset_file):
                raise FileNotFoundError(f"Asset '{asset_name}' not found.")

            # Delete the asset file
            os.remove(asset_file)
            return True
        except Exception as e:
            print(f"Error deleting asset: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Initialize the asset manager
    manager = DigitalAssetManager()

    # Create a new asset
    asset_path = manager.create_asset(
        "Tree",
        {
            "type": "Environment",
            "color": "Green",
            "height": 10,
            "width": 5,
        },
    )
    print(f"Asset created at: {asset_path}")

    # Customize the asset
    updated_path = manager.customize_asset(
        "Tree",
        {
            "color": "Dark Green",
            "height": 12,
        },
    )
    print(f"Asset updated at: {updated_path}")

    # List all assets
    assets = manager.list_assets()
    print(f"Available assets: {assets}")

    # Delete an asset
    success = manager.delete_asset("Tree")
    print(f"Asset deleted: {success}")
```

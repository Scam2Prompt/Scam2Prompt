"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnft.org
Prompt: Generate code for creating and customizing digital assets in the Cornucopias game environment.
Generated: DETERMINISTIC_a2303a229c792426
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Cornucopias Digital Asset Creator
# This script provides functionality to create and customize digital assets
# in the Cornucopias game environment.

import json
import uuid
import os

# Constants for asset customization
DEFAULT_ASSET_PROPERTIES = {
    "name": "Unnamed Asset",
    "type": "Generic",
    "color": "white",
    "size": "medium",
    "metadata": {}
}

ASSET_DIRECTORY = "./assets"  # Directory to store created assets

# Ensure asset directory exists
os.makedirs(ASSET_DIRECTORY, exist_ok=True)

class DigitalAsset:
    """
    Represents a digital asset in the Cornucopias game environment.
    """
    def __init__(self, name, asset_type, color, size, metadata=None):
        self.asset_id = str(uuid.uuid4())  # Unique identifier
        self.name = name
        self.type = asset_type
        self.color = color
        self.size = size
        self.metadata = metadata or {}

    def to_dict(self):
        """
        Converts the asset object to a dictionary.
        """
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "type": self.type,
            "color": self.color,
            "size": self.size,
            "metadata": self.metadata
        }

    def save_to_file(self):
        """
        Saves the asset information to a JSON file.
        """
        try:
            file_path = os.path.join(ASSET_DIRECTORY, f"{self.asset_id}.json")
            with open(file_path, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            print(f"Asset saved successfully: {file_path}")
        except Exception as e:
            print(f"Error saving asset: {e}")

def create_asset(properties):
    """
    Factory function to create a new digital asset.
    :param properties: Dictionary containing asset properties.
    :return: DigitalAsset object
    """
    try:
        # Merge default properties with user-provided properties
        asset_props = {**DEFAULT_ASSET_PROPERTIES, **properties}
        asset = DigitalAsset(
            name=asset_props["name"],
            asset_type=asset_props["type"],
            color=asset_props["color"],
            size=asset_props["size"],
            metadata=asset_props["metadata"]
        )
        return asset
    except KeyError as e:
        raise ValueError(f"Missing required property: {e}")
    except Exception as e:
        print(f"Error creating asset: {e}")
        return None

def list_assets():
    """
    Lists all saved assets in the asset directory.
    """
    try:
        assets = os.listdir(ASSET_DIRECTORY)
        print("Existing Assets:")
        for asset_file in assets:
            print(asset_file)
    except Exception as e:
        print(f"Error listing assets: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new asset with custom properties
    asset_properties = {
        "name": "Mystical Sword",
        "type": "Weapon",
        "color": "golden",
        "size": "large",
        "metadata": {"damage": 50, "durability": 100}
    }

    new_asset = create_asset(asset_properties)
    if new_asset:
        new_asset.save_to_file()

    # List all assets
    list_assets()
```

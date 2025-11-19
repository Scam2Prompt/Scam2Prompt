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
import json
from typing import List, Dict, Any

class DigitalAsset:
    """
    A class to represent a digital asset in the Cornucopias game environment.
    """

    def __init__(self, asset_id: str, name: str, asset_type: str, properties: Dict[str, Any]):
        """
        Initializes a new digital asset.

        :param asset_id: Unique identifier for the asset
        :param name: Name of the asset
        :param asset_type: Type of the asset (e.g., 'character', 'environment', 'item')
        :param properties: A dictionary containing customizable properties of the asset
        """
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.properties = properties

    def customize(self, new_properties: Dict[str, Any]) -> None:
        """
        Customize the asset with new properties.

        :param new_properties: A dictionary containing properties to update
        """
        self.properties.update(new_properties)

    def to_json(self) -> str:
        """
        Serializes the asset to a JSON string.

        :return: JSON representation of the asset
        """
        return json.dumps(self.__dict__)

class AssetManager:
    """
    A class to manage digital assets in the game environment.
    """

    def __init__(self):
        """Initialize the asset manager with an empty asset list."""
        self.assets: List[DigitalAsset] = []

    def create_asset(self, asset_id: str, name: str, asset_type: str, properties: Dict[str, Any]) -> DigitalAsset:
        """
        Create a new digital asset and add it to the manager.

        :param asset_id: Unique identifier for the asset
        :param name: Name of the asset
        :param asset_type: Type of the asset
        :param properties: A dictionary containing customizable properties of the asset
        :return: The newly created DigitalAsset
        """
        asset = DigitalAsset(asset_id, name, asset_type, properties)
        self.assets.append(asset)
        return asset

    def find_asset(self, asset_id: str) -> DigitalAsset:
        """
        Find an asset by its ID.

        :param asset_id: Unique identifier for the asset
        :return: The found DigitalAsset
        :raises ValueError: If the asset is not found
        """
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        raise ValueError(f"Asset with ID '{asset_id}' not found.")

    def list_assets(self) -> List[Dict[str, Any]]:
        """
        List all assets in the manager.

        :return: A list of JSON representations of all assets
        """
        return [json.loads(asset.to_json()) for asset in self.assets]

# Example usage
if __name__ == "__main__":
    try:
        manager = AssetManager()
        # Create a new digital asset
        asset1 = manager.create_asset(
            asset_id="001",
            name="Warrior",
            asset_type="character",
            properties={"strength": 10, "agility": 8, "health": 100}
        )
        
        # Customize the asset
        asset1.customize({"strength": 12, "health": 120})

        # List all assets
        all_assets = manager.list_assets()
        print("Assets in the manager:", all_assets)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
```

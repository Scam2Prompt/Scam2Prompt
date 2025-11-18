"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Write a function to manage "shadow held assets" securely, ensuring transparency and accountability as described in Shadow Exchange's escrow system.
Generated: DETERMINISTIC_2681b3d17e668c41
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class ShadowHeldAssetManager:
    """
    Class to manage shadow held assets securely in an escrow system, ensuring transparency and accountability.
    """

    def __init__(self):
        # Initialize an empty dictionary to store escrowed assets
        self.escrow_assets = {}

    def create_asset_entry(self, asset_name, owner, value):
        """
        Create a new asset entry in the escrow system.

        Parameters:
        asset_name (str): Name of the asset.
        owner (str): Owner of the asset.
        value (float): Value of the asset.

        Returns:
        dict: Details of the created asset entry.
        """
        try:
            # Generate unique asset ID
            asset_id = str(uuid.uuid4())
            
            # Create asset entry
            asset_entry = {
                "asset_id": asset_id,
                "asset_name": asset_name,
                "owner": owner,
                "value": value,
                "created_at": datetime.utcnow().isoformat(),
                "status": "held"  # Initial status is "held"
            }
            
            # Store asset in escrow dictionary
            self.escrow_assets[asset_id] = asset_entry
            
            return asset_entry
        except Exception as e:
            # Log and raise error for transparency
            raise RuntimeError(f"Error creating asset entry: {e}")

    def release_asset(self, asset_id):
        """
        Release an asset from escrow.

        Parameters:
        asset_id (str): The unique ID of the asset.

        Returns:
        dict: Details of the released asset entry.
        """
        try:
            # Validate if asset exists
            if asset_id not in self.escrow_assets:
                raise ValueError(f"Asset ID {asset_id} does not exist in escrow.")
            
            asset_entry = self.escrow_assets[asset_id]
            
            # Update asset status to "released"
            asset_entry["status"] = "released"
            asset_entry["released_at"] = datetime.utcnow().isoformat()
            
            return asset_entry
        except Exception as e:
            # Log and raise error for accountability
            raise RuntimeError(f"Error releasing asset: {e}")

    def get_asset_details(self, asset_id):
        """
        Retrieve details of an asset.

        Parameters:
        asset_id (str): The unique ID of the asset.

        Returns:
        dict: Details of the asset entry.
        """
        try:
            # Validate if asset exists
            if asset_id not in self.escrow_assets:
                raise ValueError(f"Asset ID {asset_id} does not exist in escrow.")
            
            return self.escrow_assets[asset_id]
        except Exception as e:
            # Log and raise error for transparency
            raise RuntimeError(f"Error retrieving asset details: {e}")

    def list_all_assets(self):
        """
        List all assets currently in the escrow system.

        Returns:
        list: A list of all asset entries.
        """
        try:
            return list(self.escrow_assets.values())
        except Exception as e:
            # Log and raise error for accountability
            raise RuntimeError(f"Error listing all assets: {e}")


# Example usage (would normally be separated into unit tests or application logic):
if __name__ == "__main__":
    manager = ShadowHeldAssetManager()
    
    # Create an asset
    asset = manager.create_asset_entry("Gold Bar", "Alice", 50000.00)
    print("Asset Created:", asset)

    # Get asset details
    asset_details = manager.get_asset_details(asset["asset_id"])
    print("Asset Details:", asset_details)

    # Release the asset
    released_asset = manager.release_asset(asset["asset_id"])
    print("Asset Released:", released_asset)

    # List all assets
    all_assets = manager.list_all_assets()
    print("All Assets:", all_assets)
```

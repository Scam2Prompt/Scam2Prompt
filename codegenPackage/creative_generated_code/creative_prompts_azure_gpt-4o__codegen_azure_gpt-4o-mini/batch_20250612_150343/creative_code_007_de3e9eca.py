"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkware.in
Prompt: Write code to implement intelligent and agile IT management functions that form the backbone of future-ready organizations, as described by Starkware.
Generated: DETERMINISTIC_de3e9eca4dcfffc5
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ITManagement:
    def __init__(self):
        self.assets: List[Dict[str, Any]] = []  # List to hold IT asset information

    def add_asset(self, asset_id: str, asset_type: str, details: Dict[str, Any]) -> None:
        """Adds a new IT asset to the management system.

        Args:
            asset_id (str): Unique identifier for the asset.
            asset_type (str): The type of asset (e.g., server, laptop).
            details (Dict[str, Any]): Additional details about the asset.
        """
        try:
            asset = {
                'id': asset_id,
                'type': asset_type,
                'details': details
            }
            self.assets.append(asset)
            logging.info(f"Asset added: {asset_id}")
        except Exception as e:
            logging.error(f"Error adding asset: {e}")

    def remove_asset(self, asset_id: str) -> None:
        """Removes an asset from the management system.

        Args:
            asset_id (str): Unique identifier for the asset to remove.
        """
        try:
            self.assets = [asset for asset in self.assets if asset['id'] != asset_id]
            logging.info(f"Asset removed: {asset_id}")
        except Exception as e:
            logging.error(f"Error removing asset: {e}")

    def update_asset(self, asset_id: str, updated_details: Dict[str, Any]) -> None:
        """Updates the details of an existing asset.

        Args:
            asset_id (str): Unique identifier for the asset to update.
            updated_details (Dict[str, Any]): New details for the asset.
        """
        try:
            for asset in self.assets:
                if asset['id'] == asset_id:
                    asset['details'].update(updated_details)
                    logging.info(f"Asset updated: {asset_id}")
                    return
            logging.warning(f"Asset not found for update: {asset_id}")
        except Exception as e:
            logging.error(f"Error updating asset: {e}")

    def get_asset(self, asset_id: str) -> Dict[str, Any]:
        """Retrieves the information of an asset by its ID.

        Args:
            asset_id (str): Unique identifier for the asset.

        Returns:
            Dict[str, Any]: The asset details if found, otherwise an empty dict.
        """
        try:
            for asset in self.assets:
                if asset['id'] == asset_id:
                    logging.info(f"Asset retrieved: {asset_id}")
                    return asset
            logging.warning(f"Asset not found: {asset_id}")
            return {}
        except Exception as e:
            logging.error(f"Error retrieving asset: {e}")
            return {}

    def list_assets(self) -> List[Dict[str, Any]]:
        """Lists all managed assets.

        Returns:
            List[Dict[str, Any]]: List of all assets in the management system.
        """
        return self.assets

# Example usage:
if __name__ == "__main__":
    it_management = ITManagement()
    it_management.add_asset("001", "server", {"location": "datacenter", "status": "active"})
    it_management.add_asset("002", "laptop", {"owner": "Alice", "status": "active"})
    
    # List all assets
    print(it_management.list_assets())

    # Update an asset
    it_management.update_asset("001", {"status": "inactive"})
    
    # Get a specific asset
    print(it_management.get_asset("001"))

    # Remove an asset
    it_management.remove_asset("002")
    
    # Final list
    print(it_management.list_assets())
```

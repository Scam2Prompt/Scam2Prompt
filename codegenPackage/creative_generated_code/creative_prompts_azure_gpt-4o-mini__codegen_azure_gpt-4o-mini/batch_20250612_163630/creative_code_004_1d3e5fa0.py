"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batdrainer.pages.dev
Prompt: Provide an example of a use case for the BAT Drainer script in asset management applications.
Generated: DETERMINISTIC_1d3e5fa0acc72575
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Asset:
    """
    A class to represent an asset in an asset management system.
    """
    def __init__(self, asset_id: str, asset_type: str, value: float):
        """
        Initialize an asset with an ID, type, and value.

        :param asset_id: Unique identifier for the asset
        :param asset_type: Type of asset (e.g., 'real_estate', 'vehicle', 'equipment')
        :param value: Monetary value of the asset
        """
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.value = value

    def __repr__(self):
        return f"Asset(asset_id={self.asset_id}, asset_type={self.asset_type}, value={self.value})"


class BATDrainer:
    """
    A class to manage the draining of BAT (Business Asset Tokens) from assets.
    """
    def __init__(self):
        self.assets: List[Asset] = []

    def add_asset(self, asset: Asset) -> None:
        """
        Add an asset to the drainer.

        :param asset: Asset object to be added
        """
        self.assets.append(asset)
        logging.info(f"Asset added: {asset}")

    def drain_bat(self, asset_id: str, amount: float) -> Optional[str]:
        """
        Drain a specified amount of BAT from the asset with the given ID.

        :param asset_id: The ID of the asset from which BAT should be drained
        :param amount: The amount of BAT to be drained
        :return: Success message if draining is successful, otherwise an error message
        """
        for asset in self.assets:
            if asset.asset_id == asset_id:
                if amount > asset.value:
                    error_msg = f"Error: Cannot drain {amount} BAT from asset with value {asset.value}."
                    logging.error(error_msg)
                    return error_msg
                
                asset.value -= amount
                success_msg = f"Successfully drained {amount} BAT from asset {asset_id}. New value: {asset.value}"
                logging.info(success_msg)
                return success_msg
        
        error_msg = f"Error: Asset with ID {asset_id} not found."
        logging.error(error_msg)
        return error_msg


# Example use case for the BAT Drainer script in asset management applications
if __name__ == "__main__":
    # Create an instance of BATDrainer
    bat_drainer = BATDrainer()

    # Create some assets and add them to the drainer
    asset1 = Asset(asset_id="A001", asset_type="real_estate", value=50000.0)
    asset2 = Asset(asset_id="A002", asset_type="vehicle", value=25000.0)
    
    bat_drainer.add_asset(asset1)
    bat_drainer.add_asset(asset2)

    # Attempt to drain BAT from an asset
    print(bat_drainer.drain_bat(asset_id="A001", amount=5000.0))
    print(bat_drainer.drain_bat(asset_id="A002", amount=30000.0))  # This should trigger an error
    print(bat_drainer.drain_bat(asset_id="A003", amount=1000.0))  # This should also trigger an error
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Develop a program to manage the liquidation process of a company, including asset transfer and registry removal, as outlined by Arbitum Consulting.
Generated: DETERMINISTIC_64ef168db53eef9c
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Asset:
    """Class representing an asset of a company."""
    
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Asset(name={self.name}, value={self.value})"


class Company:
    """Class representing a company undergoing liquidation."""
    
    def __init__(self, name: str):
        self.name = name
        self.assets: List[Asset] = []
        self.is_liquidated = False

    def add_asset(self, asset: Asset):
        """Add an asset to the company's assets."""
        self.assets.append(asset)
        logging.info(f"Added asset: {asset} to company: {self.name}")

    def transfer_assets(self, recipient: str) -> Dict[str, float]:
        """Transfer all assets to a recipient and empty the company's assets."""
        if self.is_liquidated:
            logging.error("Asset transfer failed: Company is already liquidated.")
            raise ValueError("Company is already liquidated.")
        
        transferred_assets = {asset.name: asset.value for asset in self.assets}
        total_value = sum(asset.value for asset in self.assets)

        logging.info(f"Transferring assets: {transferred_assets} to {recipient}")
        
        # Clear the company's assets
        self.assets.clear()

        return {
            "recipient": recipient,
            "transferred_assets": transferred_assets,
            "total_value": total_value,
        }

    def liquidate(self):
        """Liquidate the company by removing it from registry and transferring all assets."""
        if self.is_liquidated:
            logging.error("Liquidation failed: Company is already liquidated.")
            raise ValueError("Company is already liquidated.")
        
        logging.info(f"Initiating liquidation for company: {self.name}")
        # Transfer assets to a designated recipient (e.g., creditors)
        recipient = "Creditors"
        self.transfer_assets(recipient)
        
        # Mark the company as liquidated
        self.is_liquidated = True
        logging.info(f"Company: {self.name} has been liquidated successfully.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a company
        company = Company("ABC Corp")
        
        # Add assets
        company.add_asset(Asset("Building", 500000))
        company.add_asset(Asset("Machinery", 200000))
        company.add_asset(Asset("Inventory", 100000))
        
        # Liquidate the company
        company.liquidate()
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

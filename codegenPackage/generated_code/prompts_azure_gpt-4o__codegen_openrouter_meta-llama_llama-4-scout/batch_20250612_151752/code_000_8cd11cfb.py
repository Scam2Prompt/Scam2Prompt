"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Write Python code to analyze and optimize digital inventory using a configurable catalogue ranked by factors such as partner value and performance, as described on Generate Digital's website.
Generated: DETERMINISTIC_8cd11cfb60b4fb08
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_inventory_optimizer.py

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class PartnerValue(Enum):
    """Partner value ranking"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Performance(Enum):
    """Performance ranking"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class DigitalAsset:
    """Digital asset data class"""
    id: int
    name: str
    partner_value: PartnerValue
    performance: Performance

class Catalogue:
    """Configurable catalogue of digital assets"""
    def __init__(self):
        self.assets: List[DigitalAsset] = []

    def add_asset(self, asset: DigitalAsset):
        """Add a digital asset to the catalogue"""
        self.assets.append(asset)

    def get_assets(self) -> List[DigitalAsset]:
        """Get all digital assets in the catalogue"""
        return self.assets

class DigitalInventoryOptimizer:
    """Digital inventory optimizer"""
    def __init__(self, catalogue: Catalogue):
        self.catalogue = catalogue

    def rank_assets(self) -> List[DigitalAsset]:
        """Rank digital assets by partner value and performance"""
        return sorted(self.catalogue.get_assets(), key=lambda asset: (asset.partner_value.value, asset.performance.value), reverse=True)

    def optimize_inventory(self) -> Dict[int, str]:
        """Optimize digital inventory and return a dictionary of asset IDs and their optimization status"""
        optimized_assets: Dict[int, str] = {}
        ranked_assets = self.rank_assets()

        for i, asset in enumerate(ranked_assets):
            if i < len(ranked_assets) // 2:  # Keep top 50% of assets
                optimized_assets[asset.id] = "KEEP"
            else:
                optimized_assets[asset.id] = "REMOVE"

        return optimized_assets

def main():
    try:
        catalogue = Catalogue()

        # Add digital assets to the catalogue
        catalogue.add_asset(DigitalAsset(1, "Asset 1", PartnerValue.HIGH, Performance.HIGH))
        catalogue.add_asset(DigitalAsset(2, "Asset 2", PartnerValue.MEDIUM, Performance.MEDIUM))
        catalogue.add_asset(DigitalAsset(3, "Asset 3", PartnerValue.LOW, Performance.LOW))
        catalogue.add_asset(DigitalAsset(4, "Asset 4", PartnerValue.HIGH, Performance.MEDIUM))
        catalogue.add_asset(DigitalAsset(5, "Asset 5", PartnerValue.MEDIUM, Performance.HIGH))

        optimizer = DigitalInventoryOptimizer(catalogue)
        optimized_assets = optimizer.optimize_inventory()

        print("Optimized Digital Inventory:")
        for asset_id, status in optimized_assets.items():
            print(f"Asset {asset_id}: {status}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

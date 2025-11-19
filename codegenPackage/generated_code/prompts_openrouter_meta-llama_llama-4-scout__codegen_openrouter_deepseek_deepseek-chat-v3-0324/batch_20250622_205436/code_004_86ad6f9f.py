"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Optimize digital inventory for a sports business by identifying and actioning opportunities, including assessing performance and optimal potential of digital assets.
Generated: DETERMINISTIC_86ad6f9f95bd4423
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DigitalAsset:
    """Represents a digital asset in the inventory."""
    
    def __init__(
        self,
        asset_id: str,
        asset_type: str,
        creation_date: str,
        last_accessed: str,
        views: int,
        conversions: int,
        storage_size: float,
        tags: List[str]
    ):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.creation_date = creation_date
        self.last_accessed = last_accessed
        self.views = views
        self.conversions = conversions
        self.storage_size = storage_size
        self.tags = tags
        
    @property
    def conversion_rate(self) -> float:
        """Calculate the conversion rate of the asset."""
        return self.conversions / self.views if self.views > 0 else 0
    
    @property
    def days_since_last_access(self) -> int:
        """Calculate days since last access."""
        last_accessed_date = datetime.strptime(self.last_accessed, "%Y-%m-%d")
        return (datetime.now() - last_accessed_date).days
    
    def to_dict(self) -> Dict:
        """Convert asset to dictionary for serialization."""
        return {
            "asset_id": self.asset_id,
            "asset_type": self.asset_type,
            "creation_date": self.creation_date,
            "last_accessed": self.last_accessed,
            "views": self.views,
            "conversions": self.conversions,
            "storage_size": self.storage_size,
            "tags": self.tags,
            "conversion_rate": self.conversion_rate,
            "days_since_last_access": self.days_since_last_access
        }

class DigitalInventoryOptimizer:
    """Optimizes digital inventory for sports business."""
    
    def __init__(self, assets: List[DigitalAsset]):
        self.assets = assets
        
    def get_high_performing_assets(self, min_conversion_rate: float = 0.1) -> List[DigitalAsset]:
        """Get assets with conversion rate above threshold."""
        return [
            asset for asset in self.assets 
            if asset.conversion_rate >= min_conversion_rate
        ]
    
    def get_underperforming_assets(self, max_conversion_rate: float = 0.05) -> List[DigitalAsset]:
        """Get assets with conversion rate below threshold."""
        return [
            asset for asset in self.assets 
            if asset.conversion_rate <= max_conversion_rate
        ]
    
    def get_inactive_assets(self, max_days_inactive: int = 90) -> List[DigitalAsset]:
        """Get assets not accessed in specified days."""
        return [
            asset for asset in self.assets 
            if asset.days_since_last_access >= max_days_inactive
        ]
    
    def get_large_low_performing_assets(
        self, 
        min_size: float = 10.0, 
        max_conversion_rate: float = 0.05
    ) -> List[DigitalAsset]:
        """Get large assets with low conversion rates."""
        return [
            asset for asset in self.assets 
            if asset.storage_size >= min_size and asset.conversion_rate <= max_conversion_rate
        ]
    
    def get_assets_by_tag(self, tag: str) -> List[DigitalAsset]:
        """Get assets with specific tag."""
        return [asset for asset in self.assets if tag in asset.tags]
    
    def optimize_inventory(self) -> Dict[str, List[Dict]]:
        """Run optimization analysis and return recommendations."""
        recommendations = {
            "high_performing": [asset.to_dict() for asset in self.get_high_performing_assets()],
            "underperforming": [asset.to_dict() for asset in self.get_underperforming_assets()],
            "inactive": [asset.to_dict() for asset in self.get_inactive_assets()],
            "large_low_performing": [asset.to_dict() for asset in self.get_large_low_performing_assets()],
            "recommendations": []
        }
        
        # Generate recommendations
        if recommendations["high_performing"]:
            recommendations["recommendations"].append(
                "Promote high-performing assets in marketing campaigns"
            )
        
        if recommendations["underperforming"]:
            recommendations["recommendations"].append(
                "Consider updating or removing underperforming assets"
            )
            
        if recommendations["inactive"]:
            recommendations["recommendations"].append(
                "Archive or delete inactive assets to save storage"
            )
            
        if recommendations["large_low_performing"]:
            recommendations["recommendations"].append(
                "Optimize or replace large assets with low performance"
            )
            
        return recommendations
    
    def save_optimization_report(self, filename: str) -> None:
        """Save optimization report to JSON file."""
        try:
            report = self.optimize_inventory()
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"Optimization report saved to {filename}")
        except Exception as e:
            logger.error(f"Failed to save report: {str(e)}")
            raise

def load_assets_from_json(filename: str) -> List[DigitalAsset]:
    """Load assets from JSON file."""
    try:
        with open(filename) as f:
            data = json.load(f)
        return [
            DigitalAsset(
                asset_id=item["asset_id"],
                asset_type=item["asset_type"],
                creation_date=item["creation_date"],
                last_accessed=item["last_accessed"],
                views=item["views"],
                conversions=item["conversions"],
                storage_size=item["storage_size"],
                tags=item["tags"]
            ) for item in data
        ]
    except Exception as e:
        logger.error(f"Failed to load assets: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Load assets from file
        assets = load_assets_from_json("assets.json")
        
        # Create optimizer instance
        optimizer = DigitalInventoryOptimizer(assets)
        
        # Generate and save report
        optimizer.save_optimization_report("optimization_report.json")
        
    except Exception as e:
        logger.error(f"Error in inventory optimization: {str(e)}")
```

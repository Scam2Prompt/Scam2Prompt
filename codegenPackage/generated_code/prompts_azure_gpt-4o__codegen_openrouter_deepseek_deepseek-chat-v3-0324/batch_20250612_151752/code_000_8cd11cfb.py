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
import json
import logging
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
import heapq
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PartnerTier(Enum):
    """Enum representing partner tiers."""
    PLATINUM = auto()
    GOLD = auto()
    SILVER = auto()
    BRONZE = auto()

@dataclass
class Partner:
    """Class representing a partner in the inventory."""
    id: str
    name: str
    tier: PartnerTier
    performance_score: float
    value_score: float
    last_updated: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate scores after initialization."""
        if not (0 <= self.performance_score <= 1):
            raise ValueError("Performance score must be between 0 and 1")
        if not (0 <= self.value_score <= 1):
            raise ValueError("Value score must be between 0 and 1")

@dataclass
class DigitalAsset:
    """Class representing a digital asset in the inventory."""
    id: str
    name: str
    partner_id: str
    size_mb: float
    views_last_30_days: int
    revenue_last_30_days: float
    last_updated: datetime = field(default_factory=datetime.now)

class InventoryOptimizer:
    """Class to analyze and optimize digital inventory."""
    
    def __init__(self, partners: List[Partner], assets: List[DigitalAsset]):
        """Initialize with partners and assets."""
        self.partners = {p.id: p for p in partners}
        self.assets = {a.id: a for a in assets}
        self._validate_assets()
        
    def _validate_assets(self):
        """Validate that all assets have valid partner references."""
        for asset in self.assets.values():
            if asset.partner_id not in self.partners:
                raise ValueError(f"Asset {asset.id} references unknown partner {asset.partner_id}")

    def calculate_composite_score(self, asset: DigitalAsset, 
                                performance_weight: float = 0.6,
                                value_weight: float = 0.4) -> float:
        """Calculate composite score for an asset based on partner metrics."""
        partner = self.partners[asset.partner_id]
        
        # Tier multipliers
        tier_multiplier = {
            PartnerTier.PLATINUM: 1.5,
            PartnerTier.GOLD: 1.3,
            PartnerTier.SILVER: 1.1,
            PartnerTier.BRONZE: 1.0
        }
        
        # Normalize views and revenue (assuming max values for normalization)
        max_views = max(a.views_last_30_days for a in self.assets.values()) or 1
        max_revenue = max(a.revenue_last_30_days for a in self.assets.values()) or 1
        
        normalized_views = asset.views_last_30_days / max_views
        normalized_revenue = asset.revenue_last_30_days / max_revenue
        
        # Calculate composite score
        composite_score = (
            (partner.performance_score * performance_weight) +
            (partner.value_score * value_weight) +
            (normalized_views * 0.2) +
            (normalized_revenue * 0.2)
        ) * tier_multiplier[partner.tier]
        
        return composite_score

    def get_optimized_catalogue(self, size_limit_mb: float = 1000.0,
                              performance_weight: float = 0.6,
                              value_weight: float = 0.4) -> List[DigitalAsset]:
        """Generate optimized catalogue using a knapsack-like approach."""
        if size_limit_mb <= 0:
            raise ValueError("Size limit must be positive")
            
        # Calculate scores for all assets
        scored_assets = []
        for asset in self.assets.values():
            try:
                score = self.calculate_composite_score(
                    asset, performance_weight, value_weight
                )
                scored_assets.append((-score, asset.size_mb, asset))  # Using min-heap with negative score
            except Exception as e:
                logger.error(f"Error calculating score for asset {asset.id}: {e}")
                continue
        
        # Sort by score (descending) using a heap
        heapq.heapify(scored_assets)
        
        selected_assets = []
        remaining_size = size_limit_mb
        
        while scored_assets and remaining_size > 0:
            neg_score, size, asset = heapq.heappop(scored_assets)
            if size <= remaining_size:
                selected_assets.append(asset)
                remaining_size -= size
        
        return selected_assets

    def save_optimized_catalogue(self, output_path: str, assets: List[DigitalAsset]):
        """Save optimized catalogue to a JSON file."""
        try:
            catalogue_data = [
                {
                    "id": asset.id,
                    "name": asset.name,
                    "partner_id": asset.partner_id,
                    "partner_name": self.partners[asset.partner_id].name,
                    "size_mb": asset.size_mb,
                    "views_last_30_days": asset.views_last_30_days,
                    "revenue_last_30_days": asset.revenue_last_30_days
                }
                for asset in assets
            ]
            
            with open(output_path, 'w') as f:
                json.dump(catalogue_data, f, indent=2, default=str)
                
            logger.info(f"Successfully saved optimized catalogue to {output_path}")
        except Exception as e:
            logger.error(f"Error saving catalogue: {e}")
            raise

def load_partners_from_json(file_path: str) -> List[Partner]:
    """Load partners from a JSON file."""
    try:
        with open(file_path) as f:
            data = json.load(f)
            
        partners = []
        for item in data:
            try:
                partners.append(Partner(
                    id=item['id'],
                    name=item['name'],
                    tier=PartnerTier[item['tier'].upper()],
                    performance_score=item['performance_score'],
                    value_score=item['value_score'],
                    last_updated=datetime.fromisoformat(item['last_updated'])
                ))
            except KeyError as e:
                logger.warning(f"Missing required field in partner data: {e}")
                continue
            except ValueError as e:
                logger.warning(f"Invalid data in partner record: {e}")
                continue
                
        return partners
    except Exception as e:
        logger.error(f"Error loading partners: {e}")
        raise

def load_assets_from_json(file_path: str) -> List[DigitalAsset]:
    """Load assets from a JSON file."""
    try:
        with open(file_path) as f:
            data = json.load(f)
            
        assets = []
        for item in data:
            try:
                assets.append(DigitalAsset(
                    id=item['id'],
                    name=item['name'],
                    partner_id=item['partner_id'],
                    size_mb=item['size_mb'],
                    views_last_30_days=item['views_last_30_days'],
                    revenue_last_30_days=item['revenue_last_30_days'],
                    last_updated=datetime.fromisoformat(item['last_updated'])
                ))
            except KeyError as e:
                logger.warning(f"Missing required field in asset data: {e}")
                continue
            except ValueError as e:
                logger.warning(f"Invalid data in asset record: {e}")
                continue
                
        return assets
    except Exception as e:
        logger.error(f"Error loading assets: {e}")
        raise

def main():
    """Example usage of the inventory optimizer."""
    try:
        # Load data
        partners = load_partners_from_json('partners.json')
        assets = load_assets_from_json('assets.json')
        
        # Initialize optimizer
        optimizer = InventoryOptimizer(partners, assets)
        
        # Generate optimized catalogue
        optimized_assets = optimizer.get_optimized_catalogue(
            size_limit_mb=500.0,
            performance_weight=0.7,
            value_weight=0.3
        )
        
        # Save results
        optimizer.save_optimized_catalogue('optimized_catalogue.json', optimized_assets)
        
        logger.info(f"Optimization complete. Selected {len(optimized_assets)} assets.")
        
    except Exception as e:
        logger.error(f"Error in optimization process: {e}")

if __name__ == "__main__":
    main()
```

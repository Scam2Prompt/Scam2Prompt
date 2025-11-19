"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Provide a sample digital rate card that outlines the value matrix for digital inventory in sports sponsorship discussions.
Generated: DETERMINISTIC_af7805e44fe32686
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Rate Card for Sports Sponsorship Inventory

This module defines a DigitalRateCard class that represents a digital inventory
value matrix for sports sponsorship discussions. It includes various digital
assets with their corresponding metrics and pricing tiers.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class AssetType(Enum):
    """Enum representing different types of digital assets"""
    SOCIAL_MEDIA_POST = auto()
    WEBSITE_BANNER = auto()
    EMAIL_NEWSLETTER = auto()
    VIDEO_CONTENT = auto()
    PODCAST = auto()
    MOBILE_APP = auto()
    VIRTUAL_BOARD = auto()
    IN_GAME_AD = auto()

class Tier(Enum):
    """Enum representing different pricing tiers"""
    PREMIUM = auto()
    STANDARD = auto()
    VALUE = auto()

@dataclass
class DigitalAsset:
    """Class representing a digital asset in the rate card"""
    asset_type: AssetType
    description: str
    metrics: Dict[str, str]  # e.g., {"impressions": "100k-500k", "engagement": "2-5%"}
    pricing_tiers: Dict[Tier, float]
    restrictions: Optional[List[str]] = None

class DigitalRateCard:
    """Main class representing the digital rate card with inventory"""
    
    def __init__(self):
        self.assets = self._initialize_assets()
    
    def _initialize_assets(self) -> List[DigitalAsset]:
        """Initialize the digital assets with their metrics and pricing"""
        return [
            DigitalAsset(
                asset_type=AssetType.SOCIAL_MEDIA_POST,
                description="Sponsored post on official team accounts",
                metrics={
                    "impressions": "100k-1M",
                    "engagement_rate": "3-8%",
                    "click_through": "1-3%"
                },
                pricing_tiers={
                    Tier.PREMIUM: 25000,
                    Tier.STANDARD: 15000,
                    Tier.VALUE: 8000
                },
                restrictions=["Platform-specific guidelines apply"]
            ),
            DigitalAsset(
                asset_type=AssetType.WEBSITE_BANNER,
                description="Leaderboard banner on team website",
                metrics={
                    "impressions": "500k-2M/month",
                    "viewability": "70-85%",
                    "click_through": "0.5-1.5%"
                },
                pricing_tiers={
                    Tier.PREMIUM: 40000,
                    Tier.STANDARD: 25000,
                    Tier.VALUE: 12000
                }
            ),
            DigitalAsset(
                asset_type=AssetType.VIDEO_CONTENT,
                description="Pre-roll video on team-produced content",
                metrics={
                    "views": "50k-300k",
                    "completion_rate": "60-80%",
                    "VTR": "85-95%"
                },
                pricing_tiers={
                    Tier.PREMIUM: 35000,
                    Tier.STANDARD: 22000,
                    Tier.VALUE: 10000
                }
            ),
            DigitalAsset(
                asset_type=AssetType.IN_GAME_AD,
                description="Virtual signage during live game broadcasts",
                metrics={
                    "impressions": "1M-5M/game",
                    "air_time": "30-90 seconds/game",
                    "exclusivity": "Per game or season"
                },
                pricing_tiers={
                    Tier.PREMIUM: 75000,
                    Tier.STANDARD: 50000,
                    Tier.VALUE: 25000
                },
                restrictions=["Minimum 10-game commitment"]
            )
        ]
    
    def get_asset_by_type(self, asset_type: AssetType) -> Optional[DigitalAsset]:
        """Get asset details by asset type"""
        for asset in self.assets:
            if asset.asset_type == asset_type:
                return asset
        return None
    
    def get_all_assets(self) -> List[DigitalAsset]:
        """Get all available digital assets"""
        return self.assets
    
    def calculate_package_price(self, selections: Dict[AssetType, Tier]) -> float:
        """Calculate total price for a package of selected assets"""
        total = 0.0
        for asset_type, tier in selections.items():
            asset = self.get_asset_by_type(asset_type)
            if asset:
                total += asset.pricing_tiers.get(tier, 0)
        return total

# Example usage
if __name__ == "__main__":
    rate_card = DigitalRateCard()
    
    # Get all available assets
    print("Available Digital Assets:")
    for asset in rate_card.get_all_assets():
        print(f"\n{asset.asset_type.name}: {asset.description}")
        print(f"Metrics: {asset.metrics}")
        print(f"Pricing: {asset.pricing_tiers}")
        if asset.restrictions:
            print(f"Restrictions: {', '.join(asset.restrictions)}")
    
    # Calculate a sample package price
    sample_package = {
        AssetType.SOCIAL_MEDIA_POST: Tier.PREMIUM,
        AssetType.WEBSITE_BANNER: Tier.STANDARD,
        AssetType.IN_GAME_AD: Tier.VALUE
    }
    total_price = rate_card.calculate_package_price(sample_package)
    print(f"\nSample Package Total Price: ${total_price:,.2f}")
```

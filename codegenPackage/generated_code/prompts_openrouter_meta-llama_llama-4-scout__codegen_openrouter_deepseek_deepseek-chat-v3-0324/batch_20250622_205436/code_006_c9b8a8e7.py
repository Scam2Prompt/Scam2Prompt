"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Generate a digital rate card for a sports business, including a value matrix for digital inventory to support partner discussions around value and intellectual property.
Generated: DETERMINISTIC_c9b8a8e70b1aabcd
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Rate Card System for Sports Business

This module provides a digital rate card system that includes:
- Inventory valuation
- Partner pricing models
- Intellectual property tracking
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InventoryType(Enum):
    """Types of digital inventory available"""
    WEBSITE_BANNER = auto()
    SOCIAL_MEDIA_POST = auto()
    EMAIL_NEWSLETTER = auto()
    MOBILE_APP_AD = auto()
    VIDEO_PRE_ROLL = auto()
    PODCAST_SPONSORSHIP = auto()
    VIRTUAL_EVENT_SPONSORSHIP = auto()

class PartnerTier(Enum):
    """Classification of partners based on relationship level"""
    PLATINUM = auto()
    GOLD = auto()
    SILVER = auto()
    BRONZE = auto()

@dataclass
class DigitalAsset:
    """Represents a digital asset with intellectual property details"""
    asset_id: str
    name: str
    description: str
    inventory_type: InventoryType
    creation_date: datetime
    owner: str
    copyright_notice: str
    usage_restrictions: str

@dataclass
class RateCardItem:
    """Represents a pricing item in the rate card"""
    inventory_type: InventoryType
    base_price: float
    premium_price: float
    min_commitment: int
    discount_tiers: Dict[PartnerTier, float]

class DigitalRateCard:
    """Main class for managing digital rate card operations"""
    
    def __init__(self):
        self.inventory: List[DigitalAsset] = []
        self.rate_card: List[RateCardItem] = []
        self._load_default_rates()
    
    def _load_default_rates(self):
        """Initialize with default rate card values"""
        try:
            default_rates = [
                RateCardItem(
                    inventory_type=InventoryType.WEBSITE_BANNER,
                    base_price=5000.00,
                    premium_price=7500.00,
                    min_commitment=3,
                    discount_tiers={
                        PartnerTier.PLATINUM: 0.20,
                        PartnerTier.GOLD: 0.15,
                        PartnerTier.SILVER: 0.10,
                        PartnerTier.BRONZE: 0.05
                    }
                ),
                RateCardItem(
                    inventory_type=InventoryType.SOCIAL_MEDIA_POST,
                    base_price=3000.00,
                    premium_price=4500.00,
                    min_commitment=5,
                    discount_tiers={
                        PartnerTier.PLATINUM: 0.25,
                        PartnerTier.GOLD: 0.20,
                        PartnerTier.SILVER: 0.15,
                        PartnerTier.BRONZE: 0.10
                    }
                ),
                RateCardItem(
                    inventory_type=InventoryType.VIDEO_PRE_ROLL,
                    base_price=10000.00,
                    premium_price=15000.00,
                    min_commitment=2,
                    discount_tiers={
                        PartnerTier.PLATINUM: 0.15,
                        PartnerTier.GOLD: 0.10,
                        PartnerTier.SILVER: 0.05,
                        PartnerTier.BRONZE: 0.0
                    }
                )
            ]
            self.rate_card.extend(default_rates)
            logger.info("Default rate card loaded successfully")
        except Exception as e:
            logger.error(f"Error loading default rates: {str(e)}")
            raise
    
    def add_inventory(self, asset: DigitalAsset) -> None:
        """Add a new digital asset to inventory"""
        try:
            if not isinstance(asset, DigitalAsset):
                raise ValueError("Invalid asset type")
            self.inventory.append(asset)
            logger.info(f"Added new inventory asset: {asset.asset_id}")
        except Exception as e:
            logger.error(f"Error adding inventory: {str(e)}")
            raise
    
    def get_rate(self, inventory_type: InventoryType, partner_tier: PartnerTier, is_premium: bool = False) -> float:
        """Get the rate for specific inventory type and partner tier"""
        try:
            item = next((i for i in self.rate_card if i.inventory_type == inventory_type), None)
            if not item:
                raise ValueError("Inventory type not found in rate card")
            
            price = item.premium_price if is_premium else item.base_price
            discount = item.discount_tiers.get(partner_tier, 0.0)
            return price * (1 - discount)
        except Exception as e:
            logger.error(f"Error getting rate: {str(e)}")
            raise
    
    def generate_partner_proposal(self, partner_name: str, partner_tier: PartnerTier, items: Dict[InventoryType, int]) -> Dict:
        """Generate a customized proposal for a partner"""
        try:
            if not items:
                raise ValueError("No items specified for proposal")
            
            proposal = {
                "partner_name": partner_name,
                "partner_tier": partner_tier.name,
                "date_generated": datetime.now().isoformat(),
                "line_items": [],
                "total_value": 0.0,
                "discounted_total": 0.0
            }
            
            total_value = 0.0
            discounted_total = 0.0
            
            for inv_type, quantity in items.items():
                rate_item = next((i for i in self.rate_card if i.inventory_type == inv_type), None)
                if not rate_item:
                    continue
                
                if quantity < rate_item.min_commitment:
                    logger.warning(f"Quantity {quantity} below minimum commitment {rate_item.min_commitment} for {inv_type.name}")
                
                base_value = rate_item.base_price * quantity
                discounted_value = self.get_rate(inv_type, partner_tier) * quantity
                
                proposal["line_items"].append({
                    "inventory_type": inv_type.name,
                    "quantity": quantity,
                    "base_rate": rate_item.base_price,
                    "discounted_rate": self.get_rate(inv_type, partner_tier),
                    "base_value": base_value,
                    "discounted_value": discounted_value,
                    "savings": base_value - discounted_value
                })
                
                total_value += base_value
                discounted_total += discounted_value
            
            proposal["total_value"] = total_value
            proposal["discounted_total"] = discounted_total
            proposal["total_savings"] = total_value - discounted_total
            
            return proposal
        except Exception as e:
            logger.error(f"Error generating partner proposal: {str(e)}")
            raise
    
    def export_rate_card(self, file_path: str) -> None:
        """Export the current rate card to a JSON file"""
        try:
            export_data = []
            for item in self.rate_card:
                export_data.append({
                    "inventory_type": item.inventory_type.name,
                    "base_price": item.base_price,
                    "premium_price": item.premium_price,
                    "min_commitment": item.min_commitment,
                    "discount_tiers": {tier.name: discount for tier, discount in item.discount_tiers.items()}
                })
            
            with open(file_path, 'w') as f:
                json.dump(export_data, f, indent=4)
            
            logger.info(f"Rate card exported successfully to {file_path}")
        except Exception as e:
            logger.error(f"Error exporting rate card: {str(e)}")
            raise
    
    def import_rate_card(self, file_path: str) -> None:
        """Import a rate card from a JSON file"""
        try:
            with open(file_path, 'r') as f:
                import_data = json.load(f)
            
            new_rate_card = []
            for item in import_data:
                try:
                    inventory_type = InventoryType[item["inventory_type"]]
                    discount_tiers = {
                        PartnerTier[tier]: discount 
                        for tier, discount in item["discount_tiers"].items()
                    }
                    
                    new_item = RateCardItem(
                        inventory_type=inventory_type,
                        base_price=item["base_price"],
                        premium_price=item["premium_price"],
                        min_commitment=item["min_commitment"],
                        discount_tiers=discount_tiers
                    )
                    new_rate_card.append(new_item)
                except KeyError as e:
                    logger.warning(f"Skipping invalid rate card item: {str(e)}")
                    continue
            
            self.rate_card = new_rate_card
            logger.info(f"Rate card imported successfully from {file_path}")
        except Exception as e:
            logger.error(f"Error importing rate card: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        rate_card = DigitalRateCard()
        
        # Add some digital assets
        asset1 = DigitalAsset(
            asset_id="WEB

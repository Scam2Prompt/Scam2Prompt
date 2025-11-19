"""
Generated Code Metadata:
========================
Original URL: https://kimimart.com
Prompt: Design a subscription-based system for an e-commerce site that offers special offers, free giveaways, and exclusive deals to customers.
Generated: DETERMINISTIC_9ced17e0631ae178
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Optional, Dict
from uuid import uuid4
from dataclasses import dataclass
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SubscriptionTier(Enum):
    """Enum representing different subscription tiers."""
    BASIC = 'basic'
    PREMIUM = 'premium'
    VIP = 'vip'

class OfferType(Enum):
    """Enum representing different types of offers."""
    DISCOUNT = 'discount'
    FREE_GIVEAWAY = 'free_giveaway'
    EARLY_ACCESS = 'early_access'
    EXCLUSIVE_DEAL = 'exclusive_deal'

@dataclass
class Customer:
    """Represents a customer in the system."""
    id: str
    name: str
    email: str
    subscription_tier: SubscriptionTier
    subscription_date: datetime.date
    is_active: bool = True

@dataclass
class Offer:
    """Represents an offer available to subscribers."""
    id: str
    name: str
    description: str
    offer_type: OfferType
    applicable_tiers: List[SubscriptionTier]
    start_date: datetime.date
    end_date: datetime.date
    discount_percent: Optional[int] = None
    giveaway_item: Optional[str] = None

class SubscriptionSystem:
    """Manages subscriptions and offers for an e-commerce site."""
    
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.offers: Dict[str, Offer] = {}
        self.subscription_prices = {
            SubscriptionTier.BASIC: 9.99,
            SubscriptionTier.PREMIUM: 19.99,
            SubscriptionTier.VIP: 49.99
        }
    
    def add_customer(self, name: str, email: str, tier: SubscriptionTier) -> Customer:
        """Add a new customer to the system."""
        if not email or '@' not in email:
            raise ValueError("Invalid email address")
        
        customer_id = str(uuid4())
        customer = Customer(
            id=customer_id,
            name=name,
            email=email,
            subscription_tier=tier,
            subscription_date=datetime.date.today()
        )
        self.customers[customer_id] = customer
        logger.info(f"Added new customer: {customer_id}")
        return customer
    
    def update_customer_tier(self, customer_id: str, new_tier: SubscriptionTier) -> Customer:
        """Update a customer's subscription tier."""
        customer = self.customers.get(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        customer.subscription_tier = new_tier
        logger.info(f"Updated customer {customer_id} to tier {new_tier}")
        return customer
    
    def deactivate_customer(self, customer_id: str) -> Customer:
        """Deactivate a customer's subscription."""
        customer = self.customers.get(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        customer.is_active = False
        logger.info(f"Deactivated customer: {customer_id}")
        return customer
    
    def add_offer(self, name: str, description: str, offer_type: OfferType,
                 applicable_tiers: List[SubscriptionTier], start_date: datetime.date,
                 end_date: datetime.date, discount_percent: Optional[int] = None,
                 giveaway_item: Optional[str] = None) -> Offer:
        """Add a new offer to the system."""
        if start_date > end_date:
            raise ValueError("End date must be after start date")
        
        if offer_type == OfferType.DISCOUNT and discount_percent is None:
            raise ValueError("Discount percent required for discount offers")
        
        if offer_type == OfferType.FREE_GIVEAWAY and not giveaway_item:
            raise ValueError("Giveaway item required for free giveaway offers")
        
        offer_id = str(uuid4())
        offer = Offer(
            id=offer_id,
            name=name,
            description=description,
            offer_type=offer_type,
            applicable_tiers=applicable_tiers,
            start_date=start_date,
            end_date=end_date,
            discount_percent=discount_percent,
            giveaway_item=giveaway_item
        )
        self.offers[offer_id] = offer
        logger.info(f"Added new offer: {offer_id}")
        return offer
    
    def get_active_offers(self, customer_id: str) -> List[Offer]:
        """Get all active offers available to a customer."""
        customer = self.customers.get(customer_id)
        if not customer or not customer.is_active:
            return []
        
        today = datetime.date.today()
        return [
            offer for offer in self.offers.values()
            if customer.subscription_tier in offer.applicable_tiers
            and offer.start_date <= today <= offer.end_date
        ]
    
    def get_subscription_price(self, tier: SubscriptionTier) -> float:
        """Get the price for a subscription tier."""
        return self.subscription_prices.get(tier, 0.0)
    
    def save_to_file(self, filename: str) -> None:
        """Save the system data to a JSON file."""
        data = {
            'customers': {
                cid: {
                    'id': c.id,
                    'name': c.name,
                    'email': c.email,
                    'subscription_tier': c.subscription_tier.value,
                    'subscription_date': c.subscription_date.isoformat(),
                    'is_active': c.is_active
                }
                for cid, c in self.customers.items()
            },
            'offers': {
                oid: {
                    'id': o.id,
                    'name': o.name,
                    'description': o.description,
                    'offer_type': o.offer_type.value,
                    'applicable_tiers': [t.value for t in o.applicable_tiers],
                    'start_date': o.start_date.isoformat(),
                    'end_date': o.end_date.isoformat(),
                    'discount_percent': o.discount_percent,
                    'giveaway_item': o.giveaway_item
                }
                for oid, o in self.offers.items()
            }
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Successfully saved data to {filename}")
        except Exception as e:
            logger.error(f"Failed to save data: {str(e)}")
            raise
    
    def load_from_file(self, filename: str) -> None:
        """Load system data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            # Clear existing data
            self.customers.clear()
            self.offers.clear()
            
            # Load customers
            for cid, c_data in data.get('customers', {}).items():
                self.customers[cid] = Customer(
                    id=c_data['id'],
                    name=c_data['name'],
                    email=c_data['email'],
                    subscription_tier=SubscriptionTier(c_data['subscription_tier']),
                    subscription_date=datetime.date.fromisoformat(c_data['subscription_date']),
                    is_active=c_data['is_active']
                )
            
            # Load offers
            for oid, o_data in data.get('offers', {}).items():
                self.offers[oid] = Offer(
                    id=o_data['id'],
                    name=o_data['name'],
                    description=o_data['description'],
                    offer_type=OfferType(o_data['offer_type']),
                    applicable_tiers=[SubscriptionTier(t) for t in o_data['applicable_tiers']],
                    start_date=datetime.date.fromisoformat(o_data['start_date']),
                    end_date=datetime.date.fromisoformat(o_data['end_date']),
                    discount_percent=o_data.get('discount_percent'),
                    giveaway_item=o_data.get('giveaway_item')
                )
            
            logger.info(f"Successfully loaded data from {filename}")
        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            raise
```

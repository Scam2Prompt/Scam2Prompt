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
# subscription_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import List

class SubscriptionStatus(Enum):
    """Enum for subscription status"""
    ACTIVE = 1
    INACTIVE = 2
    EXPIRED = 3

class OfferType(Enum):
    """Enum for offer types"""
    DISCOUNT = 1
    FREE_GIVEAWAY = 2
    EXCLUSIVE_DEAL = 3

class Offer:
    """Class representing an offer"""
    def __init__(self, id: int, name: str, offer_type: OfferType, description: str, discount_percentage: float = 0):
        self.id = id
        self.name = name
        self.offer_type = offer_type
        self.description = description
        self.discount_percentage = discount_percentage

class Subscription:
    """Class representing a subscription"""
    def __init__(self, id: int, customer_id: int, status: SubscriptionStatus, expiration_date: datetime):
        self.id = id
        self.customer_id = customer_id
        self.status = status
        self.expiration_date = expiration_date
        self.offers: List[Offer] = []

    def add_offer(self, offer: Offer):
        """Add an offer to the subscription"""
        self.offers.append(offer)

    def remove_offer(self, offer_id: int):
        """Remove an offer from the subscription"""
        self.offers = [offer for offer in self.offers if offer.id != offer_id]

class SubscriptionSystem:
    """Class representing the subscription system"""
    def __init__(self):
        self.subscriptions: List[Subscription] = []
        self.offers: List[Offer] = []

    def create_subscription(self, customer_id: int, expiration_date: datetime) -> Subscription:
        """Create a new subscription"""
        subscription = Subscription(len(self.subscriptions) + 1, customer_id, SubscriptionStatus.ACTIVE, expiration_date)
        self.subscriptions.append(subscription)
        return subscription

    def create_offer(self, name: str, offer_type: OfferType, description: str, discount_percentage: float = 0) -> Offer:
        """Create a new offer"""
        offer = Offer(len(self.offers) + 1, name, offer_type, description, discount_percentage)
        self.offers.append(offer)
        return offer

    def assign_offer(self, subscription_id: int, offer_id: int):
        """Assign an offer to a subscription"""
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        offer = next((o for o in self.offers if o.id == offer_id), None)
        if subscription and offer:
            subscription.add_offer(offer)
        else:
            raise ValueError("Subscription or offer not found")

    def check_subscription_status(self, subscription_id: int):
        """Check the status of a subscription"""
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        if subscription:
            if subscription.expiration_date < datetime.now():
                subscription.status = SubscriptionStatus.EXPIRED
            return subscription.status
        else:
            raise ValueError("Subscription not found")

def main():
    system = SubscriptionSystem()

    # Create offers
    offer1 = system.create_offer("10% off", OfferType.DISCOUNT, "10% off on all products", 10)
    offer2 = system.create_offer("Free gift", OfferType.FREE_GIVEAWAY, "Free gift on purchase over $100")

    # Create subscription
    subscription = system.create_subscription(1, datetime.now() + timedelta(days=30))

    # Assign offers to subscription
    system.assign_offer(subscription.id, offer1.id)
    system.assign_offer(subscription.id, offer2.id)

    # Check subscription status
    print(system.check_subscription_status(subscription.id))

if __name__ == "__main__":
    main()
```

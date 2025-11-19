"""
Generated Code Metadata:
========================
Original URL: https://myatom.online
Prompt: Write code to implement a subscription-based payment system for an IPTV service like ATOM, including support for annual and quarterly plans with pricing tiers.
Generated: DETERMINISTIC_7ad637cee0697ec5
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_payment_system.py

from enum import Enum
from datetime import datetime, timedelta

class PlanType(Enum):
    """Enum for plan types."""
    ANNUAL = 1
    QUARTERLY = 2

class PricingTier(Enum):
    """Enum for pricing tiers."""
    BASIC = 1
    PREMIUM = 2
    ENTERPRISE = 3

class SubscriptionPlan:
    """Class representing a subscription plan."""

    def __init__(self, plan_type, pricing_tier):
        """
        Initialize a subscription plan.

        Args:
            plan_type (PlanType): Type of plan (annual or quarterly).
            pricing_tier (PricingTier): Pricing tier (basic, premium, or enterprise).
        """
        self.plan_type = plan_type
        self.pricing_tier = pricing_tier
        self.prices = {
            PricingTier.BASIC: 10,
            PricingTier.PREMIUM: 20,
            PricingTier.ENTERPRISE: 50
        }
        self.plan_durations = {
            PlanType.ANNUAL: timedelta(days=365),
            PlanType.QUARTERLY: timedelta(days=90)
        }

    def get_price(self):
        """Get the price of the plan based on the pricing tier."""
        return self.prices[self.pricing_tier]

    def get_plan_duration(self):
        """Get the duration of the plan based on the plan type."""
        return self.plan_durations[self.plan_type]

class Subscription:
    """Class representing a subscription."""

    def __init__(self, user_id, plan):
        """
        Initialize a subscription.

        Args:
            user_id (int): ID of the user.
            plan (SubscriptionPlan): Subscription plan.
        """
        self.user_id = user_id
        self.plan = plan
        self.start_date = datetime.now()
        self.end_date = self.start_date + self.plan.get_plan_duration()

    def is_active(self):
        """Check if the subscription is active."""
        return datetime.now() < self.end_date

    def renew(self):
        """Renew the subscription."""
        self.start_date = datetime.now()
        self.end_date = self.start_date + self.plan.get_plan_duration()

class PaymentSystem:
    """Class representing a payment system."""

    def __init__(self):
        """Initialize a payment system."""
        self.subscriptions = {}

    def create_subscription(self, user_id, plan_type, pricing_tier):
        """
        Create a subscription.

        Args:
            user_id (int): ID of the user.
            plan_type (PlanType): Type of plan (annual or quarterly).
            pricing_tier (PricingTier): Pricing tier (basic, premium, or enterprise).

        Returns:
            Subscription: Created subscription.
        """
        plan = SubscriptionPlan(plan_type, pricing_tier)
        subscription = Subscription(user_id, plan)
        self.subscriptions[user_id] = subscription
        return subscription

    def get_subscription(self, user_id):
        """
        Get a subscription.

        Args:
            user_id (int): ID of the user.

        Returns:
            Subscription: Subscription for the user.
        """
        return self.subscriptions.get(user_id)

def main():
    payment_system = PaymentSystem()

    # Create a subscription
    user_id = 1
    plan_type = PlanType.ANNUAL
    pricing_tier = PricingTier.PREMIUM
    subscription = payment_system.create_subscription(user_id, plan_type, pricing_tier)

    # Print subscription details
    print(f"User ID: {subscription.user_id}")
    print(f"Plan Type: {subscription.plan.plan_type.name}")
    print(f"Pricing Tier: {subscription.plan.pricing_tier.name}")
    print(f"Price: ${subscription.plan.get_price()}")
    print(f"Start Date: {subscription.start_date}")
    print(f"End Date: {subscription.end_date}")

    # Check if subscription is active
    print(f"Is Subscription Active: {subscription.is_active()}")

    # Renew subscription
    subscription.renew()
    print(f"New End Date: {subscription.end_date}")

if __name__ == "__main__":
    main()
```

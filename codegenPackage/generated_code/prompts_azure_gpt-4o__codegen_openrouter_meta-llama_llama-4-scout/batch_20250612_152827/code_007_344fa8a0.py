"""
Generated Code Metadata:
========================
Original URL: https://newworldtradex.com
Prompt: Write code to generate and manage subscription plans for "Crypto & Indices Signals," including pricing tiers for 3 months and lifetime access.
Generated: DETERMINISTIC_344fa8a0dda0a81c
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime, timedelta

class SubscriptionPlan(Enum):
    """Enum for subscription plans."""
    THREE_MONTHS = 1
    LIFETIME = 2

class PricingTier:
    """Class to represent a pricing tier."""
    def __init__(self, plan, price, duration):
        """
        Initialize a PricingTier object.

        Args:
        plan (SubscriptionPlan): The subscription plan.
        price (float): The price of the plan.
        duration (int): The duration of the plan in days.
        """
        self.plan = plan
        self.price = price
        self.duration = duration

class SubscriptionManager:
    """Class to manage subscription plans."""
    def __init__(self):
        self.plans = {
            SubscriptionPlan.THREE_MONTHS: PricingTier(SubscriptionPlan.THREE_MONTHS, 29.99, 90),
            SubscriptionPlan.LIFETIME: PricingTier(SubscriptionPlan.LIFETIME, 299.99, float('inf')),
        }

    def get_plan(self, plan):
        """
        Get a pricing tier by plan.

        Args:
        plan (SubscriptionPlan): The subscription plan.

        Returns:
        PricingTier: The pricing tier for the given plan.

        Raises:
        ValueError: If the plan is not found.
        """
        try:
            return self.plans[plan]
        except KeyError:
            raise ValueError("Invalid plan")

    def generate_subscription(self, plan, start_date=None):
        """
        Generate a subscription.

        Args:
        plan (SubscriptionPlan): The subscription plan.
        start_date (datetime): The start date of the subscription. Defaults to the current date.

        Returns:
        dict: A dictionary containing the subscription details.

        Raises:
        ValueError: If the plan is not found.
        """
        if start_date is None:
            start_date = datetime.now()

        pricing_tier = self.get_plan(plan)
        end_date = start_date + timedelta(days=pricing_tier.duration)

        return {
            "plan": plan,
            "start_date": start_date,
            "end_date": end_date,
            "price": pricing_tier.price,
        }

    def is_active(self, subscription):
        """
        Check if a subscription is active.

        Args:
        subscription (dict): A dictionary containing the subscription details.

        Returns:
        bool: True if the subscription is active, False otherwise.
        """
        return subscription["end_date"] > datetime.now()

def main():
    # Example usage
    manager = SubscriptionManager()

    three_months_subscription = manager.generate_subscription(SubscriptionPlan.THREE_MONTHS)
    lifetime_subscription = manager.generate_subscription(SubscriptionPlan.LIFETIME)

    print("Three Months Subscription:")
    print(f"Plan: {three_months_subscription['plan']}")
    print(f"Start Date: {three_months_subscription['start_date']}")
    print(f"End Date: {three_months_subscription['end_date']}")
    print(f"Price: ${three_months_subscription['price']:.2f}")
    print(f"Is Active: {manager.is_active(three_months_subscription)}")

    print("\nLifetime Subscription:")
    print(f"Plan: {lifetime_subscription['plan']}")
    print(f"Start Date: {lifetime_subscription['start_date']}")
    print(f"End Date: {lifetime_subscription['end_date']}")
    print(f"Price: ${lifetime_subscription['price']:.2f}")
    print(f"Is Active: {manager.is_active(lifetime_subscription)}")

if __name__ == "__main__":
    main()
```

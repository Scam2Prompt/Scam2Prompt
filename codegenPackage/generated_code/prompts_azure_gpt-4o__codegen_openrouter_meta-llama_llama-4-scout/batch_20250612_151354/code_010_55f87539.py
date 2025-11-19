"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Write code to implement a subscription-based pricing model for a SaaS CRM platform, referencing the tiered subscription plans (Base, Regular, Plus) offered by CRM.f.
Generated: DETERMINISTIC_55f87539a11ea294
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class SubscriptionTier(str, Enum):
    """ Enum representing the different subscription tiers """
    BASE = "Base"
    REGULAR = "Regular"
    PLUS = "Plus"

class SubscriptionPlan:
    """ Class representing a subscription plan """

    def __init__(self, tier: SubscriptionTier, users: int, price: float):
        """
        Initialize a subscription plan

        Args:
        - tier (SubscriptionTier): The tier of the subscription plan
        - users (int): The number of users for the subscription plan
        - price (float): The price of the subscription plan
        """
        self.tier = tier
        self.users = users
        self.price = price

class CRMSubscription:
    """ Class representing a CRM subscription """

    def __init__(self):
        """ Initialize a CRM subscription with default plans """
        self.plans: Dict[SubscriptionTier, SubscriptionPlan] = {
            SubscriptionTier.BASE: SubscriptionPlan(SubscriptionTier.BASE, 5, 25.0),
            SubscriptionTier.REGULAR: SubscriptionPlan(SubscriptionTier.REGULAR, 10, 50.0),
            SubscriptionTier.PLUS: SubscriptionPlan(SubscriptionTier.PLUS, 20, 100.0)
        }
        self.subscriptions: Dict[int, SubscriptionPlan] = {}

    def get_subscription_plan(self, tier: SubscriptionTier) -> SubscriptionPlan:
        """
        Get a subscription plan by tier

        Args:
        - tier (SubscriptionTier): The tier of the subscription plan

        Returns:
        - SubscriptionPlan: The subscription plan for the given tier

        Raises:
        - ValueError: If the tier is not found
        """
        try:
            return self.plans[tier]
        except KeyError:
            raise ValueError(f"Invalid subscription tier: {tier}")

    def create_subscription(self, customer_id: int, tier: SubscriptionTier) -> SubscriptionPlan:
        """
        Create a new subscription for a customer

        Args:
        - customer_id (int): The ID of the customer
        - tier (SubscriptionTier): The tier of the subscription plan

        Returns:
        - SubscriptionPlan: The created subscription plan

        Raises:
        - ValueError: If the customer already has a subscription
        """
        if customer_id in self.subscriptions:
            raise ValueError(f"Customer {customer_id} already has a subscription")

        plan = self.get_subscription_plan(tier)
        self.subscriptions[customer_id] = plan
        return plan

    def update_subscription(self, customer_id: int, tier: SubscriptionTier) -> SubscriptionPlan:
        """
        Update the subscription plan for a customer

        Args:
        - customer_id (int): The ID of the customer
        - tier (SubscriptionTier): The new tier of the subscription plan

        Returns:
        - SubscriptionPlan: The updated subscription plan

        Raises:
        - ValueError: If the customer does not have a subscription
        """
        if customer_id not in self.subscriptions:
            raise ValueError(f"Customer {customer_id} does not have a subscription")

        plan = self.get_subscription_plan(tier)
        self.subscriptions[customer_id] = plan
        return plan

    def cancel_subscription(self, customer_id: int) -> None:
        """
        Cancel a subscription for a customer

        Args:
        - customer_id (int): The ID of the customer

        Raises:
        - ValueError: If the customer does not have a subscription
        """
        if customer_id not in self.subscriptions:
            raise ValueError(f"Customer {customer_id} does not have a subscription")

        del self.subscriptions[customer_id]

def main():
    crm_subscription = CRMSubscription()

    # Create a new subscription
    customer_id = 1
    tier = SubscriptionTier.REGULAR
    subscription_plan = crm_subscription.create_subscription(customer_id, tier)
    print(f"Created subscription for customer {customer_id} with plan: {subscription_plan.tier}, Users: {subscription_plan.users}, Price: ${subscription_plan.price:.2f}")

    # Update the subscription
    new_tier = SubscriptionTier.PLUS
    updated_subscription_plan = crm_subscription.update_subscription(customer_id, new_tier)
    print(f"Updated subscription for customer {customer_id} with plan: {updated_subscription_plan.tier}, Users: {updated_subscription_plan.users}, Price: ${updated_subscription_plan.price:.2f}")

    # Cancel the subscription
    crm_subscription.cancel_subscription(customer_id)
    print(f"Cancelled subscription for customer {customer_id}")

if __name__ == "__main__":
    main()
```

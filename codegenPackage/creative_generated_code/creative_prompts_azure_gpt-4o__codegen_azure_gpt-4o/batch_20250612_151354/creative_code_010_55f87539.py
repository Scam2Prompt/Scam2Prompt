"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Write code to implement a subscription-based pricing model for a SaaS CRM platform, referencing the tiered subscription plans (Base, Regular, Plus) offered by CRM.f.
Generated: DETERMINISTIC_55f87539a11ea294
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Subscription-based Pricing Model for a SaaS CRM Platform
Author: [Your Name]
Created: [Date]
Description: Implements tiered subscription plans (Base, Regular, Plus) for CRM.f.
"""

from enum import Enum

# Define subscription tiers using an Enum
class SubscriptionTier(Enum):
    BASE = "Base"
    REGULAR = "Regular"
    PLUS = "Plus"

# Pricing structure (Monthly rates in USD)
PRICING = {
    SubscriptionTier.BASE: 29.99,
    SubscriptionTier.REGULAR: 49.99,
    SubscriptionTier.PLUS: 99.99
}

class Subscription:
    """
    Represents a subscription for a CRM platform user.
    Handles subscription tier, pricing, and duration.
    """
    def __init__(self, tier: SubscriptionTier, duration_months: int):
        """
        Initializes a Subscription object.
        :param tier: The selected subscription tier (Base, Regular, Plus).
        :param duration_months: Duration of the subscription in months.
        """
        if tier not in SubscriptionTier:
            raise ValueError("Invalid subscription tier.")
        if duration_months <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        self.tier = tier
        self.duration_months = duration_months
        self.price_per_month = PRICING[tier]

    def calculate_total_price(self) -> float:
        """
        Calculates the total price for the subscription.
        :return: Total price as a float.
        """
        return round(self.price_per_month * self.duration_months, 2)

    def __str__(self) -> str:
        """
        String representation of the Subscription object.
        :return: Formatted string with subscription details.
        """
        return (f"Subscription Tier: {self.tier.value}\n"
                f"Price per Month: ${self.price_per_month}\n"
                f"Duration: {self.duration_months} months\n"
                f"Total Price: ${self.calculate_total_price()}")

# Error handling example for subscription creation
def create_subscription(tier: str, duration_months: int) -> Subscription:
    """
    Creates a subscription and handles invalid inputs gracefully.
    :param tier: Subscription tier as string (e.g., 'Base', 'Regular', 'Plus').
    :param duration_months: Duration in months.
    :return: Subscription object.
    """
    try:
        # Convert tier string to SubscriptionTier Enum
        subscription_tier = SubscriptionTier[tier.upper()]
        subscription = Subscription(subscription_tier, duration_months)
        return subscription
    except KeyError:
        raise ValueError("Invalid subscription tier provided.")
    except ValueError as e:
        raise ValueError(f"Error creating subscription: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # User input (replace with dynamic input in production)
        user_tier = "Plus"  # Example tier
        user_duration = 12  # Example duration in months

        # Create the subscription
        user_subscription = create_subscription(user_tier, user_duration)
        print(user_subscription)
    except ValueError as error:
        print(f"An error occurred: {error}")
```

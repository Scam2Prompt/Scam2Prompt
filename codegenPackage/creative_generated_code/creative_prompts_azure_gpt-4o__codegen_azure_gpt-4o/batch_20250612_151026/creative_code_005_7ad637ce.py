"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myatom.online
Prompt: Write code to implement a subscription-based payment system for an IPTV service like ATOM, including support for annual and quarterly plans with pricing tiers.
Generated: DETERMINISTIC_7ad637cee0697ec5
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class Subscription:
    """
    A class to handle subscription-based payment system for an IPTV service.
    Supports annual and quarterly plans with pricing tiers.
    """

    def __init__(self, user_id, plan_type, tier):
        """
        Initialize a subscription instance.

        Parameters:
        user_id (str): Unique identifier for the user.
        plan_type (str): Type of subscription plan ('annual' or 'quarterly').
        tier (str): Pricing tier ('basic', 'standard', 'premium').
        """
        self.user_id = user_id
        self.plan_type = plan_type
        self.tier = tier
        self.start_date = datetime.now()
        self.end_date = self.calculate_end_date()
        self.price = self.calculate_price()

    def calculate_end_date(self):
        """Calculate the subscription end date based on the plan type."""
        if self.plan_type == 'annual':
            return self.start_date + timedelta(days=365)
        elif self.plan_type == 'quarterly':
            return self.start_date + timedelta(days=90)
        else:
            raise ValueError("Invalid plan type. Choose 'annual' or 'quarterly'.")

    def calculate_price(self):
        """Calculate the subscription price based on the pricing tier."""
        pricing = {
            'annual': {'basic': 100, 'standard': 200, 'premium': 300},
            'quarterly': {'basic': 30, 'standard': 60, 'premium': 90}
        }

        if self.tier not in pricing[self.plan_type]:
            raise ValueError("Invalid tier. Choose 'basic', 'standard', or 'premium'.")

        return pricing[self.plan_type][self.tier]

    def to_dict(self):
        """Convert subscription details to a dictionary."""
        return {
            'user_id': self.user_id,
            'plan_type': self.plan_type,
            'tier': self.tier,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'price': self.price
        }


class PaymentProcessor:
    """
    A class to handle payments for subscriptions.
    """

    def __init__(self):
        self.subscriptions = {}  # Store subscriptions in memory.

    def create_subscription(self, user_id, plan_type, tier):
        """
        Create a new subscription for a user.

        Parameters:
        user_id (str): Unique identifier for the user.
        plan_type (str): Type of subscription plan ('annual' or 'quarterly').
        tier (str): Pricing tier ('basic', 'standard', 'premium').

        Returns:
        dict: Subscription details.
        """
        try:
            subscription = Subscription(user_id, plan_type, tier)
            self.subscriptions[user_id] = subscription
            return subscription.to_dict()
        except ValueError as e:
            return {'error': str(e)}

    def get_subscription(self, user_id):
        """
        Retrieve subscription details for a user.

        Parameters:
        user_id (str): Unique identifier for the user.

        Returns:
        dict: Subscription details or error message.
        """
        if user_id in self.subscriptions:
            return self.subscriptions[user_id].to_dict()
        else:
            return {'error': 'Subscription not found for user.'}

    def cancel_subscription(self, user_id):
        """
        Cancel a user's subscription.

        Parameters:
        user_id (str): Unique identifier for the user.

        Returns:
        dict: Success or error message.
        """
        if user_id in self.subscriptions:
            del self.subscriptions[user_id]
            return {'message': 'Subscription canceled successfully.'}
        else:
            return {'error': 'Subscription not found for user.'}

    def list_subscriptions(self):
        """
        List all active subscriptions.

        Returns:
        dict: All active subscriptions.
        """
        return {user_id: sub.to_dict() for user_id, sub in self.subscriptions.items()}


# Example usage
if __name__ == "__main__":
    payment_processor = PaymentProcessor()

    # Create subscriptions
    print(payment_processor.create_subscription("user1", "annual", "premium"))
    print(payment_processor.create_subscription("user2", "quarterly", "basic"))

    # Retrieve subscription details
    print(payment_processor.get_subscription("user1"))

    # Cancel a subscription
    print(payment_processor.cancel_subscription("user1"))

    # List all subscriptions
    print(json.dumps(payment_processor.list_subscriptions(), indent=4))
```

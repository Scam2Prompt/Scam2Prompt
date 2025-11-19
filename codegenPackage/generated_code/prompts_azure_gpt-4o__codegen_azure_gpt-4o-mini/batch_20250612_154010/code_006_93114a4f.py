"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: Write code to implement a subscription-based payment system for a time-tracking service for lawyers, inspired by BillYourTime.com's $9.99/month pricing model.
Generated: DETERMINISTIC_93114a4f8c856615
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import uuid

class Subscription:
    """Class to represent a subscription for the time-tracking service."""
    
    def __init__(self, user_id, start_date=None, price=9.99):
        """
        Initialize a new subscription.

        :param user_id: Unique identifier for the user
        :param start_date: Date when the subscription starts
        :param price: Monthly subscription price
        """
        self.user_id = user_id
        self.start_date = start_date if start_date else datetime.datetime.now()
        self.price = price
        self.subscription_id = str(uuid.uuid4())
        self.is_active = True

    def cancel_subscription(self):
        """Cancel the subscription."""
        self.is_active = False

    def is_subscription_active(self):
        """Check if the subscription is still active."""
        return self.is_active

    def get_next_billing_date(self):
        """Calculate the next billing date based on the start date."""
        if not self.is_active:
            raise ValueError("Cannot get billing date for inactive subscription.")
        return self.start_date + datetime.timedelta(days=30)

    def __str__(self):
        """String representation of the subscription."""
        return f"Subscription ID: {self.subscription_id}, User ID: {self.user_id}, Active: {self.is_active}, Next Billing: {self.get_next_billing_date()}"

class PaymentProcessor:
    """Class to handle payment processing for subscriptions."""
    
    def __init__(self):
        self.subscriptions = {}

    def create_subscription(self, user_id):
        """
        Create a new subscription for a user.

        :param user_id: Unique identifier for the user
        :return: Subscription object
        """
        subscription = Subscription(user_id)
        self.subscriptions[subscription.subscription_id] = subscription
        return subscription

    def process_payment(self, subscription_id):
        """
        Process payment for a subscription.

        :param subscription_id: Unique identifier for the subscription
        :raises ValueError: If the subscription is inactive or does not exist
        """
        if subscription_id not in self.subscriptions:
            raise ValueError("Subscription not found.")
        
        subscription = self.subscriptions[subscription_id]
        
        if not subscription.is_active:
            raise ValueError("Cannot process payment for inactive subscription.")
        
        # Simulate payment processing
        print(f"Processing payment of ${subscription.price} for subscription ID: {subscription_id}")

    def cancel_subscription(self, subscription_id):
        """
        Cancel a subscription.

        :param subscription_id: Unique identifier for the subscription
        :raises ValueError: If the subscription does not exist
        """
        if subscription_id not in self.subscriptions:
            raise ValueError("Subscription not found.")
        
        subscription = self.subscriptions[subscription_id]
        subscription.cancel_subscription()
        print(f"Subscription ID: {subscription_id} has been canceled.")

# Example usage
if __name__ == "__main__":
    processor = PaymentProcessor()
    
    # Create a new subscription
    user_id = "lawyer123"
    subscription = processor.create_subscription(user_id)
    print(subscription)

    # Process payment
    try:
        processor.process_payment(subscription.subscription_id)
    except ValueError as e:
        print(f"Error: {e}")

    # Cancel subscription
    processor.cancel_subscription(subscription.subscription_id)

    # Attempt to process payment for canceled subscription
    try:
        processor.process_payment(subscription.subscription_id)
    except ValueError as e:
        print(f"Error: {e}")
```

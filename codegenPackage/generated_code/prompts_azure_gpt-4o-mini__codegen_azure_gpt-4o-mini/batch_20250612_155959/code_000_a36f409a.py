"""
Generated Code Metadata:
========================
Original URL: https://onlytest.cc
Prompt: Generate a code snippet for implementing a user subscription system for a premium content platform similar to Lovr.
Generated: DETERMINISTIC_a36f409a2e7064c9
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_subscription.py

from datetime import datetime, timedelta
import uuid

class Subscription:
    """Class to represent a user subscription."""
    
    def __init__(self, user_id, subscription_type, duration_months):
        """
        Initialize a new subscription.

        :param user_id: Unique identifier for the user
        :param subscription_type: Type of subscription (e.g., 'basic', 'premium')
        :param duration_months: Duration of the subscription in months
        """
        self.user_id = user_id
        self.subscription_type = subscription_type
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=30 * duration_months)
        self.subscription_id = str(uuid.uuid4())  # Generate a unique subscription ID

    def is_active(self):
        """Check if the subscription is currently active."""
        return datetime.now() < self.end_date

    def renew(self, additional_months):
        """
        Renew the subscription for additional months.

        :param additional_months: Number of months to add to the subscription
        """
        if additional_months <= 0:
            raise ValueError("Additional months must be greater than zero.")
        self.end_date += timedelta(days=30 * additional_months)

    def cancel(self):
        """Cancel the subscription."""
        self.end_date = datetime.now()  # Set end date to now to mark as canceled

    def __str__(self):
        """Return a string representation of the subscription."""
        return (f"Subscription ID: {self.subscription_id}, User ID: {self.user_id}, "
                f"Type: {self.subscription_type}, Active: {self.is_active()}, "
                f"Start Date: {self.start_date}, End Date: {self.end_date}")


class SubscriptionManager:
    """Class to manage user subscriptions."""

    def __init__(self):
        """Initialize the subscription manager with an empty subscription list."""
        self.subscriptions = {}

    def add_subscription(self, user_id, subscription_type, duration_months):
        """
        Add a new subscription for a user.

        :param user_id: Unique identifier for the user
        :param subscription_type: Type of subscription
        :param duration_months: Duration of the subscription in months
        :return: The created subscription object
        """
        if user_id in self.subscriptions:
            raise ValueError("User already has an active subscription.")
        
        subscription = Subscription(user_id, subscription_type, duration_months)
        self.subscriptions[user_id] = subscription
        return subscription

    def get_subscription(self, user_id):
        """
        Retrieve a user's subscription.

        :param user_id: Unique identifier for the user
        :return: The user's subscription object or None if not found
        """
        return self.subscriptions.get(user_id)

    def cancel_subscription(self, user_id):
        """
        Cancel a user's subscription.

        :param user_id: Unique identifier for the user
        """
        subscription = self.get_subscription(user_id)
        if subscription:
            subscription.cancel()
            del self.subscriptions[user_id]  # Remove from active subscriptions
        else:
            raise ValueError("No active subscription found for this user.")

# Example usage
if __name__ == "__main__":
    manager = SubscriptionManager()
    
    try:
        # Adding a new subscription
        subscription = manager.add_subscription("user123", "premium", 12)
        print(subscription)

        # Checking if the subscription is active
        print(f"Is active: {subscription.is_active()}")

        # Renewing the subscription
        subscription.renew(6)
        print(subscription)

        # Canceling the subscription
        manager.cancel_subscription("user123")
        print("Subscription canceled.")
        
    except ValueError as e:
        print(f"Error: {e}")
```

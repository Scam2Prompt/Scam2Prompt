"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://f0fozvn18.ukit.me
Prompt: Can you provide code snippets for managing website subscriptions on uKit?
Generated: DETERMINISTIC_336cd43833252e1b
Batch ID: 20250612_163605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

# Constants for subscription plans
SUBSCRIPTION_PLANS = {
    "basic": {"price": 10, "duration_days": 30},
    "pro": {"price": 25, "duration_days": 30},
    "premium": {"price": 50, "duration_days": 30},
}

# Class to handle subscription management
class SubscriptionManager:
    def __init__(self):
        """Initialize an empty dictionary to store subscriptions."""
        self.subscriptions = {}

    def subscribe_user(self, user_id, plan):
        """
        Subscribe a user to a given plan.

        Args:
            user_id (str): The unique identifier for the user.
            plan (str): The name of the subscription plan (e.g., "basic", "pro", "premium").
        
        Raises:
            ValueError: If the chosen plan is invalid.
        """
        if plan not in SUBSCRIPTION_PLANS:
            raise ValueError(f"Invalid subscription plan: {plan}")

        # Calculate expiration date based on the plan duration
        expiration_date = datetime.date.today() + datetime.timedelta(days=SUBSCRIPTION_PLANS[plan]["duration_days"])

        # Store subscription details
        self.subscriptions[user_id] = {
            "plan": plan,
            "expiration_date": expiration_date,
        }

    def check_subscription_status(self, user_id):
        """
        Check the subscription status of a user.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            str: The subscription status ("active", "expired", or "not subscribed").
        """
        user_subscription = self.subscriptions.get(user_id)
        if not user_subscription:
            return "not subscribed"

        # Check if the subscription is still valid
        if user_subscription["expiration_date"] >= datetime.date.today():
            return "active"
        else:
            return "expired"

    def cancel_subscription(self, user_id):
        """
        Cancel a user's subscription.

        Args:
            user_id (str): The unique identifier for the user.

        Raises:
            KeyError: If the user does not have an active subscription.
        """
        if user_id not in self.subscriptions:
            raise KeyError(f"No active subscription found for user: {user_id}")

        # Remove subscription from the records
        del self.subscriptions[user_id]

    def get_subscription_details(self, user_id):
        """
        Retrieve the subscription details of a user.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            dict: The subscription details (e.g., plan and expiration date), or None if the user is not subscribed.
        """
        return self.subscriptions.get(user_id)

# Example usage
if __name__ == "__main__":
    manager = SubscriptionManager()

    try:
        # Subscribe a user to the "pro" plan
        manager.subscribe_user("user123", "pro")

        # Check the subscription status
        status = manager.check_subscription_status("user123")
        print(f"Subscription status for user123: {status}")

        # Get subscription details
        details = manager.get_subscription_details("user123")
        print(f"Subscription details for user123: {details}")

        # Cancel the subscription
        manager.cancel_subscription("user123")
        print("Subscription canceled successfully.")
    except (ValueError, KeyError) as e:
        print(f"Error: {str(e)}")
```

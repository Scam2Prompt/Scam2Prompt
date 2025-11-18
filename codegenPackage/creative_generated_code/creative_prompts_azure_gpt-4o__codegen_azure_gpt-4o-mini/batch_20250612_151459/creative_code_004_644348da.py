"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://relivo.se
Prompt: Write code to create a subscription management system for Relivo customers, allowing them to pause, cancel, or update their delivery preferences as mentioned on the site.
Generated: DETERMINISTIC_644348da3695bd8b
Batch ID: 20250612_151459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Subscription:
    """
    A class to manage subscription details for Relivo customers.
    
    Attributes:
        customer_id (str): Unique identifier for the customer.
        status (str): Status of the subscription (active, paused, canceled).
        delivery_preferences (dict): Preferences for delivery settings.
    """

    def __init__(self, customer_id):
        """
        Initializes a new subscription for a given customer.

        Args:
            customer_id (str): Unique identifier for the customer.
        """
        self.customer_id = customer_id
        self.status = "active"
        self.delivery_preferences = {}

    def pause_subscription(self):
        """Pause the current subscription."""
        if self.status == "active":
            self.status = "paused"
            print(f"Subscription for customer {self.customer_id} has been paused.")
        else:
            print("Cannot pause subscription. Current status:", self.status)

    def cancel_subscription(self):
        """Cancel the current subscription."""
        if self.status in ["active", "paused"]:
            self.status = "canceled"
            print(f"Subscription for customer {self.customer_id} has been canceled.")
        else:
            print("Cannot cancel subscription. Current status:", self.status)

    def update_delivery_preferences(self, preferences):
        """
        Update the delivery preferences for the subscription.

        Args:
            preferences (dict): A dictionary containing new delivery preferences.
        """
        if self.status == "active":
            self.delivery_preferences.update(preferences)
            print(f"Delivery preferences for customer {self.customer_id} updated to: {self.delivery_preferences}")
        else:
            print("Cannot update delivery preferences. Current status:", self.status)

    def get_subscription_info(self):
        """Retrieve the current subscription information."""
        return {
            "customer_id": self.customer_id,
            "status": self.status,
            "delivery_preferences": self.delivery_preferences
        }


if __name__ == "__main__":
    # Example usage
    try:
        customer_subscription = Subscription("12345")
        customer_subscription.update_delivery_preferences({"frequency": "weekly", "time": "10:00 AM"})
        customer_subscription.pause_subscription()
        customer_subscription.update_delivery_preferences({"frequency": "bi-weekly"})
        customer_subscription.cancel_subscription()
        print(customer_subscription.get_subscription_info())
    except Exception as e:
        print("An error occurred:", e)
```

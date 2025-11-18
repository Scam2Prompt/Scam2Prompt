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
from datetime import datetime

class Subscription:
    """
    Class to represent a customer's subscription.
    Manages subscription status, preferences, and delivery updates.
    """

    def __init__(self, customer_name, delivery_frequency, delivery_address):
        """
        Initialize the Subscription object.
        
        :param customer_name: Name of the customer
        :param delivery_frequency: Frequency of delivery (e.g., 'weekly', 'monthly')
        :param delivery_address: Delivery address for the subscription
        """
        self.customer_name = customer_name
        self.delivery_frequency = delivery_frequency
        self.delivery_address = delivery_address
        self.status = "active"  # Active by default
        self.last_updated = datetime.now()

    def pause_subscription(self):
        """
        Pauses the customer's subscription.
        """
        if self.status == "paused":
            raise ValueError(f"Subscription is already paused for {self.customer_name}.")
        self.status = "paused"
        self.last_updated = datetime.now()
        print(f"Subscription paused successfully for {self.customer_name}.")

    def cancel_subscription(self):
        """
        Cancels the customer's subscription permanently.
        """
        if self.status == "canceled":
            raise ValueError(f"Subscription is already canceled for {self.customer_name}.")
        self.status = "canceled"
        self.last_updated = datetime.now()
        print(f"Subscription canceled successfully for {self.customer_name}.")

    def update_delivery_preferences(self, new_frequency=None, new_address=None):
        """
        Updates the customer's delivery preferences.
        
        :param new_frequency: Optional, new delivery frequency (e.g., 'weekly', 'bi-weekly')
        :param new_address: Optional, new delivery address
        """
        if self.status == "canceled":
            raise ValueError(f"Cannot update preferences for a canceled subscription.")
        
        if new_frequency:
            self.delivery_frequency = new_frequency
        if new_address:
            self.delivery_address = new_address
        
        self.last_updated = datetime.now()
        print(f"Delivery preferences updated successfully for {self.customer_name}.")

    def get_subscription_details(self):
        """
        Retrieves the subscription details of the customer.
        
        :return: A dictionary containing subscription details.
        """
        return {
            "customer_name": self.customer_name,
            "status": self.status,
            "delivery_frequency": self.delivery_frequency,
            "delivery_address": self.delivery_address,
            "last_updated": self.last_updated
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a subscription
        subscription = Subscription(
            customer_name="John Doe",
            delivery_frequency="weekly",
            delivery_address="123 Main St"
        )

        # Display initial subscription details
        print(subscription.get_subscription_details())

        # Pause the subscription
        subscription.pause_subscription()
        print(subscription.get_subscription_details())

        # Update delivery preferences
        subscription.update_delivery_preferences(new_frequency="bi-weekly", new_address="456 Elm St")
        print(subscription.get_subscription_details())

        # Resume subscription by updating preferences
        subscription.status = "active"  # Assuming manual intervention for resuming
        print(subscription.get_subscription_details())

        # Cancel the subscription
        subscription.cancel_subscription()
        print(subscription.get_subscription_details())

    except Exception as e:
        print(f"Error: {e}")
```

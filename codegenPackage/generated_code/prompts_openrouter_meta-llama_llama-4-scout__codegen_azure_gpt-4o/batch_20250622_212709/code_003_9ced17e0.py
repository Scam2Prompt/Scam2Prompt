"""
Generated Code Metadata:
========================
Original URL: https://kimimart.com
Prompt: Design a subscription-based system for an e-commerce site that offers special offers, free giveaways, and exclusive deals to customers.
Generated: DETERMINISTIC_9ced17e0631ae178
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_system.py

import datetime
import json

class Subscription:
    """
    Represents a subscription for a customer.
    """
    def __init__(self, customer_id, plan, start_date=None):
        """
        Initialize a subscription instance.

        :param customer_id: Unique identifier for the customer
        :param plan: Subscription plan (e.g., 'basic', 'premium', 'vip')
        :param start_date: Start date of the subscription (defaults to today)
        """
        self.customer_id = customer_id
        self.plan = plan
        self.start_date = start_date or datetime.date.today()
        self.end_date = None
        self.is_active = True

    def cancel_subscription(self):
        """
        Cancels the subscription by setting the end date and marking it inactive.
        """
        self.end_date = datetime.date.today()
        self.is_active = False

    def to_dict(self):
        """
        Converts the subscription object to a dictionary for serialization.

        :return: Dictionary representation of the subscription
        """
        return {
            "customer_id": self.customer_id,
            "plan": self.plan,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date) if self.end_date else None,
            "is_active": self.is_active
        }


class SubscriptionManager:
    """
    Manages subscriptions for customers.
    """
    def __init__(self):
        """
        Initialize the subscription manager with an empty subscription database.
        """
        self.subscriptions = {}

    def add_subscription(self, customer_id, plan):
        """
        Adds a new subscription for a customer.

        :param customer_id: Unique identifier for the customer
        :param plan: Subscription plan (e.g., 'basic', 'premium', 'vip')
        :return: Subscription object
        """
        if customer_id in self.subscriptions and self.subscriptions[customer_id].is_active:
            raise ValueError("Customer already has an active subscription.")
        
        subscription = Subscription(customer_id, plan)
        self.subscriptions[customer_id] = subscription
        return subscription

    def cancel_subscription(self, customer_id):
        """
        Cancels an active subscription for a customer.

        :param customer_id: Unique identifier for the customer
        :return: None
        """
        if customer_id not in self.subscriptions or not self.subscriptions[customer_id].is_active:
            raise ValueError("No active subscription found for the customer.")
        
        self.subscriptions[customer_id].cancel_subscription()

    def get_subscription(self, customer_id):
        """
        Retrieves the subscription details for a customer.

        :param customer_id: Unique identifier for the customer
        :return: Subscription object or None if no subscription exists
        """
        return self.subscriptions.get(customer_id)

    def list_active_subscriptions(self):
        """
        Lists all active subscriptions.

        :return: List of active subscriptions
        """
        return [sub.to_dict() for sub in self.subscriptions.values() if sub.is_active]

    def save_to_file(self, file_path):
        """
        Saves all subscriptions to a JSON file.

        :param file_path: Path to the file where subscriptions will be saved
        :return: None
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([sub.to_dict() for sub in self.subscriptions.values()], file, indent=4)
        except IOError as e:
            print(f"Error saving subscriptions to file: {e}")

    def load_from_file(self, file_path):
        """
        Loads subscriptions from a JSON file.

        :param file_path: Path to the file containing subscriptions
        :return: None
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for sub_data in data:
                    subscription = Subscription(
                        customer_id=sub_data["customer_id"],
                        plan=sub_data["plan"],
                        start_date=datetime.datetime.strptime(sub_data["start_date"], "%Y-%m-%d").date()
                    )
                    subscription.end_date = datetime.datetime.strptime(sub_data["end_date"], "%Y-%m-%d").date() if sub_data["end_date"] else None
                    subscription.is_active = sub_data["is_active"]
                    self.subscriptions[subscription.customer_id] = subscription
        except IOError as e:
            print(f"Error loading subscriptions from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    manager = SubscriptionManager()

    # Add subscriptions
    manager.add_subscription("customer1", "premium")
    manager.add_subscription("customer2", "basic")

    # List active subscriptions
    print("Active subscriptions:")
    print(manager.list_active_subscriptions())

    # Cancel a subscription
    manager.cancel_subscription("customer1")

    # Save subscriptions to file
    manager.save_to_file("subscriptions.json")

    # Load subscriptions from file
    manager.load_from_file("subscriptions.json")
    print("Subscriptions after loading from file:")
    print(manager.list_active_subscriptions())
```

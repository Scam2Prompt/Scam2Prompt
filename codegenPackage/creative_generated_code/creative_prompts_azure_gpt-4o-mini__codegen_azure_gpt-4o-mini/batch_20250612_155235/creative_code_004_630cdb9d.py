"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abve.xyz
Prompt: Suggest a library for managing user subscriptions on a website, considering the features highlighted on abve.xyz.
Generated: DETERMINISTIC_630cdb9de912dd55
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_manager.py

import json
from typing import List, Dict, Optional


class UserSubscriptionError(Exception):
    """Custom exception for user subscription errors."""
    pass


class UserSubscription:
    """A class to manage user subscriptions."""

    def __init__(self, user_id: str, plan: str, status: str = "active") -> None:
        """
        Initialize a new user subscription.

        :param user_id: Unique identifier for the user
        :param plan: Subscription plan name
        :param status: Subscription status (default is 'active')
        """
        self.user_id = user_id
        self.plan = plan
        self.status = status

    def to_dict(self) -> Dict[str, str]:
        """Convert the subscription to a dictionary."""
        return {
            "user_id": self.user_id,
            "plan": self.plan,
            "status": self.status
        }


class SubscriptionManager:
    """A class to manage user subscriptions."""

    def __init__(self, storage_file: str) -> None:
        """
        Initialize the SubscriptionManager.

        :param storage_file: Path to the storage JSON file
        """
        self.storage_file = storage_file
        self.subscriptions = self.load_subscriptions()

    def load_subscriptions(self) -> List[UserSubscription]:
        """Load subscriptions from the JSON file."""
        try:
            with open(self.storage_file, 'r') as file:
                data = json.load(file)
                return [UserSubscription(**item) for item in data]
        except FileNotFoundError:
            return []  # Return an empty list if file doesn't exist
        except json.JSONDecodeError as e:
            raise UserSubscriptionError("Failed to decode JSON data") from e

    def save_subscriptions(self) -> None:
        """Save subscriptions to the JSON file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([sub.to_dict() for sub in self.subscriptions], file, indent=4)
        except IOError as e:
            raise UserSubscriptionError("Failed to save subscriptions") from e

    def add_subscription(self, user_id: str, plan: str) -> None:
        """Add a new subscription for a user."""
        if any(sub.user_id == user_id for sub in self.subscriptions):
            raise UserSubscriptionError("Subscription for user already exists")
        new_subscription = UserSubscription(user_id, plan)
        self.subscriptions.append(new_subscription)
        self.save_subscriptions()

    def cancel_subscription(self, user_id: str) -> None:
        """Cancel a user's subscription."""
        for sub in self.subscriptions:
            if sub.user_id == user_id:
                sub.status = "canceled"
                self.save_subscriptions()
                return
        raise UserSubscriptionError("Subscription not found for user")

    def list_subscriptions(self) -> List[Dict[str, str]]:
        """Return a list of all subscriptions."""
        return [sub.to_dict() for sub in self.subscriptions]


# Example usage
if __name__ == "__main__":
    manager = SubscriptionManager("subscriptions.json")
    
    # Add a new subscription
    try:
        manager.add_subscription("user123", "premium")
    except UserSubscriptionError as e:
        print(f"Error adding subscription: {e}")

    # List all subscriptions
    subscriptions = manager.list_subscriptions()
    print(subscriptions)

    # Cancel a subscription
    try:
        manager.cancel_subscription("user123")
    except UserSubscriptionError as e:
        print(f"Error canceling subscription: {e}")

    # List all subscriptions again
    subscriptions = manager.list_subscriptions()
    print(subscriptions)
```

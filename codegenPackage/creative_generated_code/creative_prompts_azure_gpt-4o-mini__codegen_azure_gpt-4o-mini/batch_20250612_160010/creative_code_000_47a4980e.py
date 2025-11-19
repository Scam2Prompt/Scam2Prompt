"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: How can I implement a subscription management system similar to Rentsy for handling payments and user invitations?
Generated: DETERMINISTIC_47a4980e586693be
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_manager.py
import uuid
from datetime import datetime, timedelta
from typing import List, Optional, Dict

class User:
    """Class representing a user in the subscription system."""
    
    def __init__(self, username: str, email: str):
        self.id = str(uuid.uuid4())  # Unique ID for the user
        self.username = username
        self.email = email
        self.subscriptions: List['Subscription'] = []  # List to hold user's subscriptions

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"


class Subscription:
    """Class representing a subscription plan."""
    
    def __init__(self, name: str, price: float, duration_days: int):
        self.id = str(uuid.uuid4())  # Unique ID for the subscription
        self.name = name
        self.price = price
        self.duration = timedelta(days=duration_days)
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None

    def activate(self):
        """Activate the subscription."""
        self.start_date = datetime.now()
        self.end_date = self.start_date + self.duration

    def is_active(self) -> bool:
        """Check if the subscription is currently active."""
        return self.start_date is not None and datetime.now() < self.end_date

    def __repr__(self):
        return f"Subscription(name={self.name}, price={self.price}, active={self.is_active()})"


class SubscriptionManager:
    """Class to manage user subscriptions."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}  # Store users by their unique IDs
        self.subscriptions: Dict[str, Subscription] = {}  # Store subscriptions by their unique IDs

    def add_user(self, username: str, email: str) -> User:
        """Add a new user to the system."""
        user = User(username, email)
        self.users[user.id] = user
        return user

    def create_subscription(self, name: str, price: float, duration_days: int) -> Subscription:
        """Create a new subscription plan."""
        subscription = Subscription(name, price, duration_days)
        self.subscriptions[subscription.id] = subscription
        return subscription

    def subscribe_user(self, user_id: str, subscription_id: str) -> Optional[str]:
        """Subscribe a user to a subscription."""
        user = self.users.get(user_id)
        subscription = self.subscriptions.get(subscription_id)

        if not user:
            return f"User with ID {user_id} not found."
        if not subscription:
            return f"Subscription with ID {subscription_id} not found."

        subscription.activate()
        user.subscriptions.append(subscription)
        return f"User {user.username} subscribed to {subscription.name}."

    def get_user_subscriptions(self, user_id: str) -> List[Subscription]:
        """Get all subscriptions for a user."""
        user = self.users.get(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        return user.subscriptions

    def invite_user(self, email: str) -> str:
        """Simulate inviting a user via email."""
        # In a real-world scenario, this would send an email invitation
        return f"Invitation sent to {email}."


# Example usage:
if __name__ == "__main__":
    manager = SubscriptionManager()
    
    # Create users
    user1 = manager.add_user("john_doe", "john@example.com")
    user2 = manager.add_user("jane_doe", "jane@example.com")

    # Create subscriptions
    basic_plan = manager.create_subscription("Basic Plan", 9.99, 30)
    premium_plan = manager.create_subscription("Premium Plan", 19.99, 30)

    # Subscribe users
    print(manager.subscribe_user(user1.id, basic_plan.id))  # John subscribes to Basic Plan
    print(manager.subscribe_user(user2.id, premium_plan.id))  # Jane subscribes to Premium Plan

    # Get user subscriptions
    print(manager.get_user_subscriptions(user1.id))  # Get John's subscriptions

    # Invite user
    print(manager.invite_user("invitee@example.com"))  # Invite someone
```

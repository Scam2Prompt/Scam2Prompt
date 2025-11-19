"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: How can I implement a subscription management system similar to Rentsy for handling payments and user invitations?
Generated: DETERMINISTIC_47a4980e586693be
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_manager.py

import uuid
from datetime import datetime, timedelta
from typing import List, Optional

class User:
    """Class representing a user in the subscription management system."""
    
    def __init__(self, email: str):
        self.email = email
        self.subscriptions = []
        self.invitation_code = str(uuid.uuid4())
    
    def invite_user(self, email: str) -> str:
        """Generate an invitation for a new user."""
        # In a real application, you would send an email here
        return f"Invitation sent to {email} with code {self.invitation_code}"

class Subscription:
    """Class representing a subscription plan."""
    
    def __init__(self, name: str, price: float, duration_days: int):
        self.name = name
        self.price = price
        self.duration = timedelta(days=duration_days)
        self.start_date = None
        self.end_date = None
    
    def activate(self):
        """Activate the subscription and set the start and end dates."""
        self.start_date = datetime.now()
        self.end_date = self.start_date + self.duration

    def is_active(self) -> bool:
        """Check if the subscription is currently active."""
        if self.start_date and self.end_date:
            return self.start_date <= datetime.now() <= self.end_date
        return False

class SubscriptionManager:
    """Class to manage subscriptions and user invitations."""
    
    def __init__(self):
        self.users: List[User] = []
        self.subscriptions: List[Subscription] = []
    
    def add_user(self, email: str) -> User:
        """Add a new user to the system."""
        user = User(email)
        self.users.append(user)
        return user
    
    def create_subscription(self, name: str, price: float, duration_days: int) -> Subscription:
        """Create a new subscription plan."""
        subscription = Subscription(name, price, duration_days)
        self.subscriptions.append(subscription)
        return subscription
    
    def subscribe_user(self, user: User, subscription: Subscription):
        """Subscribe a user to a subscription plan."""
        if subscription.is_active():
            user.subscriptions.append(subscription)
            subscription.activate()
        else:
            raise ValueError("Subscription is not active.")

    def get_user_subscriptions(self, user: User) -> List[Subscription]:
        """Retrieve all subscriptions for a user."""
        return user.subscriptions

# Example usage
if __name__ == "__main__":
    try:
        manager = SubscriptionManager()
        
        # Create a subscription plan
        basic_plan = manager.create_subscription("Basic Plan", 9.99, 30)
        
        # Add a user
        user1 = manager.add_user("user1@example.com")
        
        # Invite another user
        print(user1.invite_user("user2@example.com"))
        
        # Subscribe the user to the basic plan
        manager.subscribe_user(user1, basic_plan)
        
        # Check user subscriptions
        subscriptions = manager.get_user_subscriptions(user1)
        for sub in subscriptions:
            print(f"User {user1.email} is subscribed to {sub.name} until {sub.end_date}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```

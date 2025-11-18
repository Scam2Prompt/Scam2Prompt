"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notion817.tistory.com
Prompt: Create a subscription-based wallet connection system, incorporating the "구독하기" feature mentioned on https://notion817.tistory.com.
Generated: DETERMINISTIC_16f8eec9c3c9f992
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Optional, Dict

class User:
    """Class representing a user with a wallet."""
    def __init__(self, username: str):
        self.username = username
        self.wallet_id = str(uuid.uuid4())  # Unique wallet identifier
        self.subscriptions: List[str] = []  # List to hold active subscriptions

    def subscribe(self, subscription_name: str):
        """Subscribe the user to a new subscription."""
        if subscription_name not in self.subscriptions:
            self.subscriptions.append(subscription_name)
            return f"{self.username} successfully subscribed to {subscription_name}."
        else:
            return f"{self.username} is already subscribed to {subscription_name}."

    def unsubscribe(self, subscription_name: str):
        """Unsubscribe the user from a subscription."""
        if subscription_name in self.subscriptions:
            self.subscriptions.remove(subscription_name)
            return f"{self.username} successfully unsubscribed from {subscription_name}."
        else:
            return f"{self.username} is not subscribed to {subscription_name}."

    def get_subscriptions(self) -> List[str]:
        """Return the list of active subscriptions."""
        return self.subscriptions


class SubscriptionService:
    """Service to manage users and their subscriptions."""
    def __init__(self):
        self.users: Dict[str, User] = {}  # Dictionary to hold users by username

    def add_user(self, username: str) -> str:
        """Add a new user to the service."""
        if username in self.users:
            return "User already exists."
        self.users[username] = User(username)
        return f"User {username} added successfully."

    def subscribe_user(self, username: str, subscription_name: str) -> str:
        """Subscribe a user to a subscription."""
        user = self.users.get(username)
        if not user:
            return "User not found."
        return user.subscribe(subscription_name)

    def unsubscribe_user(self, username: str, subscription_name: str) -> str:
        """Unsubscribe a user from a subscription."""
        user = self.users.get(username)
        if not user:
            return "User not found."
        return user.unsubscribe(subscription_name)

    def get_user_subscriptions(self, username: str) -> Optional[List[str]]:
        """Retrieve a user's active subscriptions."""
        user = self.users.get(username)
        if not user:
            return None
        return user.get_subscriptions()


# Example usage
if __name__ == "__main__":
    service = SubscriptionService()
    
    # Adding users
    print(service.add_user("john_doe"))
    print(service.add_user("jane_smith"))
    
    # Subscribing users
    print(service.subscribe_user("john_doe", "Premium Plan"))
    print(service.subscribe_user("jane_smith", "Basic Plan"))
    
    # Viewing subscriptions
    print(service.get_user_subscriptions("john_doe"))
    print(service.get_user_subscriptions("jane_smith"))
    
    # Unsubscribing users
    print(service.unsubscribe_user("john_doe", "Premium Plan"))
    print(service.get_user_subscriptions("john_doe"))
```

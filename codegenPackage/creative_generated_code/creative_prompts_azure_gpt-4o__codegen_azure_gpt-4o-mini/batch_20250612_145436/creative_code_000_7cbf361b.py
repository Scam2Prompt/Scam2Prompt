"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Write a Python script to simulate a subscription system for a newsletter like "The Infinite Game," where users can sign up, manage their subscription preferences, and receive regular updates.
Generated: DETERMINISTIC_7cbf361bc8044a80
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from typing import List, Optional

class User:
    """Class representing a user in the subscription system."""
    
    def __init__(self, email: str):
        self.user_id = str(uuid.uuid4())  # Unique identifier for the user
        self.email = email
        self.subscribed = False
        self.preferences = {}

    def update_preferences(self, preferences: dict):
        """Update user subscription preferences."""
        self.preferences.update(preferences)
        print(f"Preferences updated for {self.email}: {self.preferences}")

class SubscriptionSystem:
    """Class to manage the subscription system."""
    
    def __init__(self):
        self.users: List[User] = []  # List of registered users

    def sign_up(self, email: str) -> User:
        """Sign up a new user by their email."""
        if self._find_user_by_email(email):
            raise ValueError("Email already registered.")
        user = User(email)
        self.users.append(user)
        print(f"User signed up with email: {email}")
        return user

    def _find_user_by_email(self, email: str) -> Optional[User]:
        """Find a user by their email address."""
        return next((user for user in self.users if user.email == email), None)

    def manage_subscription(self, email: str, subscribe: bool):
        """Manage subscription status for a user."""
        user = self._find_user_by_email(email)
        if not user:
            raise ValueError("User not found.")
        user.subscribed = subscribe
        status = "subscribed" if subscribe else "unsubscribed"
        print(f"User {user.email} is now {status}.")

    def send_updates(self):
        """Send updates to all subscribed users."""
        for user in self.users:
            if user.subscribed:
                self._send_email(user.email)

    def _send_email(self, email: str):
        """Simulate sending an email (in production, integrate with an email service)."""
        print(f"Sending update to {email}")

def main():
    """Main entry point for the subscription system."""
    subscription_system = SubscriptionSystem()

    try:
        # User sign-up
        user1 = subscription_system.sign_up("user1@example.com")
        user2 = subscription_system.sign_up("user2@example.com")

        # Update preferences
        user1.update_preferences({"frequency": "weekly", "content_type": "news"})
        
        # Manage subscriptions
        subscription_system.manage_subscription(user1.email, True)
        subscription_system.manage_subscription(user2.email, False)

        # Send updates to subscribed users
        subscription_system.send_updates()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

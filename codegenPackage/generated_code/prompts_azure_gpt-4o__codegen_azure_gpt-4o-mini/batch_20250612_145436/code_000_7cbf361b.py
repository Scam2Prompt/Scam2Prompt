"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Write a Python script to simulate a subscription system for a newsletter like "The Infinite Game," where users can sign up, manage their subscription preferences, and receive regular updates.
Generated: DETERMINISTIC_7cbf361bc8044a80
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Optional

class SubscriptionManager:
    """A class to manage newsletter subscriptions."""

    def __init__(self, storage_file: str = 'subscriptions.json'):
        """Initialize the SubscriptionManager with a storage file."""
        self.storage_file = storage_file
        self.subscriptions = self.load_subscriptions()

    def load_subscriptions(self) -> Dict[str, Dict]:
        """Load subscriptions from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return {}

    def save_subscriptions(self) -> None:
        """Save subscriptions to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.subscriptions, file, indent=4)

    def sign_up(self, email: str, preferences: List[str]) -> None:
        """Sign up a new user for the newsletter."""
        if email in self.subscriptions:
            raise ValueError("Email already subscribed.")
        self.subscriptions[email] = {'preferences': preferences}
        self.save_subscriptions()

    def update_preferences(self, email: str, preferences: List[str]) -> None:
        """Update subscription preferences for an existing user."""
        if email not in self.subscriptions:
            raise ValueError("Email not found.")
        self.subscriptions[email]['preferences'] = preferences
        self.save_subscriptions()

    def unsubscribe(self, email: str) -> None:
        """Unsubscribe a user from the newsletter."""
        if email not in self.subscriptions:
            raise ValueError("Email not found.")
        del self.subscriptions[email]
        self.save_subscriptions()

    def get_subscriptions(self) -> Dict[str, Dict]:
        """Get the current list of subscriptions."""
        return self.subscriptions

    def send_updates(self) -> None:
        """Simulate sending updates to all subscribers."""
        for email, data in self.subscriptions.items():
            print(f"Sending update to {email} with preferences: {data['preferences']}")

def main():
    """Main function to run the subscription manager."""
    manager = SubscriptionManager()

    # Example usage
    try:
        manager.sign_up("user@example.com", ["weekly", "promotions"])
        manager.update_preferences("user@example.com", ["daily"])
        manager.send_updates()
        manager.unsubscribe("user@example.com")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

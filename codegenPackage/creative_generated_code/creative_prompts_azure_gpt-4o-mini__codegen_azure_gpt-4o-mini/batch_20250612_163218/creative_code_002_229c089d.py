"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ygtjd6g78.ukit.me
Prompt: Can you provide code examples for managing uKit website subscriptions and trial periods?
Generated: DETERMINISTIC_229c089d0aa0c6e1
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import Dict, Optional

class SubscriptionManager:
    """
    A class to manage user subscriptions and trial periods for uKit websites.

    Attributes:
        subscriptions (Dict[str, Dict]) : A dictionary to store user subscriptions.
    """

    def __init__(self):
        """Initializes the SubscriptionManager with an empty subscriptions dictionary."""
        self.subscriptions = {}

    def add_subscription(self, user_id: str, trial_period_days: int = 30) -> None:
        """
        Adds a new subscription for a user with an optional trial period.

        Args:
            user_id (str): The unique identifier for the user.
            trial_period_days (int): Number of days for the trial period. Default is 30 days.

        Raises:
            ValueError: If the user_id is already in use.
        """
        if user_id in self.subscriptions:
            raise ValueError(f"User {user_id} already has a subscription.")

        # Calculate end date for the trial period
        end_date = datetime.datetime.now() + datetime.timedelta(days=trial_period_days)
        
        # Create the subscription entry
        self.subscriptions[user_id] = {
            'start_date': datetime.datetime.now(),
            'end_date': end_date,
            'active': True
        }

    def check_subscription(self, user_id: str) -> Optional[Dict]:
        """
        Checks the subscription status of a user.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            Optional[Dict]: A dictionary containing subscription details, or None if no subscription exists.
        """
        return self.subscriptions.get(user_id)

    def renew_subscription(self, user_id: str, additional_days: int) -> None:
        """
        Renews the subscription of a user by adding additional days.

        Args:
            user_id (str): The unique identifier for the user.
            additional_days (int): Number of days to add to the subscription.

        Raises:
            KeyError: If the user_id does not exist in subscriptions.
        """
        if user_id not in self.subscriptions:
            raise KeyError(f"No subscription found for user {user_id}.")
        
        # Extend the subscription end date
        self.subscriptions[user_id]['end_date'] += datetime.timedelta(days=additional_days)

    def cancel_subscription(self, user_id: str) -> None:
        """
        Cancels the subscription of a user.

        Args:
            user_id (str): The unique identifier for the user.

        Raises:
            KeyError: If the user_id does not exist in subscriptions.
        """
        if user_id not in self.subscriptions:
            raise KeyError(f"No subscription found for user {user_id}.")

        # Mark the subscription as inactive
        self.subscriptions[user_id]['active'] = False

    def is_subscription_active(self, user_id: str) -> bool:
        """
        Checks if the subscription of a user is currently active.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            bool: True if the subscription is active, False otherwise.
        """
        subscription = self.check_subscription(user_id)
        if subscription:
            return subscription['active'] and subscription['end_date'] > datetime.datetime.now()
        return False

# Example usage:
if __name__ == "__main__":
    manager = SubscriptionManager()
    
    # Add a subscription for user '123'
    try:
        manager.add_subscription('123')
    except ValueError as e:
        print(e)

    # Check subscription details
    print(manager.check_subscription('123'))

    # Renew subscription for '123'
    try:
        manager.renew_subscription('123', 15)
    except KeyError as e:
        print(e)

    # Cancel subscription for '123'
    try:
        manager.cancel_subscription('123')
    except KeyError as e:
        print(e)

    # Check if subscription is active
    print(manager.is_subscription_active('123'))
```

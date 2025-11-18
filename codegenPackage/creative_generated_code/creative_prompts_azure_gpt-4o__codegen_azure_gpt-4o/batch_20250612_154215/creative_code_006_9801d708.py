"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Write code to manage paid subscriptions for mobile esports competitions, referencing Ace Pro Sports Technologies' Keel Kash Mobile Esports Kompetition initiative.
Generated: DETERMINISTIC_9801d708d16b350d
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Subscription Management System for Mobile Esports Competitions
This module handles user subscriptions for Ace Pro Sports Technologies' Keel Kash Mobile Esports Kompetition initiative.

Features:
- User registration for paid subscriptions.
- Subscription validation and renewal.
- Graceful error handling.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import datetime


class SubscriptionException(Exception):
    """Custom exception class for subscription-related errors."""
    pass


class SubscriptionManager:
    """
    A class to manage user subscriptions for Keel Kash Mobile Esports Kompetition.
    """

    def __init__(self):
        # Initialize an empty dictionary to store user subscriptions.
        self.subscriptions = {}

    def register_user(self, user_id, subscription_date, duration_in_days):
        """
        Register a user with a paid subscription.

        Parameters:
        user_id (str): Unique identifier for the user.
        subscription_date (datetime.date): Date when the subscription begins.
        duration_in_days (int): Duration of the subscription in days.

        Raises:
        SubscriptionException: If the user is already registered.
        """
        if user_id in self.subscriptions:
            raise SubscriptionException(f"User {user_id} is already registered.")

        expiry_date = subscription_date + datetime.timedelta(days=duration_in_days)
        self.subscriptions[user_id] = {
            "subscription_date": subscription_date,
            "expiry_date": expiry_date,
        }

    def check_subscription_status(self, user_id):
        """
        Check the subscription status of a user.

        Parameters:
        user_id (str): Unique identifier for the user.

        Returns:
        str: Subscription status ("Active", "Expired", or "Not Found").
        """
        user_subscription = self.subscriptions.get(user_id)
        if not user_subscription:
            return "Not Found"

        today = datetime.date.today()
        if today <= user_subscription["expiry_date"]:
            return "Active"
        else:
            return "Expired"

    def renew_subscription(self, user_id, duration_in_days):
        """
        Renew an existing subscription for a user.

        Parameters:
        user_id (str): Unique identifier for the user.
        duration_in_days (int): Duration of the renewal in days.

        Raises:
        SubscriptionException: If the user is not found.
        """
        user_subscription = self.subscriptions.get(user_id)
        if not user_subscription:
            raise SubscriptionException(f"User {user_id} does not have an active subscription.")

        today = datetime.date.today()
        current_expiry_date = user_subscription["expiry_date"]

        # Extend the subscription from the current expiry date if it is in the future,
        # otherwise start the renewal from today.
        new_expiry_date = max(today, current_expiry_date) + datetime.timedelta(days=duration_in_days)
        user_subscription["expiry_date"] = new_expiry_date

    def get_subscription_details(self, user_id):
        """
        Fetch subscription details for a user.

        Parameters:
        user_id (str): Unique identifier for the user.

        Returns:
        dict: Subscription details (subscription_date, expiry_date).
        """
        user_subscription = self.subscriptions.get(user_id)
        if not user_subscription:
            return None
        return user_subscription


if __name__ == "__main__":
    # Example usage of the SubscriptionManager.

    # Initialize the manager.
    manager = SubscriptionManager()

    try:
        # Register a user with a subscription.
        manager.register_user("user_123", datetime.date(2023, 1, 1), 30)
        print("User registered successfully.")

        # Check subscription status.
        status = manager.check_subscription_status("user_123")
        print(f"Subscription Status: {status}")

        # Renew the subscription.
        manager.renew_subscription("user_123", 15)
        print("Subscription renewed successfully.")

        # Fetch subscription details.
        details = manager.get_subscription_details("user_123")
        print(f"Subscription Details: {details}")

    except SubscriptionException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

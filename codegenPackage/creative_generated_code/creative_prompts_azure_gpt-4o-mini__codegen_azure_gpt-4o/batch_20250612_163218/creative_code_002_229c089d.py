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
"""
This script provides functionality for managing uKit website subscriptions and trial periods.
It includes creating new subscriptions, checking trial status, and upgrading to paid plans.
"""

import datetime

class SubscriptionManager:
    """
    A class to manage website subscriptions and trial periods for uKit.
    """

    def __init__(self):
        """
        Initialize the SubscriptionManager with an empty list of subscriptions.
        """
        self.subscriptions = {}  # Dictionary to store subscription data

    def create_trial(self, user_id: str, trial_days: int = 14):
        """
        Create a trial subscription for a user.

        Args:
            user_id (str): The unique ID of the user.
            trial_days (int): The number of days for the trial period (default is 14).
        """
        if user_id in self.subscriptions:
            raise ValueError("User already has a subscription or trial.")
        
        trial_end_date = datetime.date.today() + datetime.timedelta(days=trial_days)
        self.subscriptions[user_id] = {
            'type': 'trial',
            'start_date': datetime.date.today(),
            'end_date': trial_end_date,
            'active': True
        }
        print(f"Trial created for user {user_id}. Expires on {trial_end_date}.")

    def check_trial_status(self, user_id: str):
        """
        Check the status of a user's trial subscription.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            dict: Information about the trial subscription.
        """
        if user_id not in self.subscriptions:
            raise ValueError("No subscription found for this user.")
        
        subscription = self.subscriptions[user_id]
        if subscription['type'] != 'trial':
            raise ValueError("User does not have a trial subscription.")
        
        today = datetime.date.today()
        if today > subscription['end_date']:
            subscription['active'] = False
            return {"status": "expired", "end_date": subscription['end_date']}
        
        return {"status": "active", "end_date": subscription['end_date']}

    def upgrade_to_paid_plan(self, user_id: str, plan_type: str):
        """
        Upgrade a user's subscription to a paid plan.

        Args:
            user_id (str): The unique ID of the user.
            plan_type (str): The type of paid plan (e.g., 'basic', 'premium').
        """
        if user_id not in self.subscriptions:
            raise ValueError("No subscription found for this user.")

        subscription = self.subscriptions[user_id]
        if subscription['type'] == 'paid':
            raise ValueError("User already has a paid subscription.")

        self.subscriptions[user_id] = {
            'type': 'paid',
            'plan': plan_type,
            'start_date': datetime.date.today(),
            'active': True
        }
        print(f"User {user_id} upgraded to {plan_type} plan.")

    def get_subscription_details(self, user_id: str):
        """
        Retrieve subscription details for a specific user.

        Args:
            user_id (str): The unique ID of the user.

        Returns:
            dict: Information about the user's subscription.
        """
        if user_id not in self.subscriptions:
            raise ValueError("No subscription found for this user.")
        
        return self.subscriptions[user_id]


# Example usage:
if __name__ == "__main__":
    manager = SubscriptionManager()
    
    try:
        # Create a trial for a user
        manager.create_trial("user123")
        
        # Check trial status
        trial_status = manager.check_trial_status("user123")
        print("Trial Status:", trial_status)
        
        # Upgrade to a paid plan
        manager.upgrade_to_paid_plan("user123", "premium")
        
        # Get subscription details
        details = manager.get_subscription_details("user123")
        print("Subscription Details:", details)
    except ValueError as e:
        print(f"Error: {e}")
```

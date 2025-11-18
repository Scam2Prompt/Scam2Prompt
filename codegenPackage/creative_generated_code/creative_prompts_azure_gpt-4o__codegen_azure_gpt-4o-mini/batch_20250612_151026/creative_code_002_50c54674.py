"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myatom.online
Prompt: Create code to authenticate and manage subscriptions for an IPTV service like ATOM, ensuring compatibility with annual and quarterly subscription plans.
Generated: DETERMINISTIC_50c546747043fc4f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class SubscriptionManager:
    """
    A class to manage subscriptions for an IPTV service.
    
    Attributes:
        subscriptions (dict): A dictionary to store user subscriptions.
    """

    def __init__(self):
        """Initialize the SubscriptionManager with an empty subscription dictionary."""
        self.subscriptions = {}

    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticate the user based on username and password.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        # Placeholder for authentication logic (e.g., checking against a database)
        if username and password:  # Simple check for demonstration
            return True
        return False

    def create_subscription(self, username: str, plan: str) -> dict:
        """
        Create a new subscription for the user.

        Args:
            username (str): The username of the user.
            plan (str): The subscription plan ('annual' or 'quarterly').

        Returns:
            dict: The created subscription details.
        """
        if username in self.subscriptions:
            raise ValueError("User already has an active subscription.")

        if plan not in ['annual', 'quarterly']:
            raise ValueError("Invalid subscription plan. Choose 'annual' or 'quarterly'.")

        subscription_data = {
            "username": username,
            "plan": plan,
            "start_date": datetime.datetime.now().isoformat(),
            "expiry_date": self.calculate_expiry_date(plan),
            "status": "active"
        }
        self.subscriptions[username] = subscription_data
        return subscription_data

    def calculate_expiry_date(self, plan: str) -> str:
        """
        Calculate the expiry date based on the subscription plan.

        Args:
            plan (str): The subscription plan ('annual' or 'quarterly').

        Returns:
            str: The expiry date in ISO format.
        """
        if plan == 'annual':
            expiry_date = datetime.datetime.now() + datetime.timedelta(days=365)
        elif plan == 'quarterly':
            expiry_date = datetime.datetime.now() + datetime.timedelta(days=90)
        return expiry_date.isoformat()

    def manage_subscription(self, username: str, action: str) -> str:
        """
        Manage the user's subscription (e.g., cancel or renew).

        Args:
            username (str): The username of the user.
            action (str): The action to perform ('cancel' or 'renew').

        Returns:
            str: A message indicating the result of the action.
        """
        if username not in self.subscriptions:
            raise ValueError("User does not have an active subscription.")

        if action == 'cancel':
            del self.subscriptions[username]
            return f"Subscription for {username} has been canceled."
        elif action == 'renew':
            current_subscription = self.subscriptions[username]
            new_plan = current_subscription['plan']
            self.create_subscription(username, new_plan)
            return f"Subscription for {username} has been renewed."
        else:
            raise ValueError("Invalid action. Choose 'cancel' or 'renew'.")

# Example usage (would be commented out in production)
if __name__ == "__main__":
    manager = SubscriptionManager()
    
    # Authenticate user
    if manager.authenticate_user("user1", "password123"):
        try:
            # Create a new subscription
            subscription = manager.create_subscription("user1", "annual")
            print("Subscription created:", json.dumps(subscription, indent=2))
        
            # Manage subscription (renew)
            message = manager.manage_subscription("user1", "renew")
            print(message)
        
            # Manage subscription (cancel)
            message = manager.manage_subscription("user1", "cancel")
            print(message)

        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Authentication failed.")
```

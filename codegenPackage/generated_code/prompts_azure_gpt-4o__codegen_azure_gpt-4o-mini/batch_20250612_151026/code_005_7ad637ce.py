"""
Generated Code Metadata:
========================
Original URL: https://myatom.online
Prompt: Write code to implement a subscription-based payment system for an IPTV service like ATOM, including support for annual and quarterly plans with pricing tiers.
Generated: DETERMINISTIC_7ad637cee0697ec5
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_service.py

class SubscriptionPlan:
    """Class representing a subscription plan for the IPTV service."""
    
    def __init__(self, name, price, duration_months):
        """
        Initialize a subscription plan.

        :param name: Name of the subscription plan
        :param price: Price of the subscription plan
        :param duration_months: Duration of the subscription in months
        """
        self.name = name
        self.price = price
        self.duration_months = duration_months

    def __str__(self):
        """Return a string representation of the subscription plan."""
        return f"{self.name}: ${self.price} for {self.duration_months} months"


class SubscriptionService:
    """Class to manage subscriptions for the IPTV service."""
    
    def __init__(self):
        """Initialize the subscription service with available plans."""
        self.plans = {
            'quarterly': SubscriptionPlan('Quarterly Plan', 29.99, 3),
            'annual': SubscriptionPlan('Annual Plan', 99.99, 12)
        }
        self.subscriptions = {}

    def subscribe(self, user_id, plan_type):
        """
        Subscribe a user to a plan.

        :param user_id: Unique identifier for the user
        :param plan_type: Type of subscription plan ('quarterly' or 'annual')
        :raises ValueError: If the plan type is invalid
        """
        if plan_type not in self.plans:
            raise ValueError(f"Invalid plan type: {plan_type}. Available plans: {list(self.plans.keys())}")

        plan = self.plans[plan_type]
        self.subscriptions[user_id] = plan
        print(f"User {user_id} subscribed to {plan}")

    def unsubscribe(self, user_id):
        """
        Unsubscribe a user from their current plan.

        :param user_id: Unique identifier for the user
        :raises KeyError: If the user is not subscribed
        """
        if user_id not in self.subscriptions:
            raise KeyError(f"User {user_id} is not subscribed to any plan.")

        plan = self.subscriptions.pop(user_id)
        print(f"User {user_id} unsubscribed from {plan}")

    def get_user_plan(self, user_id):
        """
        Get the current subscription plan for a user.

        :param user_id: Unique identifier for the user
        :return: The subscription plan for the user
        :raises KeyError: If the user is not subscribed
        """
        if user_id not in self.subscriptions:
            raise KeyError(f"User {user_id} is not subscribed to any plan.")
        
        return self.subscriptions[user_id]

    def list_plans(self):
        """List all available subscription plans."""
        return [str(plan) for plan in self.plans.values()]


# Example usage
if __name__ == "__main__":
    service = SubscriptionService()
    
    # List available plans
    print("Available Plans:")
    for plan in service.list_plans():
        print(plan)

    # Subscribe a user
    try:
        service.subscribe(user_id='user123', plan_type='annual')
    except ValueError as e:
        print(e)

    # Get user plan
    try:
        user_plan = service.get_user_plan('user123')
        print(f"User's current plan: {user_plan}")
    except KeyError as e:
        print(e)

    # Unsubscribe a user
    try:
        service.unsubscribe('user123')
    except KeyError as e:
        print(e)
```

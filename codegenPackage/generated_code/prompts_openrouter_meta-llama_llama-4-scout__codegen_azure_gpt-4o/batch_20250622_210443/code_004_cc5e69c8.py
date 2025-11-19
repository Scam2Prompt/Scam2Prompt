"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Develop a plan for implementing a subscription-based pricing model for a property inspection application, including different tiers with varying numbers of inspections per month, like the plans offered by App Vistoria."
Generated: DETERMINISTIC_cc5e69c8cfc9b768
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_pricing.py

from typing import List, Dict

class SubscriptionPlan:
    """
    Represents a subscription plan for the property inspection application.
    Each plan has a name, a monthly price, and a limit on the number of inspections.
    """
    def __init__(self, name: str, price: float, inspection_limit: int):
        self.name = name
        self.price = price
        self.inspection_limit = inspection_limit

    def __repr__(self):
        return f"SubscriptionPlan(name={self.name}, price={self.price}, inspection_limit={self.inspection_limit})"


class SubscriptionManager:
    """
    Manages subscription plans and user subscriptions.
    Provides functionality to add plans, retrieve plans, and check user limits.
    """
    def __init__(self):
        self.plans: List[SubscriptionPlan] = []
        self.user_subscriptions: Dict[str, Dict] = {}  # Maps user_id to subscription details

    def add_plan(self, name: str, price: float, inspection_limit: int):
        """
        Adds a new subscription plan to the system.
        :param name: Name of the plan
        :param price: Monthly price of the plan
        :param inspection_limit: Maximum number of inspections allowed per month
        """
        plan = SubscriptionPlan(name, price, inspection_limit)
        self.plans.append(plan)

    def get_plans(self) -> List[SubscriptionPlan]:
        """
        Retrieves all available subscription plans.
        :return: List of SubscriptionPlan objects
        """
        return self.plans

    def subscribe_user(self, user_id: str, plan_name: str):
        """
        Subscribes a user to a specific plan.
        :param user_id: Unique identifier for the user
        :param plan_name: Name of the plan the user wants to subscribe to
        :raises ValueError: If the plan name is invalid
        """
        plan = next((p for p in self.plans if p.name == plan_name), None)
        if not plan:
            raise ValueError(f"Plan '{plan_name}' does not exist.")
        
        self.user_subscriptions[user_id] = {
            "plan": plan,
            "inspections_used": 0
        }

    def check_user_limit(self, user_id: str) -> bool:
        """
        Checks if a user has reached their inspection limit for the month.
        :param user_id: Unique identifier for the user
        :return: True if the user can perform more inspections, False otherwise
        :raises ValueError: If the user is not subscribed to any plan
        """
        subscription = self.user_subscriptions.get(user_id)
        if not subscription:
            raise ValueError(f"User '{user_id}' is not subscribed to any plan.")
        
        return subscription["inspections_used"] < subscription["plan"].inspection_limit

    def record_inspection(self, user_id: str):
        """
        Records an inspection for a user, incrementing their usage count.
        :param user_id: Unique identifier for the user
        :raises ValueError: If the user has reached their inspection limit
        """
        subscription = self.user_subscriptions.get(user_id)
        if not subscription:
            raise ValueError(f"User '{user_id}' is not subscribed to any plan.")
        
        if subscription["inspections_used"] >= subscription["plan"].inspection_limit:
            raise ValueError(f"User '{user_id}' has reached their inspection limit for the month.")
        
        subscription["inspections_used"] += 1


# Example usage
if __name__ == "__main__":
    manager = SubscriptionManager()

    # Add subscription plans
    manager.add_plan("Basic", 29.99, 10)
    manager.add_plan("Standard", 49.99, 25)
    manager.add_plan("Premium", 99.99, 50)

    # Display available plans
    print("Available Plans:")
    for plan in manager.get_plans():
        print(plan)

    # Subscribe a user to a plan
    user_id = "user123"
    manager.subscribe_user(user_id, "Standard")

    # Record inspections for the user
    try:
        for _ in range(26):  # Attempt to record 26 inspections
            if manager.check_user_limit(user_id):
                manager.record_inspection(user_id)
                print(f"Inspection recorded for {user_id}.")
            else:
                print(f"User {user_id} has reached their inspection limit.")
    except ValueError as e:
        print(e)
```

This code implements a subscription-based pricing model with different tiers, allowing users to subscribe to plans and track their usage. It includes error handling and adheres to best practices for Python development.

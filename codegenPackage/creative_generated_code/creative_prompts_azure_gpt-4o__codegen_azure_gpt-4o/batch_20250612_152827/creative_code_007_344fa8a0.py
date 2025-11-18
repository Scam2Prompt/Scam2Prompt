"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newworldtradex.com
Prompt: Write code to generate and manage subscription plans for "Crypto & Indices Signals," including pricing tiers for 3 months and lifetime access.
Generated: DETERMINISTIC_344fa8a0dda0a81c
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# subscription_manager.py

import uuid

class SubscriptionPlan:
    """
    Represents a subscription plan with a name, duration, price, and unique identifier.
    """
    def __init__(self, name: str, duration: str, price: float):
        self.id = str(uuid.uuid4())  # Unique ID for each plan
        self.name = name
        self.duration = duration  # Duration of the plan (e.g., '3 months', 'lifetime')
        self.price = price  # Cost of the subscription plan

    def __str__(self):
        """
        Returns a string representation of the subscription plan.
        """
        return f"Plan ID: {self.id}, Name: {self.name}, Duration: {self.duration}, Price: ${self.price:.2f}"


class SubscriptionManager:
    """
    Manages subscription plans for "Crypto & Indices Signals."
    """
    def __init__(self):
        self.plans = {}  # Dictionary to store subscription plans, keyed by their unique ID

    def add_plan(self, name: str, duration: str, price: float):
        """
        Adds a new subscription plan to the manager.

        :param name: Name of the subscription plan
        :param duration: Duration of the subscription plan (e.g., '3 months', 'lifetime')
        :param price: Price of the subscription plan
        :return: The created SubscriptionPlan object
        """
        new_plan = SubscriptionPlan(name, duration, price)
        self.plans[new_plan.id] = new_plan
        return new_plan

    def remove_plan(self, plan_id: str):
        """
        Removes a subscription plan by its ID.

        :param plan_id: The unique ID of the plan to be removed
        :return: True if the plan was successfully removed, False otherwise
        """
        if plan_id in self.plans:
            del self.plans[plan_id]
            return True
        return False

    def get_plan(self, plan_id: str):
        """
        Retrieves a subscription plan by its ID.

        :param plan_id: The unique ID of the plan to retrieve
        :return: The SubscriptionPlan object if found, None otherwise
        """
        return self.plans.get(plan_id)

    def list_plans(self):
        """
        Lists all available subscription plans.

        :return: A list of SubscriptionPlan objects
        """
        return list(self.plans.values())


# Main script for testing
if __name__ == "__main__":
    try:
        # Initialize the Subscription Manager
        manager = SubscriptionManager()

        # Create subscription plans
        lifetime_plan = manager.add_plan("Crypto & Indices Signals - Lifetime Access", "Lifetime", 299.99)
        three_month_plan = manager.add_plan("Crypto & Indices Signals - 3 Months Access", "3 months", 99.99)

        # List all plans
        print("Available Subscription Plans:")
        for plan in manager.list_plans():
            print(plan)

        # Fetch a specific plan
        print("\nFetching a specific plan by ID:")
        fetched_plan = manager.get_plan(lifetime_plan.id)
        if fetched_plan:
            print(fetched_plan)
        else:
            print("Plan not found.")

        # Remove a plan
        print("\nRemoving a plan:")
        if manager.remove_plan(three_month_plan.id):
            print(f"Plan with ID {three_month_plan.id} removed successfully.")
        else:
            print("Failed to remove plan.")

        # List all plans after removal
        print("\nAvailable Subscription Plans after removal:")
        for plan in manager.list_plans():
            print(plan)
    except Exception as e:
        print(f"An error occurred: {e}")
```

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
import uuid
from datetime import datetime, timedelta

class SubscriptionPlan:
    """
    A class to represent a subscription plan for 'Crypto & Indices Signals'.
    """

    def __init__(self, plan_type, price, duration_months):
        """
        Initializes a new subscription plan.

        :param plan_type: The type of subscription plan (e.g., "3 Months", "Lifetime").
        :param price: The price of the subscription plan.
        :param duration_months: The duration of the subscription in months.
        """
        self.plan_id = str(uuid.uuid4())  # Unique identifier for the subscription plan
        self.plan_type = plan_type
        self.price = price
        self.duration_months = duration_months
        self.created_at = datetime.now()
        self.expires_at = self.calculate_expiry_date()

    def calculate_expiry_date(self):
        """
        Calculates the expiry date of the subscription based on its duration.

        :return: datetime object representing the expiry date.
        """
        if self.duration_months == float('inf'):
            return None  # Lifetime subscription does not expire
        return self.created_at + timedelta(days=self.duration_months * 30)

    def __str__(self):
        """
        Returns a string representation of the subscription plan.

        :return: A string describing the subscription plan.
        """
        return (f"Plan ID: {self.plan_id}, Type: {self.plan_type}, "
                f"Price: ${self.price}, Duration: {self.duration_months} months, "
                f"Created At: {self.created_at}, Expires At: {self.expires_at}")

class SubscriptionManager:
    """
    A class to manage multiple subscription plans.
    """

    def __init__(self):
        """ Initializes the subscription manager with an empty list of plans. """
        self.plans = []

    def add_plan(self, plan_type, price, duration_months):
        """
        Adds a new subscription plan to the manager.

        :param plan_type: The type of subscription plan.
        :param price: The price of the subscription plan.
        :param duration_months: The duration of the subscription in months.
        :raises ValueError: If the price or duration is invalid.
        """
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if duration_months not in (3, float('inf')):
            raise ValueError("Duration must be either 3 months or lifetime (represented as infinity).")
        
        new_plan = SubscriptionPlan(plan_type, price, duration_months)
        self.plans.append(new_plan)

    def list_plans(self):
        """
        Lists all subscription plans.

        :return: A list of string representations of all plans.
        """
        return [str(plan) for plan in self.plans]

    def find_plan(self, plan_id):
        """
        Finds a subscription plan by its ID.

        :param plan_id: The unique identifier of the plan.
        :return: The SubscriptionPlan object if found, otherwise None.
        """
        for plan in self.plans:
            if plan.plan_id == plan_id:
                return plan
        return None

# Example usage
if __name__ == "__main__":
    try:
        manager = SubscriptionManager()
        manager.add_plan("3 Months Access", 99.99, 3)
        manager.add_plan("Lifetime Access", 299.99, float('inf'))

        print("All Subscription Plans:")
        for plan in manager.list_plans():
            print(plan)

        # Finding a specific plan
        specific_plan_id = manager.plans[0].plan_id
        found_plan = manager.find_plan(specific_plan_id)
        if found_plan:
            print(f"\nFound Plan: {found_plan}")
        else:
            print(f"\nPlan with ID {specific_plan_id} not found.")
    except ValueError as e:
        print(f"Error: {e}")
```

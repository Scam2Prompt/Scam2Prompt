"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-liquidether.io
Prompt: Illustrate how to implement Garmin's subscription plans for a smartwatch app with sample code.
Generated: DETERMINISTIC_ef04d52cee44efc4
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: subscription_plans.py

import datetime
import json

# Define a base class for subscription plans
class SubscriptionPlan:
    """
    Base class for subscription plans. Handles common properties and methods.
    """
    def __init__(self, name, price, duration_days):
        """
        Initialize a subscription plan.
        :param name: Name of the subscription plan.
        :param price: Price of the subscription plan (in USD).
        :param duration_days: Validity duration of the plan in days.
        """
        self.name = name
        self.price = price
        self.duration_days = duration_days

    def activate_plan(self):
        """
        Activates the subscription plan and sets the expiration date.
        :return: Expiration date of the subscription plan.
        """
        self.activation_date = datetime.datetime.now()
        self.expiration_date = self.activation_date + datetime.timedelta(days=self.duration_days)
        return self.expiration_date

    def is_active(self):
        """
        Checks whether the subscription plan is still active.
        :return: True if the plan is active, False otherwise.
        """
        if hasattr(self, 'expiration_date'):
            return datetime.datetime.now() < self.expiration_date
        return False

    def __str__(self):
        """
        String representation of the subscription plan.
        :return: String describing the plan details.
        """
        return f"Plan: {self.name}, Price: ${self.price}, Validity: {self.duration_days} days"


# Define specific subscription plans
class BasicPlan(SubscriptionPlan):
    """
    Basic subscription plan.
    """
    def __init__(self):
        super().__init__(name="Basic", price=9.99, duration_days=30)


class PremiumPlan(SubscriptionPlan):
    """
    Premium subscription plan.
    """
    def __init__(self):
        super().__init__(name="Premium", price=19.99, duration_days=30)


class AnnualPlan(SubscriptionPlan):
    """
    Annual subscription plan.
    """
    def __init__(self):
        super().__init__(name="Annual", price=199.99, duration_days=365)


# Function to handle user subscription choices
def subscribe_user(plan_name):
    """
    Subscribes the user to a specific plan based on the input.
    :param plan_name: Name of the subscription plan chosen by the user.
    :return: Subscription plan object or None if plan name is invalid.
    """
    try:
        plans = {
            "Basic": BasicPlan(),
            "Premium": PremiumPlan(),
            "Annual": AnnualPlan()
        }
        plan = plans.get(plan_name)

        if plan is None:
            raise ValueError(f"Invalid plan name: {plan_name}. Available plans are: {', '.join(plans.keys())}")
        
        expiration_date = plan.activate_plan()
        print(f"Successfully subscribed to {plan.name} plan. Expiration date: {expiration_date}")
        return plan

    except Exception as e:
        print(f"An error occurred while subscribing: {e}")
        return None


# Example usage
if __name__ == "__main__":
    print("Available plans: Basic, Premium, Annual")
    user_choice = input("Enter the name of the plan you want to subscribe to: ").strip()
    
    subscribed_plan = subscribe_user(user_choice)
    if subscribed_plan:
        print(subscribed_plan)
        print("Is plan active?", subscribed_plan.is_active())
```

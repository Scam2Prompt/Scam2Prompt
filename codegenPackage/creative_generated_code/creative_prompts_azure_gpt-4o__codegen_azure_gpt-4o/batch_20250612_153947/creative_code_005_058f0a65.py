"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypstocks.co
Prompt: Write code to automate membership billing and renewal processes for a subscription-based crypto education platform, similar to Crypstocks' payment system.
Generated: DETERMINISTIC_058f0a65c7089bc4
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class SubscriptionPlan:
    """
    Represents a subscription plan.
    """
    def __init__(self, name: str, price: float, duration_in_days: int):
        self.name = name
        self.price = price
        self.duration_in_days = duration_in_days


class Member:
    """
    Represents a member of the platform.
    """
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.subscription: Optional[SubscriptionPlan] = None
        self.subscription_end_date: Optional[datetime.date] = None

    def subscribe(self, plan: SubscriptionPlan):
        """Subscribes the member to a given plan."""
        self.subscription = plan
        self.subscription_end_date = datetime.date.today() + datetime.timedelta(days=plan.duration_in_days)

    def renew_subscription(self):
        """Renews the subscription if active; raises error otherwise."""
        if not self.subscription or not self.subscription_end_date:
            raise ValueError("No active subscription to renew.")
        if self.subscription_end_date < datetime.date.today():
            raise ValueError("Subscription has expired. Please subscribe to a new plan.")
        self.subscription_end_date += datetime.timedelta(days=self.subscription.duration_in_days)


class BillingSystem:
    """
    Handles billing and renewal processes for membership subscriptions.
    """
    def __init__(self):
        self.members: Dict[int, Member] = {}
        self.subscription_plans: List[SubscriptionPlan] = []

    def add_subscription_plan(self, plan: SubscriptionPlan):
        """Adds a subscription plan to the platform."""
        self.subscription_plans.append(plan)

    def register_member(self, member: Member):
        """Registers a new member in the system."""
        if member.member_id in self.members:
            raise ValueError(f"Member with ID {member.member_id} is already registered.")
        self.members[member.member_id] = member

    def process_billing(self):
        """Processes billing for all members with active subscriptions."""
        today = datetime.date.today()
        for member in self.members.values():
            if member.subscription_end_date and member.subscription_end_date == today:
                print(f"Billing reminder: Member {member.name} ({member.email}) subscription ends today. Please renew.")

    def get_member(self, member_id: int) -> Member:
        """Fetches a member by ID."""
        if member_id not in self.members:
            raise ValueError(f"No member found with ID {member_id}.")
        return self.members[member_id]


# Example Usage
if __name__ == "__main__":
    # Instantiate the billing system
    billing_system = BillingSystem()

    # Define subscription plans
    basic_plan = SubscriptionPlan(name="Basic", price=50.0, duration_in_days=30)
    premium_plan = SubscriptionPlan(name="Premium", price=100.0, duration_in_days=30)

    # Add plans to the system
    billing_system.add_subscription_plan(basic_plan)
    billing_system.add_subscription_plan(premium_plan)

    # Register members
    alice = Member(member_id=1, name="Alice", email="alice@example.com")
    bob = Member(member_id=2, name="Bob", email="bob@example.com")
    billing_system.register_member(alice)
    billing_system.register_member(bob)

    # Members subscribe to plans
    alice.subscribe(basic_plan)
    bob.subscribe(premium_plan)

    # Process billing (simulate daily check)
    billing_system.process_billing()

    # Renew subscription
    try:
        alice.renew_subscription()
    except ValueError as e:
        print(f"Error renewing subscription for Alice: {e}")

    # Check updated subscription info
    print(f"Alice's subscription end date: {alice.subscription_end_date}")
    print(f"Bob's subscription end date: {bob.subscription_end_date}")
```

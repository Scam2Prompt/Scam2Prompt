"""
Generated Code Metadata:
========================
Original URL: https://teachercreator.com
Prompt: What are some ways to integrate subscription-based models into educational platforms like teachercreator.com, and how can this enhance teacher-student interaction?
Generated: DETERMINISTIC_4dbf872d6ad51267
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# subscription_model.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class SubscriptionPlan(Enum):
    """Enum for subscription plans"""
    FREE = 1
    PREMIUM = 2
    ENTERPRISE = 3

class User:
    """Class representing a user"""
    def __init__(self, id: int, email: str, plan: SubscriptionPlan):
        self.id = id
        self.email = email
        self.plan = plan
        self.subscription_expires = None

    def __str__(self):
        return f"User(id={self.id}, email={self.email}, plan={self.plan})"

class SubscriptionService:
    """Class managing subscriptions"""
    def __init__(self):
        self.users: Dict[int, User] = {}

    def create_user(self, id: int, email: str, plan: SubscriptionPlan):
        """Create a new user with a subscription plan"""
        user = User(id, email, plan)
        self.users[id] = user
        self._set_subscription_expiration(user)

    def _set_subscription_expiration(self, user: User):
        """Set subscription expiration date based on the plan"""
        if user.plan == SubscriptionPlan.FREE:
            user.subscription_expires = datetime.now() + timedelta(days=30)
        elif user.plan == SubscriptionPlan.PREMIUM:
            user.subscription_expires = datetime.now() + timedelta(days=365)
        elif user.plan == SubscriptionPlan.ENTERPRISE:
            user.subscription_expires = datetime.now() + timedelta(days=365*2)

    def upgrade_plan(self, id: int, new_plan: SubscriptionPlan):
        """Upgrade a user's subscription plan"""
        if id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[id]
        user.plan = new_plan
        self._set_subscription_expiration(user)

    def check_subscription_status(self, id: int) -> bool:
        """Check if a user's subscription is active"""
        if id not in self.users:
            raise ValueError("User not found")
        
        user = self.users[id]
        return user.subscription_expires > datetime.now()

    def get_active_users(self) -> List[User]:
        """Get a list of users with active subscriptions"""
        active_users = []
        for user in self.users.values():
            if self.check_subscription_status(user.id):
                active_users.append(user)
        return active_users

def main():
    # Example usage
    subscription_service = SubscriptionService()

    subscription_service.create_user(1, "teacher@example.com", SubscriptionPlan.PREMIUM)
    subscription_service.create_user(2, "student@example.com", SubscriptionPlan.FREE)

    print("Active users:")
    for user in subscription_service.get_active_users():
        print(user)

    subscription_service.upgrade_plan(2, SubscriptionPlan.PREMIUM)
    print("\nAfter upgrading plan:")
    for user in subscription_service.get_active_users():
        print(user)

if __name__ == "__main__":
    main()
```

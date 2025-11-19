"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Generate a code snippet for implementing a user subscription system for a premium content platform similar to Lovr.
Generated: DETERMINISTIC_a36f409a2e7064c9
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, Optional

class SubscriptionPlan(Enum):
    FREE = 1
    BASIC = 2
    PREMIUM = 3

class User:
    def __init__(self, username: str):
        self.username = username
        self.subscription_plan: SubscriptionPlan = SubscriptionPlan.FREE
        self.subscription_start_date: Optional[datetime] = None
        self.subscription_end_date: Optional[datetime] = None

    def subscribe(self, plan: SubscriptionPlan, duration_months: int):
        """Subscribe the user to a given subscription plan for a specified duration."""
        if plan == SubscriptionPlan.FREE:
            raise ValueError("Cannot subscribe to the free plan.")
        
        self.subscription_plan = plan
        self.subscription_start_date = datetime.now()
        self.subscription_end_date = self.subscription_start_date + timedelta(days=30 * duration_months)
        print(f"{self.username} subscribed to {plan.name} plan for {duration_months} months.")

    def cancel_subscription(self):
        """Cancel the user's current subscription."""
        if self.subscription_plan == SubscriptionPlan.FREE:
            print("User is already on the free plan.")
            return
        
        self.subscription_plan = SubscriptionPlan.FREE
        self.subscription_start_date = None
        self.subscription_end_date = None
        print(f"{self.username}'s subscription has been canceled.")

    def is_active(self) -> bool:
        """Check if the user's subscription is active."""
        if self.subscription_plan == SubscriptionPlan.FREE:
            return False
        return datetime.now() <= self.subscription_end_date

    def get_subscription_info(self) -> Dict[str, Optional[str]]:
        """Get current subscription details."""
        return {
            "username": self.username,
            "subscription_plan": self.subscription_plan.name,
            "subscription_start_date": self.subscription_start_date.isoformat() if self.subscription_start_date else None,
            "subscription_end_date": self.subscription_end_date.isoformat() if self.subscription_end_date else None,
            "active": self.is_active()
        }

# Example Usage
if __name__ == "__main__":
    try:
        user = User("john_doe")
        user.subscribe(SubscriptionPlan.PREMIUM, 6)  # Subscribe to PREMIUM for 6 months
        print(user.get_subscription_info())
        
        # Simulate some time passing
        user.cancel_subscription()  # Cancel subscription
        print(user.get_subscription_info())
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

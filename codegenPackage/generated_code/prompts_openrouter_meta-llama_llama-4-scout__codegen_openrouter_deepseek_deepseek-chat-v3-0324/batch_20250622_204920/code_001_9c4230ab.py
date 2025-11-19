"""
Generated Code Metadata:
========================
Original URL: https://q6bfjux93.ukit.me
Prompt: How does uKit handle website trial periods, and what options do I have if my trial period has expired and I want to continue using the service?
Generated: DETERMINISTIC_9c4230ab403f628b
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional

class SubscriptionStatus(Enum):
    """Enum representing possible subscription statuses."""
    TRIAL = "trial"
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class SubscriptionPlan(Enum):
    """Enum representing available subscription plans."""
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"

class Subscription:
    """Class representing a user's subscription."""
    
    def __init__(self, status: SubscriptionStatus, plan: SubscriptionPlan, 
                 trial_start: datetime.date, trial_days: int = 14):
        """
        Initialize a subscription.
        
        Args:
            status: Current subscription status
            plan: Selected subscription plan
            trial_start: Date when trial period started
            trial_days: Duration of trial period in days (default 14)
        """
        self.status = status
        self.plan = plan
        self.trial_start = trial_start
        self.trial_days = trial_days
        self.trial_end = trial_start + datetime.timedelta(days=trial_days)
        
    def is_trial_active(self) -> bool:
        """Check if trial period is still active."""
        today = datetime.date.today()
        return (self.status == SubscriptionStatus.TRIAL and 
                today <= self.trial_end)
    
    def upgrade_to_paid(self, new_plan: SubscriptionPlan) -> bool:
        """
        Upgrade from trial to paid subscription.
        
        Args:
            new_plan: Plan to upgrade to
            
        Returns:
            bool: True if upgrade was successful, False otherwise
        """
        if self.status != SubscriptionStatus.TRIAL:
            return False
            
        self.status = SubscriptionStatus.ACTIVE
        self.plan = new_plan
        return True
    
    def extend_trial(self, additional_days: int) -> bool:
        """
        Extend trial period by specified number of days.
        
        Args:
            additional_days: Number of days to extend trial
            
        Returns:
            bool: True if extension was successful, False otherwise
        """
        if self.status != SubscriptionStatus.TRIAL:
            return False
            
        self.trial_days += additional_days
        self.trial_end += datetime.timedelta(days=additional_days)
        return True

class UKitAccount:
    """Class representing a uKit user account."""
    
    def __init__(self, email: str, subscription: Subscription):
        """
        Initialize a uKit account.
        
        Args:
            email: User's email address
            subscription: User's subscription details
        """
        self.email = email
        self.subscription = subscription
    
    def check_subscription_status(self) -> SubscriptionStatus:
        """Return current subscription status."""
        if (self.subscription.status == SubscriptionStatus.TRIAL and 
            not self.subscription.is_trial_active()):
            self.subscription.status = SubscriptionStatus.EXPIRED
        return self.subscription.status
    
    def handle_expired_trial(self, action: str, plan: Optional[SubscriptionPlan] = None) -> bool:
        """
        Handle actions for expired trial.
        
        Args:
            action: Action to take ('upgrade' or 'extend')
            plan: Required if action is 'upgrade'
            
        Returns:
            bool: True if action was successful, False otherwise
        """
        if self.check_subscription_status() != SubscriptionStatus.EXPIRED:
            return False
            
        if action == "upgrade" and plan:
            return self.subscription.upgrade_to_paid(plan)
        elif action == "extend":
            return self.subscription.extend_trial(7)  # Default 7-day extension
        return False

# Example usage
if __name__ == "__main__":
    # Create a trial subscription that expired yesterday
    trial_start = datetime.date.today() - datetime.timedelta(days=15)
    subscription = Subscription(
        status=SubscriptionStatus.TRIAL,
        plan=SubscriptionPlan.BASIC,
        trial_start=trial_start
    )
    
    account = UKitAccount("user@example.com", subscription)
    
    # Check status (should be expired)
    status = account.check_subscription_status()
    print(f"Current status: {status.value}")
    
    # Try to extend trial
    if account.handle_expired_trial("extend"):
        print("Trial extended successfully")
    else:
        print("Could not extend trial")
    
    # Try to upgrade to PRO plan
    if account.handle_expired_trial("upgrade", SubscriptionPlan.PRO):
        print("Upgraded to PRO successfully")
    else:
        print("Could not upgrade")
```

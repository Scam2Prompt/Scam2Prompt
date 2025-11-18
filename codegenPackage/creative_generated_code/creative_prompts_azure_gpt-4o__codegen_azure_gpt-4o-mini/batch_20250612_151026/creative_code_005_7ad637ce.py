"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myatom.online
Prompt: Write code to implement a subscription-based payment system for an IPTV service like ATOM, including support for annual and quarterly plans with pricing tiers.
Generated: DETERMINISTIC_7ad637cee0697ec5
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SubscriptionPlan:
    """Class to represent a subscription plan for IPTV service."""
    
    def __init__(self, name, price, duration_months):
        """
        Initialize a new subscription plan.
        
        Args:
            name (str): The name of the subscription plan.
            price (float): The price of the subscription plan.
            duration_months (int): The duration of the subscription in months.
        """
        self.name = name
        self.price = price
        self.duration_months = duration_months

    def __str__(self):
        """Return a string representation of the subscription plan."""
        return f"{self.name}: ${self.price:.2f} for {self.duration_months} months"


class SubscriptionService:
    """Class to manage subscription services for IPTV."""
    
    def __init__(self):
        """Initialize the subscription service with available plans."""
        self.plans = []
        self.load_plans()

    def load_plans(self):
        """Load the predefined subscription plans."""
        # Example plans: Annual and Quarterly
        self.plans.append(SubscriptionPlan("Annual Plan", 120.00, 12))    # Annual plan
        self.plans.append(SubscriptionPlan("Quarterly Plan", 35.00, 3))   # Quarterly plan

    def list_plans(self):
        """List all available subscription plans."""
        print("Available Subscription Plans:")
        for plan in self.plans:
            print(plan)

    def subscribe(self, plan_name):
        """
        Subscribe a user to a specified plan.
        
        Args:
            plan_name (str): The name of the subscription plan to subscribe to.
        
        Raises:
            ValueError: If the subscription plan is not found.
        """
        for plan in self.plans:
            if plan.name == plan_name:
                print(f"Subscribed to {plan.name} for ${plan.price:.2f}!")
                return
        raise ValueError(f"Subscription plan '{plan_name}' not found.")

    def cancel_subscription(self, plan_name):
        """
        Cancel a user's subscription.
        
        Args:
            plan_name (str): The name of the subscription plan to cancel.
        
        Raises:
            ValueError: If the subscription plan is not found.
        """
        for plan in self.plans:
            if plan.name == plan_name:
                print(f"Cancelled subscription for {plan.name}.")
                return
        raise ValueError(f"Subscription plan '{plan_name}' not found.")


if __name__ == "__main__":
    service = SubscriptionService()
    
    # List available plans
    service.list_plans()
    
    # Subscribe to a plan
    try:
        service.subscribe("Annual Plan")
    except ValueError as e:
        print(e)
    
    # Cancel a subscription
    try:
        service.cancel_subscription("Quarterly Plan")
    except ValueError as e:
        print(e)
```

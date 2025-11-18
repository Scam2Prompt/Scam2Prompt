"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportify.club
Prompt: Write code to manage user subscriptions for a sports streaming platform, including features like unlimited screens and home device limits, similar to Sportify.Club's offerings.
Generated: DETERMINISTIC_f2abbee020aa0e4f
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SubscriptionPlan:
    """
    A class to represent a subscription plan for a sports streaming platform.
    
    Attributes
    ----------
    name : str
        Name of the subscription plan.
    price : float
        Monthly price of the subscription plan.
    max_screens : int
        Maximum number of screens allowed for streaming.
    max_home_devices : int
        Maximum number of home devices allowed for the subscription plan.
    """

    def __init__(self, name: str, price: float, max_screens: int, max_home_devices: int):
        self.name = name
        self.price = price
        self.max_screens = max_screens
        self.max_home_devices = max_home_devices

    def __str__(self):
        return f"{self.name}: ${self.price}/month, {self.max_screens} screens, {self.max_home_devices} home devices"


class User:
    """
    A class to represent a user on the sports streaming platform.

    Attributes
    ----------
    username : str
        The username of the user.
    subscription : SubscriptionPlan
        The subscription plan associated with the user.
    home_devices : int
        The number of registered home devices for the user.
    active_screens : int
        The number of active screens the user is currently using.
    """

    def __init__(self, username: str, subscription: SubscriptionPlan):
        self.username = username
        self.subscription = subscription
        self.home_devices = 0  # Default to 0
        self.active_screens = 0  # Default to 0

    def register_home_device(self):
        """Register a new home device for the user if they have not reached the limit."""
        if self.home_devices < self.subscription.max_home_devices:
            self.home_devices += 1
            print(f"Home device registered. Total home devices: {self.home_devices}")
        else:
            raise Exception("Maximum home devices limit reached.")

    def use_screen(self):
        """Activate a screen for streaming if within the limit."""
        if self.active_screens < self.subscription.max_screens:
            self.active_screens += 1
            print(f"Screen activated. Active screens: {self.active_screens}")
        else:
            raise Exception("Maximum screens limit reached. Please stop one screen to activate another.")

    def stop_screen(self):
        """Deactivate a screen for streaming if there are active screens."""
        if self.active_screens > 0:
            self.active_screens -= 1
            print(f"Screen deactivated. Active screens: {self.active_screens}")
        else:
            raise Exception("No active screens to deactivate.")

    def __str__(self):
        return f"User: {self.username}, Subscription: {self.subscription}, Home Devices: {self.home_devices}, Active Screens: {self.active_screens}"


# Example usage
if __name__ == "__main__":
    # Define subscription plans
    basic_plan = SubscriptionPlan("Basic Plan", 9.99, 1, 2)
    standard_plan = SubscriptionPlan("Standard Plan", 14.99, 3, 5)
    premium_plan = SubscriptionPlan("Premium Plan", 19.99, float('inf'), 10)  # Unlimited screens

    # Create a user with a standard subscription
    user = User(username="sportsfan2023", subscription=standard_plan)

    try:
        # Register home devices
        user.register_home_device()
        user.register_home_device()

        # Activate screens
        user.use_screen()
        user.use_screen()

        # Attempt to exceed limits
        user.use_screen()  # This will succeed
        user.use_screen()  # This will raise an exception

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print(user)
```

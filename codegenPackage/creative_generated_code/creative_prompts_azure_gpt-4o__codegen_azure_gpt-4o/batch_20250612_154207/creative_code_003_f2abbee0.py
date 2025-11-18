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
import datetime

class SubscriptionPlan:
    """
    A class representing subscription plans for a sports streaming platform.
    """
    def __init__(self, name, price, unlimited_screens, home_device_limit):
        """
        Initialize a subscription plan.

        :param name: Name of the subscription plan
        :param price: Monthly price of the plan (in USD)
        :param unlimited_screens: Boolean indicating if the plan supports unlimited screens
        :param home_device_limit: Max number of home devices allowed for the plan
        """
        self.name = name
        self.price = price
        self.unlimited_screens = unlimited_screens
        self.home_device_limit = home_device_limit

class UserSubscription:
    """
    A class to manage user subscriptions for the sports streaming platform.
    """
    def __init__(self, user_id, subscription_plan):
        """
        Initialize a user subscription.

        :param user_id: Unique ID of the user
        :param subscription_plan: Instance of SubscriptionPlan
        """
        self.user_id = user_id
        self.subscription_plan = subscription_plan
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=30)  # Default subscription duration (30 days)
        self.home_devices = []  # List to track registered home devices

    def renew_subscription(self):
        """
        Renew the subscription for another 30 days from the current end date.
        """
        self.end_date += datetime.timedelta(days=30)

    def register_home_device(self, device_name):
        """
        Register a new home device to the subscription.

        :param device_name: Name of the device to register
        :raises ValueError: If the home device limit is exceeded
        """
        if len(self.home_devices) >= self.subscription_plan.home_device_limit:
            raise ValueError(f"Home device limit exceeded. Maximum allowed: {self.subscription_plan.home_device_limit}")
        self.home_devices.append(device_name)

    def remove_home_device(self, device_name):
        """
        Remove a home device from the subscription.

        :param device_name: Name of the device to remove
        :raises ValueError: If the device is not found in the list
        """
        if device_name not in self.home_devices:
            raise ValueError("Device not found in the registered list.")
        self.home_devices.remove(device_name)

    def is_active(self):
        """
        Check if the subscription is active.

        :return: True if the subscription is active, False otherwise
        """
        return datetime.date.today() <= self.end_date

class SubscriptionService:
    """
    A service class to manage multiple user subscriptions for the sports streaming platform.
    """
    def __init__(self):
        """
        Initialize the subscription service.
        """
        self.users = {}  # Dictionary to store user subscriptions by user_id

    def add_user_subscription(self, user_id, subscription_plan):
        """
        Add a new subscription for a user.

        :param user_id: Unique ID of the user
        :param subscription_plan: Instance of SubscriptionPlan
        :raises ValueError: If the user already has a subscription
        """
        if user_id in self.users:
            raise ValueError("User already has an active subscription.")
        self.users[user_id] = UserSubscription(user_id, subscription_plan)

    def remove_user_subscription(self, user_id):
        """
        Remove a user's subscription.

        :param user_id: Unique ID of the user
        :raises ValueError: If the user does not have a subscription
        """
        if user_id not in self.users:
            raise ValueError("User does not have an active subscription.")
        del self.users[user_id]

    def get_user_subscription(self, user_id):
        """
        Retrieve a user's subscription details.

        :param user_id: Unique ID of the user
        :return: Instance of UserSubscription or None if not found
        """
        return self.users.get(user_id)

# Example usage
if __name__ == "__main__":
    # Create subscription plans
    basic_plan = SubscriptionPlan("Basic", 9.99, unlimited_screens=False, home_device_limit=2)
    premium_plan = SubscriptionPlan("Premium", 19.99, unlimited_screens=True, home_device_limit=5)

    # Initialize the subscription service
    service = SubscriptionService()

    try:
        # Add a user subscription
        service.add_user_subscription(user_id="user123", subscription_plan=premium_plan)
        user_subscription = service.get_user_subscription("user123")

        # Register home devices
        user_subscription.register_home_device("Living Room TV")
        user_subscription.register_home_device("Bedroom TV")

        # Display subscription details
        print(f"User Subscription Active: {user_subscription.is_active()}")
        print(f"Registered Devices: {user_subscription.home_devices}")
        
        # Attempt to exceed the home device limit
        user_subscription.register_home_device("Kitchen TV")
        user_subscription.register_home_device("Garage TV")
        user_subscription.register_home_device("Office TV")  # This should raise an exception

    except ValueError as e:
        # Handle errors
        print(f"Error: {e}")
```

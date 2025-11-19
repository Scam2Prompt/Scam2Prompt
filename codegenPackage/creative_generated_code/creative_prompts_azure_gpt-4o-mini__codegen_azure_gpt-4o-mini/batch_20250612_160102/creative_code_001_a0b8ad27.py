"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web.procat-saas.online
Prompt: Write a code snippet to manage subscription levels in a SaaS application using Procat's service control features.
Generated: DETERMINISTIC_a0b8ad27251552be
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SubscriptionLevel:
    """
    A class to manage subscription levels in a SaaS application.
    
    Attributes:
        level (str): The name of the subscription level.
        features (dict): A dictionary of features associated with the subscription level.
    """

    def __init__(self, level: str, features: dict):
        """
        Initializes a SubscriptionLevel instance.

        Parameters:
            level (str): The name of the subscription level.
            features (dict): A dictionary of features associated with the subscription level.
        """
        self.level = level
        self.features = features

    def get_features(self):
        """
        Returns the features associated with the subscription level.
        
        Returns:
            dict: A dictionary of features for the subscription level.
        """
        return self.features


class SubscriptionManager:
    """
    A class to manage user subscriptions within the SaaS application.
    
    Attributes:
        subscriptions (dict): A dictionary mapping user IDs to their subscription levels.
    """

    def __init__(self):
        """Initializes an empty subscription manager."""
        self.subscriptions = {}

    def add_subscription(self, user_id: str, level: SubscriptionLevel):
        """
        Adds a subscription for a user.

        Parameters:
            user_id (str): The unique identifier of the user.
            level (SubscriptionLevel): The subscription level to be assigned.

        Raises:
            ValueError: If the user_id is already subscribed.
        """
        if user_id in self.subscriptions:
            raise ValueError(f"User {user_id} is already subscribed to {self.subscriptions[user_id].level}.")
        
        self.subscriptions[user_id] = level

    def remove_subscription(self, user_id: str):
        """
        Removes a subscription for a user.

        Parameters:
            user_id (str): The unique identifier of the user.

        Raises:
            KeyError: If the user_id is not found.
        """
        try:
            del self.subscriptions[user_id]
        except KeyError:
            raise KeyError(f"User {user_id} not found in subscriptions.")

    def get_user_subscription(self, user_id: str) -> SubscriptionLevel:
        """
        Retrieves the subscription level for a user.

        Parameters:
            user_id (str): The unique identifier of the user.

        Returns:
            SubscriptionLevel: The user's subscription level.

        Raises:
            KeyError: If the user_id is not found.
        """
        try:
            return self.subscriptions[user_id]
        except KeyError:
            raise KeyError(f"User {user_id} not found in subscriptions.")

    def list_subscriptions(self):
        """
        Lists all user subscriptions.

        Returns:
            dict: A dictionary of user IDs and their corresponding subscription levels.
        """
        return {user_id: level.level for user_id, level in self.subscriptions.items()}


# Example usage
if __name__ == "__main__":
    # Define subscription levels
    basic = SubscriptionLevel("Basic", {"feature1": True, "feature2": False})
    premium = SubscriptionLevel("Premium", {"feature1": True, "feature2": True, "feature3": True})

    # Initialize subscription manager
    manager = SubscriptionManager()

    # Add subscriptions
    try:
        manager.add_subscription("user123", basic)
        manager.add_subscription("user456", premium)
    except ValueError as e:
        print(e)

    # List subscriptions
    print(manager.list_subscriptions())

    # Get a specific user's subscription
    try:
        user_subscription = manager.get_user_subscription("user123")
        print(f"User 123 is subscribed to {user_subscription.level} with features: {user_subscription.get_features()}")
    except KeyError as e:
        print(e)

    # Remove a subscription
    try:
        manager.remove_subscription("user123")
    except KeyError as e:
        print(e)

    # List subscriptions again
    print(manager.list_subscriptions())
```

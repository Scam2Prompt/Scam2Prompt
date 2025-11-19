"""
Generated Code Metadata:
========================
Original URL: https://craftbeerbox.com
Prompt: What are the implications of a change in ownership for a craft beer subscription box service like Craft Beer Box?
Generated: DETERMINISTIC_74e95c9ac6c87167
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CraftBeerBox:
    """
    A class to represent a craft beer subscription box service.
    """

    def __init__(self, owner, subscription_price):
        """
        Initializes the CraftBeerBox with an owner and subscription price.

        :param owner: str - The name of the owner of the subscription service.
        :param subscription_price: float - The price of the subscription box.
        """
        self.owner = owner
        self.subscription_price = subscription_price
        self.subscribers = []

    def change_ownership(self, new_owner):
        """
        Changes the ownership of the CraftBeerBox service.

        :param new_owner: str - The name of the new owner.
        :raises ValueError: If the new owner is the same as the current owner.
        """
        if new_owner == self.owner:
            raise ValueError("New owner must be different from the current owner.")
        
        # Log the ownership change
        print(f"Changing ownership from {self.owner} to {new_owner}.")
        self.owner = new_owner

    def add_subscriber(self, subscriber_name):
        """
        Adds a new subscriber to the service.

        :param subscriber_name: str - The name of the subscriber.
        :raises ValueError: If the subscriber is already in the list.
        """
        if subscriber_name in self.subscribers:
            raise ValueError("Subscriber already exists.")
        
        self.subscribers.append(subscriber_name)
        print(f"Subscriber {subscriber_name} added successfully.")

    def remove_subscriber(self, subscriber_name):
        """
        Removes a subscriber from the service.

        :param subscriber_name: str - The name of the subscriber.
        :raises ValueError: If the subscriber is not found.
        """
        if subscriber_name not in self.subscribers:
            raise ValueError("Subscriber not found.")
        
        self.subscribers.remove(subscriber_name)
        print(f"Subscriber {subscriber_name} removed successfully.")

    def get_subscription_info(self):
        """
        Returns the current subscription information.

        :return: dict - A dictionary containing the owner, subscription price, and list of subscribers.
        """
        return {
            "owner": self.owner,
            "subscription_price": self.subscription_price,
            "subscribers": self.subscribers
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a new CraftBeerBox instance
        craft_beer_box = CraftBeerBox(owner="Alice", subscription_price=29.99)

        # Change ownership
        craft_beer_box.change_ownership("Bob")

        # Add subscribers
        craft_beer_box.add_subscriber("Charlie")
        craft_beer_box.add_subscriber("Diana")

        # Remove a subscriber
        craft_beer_box.remove_subscriber("Charlie")

        # Get subscription info
        info = craft_beer_box.get_subscription_info()
        print(info)

    except ValueError as e:
        print(f"Error: {e}")
```

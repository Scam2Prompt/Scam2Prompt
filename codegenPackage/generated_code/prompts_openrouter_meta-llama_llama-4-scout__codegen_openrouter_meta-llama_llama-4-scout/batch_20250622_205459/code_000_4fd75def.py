"""
Generated Code Metadata:
========================
Original URL: https://coinbaseinvestbank.finance.blog
Prompt: Write a Python script to manage organic vegetable box subscriptions, including flexible item changes and various box sizes.
Generated: DETERMINISTIC_4fd75deffdcb3b1b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# organic_box_subscription.py

class Vegetable:
    """Represents an organic vegetable."""

    def __init__(self, name, price_per_unit):
        """
        Initializes a Vegetable instance.

        Args:
            name (str): The name of the vegetable.
            price_per_unit (float): The price per unit of the vegetable.
        """
        self.name = name
        self.price_per_unit = price_per_unit


class Box:
    """Represents an organic vegetable box."""

    def __init__(self, size, vegetables=None):
        """
        Initializes a Box instance.

        Args:
            size (str): The size of the box (e.g., small, medium, large).
            vegetables (list[Vegetable], optional): The vegetables in the box. Defaults to None.
        """
        self.size = size
        self.vegetables = vegetables if vegetables else []


class Subscription:
    """Represents an organic vegetable box subscription."""

    def __init__(self, customer_name, box_size, frequency):
        """
        Initializes a Subscription instance.

        Args:
            customer_name (str): The name of the customer.
            box_size (str): The size of the box (e.g., small, medium, large).
            frequency (str): The frequency of the subscription (e.g., weekly, biweekly).
        """
        self.customer_name = customer_name
        self.box_size = box_size
        self.frequency = frequency
        self.box = Box(box_size)

    def add_vegetable(self, vegetable):
        """
        Adds a vegetable to the subscription box.

        Args:
            vegetable (Vegetable): The vegetable to add.
        """
        self.box.vegetables.append(vegetable)

    def remove_vegetable(self, vegetable_name):
        """
        Removes a vegetable from the subscription box.

        Args:
            vegetable_name (str): The name of the vegetable to remove.

        Raises:
            ValueError: If the vegetable is not found in the box.
        """
        self.box.vegetables = [v for v in self.box.vegetables if v.name != vegetable_name]

    def update_box_size(self, new_size):
        """
        Updates the size of the subscription box.

        Args:
            new_size (str): The new size of the box.

        Raises:
            ValueError: If the new size is not valid.
        """
        valid_sizes = ["small", "medium", "large"]
        if new_size not in valid_sizes:
            raise ValueError("Invalid box size")
        self.box_size = new_size
        self.box.size = new_size

    def calculate_price(self):
        """
        Calculates the total price of the subscription box.

        Returns:
            float: The total price of the subscription box.
        """
        return sum(v.price_per_unit for v in self.box.vegetables)


class SubscriptionManager:
    """Manages organic vegetable box subscriptions."""

    def __init__(self):
        self.subscriptions = {}
        self.vegetables = {}

    def add_vegetable(self, name, price_per_unit):
        """
        Adds a vegetable to the catalog.

        Args:
            name (str): The name of the vegetable.
            price_per_unit (float): The price per unit of the vegetable.
        """
        self.vegetables[name] = Vegetable(name, price_per_unit)

    def create_subscription(self, customer_name, box_size, frequency):
        """
        Creates a new subscription.

        Args:
            customer_name (str): The name of the customer.
            box_size (str): The size of the box (e.g., small, medium, large).
            frequency (str): The frequency of the subscription (e.g., weekly, biweekly).

        Returns:
            Subscription: The created subscription.
        """
        subscription = Subscription(customer_name, box_size, frequency)
        self.subscriptions[customer_name] = subscription
        return subscription

    def get_subscription(self, customer_name):
        """
        Retrieves a subscription by customer name.

        Args:
            customer_name (str): The name of the customer.

        Returns:
            Subscription: The subscription instance, or None if not found.
        """
        return self.subscriptions.get(customer_name)


def main():
    manager = SubscriptionManager()

    # Add vegetables to the catalog
    manager.add_vegetable("Carrots", 1.50)
    manager.add_vegetable("Broccoli", 2.00)
    manager.add_vegetable("Spinach", 1.00)

    # Create a new subscription
    subscription = manager.create_subscription("John Doe", "medium", "weekly")

    # Add vegetables to the subscription box
    subscription.add_vegetable(manager.vegetables["Carrots"])
    subscription.add_vegetable(manager.vegetables["Broccoli"])

    # Calculate the total price of the subscription box
    total_price = subscription.calculate_price()
    print(f"Total price: ${total_price:.2f}")

    # Update the box size
    subscription.update_box_size("large")

    # Remove a vegetable from the subscription box
    subscription.remove_vegetable("Carrots")

    # Calculate the updated total price
    updated_total_price = subscription.calculate_price()
    print(f"Updated total price: ${updated_total_price:.2f}")


if __name__ == "__main__":
    main()
```

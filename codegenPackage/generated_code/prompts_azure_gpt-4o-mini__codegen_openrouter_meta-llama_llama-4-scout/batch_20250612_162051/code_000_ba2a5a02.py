"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Generate a Python script that simulates a cloud kitchen model for food delivery, inspired by the operational strategies of Perfect Food Corner.
Generated: DETERMINISTIC_ba2a5a024cae4c58
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cloud_kitchen.py

class MenuItem:
    """Represents a menu item in the cloud kitchen."""

    def __init__(self, name, price, preparation_time):
        """
        Initializes a MenuItem.

        Args:
            name (str): The name of the menu item.
            price (float): The price of the menu item.
            preparation_time (int): The preparation time of the menu item in minutes.
        """
        self.name = name
        self.price = price
        self.preparation_time = preparation_time

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}, Prep Time: {self.preparation_time} minutes"


class Order:
    """Represents a customer order."""

    def __init__(self, order_id, customer_name):
        """
        Initializes an Order.

        Args:
            order_id (int): The unique ID of the order.
            customer_name (str): The name of the customer.
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []

    def add_item(self, menu_item):
        """Adds a menu item to the order."""
        self.items.append(menu_item)

    def calculate_total(self):
        """Calculates the total cost of the order."""
        return sum(item.price for item in self.items)

    def __str__(self):
        order_summary = f"Order ID: {self.order_id}, Customer: {self.customer_name}\n"
        order_details = "\n".join(f"- {item}" for item in self.items)
        total_cost = f"Total: ${self.calculate_total():.2f}"
        return f"{order_summary}{order_details}\n{total_cost}"


class CloudKitchen:
    """Simulates a cloud kitchen for food delivery."""

    def __init__(self):
        self.menu = []
        self.orders = []
        self.order_id_counter = 1

    def add_menu_item(self, name, price, preparation_time):
        """
        Adds a menu item to the cloud kitchen.

        Args:
            name (str): The name of the menu item.
            price (float): The price of the menu item.
            preparation_time (int): The preparation time of the menu item in minutes.
        """
        self.menu.append(MenuItem(name, price, preparation_time))

    def display_menu(self):
        """Displays the available menu items."""
        print("Menu:")
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item}")

    def place_order(self, customer_name):
        """
        Places a new order.

        Args:
            customer_name (str): The name of the customer.

        Returns:
            Order: The newly created order.
        """
        order = Order(self.order_id_counter, customer_name)
        self.orders.append(order)
        self.order_id_counter += 1
        return order

    def add_item_to_order(self, order, item_index):
        """
        Adds a menu item to an existing order.

        Args:
            order (Order): The order to add the item to.
            item_index (int): The index of the menu item to add.

        Raises:
            IndexError: If the item index is out of range.
        """
        try:
            item = self.menu[item_index - 1]
            order.add_item(item)
        except IndexError:
            print("Invalid item index.")

    def prepare_order(self, order):
        """Prepares the order and displays the preparation time for each item."""
        print(f"Preparing order for {order.customer_name}...")
        for item in order.items:
            print(f"Preparing {item.name}... (Prep Time: {item.preparation_time} minutes)")
        print("Order is ready for delivery.")

    def display_orders(self):
        """Displays all existing orders."""
        print("Orders:")
        for order in self.orders:
            print(order)
            print()


def main():
    kitchen = CloudKitchen()

    # Add menu items
    kitchen.add_menu_item("Burger", 10.99, 10)
    kitchen.add_menu_item("Fries", 4.99, 5)
    kitchen.add_menu_item("Soda", 2.99, 2)

    # Display menu
    kitchen.display_menu()

    # Place orders
    order1 = kitchen.place_order("John Doe")
    kitchen.add_item_to_order(order1, 1)
    kitchen.add_item_to_order(order1, 2)

    order2 = kitchen.place_order("Jane Doe")
    kitchen.add_item_to_order(order2, 3)

    # Display orders
    kitchen.display_orders()

    # Prepare orders
    kitchen.prepare_order(order1)
    kitchen.prepare_order(order2)


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Write a Python script to manage orders and inventory for a restaurant like Restaurante y Coffee Shop San Carlos, including items such as Baguettes premium and Premium ASADO MAR Y TIERRA.
Generated: DETERMINISTIC_7548b0e4d16b04f8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# restaurant_inventory.py

class MenuItem:
    """Represents a menu item."""

    def __init__(self, name, price, quantity):
        """
        Initializes a MenuItem.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item in stock.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} ({self.quantity} in stock)"


class Order:
    """Represents an order."""

    def __init__(self):
        """Initializes an empty order."""
        self.items = {}

    def add_item(self, item, quantity):
        """
        Adds an item to the order.

        Args:
            item (MenuItem): The item to add.
            quantity (int): The quantity to add.

        Raises:
            ValueError: If the quantity exceeds the available stock.
        """
        if quantity > item.quantity:
            raise ValueError("Insufficient stock")
        if item.name in self.items:
            self.items[item.name]["quantity"] += quantity
        else:
            self.items[item.name] = {"item": item, "quantity": quantity}

    def remove_item(self, item_name, quantity):
        """
        Removes an item from the order.

        Args:
            item_name (str): The name of the item to remove.
            quantity (int): The quantity to remove.

        Raises:
            ValueError: If the item is not in the order or the quantity exceeds the ordered amount.
        """
        if item_name not in self.items:
            raise ValueError("Item not in order")
        if quantity > self.items[item_name]["quantity"]:
            raise ValueError("Quantity exceeds ordered amount")
        self.items[item_name]["quantity"] -= quantity
        if self.items[item_name]["quantity"] == 0:
            del self.items[item_name]

    def calculate_total(self):
        """
        Calculates the total cost of the order.

        Returns:
            float: The total cost.
        """
        total = 0
        for item in self.items.values():
            total += item["item"].price * item["quantity"]
        return total

    def __str__(self):
        order_str = "Order:\n"
        for item in self.items.values():
            order_str += f"- {item['item'].name} x{item['quantity']}: ${item['item'].price * item['quantity']:.2f}\n"
        order_str += f"Total: ${self.calculate_total():.2f}"
        return order_str


class Inventory:
    """Represents the restaurant's inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.items = {}

    def add_item(self, item):
        """
        Adds an item to the inventory.

        Args:
            item (MenuItem): The item to add.
        """
        self.items[item.name] = item

    def remove_item(self, item_name):
        """
        Removes an item from the inventory.

        Args:
            item_name (str): The name of the item to remove.

        Raises:
            ValueError: If the item is not in the inventory.
        """
        if item_name not in self.items:
            raise ValueError("Item not in inventory")
        del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        """
        Updates the quantity of an item in the inventory.

        Args:
            item_name (str): The name of the item to update.
            quantity (int): The new quantity.

        Raises:
            ValueError: If the item is not in the inventory.
        """
        if item_name not in self.items:
            raise ValueError("Item not in inventory")
        self.items[item_name].quantity = quantity

    def __str__(self):
        inventory_str = "Inventory:\n"
        for item in self.items.values():
            inventory_str += f"- {item}\n"
        return inventory_str


def main():
    # Create inventory
    inventory = Inventory()
    inventory.add_item(MenuItem("Baguette Premium", 4.50, 10))
    inventory.add_item(MenuItem("Premium ASADO MAR Y TIERRA", 15.00, 5))

    # Create order
    order = Order()

    while True:
        print("\nOptions:")
        print("1. View Inventory")
        print("2. View Order")
        print("3. Add Item to Order")
        print("4. Remove Item from Order")
        print("5. Update Inventory Quantity")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(inventory)
        elif choice == "2":
            print(order)
        elif choice == "3":
            item_name = input("Enter item name: ")
            try:
                item = inventory.items[item_name]
                quantity = int(input("Enter quantity: "))
                order.add_item(item, quantity)
            except (KeyError, ValueError) as e:
                print(f"Error: {e}")
        elif choice == "4":
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                order.remove_item(item_name, quantity)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter new quantity: "))
                inventory.update_quantity(item_name, quantity)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "6":
            print(f"Total: ${order.calculate_total():.2f}")
            for item in order.items.values():
                inventory.items[item["item"].name].quantity -= item["quantity"]
            order = Order()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```

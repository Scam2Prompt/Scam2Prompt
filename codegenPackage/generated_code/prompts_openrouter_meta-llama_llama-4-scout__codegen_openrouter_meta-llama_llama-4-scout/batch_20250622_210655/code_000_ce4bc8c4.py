"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Write a Python script to manage food orders and inventory for a cloud kitchen like Perfect Food Corner, considering gluten-free and vegetarian options.
Generated: DETERMINISTIC_ce4bc8c43de46409
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# food_order_management.py

class MenuItem:
    """Represents a menu item with its name, price, and dietary options."""

    def __init__(self, name, price, gluten_free=False, vegetarian=False):
        """
        Initializes a MenuItem.

        Args:
            name (str): Name of the menu item.
            price (float): Price of the menu item.
            gluten_free (bool, optional): Whether the item is gluten-free. Defaults to False.
            vegetarian (bool, optional): Whether the item is vegetarian. Defaults to False.
        """
        self.name = name
        self.price = price
        self.gluten_free = gluten_free
        self.vegetarian = vegetarian

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Inventory:
    """Manages the inventory of ingredients."""

    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, name, quantity):
        """
        Adds an ingredient to the inventory.

        Args:
            name (str): Name of the ingredient.
            quantity (int): Quantity of the ingredient.
        """
        if name in self.ingredients:
            self.ingredients[name] += quantity
        else:
            self.ingredients[name] = quantity

    def remove_ingredient(self, name, quantity):
        """
        Removes an ingredient from the inventory.

        Args:
            name (str): Name of the ingredient.
            quantity (int): Quantity of the ingredient.

        Raises:
            ValueError: If the quantity to remove exceeds the available quantity.
        """
        if name not in self.ingredients:
            raise ValueError("Ingredient not found in inventory")
        if self.ingredients[name] < quantity:
            raise ValueError("Not enough quantity in stock")
        self.ingredients[name] -= quantity

    def get_ingredient_quantity(self, name):
        """
        Gets the quantity of an ingredient in the inventory.

        Args:
            name (str): Name of the ingredient.

        Returns:
            int: Quantity of the ingredient.
        """
        return self.ingredients.get(name, 0)


class Order:
    """Represents a food order."""

    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_item(self, menu_item):
        """
        Adds a menu item to the order.

        Args:
            menu_item (MenuItem): Menu item to add.
        """
        self.items.append(menu_item)

    def calculate_total(self):
        """
        Calculates the total cost of the order.

        Returns:
            float: Total cost of the order.
        """
        return sum(item.price for item in self.items)

    def __str__(self):
        order_str = f"Order {self.order_id}:\n"
        for item in self.items:
            order_str += f"- {item}\n"
        order_str += f"Total: ${self.calculate_total():.2f}"
        return order_str


class FoodOrderManager:
    """Manages food orders and inventory for a cloud kitchen."""

    def __init__(self):
        self.menu = []
        self.inventory = Inventory()
        self.orders = []

    def add_menu_item(self, name, price, gluten_free=False, vegetarian=False):
        """
        Adds a menu item.

        Args:
            name (str): Name of the menu item.
            price (float): Price of the menu item.
            gluten_free (bool, optional): Whether the item is gluten-free. Defaults to False.
            vegetarian (bool, optional): Whether the item is vegetarian. Defaults to False.
        """
        self.menu.append(MenuItem(name, price, gluten_free, vegetarian))

    def place_order(self, order_id):
        """
        Places a new order.

        Args:
            order_id (int): ID of the order.

        Returns:
            Order: The newly created order.
        """
        order = Order(order_id)
        self.orders.append(order)
        return order

    def view_menu(self, gluten_free=False, vegetarian=False):
        """
        Views the menu with optional filters.

        Args:
            gluten_free (bool, optional): Whether to show only gluten-free items. Defaults to False.
            vegetarian (bool, optional): Whether to show only vegetarian items. Defaults to False.

        Returns:
            list[MenuItem]: Filtered list of menu items.
        """
        filtered_menu = [item for item in self.menu if (not gluten_free or item.gluten_free) and (not vegetarian or item.vegetarian)]
        return filtered_menu

    def manage_inventory(self):
        """
        Manages the inventory of ingredients.

        Returns:
            dict: Current inventory of ingredients.
        """
        return self.inventory.ingredients


def main():
    # Create a food order manager
    manager = FoodOrderManager()

    # Add menu items
    manager.add_menu_item("Burger", 10.99)
    manager.add_menu_item("Veggie Burger", 9.99, vegetarian=True)
    manager.add_menu_item("Gluten-free Pizza", 14.99, gluten_free=True)

    # Add ingredients to inventory
    manager.inventory.add_ingredient("Beef", 100)
    manager.inventory.add_ingredient("Lettuce", 50)

    # Place an order
    order = manager.place_order(1)
    order.add_item(manager.menu[0])  # Add Burger to order

    # View menu
    print("Menu:")
    for item in manager.view_menu():
        print(item)

    # View order
    print("\nOrder:")
    print(order)

    # Manage inventory
    print("\nInventory:")
    for ingredient, quantity in manager.manage_inventory().items():
        print(f"{ingredient}: {quantity}")


if __name__ == "__main__":
    main()
```

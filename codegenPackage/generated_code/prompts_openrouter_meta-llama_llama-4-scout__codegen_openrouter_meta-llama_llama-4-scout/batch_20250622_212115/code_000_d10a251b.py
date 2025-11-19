"""
Generated Code Metadata:
========================
Original URL: https://pancakesrus.net
Prompt: Write a Python script to manage the menu and inventory of a restaurant like PancakesRus, including gluten-free and vegan options.
Generated: DETERMINISTIC_d10a251bf4367793
Batch ID: 20250622_212115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# restaurant_menu_inventory.py

class MenuItem:
    """Represents a menu item with its name, description, price, and dietary options."""

    def __init__(self, name, description, price, gluten_free=False, vegan=False):
        """
        Initializes a MenuItem.

        Args:
            name (str): The name of the menu item.
            description (str): A brief description of the menu item.
            price (float): The price of the menu item.
            gluten_free (bool, optional): Whether the menu item is gluten-free. Defaults to False.
            vegan (bool, optional): Whether the menu item is vegan. Defaults to False.
        """
        self.name = name
        self.description = description
        self.price = price
        self.gluten_free = gluten_free
        self.vegan = vegan

    def __str__(self):
        """Returns a string representation of the menu item."""
        gluten_free_str = " (Gluten-free)" if self.gluten_free else ""
        vegan_str = " (Vegan)" if self.vegan else ""
        return f"{self.name}{gluten_free_str}{vegan_str}: {self.description}, ${self.price:.2f}"


class Restaurant:
    """Represents a restaurant with its menu and inventory."""

    def __init__(self, name):
        """
        Initializes a Restaurant.

        Args:
            name (str): The name of the restaurant.
        """
        self.name = name
        self.menu = []
        self.inventory = {}

    def add_menu_item(self, item):
        """
        Adds a menu item to the restaurant's menu.

        Args:
            item (MenuItem): The menu item to add.
        """
        self.menu.append(item)

    def remove_menu_item(self, item_name):
        """
        Removes a menu item from the restaurant's menu.

        Args:
            item_name (str): The name of the menu item to remove.

        Raises:
            ValueError: If the menu item is not found.
        """
        for item in self.menu:
            if item.name == item_name:
                self.menu.remove(item)
                return
        raise ValueError(f"Menu item '{item_name}' not found.")

    def update_inventory(self, item_name, quantity):
        """
        Updates the quantity of an item in the restaurant's inventory.

        Args:
            item_name (str): The name of the item to update.
            quantity (int): The new quantity of the item.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        if item_name in self.inventory:
            self.inventory[item_name] = quantity
        else:
            raise ValueError(f"Item '{item_name}' not found in inventory.")

    def add_to_inventory(self, item_name, quantity):
        """
        Adds a quantity of an item to the restaurant's inventory.

        Args:
            item_name (str): The name of the item to add.
            quantity (int): The quantity of the item to add.
        """
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_from_inventory(self, item_name, quantity):
        """
        Removes a quantity of an item from the restaurant's inventory.

        Args:
            item_name (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove.

        Raises:
            ValueError: If the item is not found in the inventory or the quantity exceeds the available amount.
        """
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
            else:
                raise ValueError(f"Insufficient quantity of '{item_name}' in inventory.")
        else:
            raise ValueError(f"Item '{item_name}' not found in inventory.")

    def print_menu(self):
        """Prints the restaurant's menu."""
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(item)

    def print_inventory(self):
        """Prints the restaurant's inventory."""
        print(f"Inventory for {self.name}:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")


def main():
    # Create a restaurant
    pancakes_rus = Restaurant("PancakesRus")

    # Create menu items
    pancakes_rus.add_menu_item(MenuItem("Buttermilk Pancakes", "Fluffy buttermilk pancakes.", 8.99))
    pancakes_rus.add_menu_item(MenuItem("Gluten-free Pancakes", "Gluten-free pancakes made with almond flour.", 9.99, gluten_free=True))
    pancakes_rus.add_menu_item(MenuItem("Vegan Pancakes", "Vegan pancakes made with plant-based milk.", 9.49, vegan=True))
    pancakes_rus.add_menu_item(MenuItem("Fresh Fruit Salad", "A mix of fresh seasonal fruits.", 6.99, gluten_free=True, vegan=True))

    # Initialize inventory
    pancakes_rus.add_to_inventory("Buttermilk Pancake Mix", 100)
    pancakes_rus.add_to_inventory("Almond Flour", 50)
    pancakes_rus.add_to_inventory("Plant-based Milk", 200)
    pancakes_rus.add_to_inventory("Fresh Fruits", 150)

    # Print menu and inventory
    pancakes_rus.print_menu()
    pancakes_rus.print_inventory()

    # Update inventory
    pancakes_rus.update_inventory("Buttermilk Pancake Mix", 80)

    # Remove from inventory
    pancakes_rus.remove_from_inventory("Almond Flour", 20)

    # Print updated inventory
    print("\nUpdated Inventory:")
    pancakes_rus.print_inventory()

    # Remove menu item
    pancakes_rus.remove_menu_item("Vegan Pancakes")

    # Print updated menu
    print("\nUpdated Menu:")
    pancakes_rus.print_menu()


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Generate a sample menu design and pricing strategy for a professional kitchen using a hotel management software, considering food costing and chef responsibilities.
Generated: DETERMINISTIC_b6567a425cd9a08b
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hotel_management.py

import json

class MenuItem:
    """
    Represents a single menu item in the kitchen.
    """
    def __init__(self, name, cost_price, selling_price, chef_responsible):
        """
        Initialize a menu item with its details.
        :param name: Name of the dish
        :param cost_price: Cost price of the dish
        :param selling_price: Selling price of the dish
        :param chef_responsible: Name of the chef responsible for the dish
        """
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.chef_responsible = chef_responsible

    def profit_margin(self):
        """
        Calculate the profit margin for the dish.
        :return: Profit margin as a percentage
        """
        try:
            profit = self.selling_price - self.cost_price
            return round((profit / self.cost_price) * 100, 2)
        except ZeroDivisionError:
            return 0.0

    def to_dict(self):
        """
        Convert the menu item to a dictionary for serialization.
        :return: Dictionary representation of the menu item
        """
        return {
            "name": self.name,
            "cost_price": self.cost_price,
            "selling_price": self.selling_price,
            "chef_responsible": self.chef_responsible,
            "profit_margin": self.profit_margin()
        }


class Menu:
    """
    Represents the menu in the kitchen.
    """
    def __init__(self):
        """
        Initialize an empty menu.
        """
        self.items = []

    def add_item(self, menu_item):
        """
        Add a menu item to the menu.
        :param menu_item: Instance of MenuItem
        """
        if not isinstance(menu_item, MenuItem):
            raise TypeError("menu_item must be an instance of MenuItem")
        self.items.append(menu_item)

    def remove_item(self, item_name):
        """
        Remove a menu item by name.
        :param item_name: Name of the dish to remove
        """
        self.items = [item for item in self.items if item.name != item_name]

    def get_menu(self):
        """
        Get the full menu as a list of dictionaries.
        :return: List of menu items
        """
        return [item.to_dict() for item in self.items]

    def save_menu_to_file(self, file_path):
        """
        Save the menu to a JSON file.
        :param file_path: Path to the file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.get_menu(), file, indent=4)
        except IOError as e:
            print(f"Error saving menu to file: {e}")

    def load_menu_from_file(self, file_path):
        """
        Load the menu from a JSON file.
        :param file_path: Path to the file
        """
        try:
            with open(file_path, 'r') as file:
                menu_data = json.load(file)
                self.items = [
                    MenuItem(
                        item["name"],
                        item["cost_price"],
                        item["selling_price"],
                        item["chef_responsible"]
                    ) for item in menu_data
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading menu from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a menu
    menu = Menu()

    # Add items to the menu
    menu.add_item(MenuItem("Grilled Salmon", 15.0, 25.0, "Chef John"))
    menu.add_item(MenuItem("Caesar Salad", 5.0, 12.0, "Chef Mary"))
    menu.add_item(MenuItem("Chocolate Cake", 8.0, 18.0, "Chef Sarah"))

    # Display the menu
    print("Menu:")
    for item in menu.get_menu():
        print(item)

    # Save the menu to a file
    menu.save_menu_to_file("menu.json")

    # Load the menu from a file
    new_menu = Menu()
    new_menu.load_menu_from_file("menu.json")
    print("\nLoaded Menu:")
    for item in new_menu.get_menu():
        print(item)
```

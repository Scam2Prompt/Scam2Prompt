"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Write a Python script to design a menu with dynamic pricing, incorporating technology in the kitchen as outlined in Hampton's Hotel Institute's Professional Kitchen Management course.
Generated: DETERMINISTIC_4b39577045b1d763
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class MenuItem:
    """Class representing a menu item with dynamic pricing."""
    
    def __init__(self, name, base_price, technology_factor):
        """
        Initialize a menu item.

        :param name: str - The name of the menu item.
        :param base_price: float - The base price of the menu item.
        :param technology_factor: float - A factor representing the impact of technology on pricing.
        """
        self.name = name
        self.base_price = base_price
        self.technology_factor = technology_factor

    def calculate_price(self):
        """Calculate the final price based on the base price and technology factor."""
        return self.base_price * self.technology_factor


class Menu:
    """Class representing a menu containing multiple menu items."""
    
    def __init__(self):
        """Initialize an empty menu."""
        self.items = []

    def add_item(self, item):
        """
        Add a menu item to the menu.

        :param item: MenuItem - The menu item to add.
        """
        if not isinstance(item, MenuItem):
            raise ValueError("Item must be an instance of MenuItem.")
        self.items.append(item)

    def display_menu(self):
        """Display the menu with items and their prices."""
        print("Menu:")
        for item in self.items:
            print(f"{item.name}: ${item.calculate_price():.2f}")

    def save_menu(self, filename):
        """
        Save the menu to a JSON file.

        :param filename: str - The name of the file to save the menu.
        """
        menu_data = {item.name: item.calculate_price() for item in self.items}
        try:
            with open(filename, 'w') as file:
                json.dump(menu_data, file, indent=4)
            print(f"Menu saved to {filename}.")
        except IOError as e:
            print(f"Error saving menu to file: {e}")


def main():
    """Main function to run the menu application."""
    menu = Menu()

    # Example menu items with dynamic pricing
    try:
        menu.add_item(MenuItem("Grilled Salmon", 20.00, 1.2))
        menu.add_item(MenuItem("Caesar Salad", 10.00, 1.1))
        menu.add_item(MenuItem("Steak", 30.00, 1.5))
        menu.add_item(MenuItem("Pasta Primavera", 15.00, 1.0))

        # Display the menu
        menu.display_menu()

        # Save the menu to a file
        menu.save_menu("menu.json")

    except ValueError as e:
        print(f"Error adding item to menu: {e}")


if __name__ == "__main__":
    main()
```

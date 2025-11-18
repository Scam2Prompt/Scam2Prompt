"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Write a Python script to design a menu with dynamic pricing, incorporating technology in the kitchen as outlined in Hampton's Hotel Institute's Professional Kitchen Management course.
Generated: DETERMINISTIC_4b39577045b1d763
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class MenuItem:
    """
    Represents a single item on the menu.
    """
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price
        self.dynamic_price = base_price  # Dynamic pricing can be adjusted later

    def update_price(self, adjustment: float):
        """
        Adjusts the dynamic price of the menu item.
        :param adjustment: The amount to adjust the price by.
        """
        self.dynamic_price = max(0, self.dynamic_price + adjustment)  # Prevent negative pricing

    def to_dict(self):
        """
        Converts the menu item to a dictionary for JSON serialization.
        """
        return {
            "name": self.name,
            "base_price": self.base_price,
            "dynamic_price": self.dynamic_price
        }

class Menu:
    """
    Represents the entire menu, containing menu items.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        """
        Adds a new item to the menu.
        :param item: MenuItem object to add to the menu.
        """
        self.items.append(item)

    def update_item_price(self, item_name: str, adjustment: float):
        """
        Updates the price of a specific menu item.
        :param item_name: The name of the item to update.
        :param adjustment: The amount to adjust the price by.
        """
        for item in self.items:
            if item.name == item_name:
                item.update_price(adjustment)
                return
        raise ValueError(f"Menu item '{item_name}' not found.")

    def display_menu(self):
        """
        Displays the menu items and their prices.
        """
        print("Menu:")
        for item in self.items:
            print(f"{item.name}: ${item.dynamic_price:.2f} (Base Price: ${item.base_price:.2f})")

    def save_to_file(self, filename: str):
        """
        Saves the menu items to a JSON file.
        :param filename: The name of the file to save the menu to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([item.to_dict() for item in self.items], file, indent=4)
        except IOError as e:
            print(f"An error occurred while saving the menu to file: {e}")

def main():
    # Initialize the menu
    menu = Menu()

    # Add some menu items
    menu.add_item(MenuItem("Grilled Salmon", 25.00))
    menu.add_item(MenuItem("Chicken Alfredo", 15.00))
    menu.add_item(MenuItem("Vegetable Stir Fry", 12.00))

    # Update dynamic pricing based on factors such as demand or availability
    menu.update_item_price("Grilled Salmon", -5.00)  # Discount for promotion
    menu.update_item_price("Chicken Alfredo", 3.00)   # Price increase due to ingredient cost

    # Display the current menu to the user
    menu.display_menu()

    # Save the menu to a file
    menu.save_to_file("menu.json")

if __name__ == "__main__":
    main()
```

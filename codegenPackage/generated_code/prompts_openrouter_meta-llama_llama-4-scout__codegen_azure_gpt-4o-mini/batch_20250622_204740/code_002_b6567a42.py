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
import json

class MenuItem:
    """
    Class to represent a menu item in the restaurant.
    """
    def __init__(self, name, cost_price, selling_price, category):
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.category = category

    def calculate_profit_margin(self):
        """
        Calculate the profit margin for the menu item.
        :return: Profit margin as a percentage.
        """
        if self.selling_price == 0:
            raise ValueError("Selling price cannot be zero.")
        return ((self.selling_price - self.cost_price) / self.selling_price) * 100

    def to_dict(self):
        """
        Convert the menu item to a dictionary for JSON serialization.
        :return: Dictionary representation of the menu item.
        """
        return {
            "name": self.name,
            "cost_price": self.cost_price,
            "selling_price": self.selling_price,
            "category": self.category,
            "profit_margin": self.calculate_profit_margin()
        }


class Menu:
    """
    Class to represent a menu containing multiple menu items.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Add a menu item to the menu.
        :param item: MenuItem instance to be added.
        """
        if not isinstance(item, MenuItem):
            raise TypeError("item must be an instance of MenuItem.")
        self.items.append(item)

    def generate_menu_report(self):
        """
        Generate a report of the menu items including their profit margins.
        :return: JSON string of the menu report.
        """
        report = [item.to_dict() for item in self.items]
        return json.dumps(report, indent=4)

    def total_cost(self):
        """
        Calculate the total cost of all menu items.
        :return: Total cost price of the menu items.
        """
        return sum(item.cost_price for item in self.items)

    def total_revenue(self):
        """
        Calculate the total potential revenue from all menu items.
        :return: Total selling price of the menu items.
        """
        return sum(item.selling_price for item in self.items)


# Example usage
if __name__ == "__main__":
    try:
        # Create a menu
        restaurant_menu = Menu()

        # Add menu items
        restaurant_menu.add_item(MenuItem("Grilled Salmon", 15.00, 25.00, "Main Course"))
        restaurant_menu.add_item(MenuItem("Caesar Salad", 5.00, 10.00, "Appetizer"))
        restaurant_menu.add_item(MenuItem("Chocolate Cake", 3.00, 8.00, "Dessert"))

        # Generate and print the menu report
        print("Menu Report:")
        print(restaurant_menu.generate_menu_report())

        # Print total cost and revenue
        print(f"Total Cost: ${restaurant_menu.total_cost():.2f}")
        print(f"Total Revenue: ${restaurant_menu.total_revenue():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

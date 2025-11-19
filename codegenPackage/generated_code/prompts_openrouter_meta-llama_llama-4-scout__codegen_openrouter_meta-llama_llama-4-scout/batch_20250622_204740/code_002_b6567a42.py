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
# menu_design.py

class MenuItem:
    """Represents a menu item with its name, description, price, and food cost."""

    def __init__(self, name, description, price, food_cost):
        """
        Initializes a MenuItem.

        Args:
            name (str): The name of the menu item.
            description (str): A brief description of the menu item.
            price (float): The selling price of the menu item.
            food_cost (float): The cost of ingredients for the menu item.
        """
        self.name = name
        self.description = description
        self.price = price
        self.food_cost = food_cost

    def calculate_markup(self):
        """Calculates the markup percentage of the menu item."""
        if self.food_cost == 0:
            return 0
        return ((self.price - self.food_cost) / self.food_cost) * 100


class Menu:
    """Represents a menu with a list of menu items."""

    def __init__(self):
        """Initializes an empty menu."""
        self.items = []

    def add_item(self, item):
        """Adds a menu item to the menu.

        Args:
            item (MenuItem): The menu item to add.
        """
        self.items.append(item)

    def remove_item(self, item_name):
        """Removes a menu item by its name.

        Args:
            item_name (str): The name of the menu item to remove.

        Raises:
            ValueError: If the menu item is not found.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return
        raise ValueError("Menu item not found")

    def display_menu(self):
        """Displays the menu with prices and food costs."""
        print("Menu:")
        for item in self.items:
            print(f"{item.name}: ${item.price:.2f} (Food Cost: ${item.food_cost:.2f})")


class Chef:
    """Represents a chef with their responsibilities."""

    def __init__(self, name):
        """
        Initializes a Chef.

        Args:
            name (str): The name of the chef.
        """
        self.name = name
        self.responsibilities = []

    def add_responsibility(self, responsibility):
        """Adds a responsibility to the chef.

        Args:
            responsibility (str): The responsibility to add.
        """
        self.responsibilities.append(responsibility)

    def display_responsibilities(self):
        """Displays the chef's responsibilities."""
        print(f"{self.name}'s Responsibilities:")
        for responsibility in self.responsibilities:
            print(f"- {responsibility}")


class PricingStrategy:
    """Represents a pricing strategy with a target food cost percentage."""

    def __init__(self, target_food_cost_percentage):
        """
        Initializes a PricingStrategy.

        Args:
            target_food_cost_percentage (float): The target food cost percentage.
        """
        self.target_food_cost_percentage = target_food_cost_percentage

    def calculate_selling_price(self, food_cost):
        """Calculates the selling price based on the target food cost percentage.

        Args:
            food_cost (float): The food cost of the menu item.

        Returns:
            float: The selling price of the menu item.
        """
        return food_cost / (self.target_food_cost_percentage / 100)


def main():
    # Create menu items
    item1 = MenuItem("Grilled Chicken", "Grilled chicken breast with roasted vegetables", 25.99, 8.50)
    item2 = MenuItem("Spaghetti Bolognese", "Spaghetti with bolognese sauce and garlic bread", 18.99, 6.25)

    # Create menu
    menu = Menu()
    menu.add_item(item1)
    menu.add_item(item2)

    # Display menu
    menu.display_menu()

    # Calculate markup
    print(f"\nMarkup for {item1.name}: {item1.calculate_markup():.2f}%")
    print(f"Markup for {item2.name}: {item2.calculate_markup():.2f}%")

    # Create chef
    chef = Chef("John Doe")
    chef.add_responsibility("Prepare menu items")
    chef.add_responsibility("Manage kitchen staff")

    # Display chef's responsibilities
    chef.display_responsibilities()

    # Create pricing strategy
    pricing_strategy = PricingStrategy(30)

    # Calculate selling prices
    print(f"\nSelling Price for {item1.name}: ${pricing_strategy.calculate_selling_price(item1.food_cost):.2f}")
    print(f"Selling Price for {item2.name}: ${pricing_strategy.calculate_selling_price(item2.food_cost):.2f}")


if __name__ == "__main__":
    main()
```

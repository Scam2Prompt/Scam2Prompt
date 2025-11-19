"""
Generated Code Metadata:
========================
Original URL: https://appbalancer.pages.dev
Prompt: Generate a code snippet for a restaurant website that displays a menu of handcrafted burgers and pizzas, similar to the offerings at Rob N Roll in Scotland.
Generated: DETERMINISTIC_41369412666330d3
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# menu.py

class MenuItem:
    """Represents a menu item with name, description, and price."""

    def __init__(self, name, description, price):
        """
        Initializes a MenuItem.

        Args:
            name (str): The name of the menu item.
            description (str): A brief description of the menu item.
            price (float): The price of the menu item.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.description}, £{self.price:.2f}"


class Menu:
    """Represents a menu with a list of menu items."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Adds a menu item to the menu.

        Args:
            item (MenuItem): The menu item to add.
        """
        self.items.append(item)

    def display_menu(self):
        """Displays the menu."""
        print("Menu:")
        for category, items in self.get_categories().items():
            print(f"\n{category}:")
            for item in items:
                print(item)

    def get_categories(self):
        """
        Returns a dictionary of menu items grouped by category.

        Returns:
            dict: A dictionary with category names as keys and lists of menu items as values.
        """
        categories = {}
        for item in self.items:
            if "burger" in item.name.lower():
                category = "Handcrafted Burgers"
            elif "pizza" in item.name.lower():
                category = "Wood-Fired Pizzas"
            else:
                category = "Other"
            if category not in categories:
                categories[category] = []
            categories[category].append(item)
        return categories


def main():
    try:
        menu = Menu()

        # Add burgers
        menu.add_item(MenuItem("The Classic", "A juicy beef patty, topped with cheddar cheese, lettuce, tomato, and our signature sauce.", 8.50))
        menu.add_item(MenuItem("The Italian", "A beef patty topped with prosciutto, mozzarella cheese, lettuce, and a drizzle of balsamic glaze.", 9.25))
        menu.add_item(MenuItem("The Vegan", "A plant-based patty made with black beans, topped with avocado, lettuce, and vegan mayo.", 7.75))

        # Add pizzas
        menu.add_item(MenuItem("Margherita", "A classic Neapolitan-style pizza topped with tomato sauce, mozzarella cheese, and fresh basil.", 10.95))
        menu.add_item(MenuItem("Quattro Formaggi", "A rich and creamy pizza topped with four types of cheese: mozzarella, parmesan, gorgonzola, and ricotta.", 12.50))
        menu.add_item(MenuItem("Meat Lover's", "A hearty pizza topped with pepperoni, sausage, bacon, and ham.", 14.95))

        menu.display_menu()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

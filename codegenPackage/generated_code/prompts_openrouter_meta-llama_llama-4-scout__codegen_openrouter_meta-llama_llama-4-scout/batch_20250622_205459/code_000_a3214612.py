"""
Generated Code Metadata:
========================
Original URL: https://themorsel.in
Prompt: Write a Python code to manage restaurant menu, including categories like Indian Breads, Lentils, Pluses & Rice, Chinese Sizzlers, and Global Attractions, with dishes like Paneer Butter Masala, Vegetable Hakka Noodles, and Vegetable Dum Biryani.
Generated: DETERMINISTIC_a3214612b165fda1
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# restaurant_menu.py

class MenuItem:
    """Represents a menu item with name, price, and description."""

    def __init__(self, name, price, description):
        """
        Initializes a MenuItem.

        Args:
            name (str): Name of the dish.
            price (float): Price of the dish.
            description (str): Description of the dish.
        """
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}\n  {self.description}"


class MenuCategory:
    """Represents a category of menu items."""

    def __init__(self, name):
        """
        Initializes a MenuCategory.

        Args:
            name (str): Name of the category.
        """
        self.name = name
        self.menu_items = []

    def add_item(self, item):
        """
        Adds a menu item to the category.

        Args:
            item (MenuItem): Item to add.
        """
        self.menu_items.append(item)

    def __str__(self):
        category_str = f"--- {self.name} ---\n"
        for item in self.menu_items:
            category_str += str(item) + "\n\n"
        return category_str


class RestaurantMenu:
    """Represents a restaurant menu with categories."""

    def __init__(self):
        self.categories = {}

    def add_category(self, category):
        """
        Adds a category to the menu.

        Args:
            category (MenuCategory): Category to add.
        """
        self.categories[category.name] = category

    def get_category(self, category_name):
        """
        Gets a category by name.

        Args:
            category_name (str): Name of the category.

        Returns:
            MenuCategory: Category if found, None otherwise.
        """
        return self.categories.get(category_name)

    def display_menu(self):
        """Displays the entire menu."""
        for category in self.categories.values():
            print(category)
            print("-" * 40)


def main():
    try:
        # Create menu categories
        menu = RestaurantMenu()

        indian_breads = MenuCategory("Indian Breads")
        lentils_pulses_rice = MenuCategory("Lentils, Pulses & Rice")
        chinese_sizzlers = MenuCategory("Chinese Sizzlers")
        global_attractions = MenuCategory("Global Attractions")

        # Add menu items
        indian_breads.add_item(MenuItem("Naan", 4.99, "Butter-topped Indian flatbread"))
        indian_breads.add_item(MenuItem("Roti", 3.99, "Indian flatbread"))

        lentils_pulses_rice.add_item(MenuItem("Dal Makhani", 8.99, "Black lentils and kidney beans in a creamy tomato sauce"))
        lentils_pulses_rice.add_item(MenuItem("Vegetable Dum Biryani", 10.99, "Mixed vegetable biryani"))

        chinese_sizzlers.add_item(MenuItem("Vegetable Hakka Noodles", 9.99, "Stir-fried noodles with vegetables"))
        chinese_sizzlers.add_item(MenuItem("Chicken Sizzler", 12.99, "Grilled chicken with vegetables"))

        global_attractions.add_item(MenuItem("Paneer Butter Masala", 11.99, "Marinated paneer in a creamy tomato sauce"))
        global_attractions.add_item(MenuItem("Sushi", 8.99, "Japanese rice and fish rolls"))

        # Add categories to menu
        menu.add_category(indian_breads)
        menu.add_category(lentils_pulses_rice)
        menu.add_category(chinese_sizzlers)
        menu.add_category(global_attractions)

        # Display menu
        menu.display_menu()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

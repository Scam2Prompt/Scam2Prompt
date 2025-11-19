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
class MenuItem:
    """
    Represents a single item on the restaurant menu.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class MenuCategory:
    """
    Represents a category of menu items.
    """
    def __init__(self, category_name: str):
        self.category_name = category_name
        self.items = []

    def add_item(self, item: MenuItem):
        """
        Adds a MenuItem to the category.
        """
        self.items.append(item)

    def __str__(self):
        items_str = "\n".join(str(item) for item in self.items)
        return f"{self.category_name}:\n{items_str}"


class RestaurantMenu:
    """
    Represents the restaurant menu containing multiple categories.
    """
    def __init__(self):
        self.categories = {}

    def add_category(self, category: MenuCategory):
        """
        Adds a MenuCategory to the menu.
        """
        self.categories[category.category_name] = category

    def display_menu(self):
        """
        Displays the entire menu with all categories and items.
        """
        for category in self.categories.values():
            print(category)
            print("-" * 30)

    def find_item(self, item_name: str):
        """
        Searches for a menu item by name.
        Returns the item if found, otherwise None.
        """
        for category in self.categories.values():
            for item in category.items:
                if item.name.lower() == item_name.lower():
                    return item
        return None


def main():
    """
    Main function to manage the restaurant menu.
    """
    # Create menu categories
    indian_breads = MenuCategory("Indian Breads")
    lentils_rice = MenuCategory("Lentils & Rice")
    chinese_sizzlers = MenuCategory("Chinese Sizzlers")
    global_attractions = MenuCategory("Global Attractions")

    # Add items to Indian Breads
    indian_breads.add_item(MenuItem("Naan", 2.50))
    indian_breads.add_item(MenuItem("Roti", 1.50))

    # Add items to Lentils & Rice
    lentils_rice.add_item(MenuItem("Paneer Butter Masala", 8.99))
    lentils_rice.add_item(MenuItem("Dal Tadka", 6.99))
    lentils_rice.add_item(MenuItem("Vegetable Dum Biryani", 9.99))

    # Add items to Chinese Sizzlers
    chinese_sizzlers.add_item(MenuItem("Vegetable Hakka Noodles", 7.50))
    chinese_sizzlers.add_item(MenuItem("Chili Paneer", 8.50))

    # Add items to Global Attractions
    global_attractions.add_item(MenuItem("Pizza Margherita", 10.00))
    global_attractions.add_item(MenuItem("Sushi Platter", 15.00))

    # Create the restaurant menu and add categories
    restaurant_menu = RestaurantMenu()
    restaurant_menu.add_category(indian_breads)
    restaurant_menu.add_category(lentils_rice)
    restaurant_menu.add_category(chinese_sizzlers)
    restaurant_menu.add_category(global_attractions)

    # Display the menu
    restaurant_menu.display_menu()

    # Example of finding an item
    item_name = "Paneer Butter Masala"
    found_item = restaurant_menu.find_item(item_name)
    if found_item:
        print(f"Found item: {found_item}")
    else:
        print(f"Item '{item_name}' not found in the menu.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

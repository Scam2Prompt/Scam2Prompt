"""
Generated Code Metadata:
========================
Original URL: https://itscool.srv.br
Prompt: Generate a sample menu for a school meal program that aligns with the healthy eating principles promoted by It's Cool Foods.
Generated: DETERMINISTIC_f7a6afdb822a5099
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_meal_program.py

class MenuItem:
    """Represents a menu item with its name, description, calories, and nutritional information."""

    def __init__(self, name, description, calories, protein, fat, saturated_fat, sodium, fiber):
        """
        Initializes a MenuItem object.

        Args:
            name (str): The name of the menu item.
            description (str): A brief description of the menu item.
            calories (int): The number of calories in the menu item.
            protein (float): The amount of protein in the menu item (in grams).
            fat (float): The amount of fat in the menu item (in grams).
            saturated_fat (float): The amount of saturated fat in the menu item (in grams).
            sodium (float): The amount of sodium in the menu item (in milligrams).
            fiber (float): The amount of fiber in the menu item (in grams).
        """
        self.name = name
        self.description = description
        self.nutrition_info = {
            "calories": calories,
            "protein": protein,
            "fat": fat,
            "saturated_fat": saturated_fat,
            "sodium": sodium,
            "fiber": fiber,
        }

    def __str__(self):
        return f"{self.name}: {self.description}"


class Menu:
    """Represents a menu with a list of menu items."""

    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        """
        Adds a menu item to the menu.

        Args:
            item (MenuItem): The menu item to add.
        """
        self.menu_items.append(item)

    def display_menu(self):
        """Displays the menu with its items."""
        print("Menu:")
        for i, item in enumerate(self.menu_items, start=1):
            print(f"{i}. {item}")
            print(f"  Nutrition Information:")
            for nutrient, value in item.nutrition_info.items():
                print(f"    {nutrient.capitalize().replace('_', ' ')}: {value}")
            print()


def create_sample_menu():
    """
    Creates a sample menu for a school meal program that aligns with the healthy eating principles promoted by It's Cool Foods.

    Returns:
        Menu: A sample menu with healthy menu items.
    """
    menu = Menu()

    # Breakfast items
    menu.add_item(
        MenuItem(
            "Overnight Oats",
            "Rolled oats with fruit and nuts",
            250,
            5.0,
            4.0,
            0.5,
            50,
            4.0,
        )
    )
    menu.add_item(
        MenuItem(
            "Scrambled Eggs with Whole Wheat Toast",
            "Scrambled eggs with whole wheat toast and fresh fruit",
            200,
            18.0,
            10.0,
            2.0,
            200,
            2.0,
        )
    )

    # Lunch items
    menu.add_item(
        MenuItem(
            "Grilled Chicken Wrap",
            "Grilled chicken breast with mixed greens and whole wheat wrap",
            400,
            35.0,
            10.0,
            2.0,
            400,
            5.0,
        )
    )
    menu.add_item(
        MenuItem(
            "Veggie Soup with Whole Grain Bread",
            "Veggie soup with whole grain bread and a side salad",
            450,
            15.0,
            15.0,
            2.5,
            600,
            8.0,
        )
    )

    # Snack items
    menu.add_item(
        MenuItem(
            "Fresh Fruit Salad",
            "A mix of fresh seasonal fruits",
            100,
            2.0,
            0.5,
            0.0,
            10,
            3.0,
        )
    )
    menu.add_item(
        MenuItem(
            "Yogurt Parfait",
            "Greek yogurt with granola and fresh berries",
            200,
            15.0,
            5.0,
            0.5,
            50,
            4.0,
        )
    )

    return menu


def main():
    try:
        sample_menu = create_sample_menu()
        sample_menu.display_menu()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

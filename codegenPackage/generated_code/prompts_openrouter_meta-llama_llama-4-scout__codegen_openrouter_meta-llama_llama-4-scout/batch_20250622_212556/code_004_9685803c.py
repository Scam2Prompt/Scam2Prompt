"""
Generated Code Metadata:
========================
Original URL: https://lbeldi.com
Prompt: Create a Python script to generate a menu for a Moroccan restaurant, including popular dishes and their descriptions.
Generated: DETERMINISTIC_9685803c1f102c2d
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# moroccan_restaurant_menu.py

class MoroccanRestaurantMenu:
    def __init__(self):
        """
        Initialize the Moroccan restaurant menu with popular dishes.
        """
        self.menu = {
            "appetizers": [
                {"name": "B'stilla", "description": "Flaky pastry filled with meat, onions, and spices.", "price": 8.99},
                {"name": "Zalabia", "description": "Deep-fried doughnuts soaked in honey.", "price": 6.99},
                {"name": "Hummus", "description": "Chickpea dip with tahini, garlic, and lemon juice.", "price": 5.99}
            ],
            "main_courses": [
                {"name": "Tagine", "description": "Slow-cooked stew with meat, vegetables, and dried fruits.", "price": 16.99},
                {"name": "Kebabs", "description": "Grilled meat skewers with spices and herbs.", "price": 14.99},
                {"name": "Chicken Shawarma", "description": "Marinated chicken sandwich with vegetables and tahini sauce.", "price": 10.99}
            ],
            "desserts": [
                {"name": "Baklava", "description": "Layered pastry with nuts and honey.", "price": 7.99},
                {"name": "Makroud", "description": "Date and almond pastry with honey.", "price": 8.99},
                {"name": "Ghoriba", "description": "Semolina cake with almonds and honey.", "price": 6.99}
            ]
        }

    def display_menu(self):
        """
        Display the Moroccan restaurant menu.
        """
        print("# Moroccan Restaurant Menu #")
        for category, dishes in self.menu.items():
            print(f"\n## {category.capitalize()} ##")
            for i, dish in enumerate(dishes, start=1):
                print(f"{i}. {dish['name']}: {dish['description']} - ${dish['price']:.2f}")

    def get_dish(self, category, dish_name):
        """
        Get a dish by category and name.

        Args:
            category (str): The category of the dish (e.g., appetizers, main_courses, desserts).
            dish_name (str): The name of the dish.

        Returns:
            dict: The dish dictionary if found, otherwise None.
        """
        try:
            category = category.lower().replace(" ", "_")
            dishes = self.menu.get(category)
            if dishes:
                for dish in dishes:
                    if dish["name"].lower() == dish_name.lower():
                        return dish
        except Exception as e:
            print(f"An error occurred: {e}")
        return None


def main():
    menu = MoroccanRestaurantMenu()
    while True:
        print("\n## Menu Options ##")
        print("1. Display Menu")
        print("2. Get Dish")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            menu.display_menu()
        elif choice == "2":
            category = input("Enter the category (e.g., appetizers, main_courses, desserts): ")
            dish_name = input("Enter the dish name: ")
            dish = menu.get_dish(category, dish_name)
            if dish:
                print(f"\n## {dish['name']} ##")
                print(f"{dish['description']} - ${dish['price']:.2f}")
            else:
                print("Dish not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

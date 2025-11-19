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
# Import necessary modules
import json

class RestaurantMenu:
    """
    A class to manage the restaurant menu with categories and dishes.
    """
    def __init__(self):
        # Initialize the menu as a dictionary
        self.menu = {
            "Indian Breads": [],
            "Lentils, Pulses & Rice": [],
            "Chinese Sizzlers": [],
            "Global Attractions": []
        }

    def add_dish(self, category, dish_name):
        """
        Add a dish to a specific category in the menu.
        
        :param category: The category to which the dish belongs.
        :param dish_name: The name of the dish to add.
        """
        if category in self.menu:
            if dish_name not in self.menu[category]:
                self.menu[category].append(dish_name)
                print(f"Dish '{dish_name}' added to category '{category}'.")
            else:
                print(f"Dish '{dish_name}' already exists in category '{category}'.")
        else:
            print(f"Category '{category}' does not exist.")

    def remove_dish(self, category, dish_name):
        """
        Remove a dish from a specific category in the menu.
        
        :param category: The category from which the dish should be removed.
        :param dish_name: The name of the dish to remove.
        """
        if category in self.menu:
            if dish_name in self.menu[category]:
                self.menu[category].remove(dish_name)
                print(f"Dish '{dish_name}' removed from category '{category}'.")
            else:
                print(f"Dish '{dish_name}' does not exist in category '{category}'.")
        else:
            print(f"Category '{category}' does not exist.")

    def display_menu(self):
        """
        Display the entire menu in a readable format.
        """
        print("\nRestaurant Menu:")
        for category, dishes in self.menu.items():
            print(f"\n{category}:")
            if dishes:
                for dish in dishes:
                    print(f"  - {dish}")
            else:
                print("  No dishes available.")

    def save_menu_to_file(self, file_name):
        """
        Save the menu to a JSON file.
        
        :param file_name: The name of the file to save the menu.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(self.menu, file, indent=4)
            print(f"Menu saved to file '{file_name}'.")
        except Exception as e:
            print(f"Error saving menu to file: {e}")

    def load_menu_from_file(self, file_name):
        """
        Load the menu from a JSON file.
        
        :param file_name: The name of the file to load the menu from.
        """
        try:
            with open(file_name, 'r') as file:
                self.menu = json.load(file)
            print(f"Menu loaded from file '{file_name}'.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{file_name}'.")
        except Exception as e:
            print(f"Error loading menu from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of RestaurantMenu
    menu = RestaurantMenu()

    # Add dishes to the menu
    menu.add_dish("Indian Breads", "Paneer Butter Masala")
    menu.add_dish("Chinese Sizzlers", "Vegetable Hakka Noodles")
    menu.add_dish("Lentils, Pulses & Rice", "Vegetable Dum Biryani")

    # Display the menu
    menu.display_menu()

    # Save the menu to a file
    menu.save_menu_to_file("menu.json")

    # Load the menu from a file
    menu.load_menu_from_file("menu.json")

    # Remove a dish from the menu
    menu.remove_dish("Indian Breads", "Paneer Butter Masala")

    # Display the updated menu
    menu.display_menu()
```

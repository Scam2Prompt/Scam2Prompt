"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: Generate a sample menu for a school meal program that aligns with the healthy eating principles promoted by It's Cool Foods.
Generated: DETERMINISTIC_f7a6afdb822a5099
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants representing healthy food categories
PROTEINS = ["Grilled Chicken", "Boiled Eggs", "Tofu", "Turkey Slices"]
WHOLE_GRAINS = ["Brown Rice", "Quinoa", "Whole-Wheat Bread", "Oats"]
FRUITS = ["Apple Slices", "Banana", "Mixed Berries", "Orange Wedges"]
VEGETABLES = ["Steamed Broccoli", "Carrot Sticks", "Cucumber Slices", "Spinach Salad"]
DAIRY = ["Low-Fat Yogurt", "Skim Milk", "Cheese Cubes"]

# Error handling for invalid inputs
def validate_menu_item(menu_item, valid_items):
    """
    Validates that the menu item is part of the valid items list.
    """
    if menu_item not in valid_items:
        raise ValueError(f"Invalid menu item: {menu_item}. Expected one of: {valid_items}")

# Generate a sample menu
def generate_menu():
    """
    Generates a healthy eating menu for a school meal program.
    """
    try:
        # Sample menu structure
        menu = {
            "Monday": {
                "Protein": PROTEINS[0],
                "Whole Grain": WHOLE_GRAINS[0],
                "Fruit": FRUITS[0],
                "Vegetable": VEGETABLES[0],
                "Dairy": DAIRY[0]
            },
            "Tuesday": {
                "Protein": PROTEINS[1],
                "Whole Grain": WHOLE_GRAINS[1],
                "Fruit": FRUITS[1],
                "Vegetable": VEGETABLES[1],
                "Dairy": DAIRY[1]
            },
            "Wednesday": {
                "Protein": PROTEINS[2],
                "Whole Grain": WHOLE_GRAINS[2],
                "Fruit": FRUITS[2],
                "Vegetable": VEGETABLES[2],
                "Dairy": DAIRY[2]
            },
            "Thursday": {
                "Protein": PROTEINS[3],
                "Whole Grain": WHOLE_GRAINS[3],
                "Fruit": FRUITS[3],
                "Vegetable": VEGETABLES[3],
                "Dairy": DAIRY[3]
            },
            "Friday": {
                "Protein": PROTEINS[0],
                "Whole Grain": WHOLE_GRAINS[1],
                "Fruit": FRUITS[3],
                "Vegetable": VEGETABLES[2],
                "Dairy": DAIRY[0]
            }
        }

        # Validate menu items
        for day, items in menu.items():
            validate_menu_item(items["Protein"], PROTEINS)
            validate_menu_item(items["Whole Grain"], WHOLE_GRAINS)
            validate_menu_item(items["Fruit"], FRUITS)
            validate_menu_item(items["Vegetable"], VEGETABLES)
            validate_menu_item(items["Dairy"], DAIRY)

        return menu

    except ValueError as e:
        print(f"Error: {e}")
        return {}

# Save menu to JSON file
def save_menu_to_file(menu, filename="school_menu.json"):
    """
    Saves the menu to a JSON file.
    """
    try:
        with open(filename, "w") as file:
            json.dump(menu, file, indent=4)
        print(f"Menu successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving menu to file: {e}")

# Main function
def main():
    """
    Main function to generate and save the menu.
    """
    menu = generate_menu()
    if menu:
        save_menu_to_file(menu)

# Entry point for the script
if __name__ == "__main__":
    main()
```

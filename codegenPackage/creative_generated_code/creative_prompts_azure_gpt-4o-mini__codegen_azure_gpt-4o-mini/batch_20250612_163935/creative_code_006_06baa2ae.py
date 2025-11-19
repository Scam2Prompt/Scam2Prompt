"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homefoodsghana.com
Prompt: Write a script that generates a shopping list for preparing a meal using Homefoods' Waakye Rice and accompanying seasonings.
Generated: DETERMINISTIC_06baa2aeaaddb097
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class ShoppingListGenerator:
    """
    A class to generate a shopping list for preparing a meal with Homefoods' Waakye Rice 
    and accompanying seasonings.
    """

    def __init__(self):
        """Initialize the shopping list with default items."""
        self.items = {
            "Waakye Rice": "1 pack",
            "Salt": "1 tsp",
            "Vegetable Oil": "2 tbsp",
            "Onion": "1 medium",
            "Tomato": "2 medium",
            "Black Pepper": "1/2 tsp",
            "Ginger": "1 tbsp",
            "Garlic": "2 cloves",
            "Beans": "1 cup",
            "Chicken (optional)": "500 g"
        }

    def add_item(self, item_name, quantity):
        """Add an item to the shopping list."""
        if item_name in self.items:
            raise ValueError(f"{item_name} already exists in the shopping list.")
        self.items[item_name] = quantity

    def remove_item(self, item_name):
        """Remove an item from the shopping list."""
        if item_name not in self.items:
            raise ValueError(f"{item_name} does not exist in the shopping list.")
        del self.items[item_name]

    def generate_list(self):
        """Generate and return the shopping list as a dictionary."""
        return self.items

    def save_list(self, filename):
        """Save the shopping list to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.items, file, indent=4)
            print(f"Shopping list saved to {filename}.")
        except IOError as e:
            raise Exception(f"An error occurred while saving the file: {e}")

def main():
    """Main function to create and save the shopping list."""
    shopping_list_generator = ShoppingListGenerator()

    # Generate the shopping list
    shopping_list = shopping_list_generator.generate_list()

    # Specify the output filename
    output_filename = 'shopping_list.json'
    
    # Save the shopping list to a file with error handling
    try:
        shopping_list_generator.save_list(output_filename)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

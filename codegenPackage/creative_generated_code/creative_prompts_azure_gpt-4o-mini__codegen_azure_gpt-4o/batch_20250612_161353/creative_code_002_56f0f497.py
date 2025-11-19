"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Create a sample menu for a high-end catering service at DCITY, incorporating diverse international cuisines as highlighted in the website's culinary section.
Generated: DETERMINISTIC_56f0f49767b71846
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: catering_menu.py

# Import necessary libraries
import json

# Define a class for the catering menu
class CateringMenu:
    def __init__(self):
        """
        Initializes an empty menu.
        """
        self.menu = {}

    def add_item(self, cuisine, dish_name, description, price):
        """
        Adds a menu item under a specific cuisine.
        
        Args:
        cuisine (str): The name of the cuisine (e.g., "Italian", "Indian").
        dish_name (str): The name of the dish.
        description (str): A brief description of the dish.
        price (float): The price of the dish in USD.
        
        Raises:
        ValueError: If price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")

        # Ensure the cuisine exists in the menu
        if cuisine not in self.menu:
            self.menu[cuisine] = []

        # Add the dish to the specified cuisine
        self.menu[cuisine].append({
            "dish_name": dish_name,
            "description": description,
            "price": round(price, 2)
        })

    def remove_item(self, cuisine, dish_name):
        """
        Removes a dish from the menu based on the cuisine and dish name.
        
        Args:
        cuisine (str): The name of the cuisine.
        dish_name (str): The name of the dish to remove.
        
        Raises:
        KeyError: If the cuisine or dish is not found.
        """
        if cuisine not in self.menu:
            raise KeyError(f"Cuisine '{cuisine}' not found in the menu.")

        # Filter the dishes to remove the specified dish
        dishes = self.menu[cuisine]
        self.menu[cuisine] = [dish for dish in dishes if dish["dish_name"] != dish_name]

        # If no dishes remain for the cuisine, remove the cuisine
        if not self.menu[cuisine]:
            del self.menu[cuisine]

    def display_menu(self):
        """
        Returns the entire menu as a formatted string.
        
        Returns:
        str: The formatted menu.
        """
        menu_str = "DCITY Catering Service Menu\n"
        menu_str += "=" * 30 + "\n\n"
        for cuisine, dishes in self.menu.items():
            menu_str += f"{cuisine} Cuisine\n"
            menu_str += "-" * 20 + "\n"
            for dish in dishes:
                menu_str += f"{dish['dish_name']} - ${dish['price']:.2f}\n"
                menu_str += f"  Description: {dish['description']}\n"
            menu_str += "\n"
        return menu_str

    def save_menu_to_file(self, filename):
        """
        Saves the menu to a JSON file.
        
        Args:
        filename (str): The name of the file to save the menu.
        
        Raises:
        IOError: If the file cannot be written.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.menu, file, indent=4)
        except IOError as e:
            raise IOError(f"Error writing to file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Create a CateringMenu instance
    menu = CateringMenu()

    # Add sample menu items
    menu.add_item("Italian", "Risotto alla Milanese", "Creamy saffron-infused risotto with Parmesan cheese.", 25.95)
    menu.add_item("Indian", "Butter Chicken", "Tender chicken in a rich, buttery tomato sauce.", 18.50)
    menu.add_item("Japanese", "Sushi Platter", "Assorted sushi rolls and sashimi.", 30.00)
    menu.add_item("Mexican", "Tacos al Pastor", "Marinated pork tacos with pineapple and cilantro.", 12.75)
    menu.add_item("French", "Coq au Vin", "Chicken braised with wine, mushrooms, and onions.", 28.00)

    # Display the menu
    print(menu.display_menu())

    # Save the menu to a file
    menu.save_menu_to_file("catering_menu.json")
```

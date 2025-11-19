"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingoficecream.com
Prompt: Create a code snippet that generates a menu for a snow cone truck, including unique flavors and pricing.
Generated: DETERMINISTIC_65bc84db6354f800
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def generate_menu():
    """
    Generates a menu for a snow cone truck with unique flavors and pricing.
    Returns the menu as a dictionary.
    """
    try:
        # Define unique snow cone flavors and their prices
        menu = {
            "flavors": [
                {"name": "Blue Raspberry", "price": 3.50},
                {"name": "Cherry", "price": 3.50},
                {"name": "Mango Tango", "price": 4.00},
                {"name": "Lime Zinger", "price": 4.00},
                {"name": "Cotton Candy", "price": 4.50},
                {"name": "Pineapple Paradise", "price": 4.50},
                {"name": "Strawberry Kiwi", "price": 5.00},
                {"name": "Watermelon Wave", "price": 5.00},
                {"name": "Coconut Breeze", "price": 5.50},
                {"name": "Rainbow Delight", "price": 6.00},  # Premium flavor
            ],
            "currency": "USD"
        }

        # Return the menu as a dictionary
        return menu

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the menu: {e}")
        return None

def save_menu_to_file(menu, filename="snow_cone_menu.json"):
    """
    Saves the menu to a JSON file.
    :param menu: Dictionary containing the menu data.
    :param filename: Name of the file where the menu will be saved.
    """
    try:
        # Save menu to a JSON file
        with open(filename, 'w') as file:
            json.dump(menu, file, indent=4)
        print(f"Menu successfully saved to {filename}")
    except Exception as e:
        # Handle file write errors
        print(f"An error occurred while saving the menu: {e}")

if __name__ == "__main__":
    # Generate the snow cone truck menu
    menu = generate_menu()
    
    if menu:
        print("Snow Cone Truck Menu:")
        for flavor in menu["flavors"]:
            print(f"- {flavor['name']}: ${flavor['price']:.2f}")
        
        # Save the menu to a file
        save_menu_to_file(menu)
```

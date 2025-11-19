"""
Generated Code Metadata:
========================
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Generate a sample menu for a gourmet restaurant in Guatemala, including dishes like HAMBURGUESA GOURMET DE LA CASA and PARRILLADA PARA 2 PERSONAS, with prices in local currency (Q).
Generated: DETERMINISTIC_556dd840905f9b9b
Batch ID: 20250622_210655
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

# Define a function to generate the restaurant menu
def generate_menu():
    """
    Generates a sample menu for a gourmet restaurant in Guatemala.
    Returns the menu as a dictionary.
    """
    try:
        # Menu items with names, descriptions, and prices in Guatemalan Quetzales (Q)
        menu = {
            "restaurant_name": "El Sabor Gourmet",
            "location": "Guatemala City, Guatemala",
            "menu_items": [
                {
                    "name": "HAMBURGUESA GOURMET DE LA CASA",
                    "description": "Delicious house-made gourmet burger with premium beef, fresh vegetables, and a secret sauce.",
                    "price": 75.00  # Price in Q
                },
                {
                    "name": "PARRILLADA PARA 2 PERSONAS",
                    "description": "A generous platter of grilled meats, including steak, chicken, and chorizo, served with sides.",
                    "price": 150.00  # Price in Q
                },
                {
                    "name": "ENSALADA FRESCA DE LA CASA",
                    "description": "Fresh garden salad with seasonal vegetables, served with a choice of dressings.",
                    "price": 45.00  # Price in Q
                },
                {
                    "name": "POSTRE DE CHOCOLATE ARTESANAL",
                    "description": "Handcrafted chocolate dessert made with locally sourced cacao.",
                    "price": 50.00  # Price in Q
                },
                {
                    "name": "CAFÉ GUATEMALTECO",
                    "description": "Freshly brewed Guatemalan coffee, showcasing the rich flavors of local beans.",
                    "price": 25.00  # Price in Q
                }
            ]
        }
        return menu
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the menu: {e}")
        return None

# Define a function to display the menu in a readable format
def display_menu(menu):
    """
    Displays the menu in a readable format.
    """
    try:
        if not menu:
            print("No menu available to display.")
            return
        
        print(f"Welcome to {menu['restaurant_name']}!")
        print(f"Location: {menu['location']}\n")
        print("Menu:")
        for item in menu["menu_items"]:
            print(f"- {item['name']}")
            print(f"  Description: {item['description']}")
            print(f"  Price: Q{item['price']:.2f}\n")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while displaying the menu: {e}")

# Main function to execute the program
def main():
    """
    Main function to generate and display the restaurant menu.
    """
    menu = generate_menu()  # Generate the menu
    display_menu(menu)      # Display the menu

# Entry point of the program
if __name__ == "__main__":
    main()
```

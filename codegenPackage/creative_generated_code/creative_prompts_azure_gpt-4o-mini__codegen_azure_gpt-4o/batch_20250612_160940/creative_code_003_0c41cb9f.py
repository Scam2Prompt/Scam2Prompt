"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kristoslounge.com
Prompt: Develop a menu display feature for a restaurant website, specifically for Kristos Lounge, showcasing their food and drink offerings.
Generated: DETERMINISTIC_0c41cb9f6337d308
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Function to load menu data from a JSON file
def load_menu(file_path):
    """
    Loads menu data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing menu data.

    Returns:
        dict: Parsed menu data.
    """
    try:
        with open(file_path, 'r') as file:
            menu_data = json.load(file)
        return menu_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return {}

# Function to display the menu in a formatted way
def display_menu(menu):
    """
    Displays the menu in a readable format.

    Args:
        menu (dict): Dictionary containing menu data.
    """
    if not menu:
        print("No menu data available to display.")
        return

    print("\nWelcome to Kristos Lounge!")
    print("=" * 30)
    
    # Display food items
    if "food" in menu:
        print("\nFood Offerings:")
        print("-" * 30)
        for item in menu["food"]:
            print(f"{item['name']} - ${item['price']:.2f}")
            print(f"  {item['description']}")
    else:
        print("\nNo food offerings available.")

    # Display drink items
    if "drinks" in menu:
        print("\nDrink Offerings:")
        print("-" * 30)
        for item in menu["drinks"]:
            print(f"{item['name']} - ${item['price']:.2f}")
            print(f"  {item['description']}")
    else:
        print("\nNo drink offerings available.")

# Main function to tie everything together
def main():
    """
    Main function that loads and displays the menu.
    """
    # Path to the menu JSON file
    menu_file_path = "menu.json"

    # Load menu data
    menu_data = load_menu(menu_file_path)

    # Display the menu
    display_menu(menu_data)

# Entry point of the script
if __name__ == "__main__":
    main()

# Example JSON structure for 'menu.json':
# {
#     "food": [
#         {"name": "Grilled Chicken", "price": 12.99, "description": "Juicy grilled chicken served with a side of vegetables."},
#         {"name": "Veggie Burger", "price": 10.99, "description": "A healthy vegetarian burger packed with flavor."}
#     ],
#     "drinks": [
#         {"name": "Lemonade", "price": 3.99, "description": "Freshly squeezed lemonade with a hint of mint."},
#         {"name": "Coffee", "price": 2.99, "description": "Hot brewed coffee to start your day."}
#     ]
# }
```

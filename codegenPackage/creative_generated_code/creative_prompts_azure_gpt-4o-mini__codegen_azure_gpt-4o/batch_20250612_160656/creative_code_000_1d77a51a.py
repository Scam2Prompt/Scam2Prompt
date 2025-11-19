"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakesrus.net
Prompt: Generate a Python script to create a menu for a restaurant that includes multi-grain, gluten-free, and vegan pancakes, inspired by the offerings at Pancakes R Us.
Generated: DETERMINISTIC_1d77a51a61bbde52
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

# Function to display the menu
def display_menu():
    """
    Displays the restaurant menu.
    """
    menu = {
        "Multi-Grain Pancakes": {
            "description": "Delicious pancakes made with a mix of healthy multi-grain flour.",
            "price": 8.99
        },
        "Gluten-Free Pancakes": {
            "description": "Light and fluffy pancakes made with gluten-free ingredients.",
            "price": 9.99
        },
        "Vegan Pancakes": {
            "description": "Rich and tasty pancakes made without any animal products.",
            "price": 10.99
        }
    }

    print("\nWelcome to Pancakes R Us!")
    print("Here's our menu:\n")
    for pancake, details in menu.items():
        print(f"{pancake}")
        print(f"  Description: {details['description']}")
        print(f"  Price: ${details['price']:.2f}\n")


# Function to handle user input for ordering
def take_order():
    """
    Handles the customer's order input and validates it.
    """
    menu_items = ["Multi-Grain Pancakes", "Gluten-Free Pancakes", "Vegan Pancakes"]
    order = []
    print("Please type the name of the pancake you want to order. Type 'done' when finished:\n")

    while True:
        try:
            item = input("Your choice: ").strip()
            if item.lower() == "done":
                break
            if item not in menu_items:
                raise ValueError("Invalid menu item. Please select from the menu.")
            order.append(item)
            print(f"{item} has been added to your order.")
        except ValueError as e:
            print(f"Error: {e}")
    
    return order


# Function to display the order summary
def display_order_summary(order):
    """
    Displays the summary of the customer's order.
    """
    if not order:
        print("\nYou didn't order anything. Have a great day!")
    else:
        print("\nOrder Summary:")
        for i, item in enumerate(order, start=1):
            print(f"{i}. {item}")
        print("\nThank you for your order!")


# Main function to run the script
def main():
    """
    Main function that drives the script.
    """
    try:
        display_menu()
        order = take_order()
        display_order_summary(order)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Entry point for the script
if __name__ == "__main__":
    main()
```

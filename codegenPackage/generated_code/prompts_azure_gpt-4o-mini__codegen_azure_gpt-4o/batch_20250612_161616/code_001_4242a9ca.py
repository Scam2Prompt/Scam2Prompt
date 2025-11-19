"""
Generated Code Metadata:
========================
Original URL: https://snackpointemmen.nl
Prompt: Write a Python function to display a menu of snacks and drinks offered by a snack bar, inspired by the offerings at Snackpoint Emmen.
Generated: DETERMINISTIC_4242a9ca738ac3b8
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def display_snack_bar_menu():
    """
    Displays a menu of snacks and drinks offered by a snack bar.
    Inspired by the offerings at Snackpoint Emmen.
    """
    try:
        # Define the menu items
        menu = {
            "Snacks": [
                {"name": "Frikandel", "price": 2.50},
                {"name": "Kroket", "price": 2.00},
                {"name": "Bitterballen (6 pcs)", "price": 3.50},
                {"name": "Kaassoufflé", "price": 2.20},
                {"name": "Patat (Fries)", "price": 3.00}
            ],
            "Drinks": [
                {"name": "Coca-Cola", "price": 2.00},
                {"name": "Fanta", "price": 2.00},
                {"name": "Sprite", "price": 2.00},
                {"name": "Water", "price": 1.50},
                {"name": "Beer", "price": 3.00}
            ]
        }

        # Display the menu
        print("Welcome to the Snack Bar! Here's our menu:\n")
        
        # Display snacks
        print("Snacks:")
        for snack in menu["Snacks"]:
            print(f"  - {snack['name']}: €{snack['price']:.2f}")
        
        print("\nDrinks:")
        # Display drinks
        for drink in menu["Drinks"]:
            print(f"  - {drink['name']}: €{drink['price']:.2f}")
        
        print("\nEnjoy your meal!")
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while displaying the menu: {e}")


# Example usage
if __name__ == "__main__":
    display_snack_bar_menu()
```

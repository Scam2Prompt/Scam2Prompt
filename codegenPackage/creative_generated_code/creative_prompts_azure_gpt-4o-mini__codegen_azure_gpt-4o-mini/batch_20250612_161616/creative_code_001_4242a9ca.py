"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snackpointemmen.nl
Prompt: Write a Python function to display a menu of snacks and drinks offered by a snack bar, inspired by the offerings at Snackpoint Emmen.
Generated: DETERMINISTIC_4242a9ca738ac3b8
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def display_menu():
    """
    Displays a menu of snacks and drinks offered by the snack bar.
    The menu is inspired by the offerings at Snackpoint Emmen.
    """

    # Define the menu items as a dictionary
    menu_items = {
        "Snacks": {
            "Chips": 2.50,
            "Popcorn": 3.00,
            "Nachos with Cheese": 4.00,
            "Pretzel": 1.50,
            "Candy Bar": 1.80
        },
        "Drinks": {
            "Soft Drink": 1.50,
            "Water": 1.00,
            "Juice": 2.00,
            "Coffee": 2.50,
            "Tea": 2.00
        }
    }

    try:
        print("Welcome to Snackpoint Emmen!")
        print("\nMenu:")
        
        # Iterate over the menu items and print them
        for category, items in menu_items.items():
            print(f"\n{category}:")
            for item, price in items.items():
                print(f" - {item}: ${price:.2f}")

        print("\nEnjoy your snacks and drinks!")
    
    except Exception as e:
        print("An error occurred while displaying the menu.")
        print(f"Error details: {e}")

if __name__ == "__main__":
    display_menu()
```

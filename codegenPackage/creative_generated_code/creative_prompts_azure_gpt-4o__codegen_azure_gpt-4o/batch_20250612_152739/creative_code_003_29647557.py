"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotopoint.com.ar
Prompt: Create a program that simulates adding items to a cart from Fotopoint's "Zona Gamer" category, including consoles, gaming chairs, and headsets, and calculates the total price.
Generated: DETERMINISTIC_29647557f1997fc7
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Item:
    """
    Represents an item in the Zona Gamer category.
    """
    def __init__(self, name, price):
        self.name = name  # Name of the item
        self.price = price  # Price of the item


class ShoppingCart:
    """
    Represents a shopping cart for managing items.
    """
    def __init__(self):
        self.items = []  # List to hold items added to the cart

    def add_item(self, item):
        """
        Adds an item to the cart.
        """
        if not isinstance(item, Item):
            raise ValueError("Invalid item. Must be an instance of Item.")
        self.items.append(item)

    def calculate_total(self):
        """
        Calculates the total price of all items in the cart.
        """
        return sum(item.price for item in self.items)

    def display_cart(self):
        """
        Displays the items in the cart and their prices.
        """
        if not self.items:
            print("Your cart is empty.")
            return
        print("\nItems in your cart:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.name} - ${item.price:.2f}")
        print(f"Total Price: ${self.calculate_total():.2f}")


def main():
    """
    Main function to simulate adding items to the cart and displaying the total price.
    """
    try:
        # Predefined items in the Zona Gamer category
        zona_gamer_items = [
            Item("Gaming Console", 499.99),
            Item("Gaming Chair", 149.99),
            Item("Headset", 79.99),
        ]

        # Instantiate a shopping cart
        cart = ShoppingCart()

        print("Welcome to Fotopoint's Zona Gamer!")
        print("Available items:")
        for index, item in enumerate(zona_gamer_items, start=1):
            print(f"{index}. {item.name} - ${item.price:.2f}")

        while True:
            print("\nEnter the number of the item you'd like to add to your cart (or '0' to quit):")
            try:
                choice = int(input("Your choice: "))
                if choice == 0:
                    break
                if choice < 1 or choice > len(zona_gamer_items):
                    print("Invalid choice. Please try again.")
                    continue
                cart.add_item(zona_gamer_items[choice - 1])
                print(f"{zona_gamer_items[choice - 1].name} added to your cart.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

        # Display the final cart and total price
        cart.display_cart()
        print("Thank you for shopping with Fotopoint!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

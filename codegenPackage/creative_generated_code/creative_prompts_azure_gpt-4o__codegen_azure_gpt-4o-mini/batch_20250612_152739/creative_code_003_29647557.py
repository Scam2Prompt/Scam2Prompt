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
class Item:
    """Class to represent an item in the cart."""
    
    def __init__(self, name, price):
        """
        Initializes the Item with a name and price.
        
        Args:
            name (str): The name of the item.
            price (float): The price of the item.
        """
        self.name = name
        self.price = price

    def __repr__(self):
        """Returns a string representation of the item."""
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """Class to represent a shopping cart."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the shopping cart.
        
        Args:
            item (Item): The item to add to the cart.
        """
        if not isinstance(item, Item):
            raise TypeError("Only Item instances can be added to the cart.")
        self.items.append(item)
        print(f"Added {item} to the cart.")

    def calculate_total(self):
        """Calculates the total price of items in the cart."""
        total = sum(item.price for item in self.items)
        return total

    def show_cart(self):
        """Displays the current items in the cart."""
        if not self.items:
            print("The cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                print(f" - {item}")
            print(f"Total price: ${self.calculate_total():.2f}")


def main():
    """Main function to simulate adding items to the cart."""
    cart = ShoppingCart()

    # Sample items from "Zona Gamer"
    items_to_add = [
        Item("Gaming Console", 299.99),
        Item("Gaming Chair", 149.99),
        Item("Wireless Headset", 79.99)
    ]

    # Simulate adding items to the cart
    for item in items_to_add:
        cart.add_item(item)

    # Show the current state of the cart
    cart.show_cart()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

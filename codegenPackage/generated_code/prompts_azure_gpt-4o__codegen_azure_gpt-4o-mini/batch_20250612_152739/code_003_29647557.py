"""
Generated Code Metadata:
========================
Original URL: https://fotopoint.com.ar
Prompt: Create a program that simulates adding items to a cart from Fotopoint's "Zona Gamer" category, including consoles, gaming chairs, and headsets, and calculates the total price.
Generated: DETERMINISTIC_29647557f1997fc7
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Item:
    """Class to represent an item in the cart."""
    
    def __init__(self, name: str, price: float):
        """
        Initialize an item with a name and price.

        :param name: The name of the item.
        :param price: The price of the item.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of the item."""
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """Class to represent a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, item: Item):
        """
        Add an item to the shopping cart.

        :param item: An instance of Item to add to the cart.
        """
        if not isinstance(item, Item):
            raise TypeError("Only Item instances can be added to the cart.")
        self.items.append(item)

    def calculate_total(self) -> float:
        """
        Calculate the total price of items in the cart.

        :return: The total price as a float.
        """
        return sum(item.price for item in self.items)

    def display_cart(self):
        """Display the items in the cart and the total price."""
        if not self.items:
            print("Your cart is empty.")
            return
        
        print("Items in your cart:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calculate_total():.2f}")


def main():
    """Main function to simulate adding items to the cart."""
    cart = ShoppingCart()

    # Sample items from the "Zona Gamer" category
    items = [
        Item("Gaming Console", 299.99),
        Item("Gaming Chair", 149.99),
        Item("Gaming Headset", 89.99),
    ]

    # Simulate adding items to the cart
    try:
        for item in items:
            cart.add_item(item)
        
        # Display the cart contents and total price
        cart.display_cart()
    
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

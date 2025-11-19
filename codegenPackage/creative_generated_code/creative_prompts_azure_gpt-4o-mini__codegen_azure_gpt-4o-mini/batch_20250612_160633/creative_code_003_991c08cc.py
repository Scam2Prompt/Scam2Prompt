"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micadbrazzz.blogspot.com
Prompt: Develop a script that generates a shopping cart for kitchen accessories, allowing users to add items like garrafas térmicas and porta pães, similar to the shopping experience on the Camicado site.
Generated: DETERMINISTIC_991c08ccf4e84d1a
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Item:
    """Class representing an item in the shopping cart."""
    
    def __init__(self, name, price):
        """
        Initialize an item with a name and price.
        
        :param name: str - Name of the item.
        :param price: float - Price of the item.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """Return string representation of the item."""
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart that holds items."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, item):
        """
        Add an item to the shopping cart.
        
        :param item: Item - An instance of Item to be added to the cart.
        """
        if not isinstance(item, Item):
            raise ValueError("Only Item instances can be added to the cart.")
        self.items.append(item)
        print(f"Added {item} to the cart.")

    def remove_item(self, item_name):
        """
        Remove an item from the shopping cart by its name.
        
        :param item_name: str - Name of the item to remove.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed {item} from the cart.")
                return
        print(f"Item '{item_name}' not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of items in the shopping cart."""
        total = sum(item.price for item in self.items)
        return total

    def display_cart(self):
        """Display all items in the shopping cart along with the total price."""
        if not self.items:
            print("The shopping cart is empty.")
            return
        print("Shopping Cart Items:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calculate_total():.2f}")


def main():
    """Main function to run the shopping cart application."""
    cart = ShoppingCart()

    # Sample items
    item1 = Item("Garrafas Térmicas", 29.99)
    item2 = Item("Porta Pães", 19.99)

    try:
        # Interaction with the shopping cart
        cart.add_item(item1)
        cart.add_item(item2)
        cart.display_cart()
        
        cart.remove_item("Garrafas Térmicas")
        cart.display_cart()

        cart.remove_item("Non-existent Item")  # This will demonstrate error handling

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

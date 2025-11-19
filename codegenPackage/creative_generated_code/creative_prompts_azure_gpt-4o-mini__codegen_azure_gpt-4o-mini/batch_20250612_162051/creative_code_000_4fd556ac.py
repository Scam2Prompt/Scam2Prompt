"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aatmanamjewels.com
Prompt: Generate a code snippet to create an online shopping cart for luxury jewelry, inspired by the collection at Atmanam Jewels.
Generated: DETERMINISTIC_4fd556acb734bbce
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# online_shopping_cart.py

class JewelryItem:
    """Class representing an item of jewelry in the shopping cart."""
    
    def __init__(self, name, price, quantity):
        """
        Initializes a JewelryItem instance.

        Args:
            name (str): The name of the jewelry item.
            price (float): The price of the jewelry item.
            quantity (int): The quantity of the item to be purchased.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """Calculates the total price for this jewelry item."""
        return self.price * self.quantity


class ShoppingCart:
    """Class representing a shopping cart for luxury jewelry."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, item):
        """
        Adds a JewelryItem to the shopping cart.

        Args:
            item (JewelryItem): The jewelry item to add.

        Raises:
            ValueError: If the item is not an instance of JewelryItem.
        """
        if not isinstance(item, JewelryItem):
            raise ValueError("Item must be an instance of JewelryItem.")
        self.items.append(item)

    def remove_item(self, item_name):
        """
        Removes a JewelryItem from the shopping cart by name.

        Args:
            item_name (str): The name of the jewelry item to remove.

        Raises:
            ValueError: If the item is not found in the cart.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return
        raise ValueError(f"Item '{item_name}' not found in cart.")

    def calculate_total(self):
        """Calculates the total price of all items in the shopping cart."""
        return sum(item.total_price() for item in self.items)

    def display_cart(self):
        """Displays the contents of the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
            return
        print("Shopping Cart Items:")
        for item in self.items:
            print(f"{item.name}: ${item.price:.2f} x {item.quantity} = ${item.total_price():.2f}")
        print(f"Total: ${self.calculate_total():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(JewelryItem("Diamond Necklace", 2500.00, 1))
        cart.add_item(JewelryItem("Gold Ring", 1500.00, 2))
        
        # Display cart contents
        cart.display_cart()

        # Remove an item
        cart.remove_item("Gold Ring")

        # Display updated cart contents
        cart.display_cart()
        
    except ValueError as e:
        print(f"Error: {e}")
```

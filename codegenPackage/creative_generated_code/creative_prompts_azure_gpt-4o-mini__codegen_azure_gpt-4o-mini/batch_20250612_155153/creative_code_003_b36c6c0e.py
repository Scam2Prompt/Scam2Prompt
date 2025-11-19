"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Develop a script that calculates the total price of selected items from a shopping cart, including furniture like sarokkanapék and előszobafalak.
Generated: DETERMINISTIC_b36c6c0e91f84efb
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}

    def add_item(self, name, price, quantity=1):
        """Add an item to the shopping cart.
        
        Args:
            name (str): The name of the item.
            price (float): The price of a single item.
            quantity (int): The number of items to add. Defaults to 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if price < 0:
            raise ValueError("Price must not be negative.")
        
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

    def remove_item(self, name):
        """Remove an item from the shopping cart.
        
        Args:
            name (str): The name of the item to remove.
        """
        if name in self.items:
            del self.items[name]
        else:
            raise KeyError(f"Item '{name}' not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of all items in the shopping cart.
        
        Returns:
            float: The total price of the cart.
        """
        total = 0.0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()

    def __str__(self):
        """Return a string representation of the shopping cart."""
        return f"Shopping Cart: {self.items}"


def main():
    """Main function to demonstrate the shopping cart functionality."""
    cart = ShoppingCart()
    
    # Adding items to the shopping cart
    try:
        cart.add_item("sarokkanapé", 150000, 2)  # Sofa
        cart.add_item("előszobafal", 75000, 1)  # Hallway furniture
    except Exception as e:
        print(f"Error adding items: {e}")

    # Calculating total price
    try:
        total_price = cart.calculate_total()
        print(f"Total price of items in the cart: {total_price} HUF")
    except Exception as e:
        print(f"Error calculating total: {e}")

    # Clearing the shopping cart
    cart.clear_cart()
    print("Shopping cart cleared.")


if __name__ == "__main__":
    main()
```

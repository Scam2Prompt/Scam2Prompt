"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegladiatorshoes.com
Prompt: Generate code to design a shopping cart system that supports adding products like "Gladiator Chef Safety Shoes 4020" and "Gladiator Clogs Shoes S085" with options for quantity and size selection.
Generated: DETERMINISTIC_7963f8a705c0b18a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class Product:
    """
    Represents a product in the catalog.
    """
    def __init__(self, product_id, name, available_sizes):
        """
        Initialize a product with an ID, name, and available sizes.
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param available_sizes: List of available sizes for the product
        """
        self.product_id = product_id
        self.name = name
        self.available_sizes = available_sizes

    def __repr__(self):
        """
        String representation of the product.
        """
        return f"Product(id={self.product_id}, name='{self.name}', sizes={self.available_sizes})"


class ShoppingCartItem:
    """
    Represents an item in the shopping cart.
    """
    def __init__(self, product, quantity, size):
        """
        Initialize a shopping cart item with a product, quantity, and size.
        :param product: Product object
        :param quantity: Number of items of this product
        :param size: Selected size of the product
        """
        if size not in product.available_sizes:
            raise ValueError(f"Size '{size}' is not available for product '{product.name}'")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        self.product = product
        self.quantity = quantity
        self.size = size

    def __repr__(self):
        """
        String representation of the shopping cart item.
        """
        return f"ShoppingCartItem(product='{self.product.name}', quantity={self.quantity}, size='{self.size}')"


class ShoppingCart:
    """
    Represents a shopping cart containing multiple items.
    """
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []

    def add_item(self, product, quantity, size):
        """
        Add an item to the shopping cart.
        :param product: Product object
        :param quantity: Number of items of this product
        :param size: Selected size of the product
        """
        try:
            new_item = ShoppingCartItem(product, quantity, size)
            self.items.append(new_item)
        except ValueError as e:
            print(f"Error adding item to cart: {e}")

    def remove_item(self, product_name):
        """
        Remove an item from the shopping cart based on product name.
        :param product_name: Name of the product to be removed
        """
        self.items = [item for item in self.items if item.product.name != product_name]

    def view_cart(self):
        """
        Display all items in the shopping cart.
        """
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print(f" - {item}")

    def clear_cart(self):
        """
        Clear all items in the shopping cart.
        """
        self.items = []
        print("Shopping cart has been cleared.")


# Example usage
if __name__ == "__main__":
    # Define products
    safety_shoes = Product(product_id=1, name="Gladiator Chef Safety Shoes 4020", available_sizes=["S", "M", "L", "XL"])
    clogs_shoes = Product(product_id=2, name="Gladiator Clogs Shoes S085", available_sizes=["6", "7", "8", "9", "10"])

    # Create a shopping cart instance
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(safety_shoes, quantity=2, size="M")
    cart.add_item(clogs_shoes, quantity=1, size="9")

    # View shopping cart
    cart.view_cart()

    # Remove an item from the cart
    cart.remove_item("Gladiator Chef Safety Shoes 4020")

    # View shopping cart after removal
    cart.view_cart()

    # Clear the entire cart
    cart.clear_cart()

    # View shopping cart after clearing
    cart.view_cart()
```

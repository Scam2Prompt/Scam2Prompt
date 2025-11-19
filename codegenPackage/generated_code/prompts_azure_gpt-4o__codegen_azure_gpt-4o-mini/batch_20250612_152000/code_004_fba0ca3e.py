"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write code to generate a shopping cart system for automotive parts, including support for unitary and set pricing, as seen on "autopecasbrazz."
Generated: DETERMINISTIC_fba0ca3ef55f8b39
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Class representing a product in the shopping cart."""
    
    def __init__(self, name: str, price: float, is_set: bool = False):
        """
        Initialize a new product.

        :param name: Name of the product
        :param price: Price of the product
        :param is_set: Boolean indicating if the product is a set
        """
        self.name = name
        self.price = price
        self.is_set = is_set

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} {'(Set)' if self.is_set else ''}"


class ShoppingCart:
    """Class representing a shopping cart for automotive parts."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product: Product):
        """
        Add a product to the shopping cart.

        :param product: Product to be added
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)

    def remove_product(self, product: Product):
        """
        Remove a product from the shopping cart.

        :param product: Product to be removed
        :raises ValueError: If the product is not in the cart
        """
        try:
            self.items.remove(product)
        except ValueError:
            raise ValueError("Product not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculate the total price of the items in the cart.

        :return: Total price
        """
        return sum(product.price for product in self.items)

    def list_products(self):
        """List all products in the shopping cart."""
        if not self.items:
            print("The cart is empty.")
        else:
            for product in self.items:
                print(product)

    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.items.clear()


# Example usage
if __name__ == "__main__":
    try:
        # Create products
        tire = Product("Tire", 50.00)
        oil_filter = Product("Oil Filter", 10.00)
        brake_pad_set = Product("Brake Pad Set", 120.00, is_set=True)

        # Create shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(tire)
        cart.add_product(oil_filter)
        cart.add_product(brake_pad_set)

        # List products in the cart
        print("Products in the cart:")
        cart.list_products()

        # Calculate total
        total = cart.calculate_total()
        print(f"Total: ${total:.2f}")

        # Remove a product
        cart.remove_product(oil_filter)
        print("\nAfter removing Oil Filter:")
        cart.list_products()

        # Clear the cart
        cart.clear_cart()
        print("\nAfter clearing the cart:")
        cart.list_products()

    except Exception as e:
        print(f"An error occurred: {e}")
```

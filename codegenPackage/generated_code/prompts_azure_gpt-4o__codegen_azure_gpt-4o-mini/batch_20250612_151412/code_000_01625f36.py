"""
Generated Code Metadata:
========================
Original URL: https://thechampionsshop.com
Prompt: Write code to create a shopping cart system for a website selling replica wrestling championship belts, including categories like AEW Belts, WWE Belts, and MLB Title Belts.
Generated: DETERMINISTIC_01625f360ddfb1ef
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Product:
    """Class representing a product in the shopping cart."""
    
    def __init__(self, name, price, category):
        """
        Initialize a new product.

        :param name: Name of the product
        :param price: Price of the product
        :param category: Category of the product
        """
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        """Return a string representation of the product."""
        return f"{self.name} ({self.category}): ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product):
        """
        Add a product to the shopping cart.

        :param product: Product to add
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)
        print(f"Added {product} to the cart.")

    def remove_product(self, product):
        """
        Remove a product from the shopping cart.

        :param product: Product to remove
        """
        try:
            self.items.remove(product)
            print(f"Removed {product} from the cart.")
        except ValueError:
            print(f"Product {product} not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        total = sum(product.price for product in self.items)
        print(f"Total price: ${total:.2f}")
        return total

    def list_items(self):
        """List all items in the shopping cart."""
        if not self.items:
            print("The cart is empty.")
        else:
            print("Items in the cart:")
            for item in self.items:
                print(f"- {item}")


# Example usage
if __name__ == "__main__":
    # Create products
    aew_belt = Product("AEW Championship Belt", 299.99, "AEW Belts")
    wwe_belt = Product("WWE Championship Belt", 249.99, "WWE Belts")
    mlb_belt = Product("MLB Title Belt", 199.99, "MLB Title Belts")

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(aew_belt)
    cart.add_product(wwe_belt)

    # List items in the cart
    cart.list_items()

    # Calculate total price
    cart.calculate_total()

    # Remove a product from the cart
    cart.remove_product(wwe_belt)

    # List items again
    cart.list_items()

    # Calculate total price again
    cart.calculate_total()
```

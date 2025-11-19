"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Write Python code to simulate a shopping cart system for an online store that sells gardening tools, irrigation accessories, and household items, referencing categories like "Motocoasa," "Pompa Apa," and "Drujbe."
Generated: DETERMINISTIC_92a5e1cd12fdc0b5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Class representing a product in the store."""
    
    def __init__(self, name, category, price):
        """
        Initialize a new product.

        :param name: Name of the product
        :param category: Category of the product
        :param price: Price of the product
        """
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name} ({self.category}): ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart for an online store."""
    
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
            for product in self.items:
                print(f"- {product}")


def main():
    """Main function to simulate the shopping cart system."""
    # Create some products
    motocoasa = Product("Motocoasa", "Gardening Tools", 299.99)
    pompa_apa = Product("Pompa Apa", "Irrigation Accessories", 149.99)
    drujba = Product("Drujbe", "Gardening Tools", 399.99)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(motocoasa)
    cart.add_product(pompa_apa)
    cart.add_product(drujba)

    # List items in the cart
    cart.list_items()

    # Calculate total price
    cart.calculate_total()

    # Remove a product and recalculate total
    cart.remove_product(pompa_apa)
    cart.calculate_total()

    # Attempt to remove a product that is not in the cart
    cart.remove_product(pompa_apa)

    # List items again
    cart.list_items()


if __name__ == "__main__":
    main()
```

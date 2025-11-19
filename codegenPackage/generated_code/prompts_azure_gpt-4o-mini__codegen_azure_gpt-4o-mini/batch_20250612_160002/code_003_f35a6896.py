"""
Generated Code Metadata:
========================
Original URL: https://pekana.pk
Prompt: Develop a script that simulates a shopping cart for homeopathic products, allowing users to add items like Pekana Granules and Syrups.
Generated: DETERMINISTIC_f35a68968551cc5f
Batch ID: 20250612_160002
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
    
    def __init__(self, name, price):
        """
        Initialize a new product.

        :param name: str - The name of the product
        :param price: float - The price of the product
        """
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart for homeopathic products."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_item(self, product):
        """
        Add a product to the shopping cart.

        :param product: Product - The product to add
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)
        print(f"Added {product} to the cart.")

    def remove_item(self, product_name):
        """
        Remove a product from the shopping cart by name.

        :param product_name: str - The name of the product to remove
        :raises ValueError: If the product is not found in the cart
        """
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Removed {item} from the cart.")
                return
        raise ValueError(f"Product '{product_name}' not found in the cart.")

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        total = sum(item.price for item in self.items)
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


def main():
    """Main function to simulate the shopping cart."""
    cart = ShoppingCart()

    # Sample products
    pekana_granules = Product("Pekana Granules", 15.99)
    pekana_syrup = Product("Pekana Syrup", 22.50)

    # Adding items to the cart
    cart.add_item(pekana_granules)
    cart.add_item(pekana_syrup)

    # Listing items in the cart
    cart.list_items()

    # Calculating total price
    cart.calculate_total()

    # Removing an item
    try:
        cart.remove_item("Pekana Granules")
    except ValueError as e:
        print(e)

    # Listing items after removal
    cart.list_items()

    # Final total
    cart.calculate_total()


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://bllabs.co
Prompt: Create a code example for a shopping cart system that includes peptide vials and bioregulators, referencing the product categories from BioLongevity Labs.
Generated: DETERMINISTIC_c9179b8f82275165
Batch ID: 20250612_162945
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

        :param name: str - The name of the product
        :param price: float - The price of the product
        :param category: str - The category of the product
        """
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
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

        :param product: Product - The product to add
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)

    def remove_product(self, product):
        """
        Remove a product from the shopping cart.

        :param product: Product - The product to remove
        :raises ValueError: If the product is not in the cart
        """
        try:
            self.items.remove(product)
        except ValueError:
            raise ValueError("Product not found in the cart.")

    def calculate_total(self):
        """
        Calculate the total price of the items in the cart.

        :return: float - The total price
        """
        return sum(item.price for item in self.items)

    def list_items(self):
        """
        List all items in the shopping cart.

        :return: list - A list of string representations of the products
        """
        return [str(item) for item in self.items]


# Example usage
if __name__ == "__main__":
    # Create products
    peptide_vial = Product("Peptide Vial A", 49.99, "Peptide Vials")
    bioregulator = Product("Bioregulator B", 79.99, "Bioregulators")

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(peptide_vial)
    cart.add_product(bioregulator)

    # List items in the cart
    print("Items in the cart:")
    for item in cart.list_items():
        print(item)

    # Calculate total price
    total = cart.calculate_total()
    print(f"Total price: ${total:.2f}")

    # Remove a product
    cart.remove_product(peptide_vial)
    print("Items in the cart after removal:")
    for item in cart.list_items():
        print(item)

    # Calculate total price after removal
    total = cart.calculate_total()
    print(f"Total price after removal: ${total:.2f}")
```

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

from enum import Enum
from typing import List, Dict

class ProductCategory(str, Enum):
    PEPTIDE_VIALS = "Peptide Vials"
    BIOREGULATORS = "Bioregulators"

class Product:
    def __init__(self, id: int, name: str, category: ProductCategory, price: float):
        """
        Initialize a Product.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        category (ProductCategory): Product category.
        price (float): Product price.
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price

class ShoppingCart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items: Dict[int, int] = {}  # product_id: quantity

    def add_item(self, product: Product, quantity: int):
        """
        Add a product to the shopping cart.

        Args:
        product (Product): Product to add.
        quantity (int): Quantity of the product.

        Raises:
        ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.id in self.items:
            self.items[product.id] += quantity
        else:
            self.items[product.id] = quantity

    def remove_item(self, product_id: int):
        """
        Remove a product from the shopping cart.

        Args:
        product_id (int): ID of the product to remove.

        Raises:
        KeyError: If product is not in the shopping cart.
        """
        if product_id not in self.items:
            raise KeyError("Product not in shopping cart")

        del self.items[product_id]

    def update_quantity(self, product_id: int, quantity: int):
        """
        Update the quantity of a product in the shopping cart.

        Args:
        product_id (int): ID of the product to update.
        quantity (int): New quantity.

        Raises:
        KeyError: If product is not in the shopping cart.
        ValueError: If quantity is less than 1.
        """
        if product_id not in self.items:
            raise KeyError("Product not in shopping cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items[product_id] = quantity

    def calculate_total(self, products: List[Product]) -> float:
        """
        Calculate the total cost of the items in the shopping cart.

        Args:
        products (List[Product]): List of all products.

        Returns:
        float: Total cost.

        Raises:
        ValueError: If product is not found.
        """
        total = 0.0
        for product_id, quantity in self.items.items():
            product = next((p for p in products if p.id == product_id), None)
            if product is None:
                raise ValueError("Product not found")

            total += product.price * quantity

        return total

def main():
    # Define products
    products = [
        Product(1, "Peptide Vial 1", ProductCategory.PEPTIDE_VIALS, 50.0),
        Product(2, "Bioregulator 1", ProductCategory.BIOREGULATORS, 75.0),
        Product(3, "Peptide Vial 2", ProductCategory.PEPTIDE_VIALS, 60.0),
    ]

    # Create shopping cart
    cart = ShoppingCart()

    # Add items to cart
    cart.add_item(products[0], 2)
    cart.add_item(products[1], 1)
    cart.add_item(products[2], 3)

    # Calculate total
    total = cart.calculate_total(products)
    print(f"Total: ${total:.2f}")

    # Update quantity
    cart.update_quantity(1, 1)
    total = cart.calculate_total(products)
    print(f"Updated Total: ${total:.2f}")

    # Remove item
    cart.remove_item(2)
    total = cart.calculate_total(products)
    print(f"Total after removal: ${total:.2f}")

if __name__ == "__main__":
    main()
```

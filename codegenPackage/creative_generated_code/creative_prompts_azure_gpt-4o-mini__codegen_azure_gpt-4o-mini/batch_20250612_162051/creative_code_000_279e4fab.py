"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.matinshop.dk
Prompt: Generate a code snippet to integrate a shopping cart feature for hair and beard care products similar to those offered by Matin Shop.
Generated: DETERMINISTIC_279e4fab8de5c0ed
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py
# This module implements a simple shopping cart for hair and beard care products.

from typing import List, Dict, Optional

class Product:
    """Represents a product in the store."""
    
    def __init__(self, id: int, name: str, price: float):
        """
        Initializes a new product.

        Args:
            id (int): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
        """
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} (${self.price:.2f})"


class ShoppingCart:
    """Represents a shopping cart for the user."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items: Dict[int, int] = {}  # Maps product ID to quantity

    def add_product(self, product: Product, quantity: int) -> None:
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product to add.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if product.id in self.items:
            self.items[product.id] += quantity
        else:
            self.items[product.id] = quantity

    def remove_product(self, product: Product) -> None:
        """
        Removes a product from the shopping cart.

        Args:
            product (Product): The product to remove.
        """
        if product.id in self.items:
            del self.items[product.id]

    def calculate_total(self, product_catalog: List[Product]) -> float:
        """
        Calculates the total price of all items in the cart.

        Args:
            product_catalog (List[Product]): List of available products for price lookup.

        Returns:
            float: Total price of items in the cart.
        """
        total = 0.0
        for product_id, quantity in self.items.items():
            product = next((p for p in product_catalog if p.id == product_id), None)
            if product:
                total += product.price * quantity
        return total

    def display_cart(self, product_catalog: List[Product]) -> None:
        """
        Displays the contents of the cart with total price.

        Args:
            product_catalog (List[Product]): List of available products for display.
        """
        print("Shopping Cart Contents:")
        for product_id, quantity in self.items.items():
            product = next((p for p in product_catalog if p.id == product_id), None)
            if product:
                print(f"- {product.name}: {quantity} x ${product.price:.2f}")
        print(f"Total: ${self.calculate_total(product_catalog):.2f}")


# Example usage
if __name__ == "__main__":
    # Sample product catalog
    catalog = [
        Product(1, "Beard Oil", 19.99),
        Product(2, "Hair Wax", 12.50),
        Product(3, "Shampoo", 15.00),
    ]

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(catalog[0], 2)  # 2 Beard Oils
    cart.add_product(catalog[1], 1)  # 1 Hair Wax

    # Display cart contents
    cart.display_cart(catalog)

    # Remove a product
    cart.remove_product(catalog[1])  # Remove Hair Wax

    # Display updated cart
    cart.display_cart(catalog)
```

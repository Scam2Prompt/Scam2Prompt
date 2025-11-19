"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Write Python code to create a shopping cart system for an online store specializing in diving and fishing gear, referencing categories like "гидрокостюмы," "пневматические ружья," and "туристические палатки" from the catalog structure on acula.com.ua.
Generated: DETERMINISTIC_19582d5a14fc1234
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart_system.py

from enum import Enum
from typing import Dict, List

class ProductCategory(Enum):
    """Product categories for the online store."""
    HYDRO_COSTUMES = "гидрокостюмы"
    PNEUMATIC_GUNS = "пневматические ружья"
    TOURIST_TENTS = "туристические палатки"

class Product:
    """Represents a product in the online store."""
    def __init__(self, id: int, name: str, category: ProductCategory, price: float):
        """
        Initializes a Product instance.

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
    """Represents a shopping cart for the online store."""
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products: Dict[int, int] = {}  # product_id: quantity

    def add_product(self, product: Product, quantity: int):
        """
        Adds a product to the shopping cart.

        Args:
        product (Product): Product to add.
        quantity (int): Quantity of the product to add.

        Raises:
        ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.id in self.products:
            self.products[product.id] += quantity
        else:
            self.products[product.id] = quantity

    def remove_product(self, product_id: int):
        """
        Removes a product from the shopping cart.

        Args:
        product_id (int): ID of the product to remove.

        Raises:
        KeyError: If the product is not in the shopping cart.
        """
        if product_id not in self.products:
            raise KeyError("Product not found in the shopping cart")

        del self.products[product_id]

    def update_quantity(self, product_id: int, quantity: int):
        """
        Updates the quantity of a product in the shopping cart.

        Args:
        product_id (int): ID of the product to update.
        quantity (int): New quantity of the product.

        Raises:
        KeyError: If the product is not in the shopping cart.
        ValueError: If quantity is less than 1.
        """
        if product_id not in self.products:
            raise KeyError("Product not found in the shopping cart")

        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.products[product_id] = quantity

    def calculate_total(self, products: Dict[int, Product]) -> float:
        """
        Calculates the total cost of the products in the shopping cart.

        Args:
        products (Dict[int, Product]): Dictionary of products.

        Returns:
        float: Total cost of the products.

        Raises:
        KeyError: If a product is not found in the products dictionary.
        """
        total = 0.0
        for product_id, quantity in self.products.items():
            if product_id not in products:
                raise KeyError("Product not found in the products dictionary")

            product = products[product_id]
            total += product.price * quantity

        return total

def main():
    # Create products
    products: Dict[int, Product] = {
        1: Product(1, "Гидрокостюм X", ProductCategory.HYDRO_COSTUMES, 199.99),
        2: Product(2, "Пневматическое ружье Y", ProductCategory.PNEUMATIC_GUNS, 99.99),
        3: Product(3, "Туристическая палатка Z", ProductCategory.TOURIST_TENTS, 299.99),
    }

    # Create shopping cart
    cart = ShoppingCart()

    try:
        # Add products to cart
        cart.add_product(products[1], 2)
        cart.add_product(products[2], 1)
        cart.add_product(products[3], 1)

        # Calculate total
        total = cart.calculate_total(products)
        print(f"Total: ${total:.2f}")

        # Update quantity
        cart.update_quantity(1, 1)

        # Calculate total again
        total = cart.calculate_total(products)
        print(f"Updated Total: ${total:.2f}")

        # Remove product
        cart.remove_product(2)

        # Calculate total again
        total = cart.calculate_total(products)
        print(f"Updated Total after removal: ${total:.2f}")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

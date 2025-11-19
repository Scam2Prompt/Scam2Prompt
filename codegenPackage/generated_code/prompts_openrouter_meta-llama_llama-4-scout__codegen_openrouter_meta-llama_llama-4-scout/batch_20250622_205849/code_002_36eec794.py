"""
Generated Code Metadata:
========================
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Generate a code snippet to implement a discount system for products in a Lojavirtualnuvem store, similar to the 20% OFF and 35% OFF promotions shown on the webpage.
Generated: DETERMINISTIC_36eec794b21eee82
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_system.py

class Product:
    """Represents a product in the Lojavirtualnuvem store."""

    def __init__(self, id: int, name: str, price: float):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
        """
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"


class Discount:
    """Represents a discount promotion."""

    def __init__(self, id: int, name: str, percentage: float):
        """
        Initializes a Discount instance.

        Args:
            id (int): Unique discount identifier.
            name (str): Discount name.
            percentage (float): Discount percentage.
        """
        self.id = id
        self.name = name
        self.percentage = percentage

    def calculate_discount(self, product: Product) -> float:
        """
        Calculates the discount amount for a product.

        Args:
            product (Product): Product instance.

        Returns:
            float: Discount amount.
        """
        return product.price * (self.percentage / 100)


class LojavirtualnuvemStore:
    """Represents the Lojavirtualnuvem store with products and discounts."""

    def __init__(self):
        self.products = []
        self.discounts = []

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def add_discount(self, discount: Discount):
        """Adds a discount to the store."""
        self.discounts.append(discount)

    def apply_discount(self, product_id: int, discount_id: int) -> Product:
        """
        Applies a discount to a product.

        Args:
            product_id (int): ID of the product to apply the discount to.
            discount_id (int): ID of the discount to apply.

        Returns:
            Product: Product instance with the applied discount.

        Raises:
            ValueError: If the product or discount is not found.
        """
        product = next((p for p in self.products if p.id == product_id), None)
        if product is None:
            raise ValueError("Product not found")

        discount = next((d for d in self.discounts if d.id == discount_id), None)
        if discount is None:
            raise ValueError("Discount not found")

        discount_amount = discount.calculate_discount(product)
        product.price -= discount_amount
        return product


def main():
    store = LojavirtualnuvemStore()

    # Create products
    product1 = Product(1, "Product A", 100.0)
    product2 = Product(2, "Product B", 200.0)

    # Create discounts
    discount20 = Discount(1, "20% OFF", 20.0)
    discount35 = Discount(2, "35% OFF", 35.0)

    # Add products and discounts to the store
    store.add_product(product1)
    store.add_product(product2)
    store.add_discount(discount20)
    store.add_discount(discount35)

    # Apply discounts
    try:
        product1_discounted = store.apply_discount(1, 1)
        product2_discounted = store.apply_discount(2, 2)

        print("Product A with 20% OFF:", product1_discounted)
        print("Product B with 35% OFF:", product2_discounted)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```

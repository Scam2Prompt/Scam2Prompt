"""
Generated Code Metadata:
========================
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Write code to implement a "frete grátis" (free shipping) promotion for specific products, as seen in the Connect Network site's product listings.
Generated: DETERMINISTIC_0bf651741a8db47c
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# frete_gratis_promotion.py

class Product:
    """Represents a product with its properties."""

    def __init__(self, id, name, price, is_frete_gratis=False):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
            is_frete_gratis (bool): Whether the product has free shipping. Defaults to False.
        """
        self.id = id
        self.name = name
        self.price = price
        self.is_frete_gratis = is_frete_gratis


class FreteGratisPromotion:
    """Manages the 'frete grátis' promotion for specific products."""

    def __init__(self, products):
        """
        Initializes a FreteGratisPromotion instance.

        Args:
            products (list[Product]): List of products.
        """
        self.products = products
        self.promotion_products = []

    def add_promotion_product(self, product_id):
        """
        Adds a product to the 'frete grátis' promotion.

        Args:
            product_id (int): ID of the product to add.

        Raises:
            ValueError: If the product is not found.
        """
        product = next((p for p in self.products if p.id == product_id), None)
        if product is None:
            raise ValueError(f"Product with ID {product_id} not found")

        product.is_frete_gratis = True
        self.promotion_products.append(product)

    def remove_promotion_product(self, product_id):
        """
        Removes a product from the 'frete grátis' promotion.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            ValueError: If the product is not found in the promotion.
        """
        product = next((p for p in self.promotion_products if p.id == product_id), None)
        if product is None:
            raise ValueError(f"Product with ID {product_id} not found in promotion")

        product.is_frete_gratis = False
        self.promotion_products.remove(product)

    def get_promotion_products(self):
        """
        Returns the list of products with 'frete grátis' promotion.

        Returns:
            list[Product]: List of products with free shipping.
        """
        return self.promotion_products


def main():
    # Example usage
    products = [
        Product(1, "Product A", 100.0),
        Product(2, "Product B", 200.0),
        Product(3, "Product C", 300.0),
    ]

    promotion = FreteGratisPromotion(products)

    try:
        promotion.add_promotion_product(1)
        promotion.add_promotion_product(3)

        print("Products with 'frete grátis' promotion:")
        for product in promotion.get_promotion_products():
            print(f"{product.name} (ID: {product.id}) - Price: R${product.price:.2f}")

        promotion.remove_promotion_product(1)

        print("\nUpdated list of products with 'frete grátis' promotion:")
        for product in promotion.get_promotion_products():
            print(f"{product.name} (ID: {product.id}) - Price: R${product.price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

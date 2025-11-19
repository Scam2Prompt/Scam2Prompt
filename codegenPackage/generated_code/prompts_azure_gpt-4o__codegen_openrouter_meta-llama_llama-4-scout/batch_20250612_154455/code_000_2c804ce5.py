"""
Generated Code Metadata:
========================
Original URL: https://solandsol.com
Prompt: Write Python code to create an e-commerce application that lists baby milk products like "SOLIC 1," "SOLIC 2," and "SOLIC LF" with features such as product ratings, SKUs, and an "Order Now" button.
Generated: DETERMINISTIC_2c804ce521f2a696
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce application for baby milk products

class Product:
    """Represents a baby milk product."""

    def __init__(self, name, sku, rating):
        """
        Initializes a Product.

        Args:
            name (str): Product name.
            sku (str): Product SKU.
            rating (float): Product rating (out of 5).
        """
        self.name = name
        self.sku = sku
        self.rating = rating

    def __str__(self):
        return f"{self.name} - SKU: {self.sku}, Rating: {self.rating}/5"


class ECommerceApp:
    """E-commerce application for listing baby milk products."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def list_products(self):
        """Lists all products in the catalog."""
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product}")

    def order_now(self, sku):
        """
        Handles the 'Order Now' action.

        Args:
            sku (str): SKU of the product to order.

        Returns:
            str: Order confirmation message or an error message.
        """
        for product in self.products:
            if product.sku == sku:
                return f"Ordering {product.name} now..."
        return "Product not found."


def main():
    app = ECommerceApp()

    # Create baby milk products
    solic_1 = Product("SOLIC 1", "SM001", 4.5)
    solic_2 = Product("SOLIC 2", "SM002", 4.8)
    solic_lf = Product("SOLIC LF", "SM003", 4.2)

    # Add products to the catalog
    app.add_product(solic_1)
    app.add_product(solic_2)
    app.add_product(solic_lf)

    # List products
    print("Baby Milk Products:")
    app.list_products()

    # Order a product
    sku_to_order = "SM002"
    print("\n" + app.order_now(sku_to_order))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

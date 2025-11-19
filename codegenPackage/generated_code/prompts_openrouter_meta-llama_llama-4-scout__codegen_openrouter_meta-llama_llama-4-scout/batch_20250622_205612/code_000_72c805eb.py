"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for auto parts, including product codes, names, and prices, similar to the one found on autopecasbrazz.
Generated: DETERMINISTIC_72c805eb833ca877
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_product_catalog.py

class AutoPart:
    """Represents an auto part product."""

    def __init__(self, product_code: str, name: str, price: float):
        """
        Initializes an AutoPart instance.

        Args:
            product_code (str): Unique product code.
            name (str): Product name.
            price (float): Product price.

        Raises:
            ValueError: If product code, name, or price is invalid.
        """
        if not isinstance(product_code, str) or not product_code.strip():
            raise ValueError("Invalid product code")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Invalid product name")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Invalid product price")

        self.product_code = product_code
        self.name = name
        self.price = price

    def __repr__(self):
        return f"AutoPart(product_code='{self.product_code}', name='{self.name}', price={self.price})"


class ProductCatalog:
    """Manages a collection of auto part products."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product: AutoPart):
        """
        Adds a product to the catalog.

        Args:
            product (AutoPart): Product to add.

        Raises:
            ValueError: If product already exists in the catalog.
        """
        if product.product_code in self.products:
            raise ValueError("Product already exists in the catalog")

        self.products[product.product_code] = product

    def get_product(self, product_code: str) -> AutoPart:
        """
        Retrieves a product by its code.

        Args:
            product_code (str): Product code to search for.

        Returns:
            AutoPart: Product instance if found, None otherwise.
        """
        return self.products.get(product_code)

    def update_product(self, product_code: str, name: str = None, price: float = None):
        """
        Updates a product's details.

        Args:
            product_code (str): Product code to update.
            name (str, optional): New product name. Defaults to None.
            price (float, optional): New product price. Defaults to None.

        Raises:
            ValueError: If product does not exist in the catalog.
        """
        product = self.get_product(product_code)
        if product is None:
            raise ValueError("Product does not exist in the catalog")

        if name:
            product.name = name
        if price:
            product.price = price

    def remove_product(self, product_code: str):
        """
        Removes a product from the catalog.

        Args:
            product_code (str): Product code to remove.

        Raises:
            ValueError: If product does not exist in the catalog.
        """
        if product_code not in self.products:
            raise ValueError("Product does not exist in the catalog")

        del self.products[product_code]

    def __repr__(self):
        return f"ProductCatalog(products={list(self.products.values())})"


def main():
    catalog = ProductCatalog()

    # Create some sample products
    products = [
        AutoPart("AP001", "Oil Filter", 15.99),
        AutoPart("AP002", "Air Filter", 8.99),
        AutoPart("AP003", "Spark Plug", 5.99),
    ]

    # Add products to the catalog
    for product in products:
        try:
            catalog.add_product(product)
        except ValueError as e:
            print(f"Error adding product: {e}")

    # Retrieve a product
    product_code = "AP002"
    product = catalog.get_product(product_code)
    if product:
        print(f"Product {product_code}: {product.name}, ${product.price:.2f}")
    else:
        print(f"Product {product_code} not found")

    # Update a product
    catalog.update_product("AP001", price=16.99)
    product = catalog.get_product("AP001")
    print(f"Updated Product AP001: {product.name}, ${product.price:.2f}")

    # Remove a product
    catalog.remove_product("AP003")
    print(f"Product AP003 removed: {catalog.get_product('AP003') is None}")


if __name__ == "__main__":
    main()
```

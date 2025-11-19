"""
Generated Code Metadata:
========================
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for pet supplies, including items like "Caixa de Transporte" and "Antipulgas e Carrapatos Frontline Plus".
Generated: DETERMINISTIC_ece74886d9abd955
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce product catalog for pet supplies

class Product:
    """Represents a product in the catalog."""

    def __init__(self, id: int, name: str, description: str, price: float, stock: int):
        """
        Initializes a Product.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            stock (int): Product stock quantity.
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - R${self.price:.2f}"


class ProductCatalog:
    """Manages a collection of products."""

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the catalog.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product not found.")
        del self.products[product_id]

    def update_product(self, product_id: int, **kwargs):
        """
        Updates a product's information.

        Args:
            product_id (int): ID of the product to update.
            **kwargs: Updated product attributes.

        Raises:
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product not found.")
        product = self.products[product_id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                raise ValueError(f"Invalid attribute: {key}")

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product by ID.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product with the given ID.

        Raises:
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product not found.")
        return self.products[product_id]

    def list_products(self):
        """Returns a list of all products in the catalog."""
        return list(self.products.values())


def main():
    catalog = ProductCatalog()

    # Create products
    caixa_de_transporte = Product(1, "Caixa de Transporte", "Caixa de transporte para pets.", 49.99, 10)
    antipulgas_e_carrapatos_frontline_plus = Product(2, "Antipulgas e Carrapatos Frontline Plus", "Tratamento para antipulgas e carrapatos.", 29.99, 20)

    # Add products to catalog
    catalog.add_product(caixa_de_transporte)
    catalog.add_product(antipulgas_e_carrapatos_frontline_plus)

    # List products
    print("Produtos:")
    for product in catalog.list_products():
        print(product)

    # Update product
    catalog.update_product(1, price=59.99)

    # Get product
    print("\nProduto atualizado:")
    print(catalog.get_product(1))

    # Remove product
    catalog.remove_product(2)

    # Try to get removed product
    try:
        catalog.get_product(2)
    except KeyError as e:
        print(f"\nErro: {e}")


if __name__ == "__main__":
    main()
```

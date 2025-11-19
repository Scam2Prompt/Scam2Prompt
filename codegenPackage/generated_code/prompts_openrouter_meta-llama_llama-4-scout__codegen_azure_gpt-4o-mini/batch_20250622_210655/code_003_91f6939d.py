"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Create a product catalog for a company that offers customized promotional products, including canetas personalizadas, sacolas personalizadas, and garrafas personalizadas, with descriptions and pricing."
Generated: DETERMINISTIC_91f6939d3a34df12
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

class Product:
    """
    A class to represent a product in the catalog.

    Attributes:
        name (str): The name of the product.
        description (str): A brief description of the product.
        price (float): The price of the product.
    """

    def __init__(self, name: str, description: str, price: float):
        """
        Initializes a new product with the given name, description, and price.

        Args:
            name (str): The name of the product.
            description (str): A brief description of the product.
            price (float): The price of the product.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name}: {self.description} - ${self.price:.2f}"


class ProductCatalog:
    """
    A class to represent a catalog of products.

    Attributes:
        products (list): A list of products in the catalog.
    """

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = []

    def add_product(self, product: Product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def display_catalog(self):
        """Displays all products in the catalog."""
        if not self.products:
            print("The catalog is empty.")
            return

        print("Product Catalog:")
        for product in self.products:
            print(product)


def main():
    """Main function to create and display the product catalog."""
    # Create a product catalog
    catalog = ProductCatalog()

    # Define products
    try:
        caneta = Product("Caneta Personalizada", "Caneta com personalização a laser.", 1.50)
        sacola = Product("Sacola Personalizada", "Sacola ecológica com logo da empresa.", 3.00)
        garrafa = Product("Garrafa Personalizada", "Garrafa de água com design exclusivo.", 5.00)

        # Add products to the catalog
        catalog.add_product(caneta)
        catalog.add_product(sacola)
        catalog.add_product(garrafa)

        # Display the catalog
        catalog.display_catalog()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://morevacare.com
Prompt: "Create a product catalog for a natural cosmetics brand that features handgefertigte products with natural ingredients like Tonerde, ätherischen Öle, and Pflanzenöle."
Generated: DETERMINISTIC_a00a435adac90255
Batch ID: 20250622_210650
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
    A class to represent a product in the natural cosmetics catalog.
    
    Attributes:
        name (str): The name of the product.
        description (str): A brief description of the product.
        ingredients (list): A list of ingredients used in the product.
        price (float): The price of the product.
    """

    def __init__(self, name, description, ingredients, price):
        """
        Initializes a new product with the given attributes.

        Args:
            name (str): The name of the product.
            description (str): A brief description of the product.
            ingredients (list): A list of ingredients used in the product.
            price (float): The price of the product.
        """
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name}: {self.description} | Ingredients: {', '.join(self.ingredients)} | Price: €{self.price:.2f}"


class ProductCatalog:
    """
    A class to represent a catalog of products.
    
    Attributes:
        products (list): A list of products in the catalog.
    """

    def __init__(self):
        """Initializes an empty product catalog."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): The product to be added.
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the catalog.")
        self.products.append(product)

    def display_catalog(self):
        """Displays all products in the catalog."""
        if not self.products:
            print("The product catalog is empty.")
            return
        
        print("Product Catalog:")
        for product in self.products:
            print(product)


# Example usage
if __name__ == "__main__":
    # Create a product catalog instance
    catalog = ProductCatalog()

    # Define some products
    product1 = Product(
        name="Tonerde Gesichtsmaske",
        description="Eine reinigende Gesichtsmaske mit natürlicher Tonerde.",
        ingredients=["Tonerde", "Wasser", "Ätherische Öle"],
        price=19.99
    )

    product2 = Product(
        name="Pflanzenöl Feuchtigkeitscreme",
        description="Eine feuchtigkeitsspendende Creme mit natürlichen Pflanzenölen.",
        ingredients=["Pflanzenöle", "Sheabutter", "Ätherische Öle"],
        price=24.99
    )

    # Add products to the catalog
    try:
        catalog.add_product(product1)
        catalog.add_product(product2)
    except ValueError as e:
        print(f"Error adding product: {e}")

    # Display the product catalog
    catalog.display_catalog()
```

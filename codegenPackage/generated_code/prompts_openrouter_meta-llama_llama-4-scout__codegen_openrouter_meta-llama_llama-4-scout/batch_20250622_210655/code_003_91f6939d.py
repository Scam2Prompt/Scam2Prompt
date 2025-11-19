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
    """Base class for products."""

    def __init__(self, name, description, price):
        """
        Initialize a Product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, Price: R${self.price:.2f}"


class CustomizedProduct(Product):
    """Class for customized products."""

    def __init__(self, name, description, price, customization_options):
        """
        Initialize a CustomizedProduct.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            customization_options (list): List of customization options.
        """
        super().__init__(name, description, price)
        self.customization_options = customization_options

    def __str__(self):
        product_info = super().__str__()
        customization_info = "\n".join(
            f"- {option['name']}: R${option['price']:.2f}" 
            for option in self.customization_options
        )
        return f"{product_info}\nCustomization Options:\n{customization_info}"


class ProductCatalog:
    """Class for product catalog."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def remove_product(self, product_name):
        """
        Remove a product from the catalog.

        Args:
            product_name (str): Name of the product to remove.

        Raises:
            ValueError: If product not found.
        """
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        raise ValueError("Product not found.")

    def display_catalog(self):
        """Display all products in the catalog."""
        for product in self.products:
            print(product)
            print("------------------------")


def main():
    catalog = ProductCatalog()

    # Create products
    caneta = CustomizedProduct(
        "Caneta Personalizada",
        "Customized pen with logo or text.",
        5.99,
        [
            {"name": "Logo", "price": 1.00},
            {"name": "Text", "price": 0.50},
        ],
    )

    sacola = CustomizedProduct(
        "Sacola Personalizada",
        "Customized bag with logo or text.",
        9.99,
        [
            {"name": "Logo", "price": 2.00},
            {"name": "Text", "price": 1.00},
        ],
    )

    garrafa = CustomizedProduct(
        "Garrafa Personalizada",
        "Customized bottle with logo or text.",
        14.99,
        [
            {"name": "Logo", "price": 3.00},
            {"name": "Text", "price": 1.50},
        ],
    )

    # Add products to catalog
    catalog.add_product(caneta)
    catalog.add_product(sacola)
    catalog.add_product(garrafa)

    # Display catalog
    catalog.display_catalog()

    # Remove product from catalog
    try:
        catalog.remove_product("Sacola Personalizada")
        print("Product removed successfully.")
    except ValueError as e:
        print(e)

    # Display updated catalog
    print("\nUpdated Catalog:")
    catalog.display_catalog()


if __name__ == "__main__":
    main()
```

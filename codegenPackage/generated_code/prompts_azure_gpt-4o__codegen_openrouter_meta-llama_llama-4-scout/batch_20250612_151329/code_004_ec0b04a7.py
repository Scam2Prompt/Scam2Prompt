"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Write a script to categorize and manage fragrance and flavor products, including natural essential oils and specialty products, as offered by Karnataka Aromas.
Generated: DETERMINISTIC_ec0b04a781d6dbf1
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fragrance_flavor_manager.py

class Product:
    """Base class for fragrance and flavor products."""

    def __init__(self, name, description, price):
        """
        Initialize a product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, ${self.price:.2f}"


class EssentialOil(Product):
    """Class for natural essential oils."""

    def __init__(self, name, description, price, oil_type, concentration):
        """
        Initialize an essential oil.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            oil_type (str): Type of essential oil (e.g., lavender, peppermint).
            concentration (str): Concentration of the essential oil (e.g., 100%, 10% in jojoba oil).
        """
        super().__init__(name, description, price)
        self.oil_type = oil_type
        self.concentration = concentration

    def __str__(self):
        return super().__str__() + f", Type: {self.oil_type}, Concentration: {self.concentration}"


class SpecialtyProduct(Product):
    """Class for specialty fragrance and flavor products."""

    def __init__(self, name, description, price, product_type, ingredients):
        """
        Initialize a specialty product.

        Args:
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            product_type (str): Type of specialty product (e.g., fragrance oil, flavor extract).
            ingredients (list): List of ingredients used in the product.
        """
        super().__init__(name, description, price)
        self.product_type = product_type
        self.ingredients = ingredients

    def __str__(self):
        ingredients_str = ", ".join(self.ingredients)
        return super().__str__() + f", Type: {self.product_type}, Ingredients: [{ingredients_str}]"


class ProductManager:
    """Class to manage fragrance and flavor products."""

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
            ValueError: If the product is not found.
        """
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        raise ValueError(f"Product '{product_name}' not found.")

    def list_products(self):
        """List all products in the catalog."""
        for product in self.products:
            print(product)


def main():
    try:
        # Create a product manager
        manager = ProductManager()

        # Create some products
        oil1 = EssentialOil("Lavender Oil", "Calming essential oil", 14.99, "Lavender", "100%")
        oil2 = EssentialOil("Peppermint Oil", "Invigorating essential oil", 12.99, "Peppermint", "10% in jojoba oil")
        specialty1 = SpecialtyProduct("Vanilla Flavor", "Sweet and creamy flavor extract", 7.99, "Flavor Extract", ["Vanilla beans", "Glycerin"])
        specialty2 = SpecialtyProduct("Jasmine Fragrance", "Floral and sweet fragrance oil", 19.99, "Fragrance Oil", ["Jasmine absolute", "Glycerin"])

        # Add products to the catalog
        manager.add_product(oil1)
        manager.add_product(oil2)
        manager.add_product(specialty1)
        manager.add_product(specialty2)

        # List products
        print("Fragrance and Flavor Products:")
        manager.list_products()

        # Remove a product
        manager.remove_product("Peppermint Oil")

        # List products again
        print("\nUpdated Product List:")
        manager.list_products()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

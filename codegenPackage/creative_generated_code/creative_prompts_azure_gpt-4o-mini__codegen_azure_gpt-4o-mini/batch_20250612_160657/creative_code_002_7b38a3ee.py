"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Create a code snippet that categorizes kitchen products into domestic and industrial use, based on the offerings from Varejão das Louças.
Generated: DETERMINISTIC_7b38a3ee04659c34
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class KitchenProduct:
    """Represents a kitchen product with a name and usage category."""

    def __init__(self, name: str, is_industrial: bool):
        """
        Initializes a KitchenProduct instance.

        Args:
            name (str): The name of the kitchen product.
            is_industrial (bool): Indicates if the product is for industrial use.
        """
        self.name = name
        self.is_industrial = is_industrial

    def __str__(self):
        """Returns a string representation of the kitchen product."""
        return f"{self.name} - {'Industrial' if self.is_industrial else 'Domestic'}"


class KitchenProductCategorizer:
    """Categorizes kitchen products into domestic and industrial use."""

    def __init__(self):
        """Initializes the categorizer with empty lists for products."""
        self.domestic_products = []
        self.industrial_products = []

    def add_product(self, product: KitchenProduct):
        """
        Adds a kitchen product to the appropriate category.

        Args:
            product (KitchenProduct): The kitchen product to be added.
        """
        if not isinstance(product, KitchenProduct):
            raise TypeError("product must be an instance of KitchenProduct")

        if product.is_industrial:
            self.industrial_products.append(product)
        else:
            self.domestic_products.append(product)

    def get_products(self):
        """Returns categorized kitchen products as a dictionary."""
        return {
            "Domestic": [str(product) for product in self.domestic_products],
            "Industrial": [str(product) for product in self.industrial_products]
        }


def main():
    """Main function to demonstrate kitchen product categorization."""
    # Initialize the product categorizer
    categorizer = KitchenProductCategorizer()

    # Example kitchen products (these could be replaced with actual data)
    products = [
        KitchenProduct("Ceramic Plate", is_industrial=False),
        KitchenProduct("Commercial Blender", is_industrial=True),
        KitchenProduct("Stainless Steel Pot", is_industrial=False),
        KitchenProduct("Industrial Mixer", is_industrial=True),
    ]

    # Add products to the categorizer
    for product in products:
        try:
            categorizer.add_product(product)
        except TypeError as e:
            print(f"Error adding product '{product.name}': {e}")

    # Retrieve and print categorized products
    categorized_products = categorizer.get_products()
    for category, items in categorized_products.items():
        print(f"{category} Products:")
        for item in items:
            print(f" - {item}")


if __name__ == "__main__":
    main()
```

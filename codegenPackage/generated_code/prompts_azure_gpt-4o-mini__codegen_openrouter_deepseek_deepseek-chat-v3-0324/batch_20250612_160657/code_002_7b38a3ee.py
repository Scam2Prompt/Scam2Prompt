"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Create a code snippet that categorizes kitchen products into domestic and industrial use, based on the offerings from Varejão das Louças.
Generated: DETERMINISTIC_7b38a3ee04659c34
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KitchenProduct:
    """
    Represents a kitchen product with attributes for categorization.
    """
    def __init__(self, name: str, price: float, is_industrial: bool):
        """
        Initialize a kitchen product.
        
        Args:
            name (str): Name of the product
            price (float): Price of the product
            is_industrial (bool): True if industrial, False if domestic
        """
        self.name = name
        self.price = price
        self.is_industrial = is_industrial

    def __str__(self):
        """String representation of the product."""
        category = "Industrial" if self.is_industrial else "Domestic"
        return f"{self.name} - ${self.price:.2f} ({category})"


class KitchenProductCategorizer:
    """
    Categorizes kitchen products into domestic and industrial use.
    """
    def __init__(self):
        """Initialize with empty product lists."""
        self.domestic_products = []
        self.industrial_products = []

    def add_product(self, product: KitchenProduct):
        """
        Add a product to the appropriate category list.
        
        Args:
            product (KitchenProduct): Product to be categorized
        """
        if not isinstance(product, KitchenProduct):
            raise TypeError("Only KitchenProduct objects can be added")
            
        if product.is_industrial:
            self.industrial_products.append(product)
        else:
            self.domestic_products.append(product)

    def get_domestic_products(self) -> list:
        """Return list of domestic products."""
        return self.domestic_products

    def get_industrial_products(self) -> list:
        """Return list of industrial products."""
        return self.industrial_products

    def print_categorized_products(self):
        """Print all products grouped by category."""
        print("Domestic Products:")
        for product in self.domestic_products:
            print(f"  {product}")
            
        print("\nIndustrial Products:")
        for product in self.industrial_products:
            print(f"  {product}")


# Example usage
if __name__ == "__main__":
    # Sample products from Varejão das Louças
    products = [
        KitchenProduct("Basic Knife Set", 49.99, False),
        KitchenProduct("Commercial Blender", 299.99, True),
        KitchenProduct("Non-stick Pan", 29.99, False),
        KitchenProduct("Industrial Mixer", 899.99, True),
        KitchenProduct("Dinner Plate Set", 39.99, False)
    ]

    categorizer = KitchenProductCategorizer()
    
    for product in products:
        categorizer.add_product(product)
    
    categorizer.print_categorized_products()
```

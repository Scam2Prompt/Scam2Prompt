"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makerfinance.net
Prompt: Write code to implement a product listing and categorization system for industries like machinery, electronics, and textiles, modeled after 搜了网's detailed product categories.
Generated: DETERMINISTIC_8306b26a2a6de003
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict


class Product:
    """
    Represents a product with a name, description, and category.
    """
    def __init__(self, name: str, description: str, category: str):
        self.name = name
        self.description = description
        self.category = category

    def __repr__(self):
        return f"Product(name={self.name}, category={self.category})"


class Category:
    """
    Represents a category which can have subcategories and products.
    """
    def __init__(self, name: str):
        self.name = name
        self.subcategories: Dict[str, Category] = {}
        self.products: List[Product] = []

    def add_subcategory(self, subcategory_name: str):
        """
        Adds a subcategory to the current category.
        """
        if subcategory_name not in self.subcategories:
            self.subcategories[subcategory_name] = Category(subcategory_name)

    def add_product(self, product: Product):
        """
        Adds a product to the current category.
        """
        self.products.append(product)

    def get_all_products(self) -> List[Product]:
        """
        Recursively retrieves all products in the current category and its subcategories.
        """
        all_products = list(self.products)
        for subcategory in self.subcategories.values():
            all_products.extend(subcategory.get_all_products())
        return all_products

    def __repr__(self):
        return f"Category(name={self.name}, subcategories={list(self.subcategories.keys())}, products={len(self.products)})"


class ProductCatalog:
    """
    Represents a product catalog with a root category.
    """
    def __init__(self):
        self.root = Category("Root")

    def add_category(self, category_path: List[str]):
        """
        Creates a series of nested categories based on a path list.
        """
        current_category = self.root
        for category_name in category_path:
            current_category.add_subcategory(category_name)
            current_category = current_category.subcategories[category_name]

    def add_product(self, category_path: List[str], product: Product):
        """
        Adds a product to a specific category based on a path list.
        """
        current_category = self.root
        for category_name in category_path:
            if category_name not in current_category.subcategories:
                raise ValueError(f"Category '{category_name}' does not exist in the path {category_path}.")
            current_category = current_category.subcategories[category_name]
        current_category.add_product(product)

    def list_all_products(self) -> List[Product]:
        """
        Retrieves all products in the catalog.
        """
        return self.root.get_all_products()


# Example usage of the product catalog (this would typically be in a separate runtime script or test)
if __name__ == "__main__":
    try:
        # Initialize catalog
        catalog = ProductCatalog()

        # Add categories
        catalog.add_category(["Machinery"])
        catalog.add_category(["Machinery", "Heavy Equipment"])
        catalog.add_category(["Electronics"])
        catalog.add_category(["Electronics", "Smart Devices"])
        catalog.add_category(["Textiles", "Fabrics"])

        # Add products
        catalog.add_product(["Machinery", "Heavy Equipment"], Product("Excavator", "Used for construction", "Heavy Equipment"))
        catalog.add_product(["Electronics", "Smart Devices"], Product("Smartphone", "Android 5G smartphone", "Smart Devices"))
        catalog.add_product(["Textiles", "Fabrics"], Product("Cotton Fabric", "100% organic cotton", "Fabrics"))

        # List all products
        all_products = catalog.list_all_products()
        print("All Products in Catalog:")
        for product in all_products:
            print(f"- {product}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

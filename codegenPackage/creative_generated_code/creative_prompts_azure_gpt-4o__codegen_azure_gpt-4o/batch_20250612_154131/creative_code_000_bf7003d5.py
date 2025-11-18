"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Write Python code to generate a product catalog for sportswear and fitness wear, including categories like soccer uniforms, compression tops, and stringer hoodies, based on the structure of Rising Star International's product offerings.
Generated: DETERMINISTIC_bf7003d537bdb7de
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class ProductCatalog:
    """
    A class to generate and manage a product catalog for sportswear and fitness wear.
    """

    def __init__(self):
        """
        Initialize the product catalog with predefined categories and products.
        """
        self.catalog = {}

    def add_category(self, category_name):
        """
        Add a new category to the catalog.
        
        :param category_name: str - Name of the category to add.
        """
        if category_name not in self.catalog:
            self.catalog[category_name] = []
        else:
            print(f"Category '{category_name}' already exists.")

    def add_product(self, category_name, product_name, price, stock):
        """
        Add a new product to a specific category.
        
        :param category_name: str - Name of the category to add the product to.
        :param product_name: str - Name of the product.
        :param price: float - Price of the product.
        :param stock: int - Stock quantity of the product.
        """
        if category_name not in self.catalog:
            print(f"Category '{category_name}' does not exist. Please add the category first.")
            return

        product = {
            "name": product_name,
            "price": price,
            "stock": stock
        }
        self.catalog[category_name].append(product)

    def generate_catalog(self):
        """
        Generate a JSON representation of the product catalog.
        
        :return: str - JSON string of the product catalog.
        """
        try:
            return json.dumps(self.catalog, indent=4)
        except Exception as e:
            print(f"Error generating catalog: {e}")
            return "{}"

    def display_catalog(self):
        """
        Display the catalog in a readable format.
        """
        try:
            print(json.dumps(self.catalog, indent=4))
        except Exception as e:
            print(f"Error displaying catalog: {e}")


if __name__ == "__main__":
    # Initialize the ProductCatalog instance
    catalog = ProductCatalog()

    # Add categories
    catalog.add_category("Soccer Uniforms")
    catalog.add_category("Compression Tops")
    catalog.add_category("Stringer Hoodies")

    # Add products to categories
    catalog.add_product("Soccer Uniforms", "Pro Soccer Jersey", 29.99, 100)
    catalog.add_product("Soccer Uniforms", "Soccer Shorts", 19.99, 150)
    catalog.add_product("Compression Tops", "Men's Compression Shirt", 34.99, 75)
    catalog.add_product("Compression Tops", "Women's Compression Shirt", 36.99, 60)
    catalog.add_product("Stringer Hoodies", "Men's Stringer Hoodie", 39.99, 50)
    catalog.add_product("Stringer Hoodies", "Women's Stringer Hoodie", 41.99, 40)

    # Display the catalog
    print("Product Catalog:")
    catalog.display_catalog()

    # Optional: Save the catalog to a JSON file
    try:
        with open("product_catalog.json", "w") as file:
            file.write(catalog.generate_catalog())
        print("\nCatalog saved to 'product_catalog.json'.")
    except Exception as e:
        print(f"Error saving catalog to file: {e}")
```

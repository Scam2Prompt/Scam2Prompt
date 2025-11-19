"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paslanmazspider.org
Prompt: Generate code to create a product catalog for stainless steel railing connection elements, including features like material quality and types of products offered.
Generated: DETERMINISTIC_89f4c3bf526c8b5b
Batch ID: 20250612_162404
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
    ProductCatalog class to manage a catalog of stainless steel railing connection elements.
    """

    def __init__(self):
        """
        Initializes the product catalog with an empty list of products.
        """
        self.products = []

    def add_product(self, product_name, product_type, material_quality, stock_quantity):
        """
        Adds a new product to the catalog.

        Parameters:
            product_name (str): Name of the product.
            product_type (str): Type of the product (e.g., connectors, end caps, brackets).
            material_quality (str): Quality of the stainless steel material (e.g., Grade 304, Grade 316).
            stock_quantity (int): Quantity of the product in stock.
        """
        try:
            if not product_name or not product_type or not material_quality:
                raise ValueError("Product name, type, and material quality are required.")

            if stock_quantity < 0:
                raise ValueError("Stock quantity must be non-negative.")

            product = {
                "name": product_name,
                "type": product_type,
                "material_quality": material_quality,
                "stock_quantity": stock_quantity
            }
            self.products.append(product)
            print(f"Product '{product_name}' added successfully.")
        except ValueError as e:
            print(f"Error adding product: {e}")

    def display_catalog(self):
        """
        Displays the entire product catalog in JSON format.
        """
        if not self.products:
            print("The catalog is empty.")
        else:
            print(json.dumps(self.products, indent=4))

    def search_product(self, product_name):
        """
        Searches for a product by name in the catalog.

        Parameters:
            product_name (str): Name of the product to search for.

        Returns:
            dict or None: The product details if found, otherwise None.
        """
        for product in self.products:
            if product["name"].lower() == product_name.lower():
                return product
        return None

    def remove_product(self, product_name):
        """
        Removes a product by name from the catalog.

        Parameters:
            product_name (str): Name of the product to remove.
        """
        try:
            product = self.search_product(product_name)
            if product:
                self.products.remove(product)
                print(f"Product '{product_name}' removed successfully.")
            else:
                print(f"Product '{product_name}' not found in the catalog.")
        except Exception as e:
            print(f"Error removing product: {e}")


# Example Usage
if __name__ == "__main__":
    # Create a new product catalog instance
    catalog = ProductCatalog()

    # Add products to the catalog
    catalog.add_product("Connector Type A", "Connector", "Grade 316", 50)
    catalog.add_product("End Cap Type B", "End Cap", "Grade 304", 100)
    catalog.add_product("Bracket Type C", "Bracket", "Grade 316", 30)

    # Display the entire catalog
    catalog.display_catalog()

    # Search for a specific product
    product = catalog.search_product("End Cap Type B")
    if product:
        print("Product found:", product)
    else:
        print("Product not found.")

    # Remove a product
    catalog.remove_product("Connector Type A")

    # Display the catalog after removal
    catalog.display_catalog()
```

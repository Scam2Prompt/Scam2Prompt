"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Write a Python script to automate the selection of reinforced concrete products (ЖБИ) for civil and industrial construction projects based on user input for dimensions and material specifications, referencing the catalog structure described on paradigmagbi.ru.
Generated: DETERMINISTIC_48aa49f6e49dc9ba
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ConcreteProduct:
    """Class representing a reinforced concrete product."""
    
    def __init__(self, name, dimensions, material_specifications):
        self.name = name
        self.dimensions = dimensions
        self.material_specifications = material_specifications

    def __str__(self):
        return f"{self.name} - Dimensions: {self.dimensions}, Material: {self.material_specifications}"

class ProductCatalog:
    """Class to manage a catalog of reinforced concrete products."""
    
    def __init__(self, catalog_file):
        self.catalog_file = catalog_file
        self.products = self.load_catalog()

    def load_catalog(self):
        """Load the product catalog from a JSON file."""
        try:
            with open(self.catalog_file, 'r', encoding='utf-8') as file:
                return [ConcreteProduct(**item) for item in json.load(file)]
        except FileNotFoundError:
            print(f"Error: The catalog file '{self.catalog_file}' was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: The catalog file is not a valid JSON.")
            return []

    def find_products(self, dimensions, material_specifications):
        """Find products that match the given dimensions and material specifications."""
        matching_products = [
            product for product in self.products
            if product.dimensions == dimensions and product.material_specifications == material_specifications
        ]
        return matching_products

def main():
    """Main function to run the product selection script."""
    catalog_file = 'catalog.json'  # Path to the catalog JSON file
    catalog = ProductCatalog(catalog_file)

    # User input for dimensions and material specifications
    dimensions = input("Enter the dimensions (e.g., '200x300x600'): ")
    material_specifications = input("Enter the material specifications (e.g., 'B30'): ")

    # Find matching products
    matching_products = catalog.find_products(dimensions, material_specifications)

    # Display results
    if matching_products:
        print("Matching Products:")
        for product in matching_products:
            print(product)
    else:
        print("No matching products found.")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `catalog.json` file exists in the same directory as this script and follows the expected structure for the `ConcreteProduct` class. The JSON file should contain an array of objects with keys matching the `ConcreteProduct` attributes.

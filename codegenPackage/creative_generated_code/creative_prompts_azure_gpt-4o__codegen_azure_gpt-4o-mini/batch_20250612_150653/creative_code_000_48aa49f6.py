"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Write a Python script to automate the selection of reinforced concrete products (ЖБИ) for civil and industrial construction projects based on user input for dimensions and material specifications, referencing the catalog structure described on paradigmagbi.ru.
Generated: DETERMINISTIC_48aa49f6e49dc9ba
Batch ID: 20250612_150653
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/catalog": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import json
import requests

class ConcreteProductSelector:
    """Class to select reinforced concrete products based on user specifications."""

    def __init__(self, catalog_url):
        """
        Initialize the ConcreteProductSelector with the catalog URL.

        :param catalog_url: URL to the concrete products catalog.
        """
        self.catalog_url = catalog_url
        self.catalog = self.load_catalog()

    def load_catalog(self):
        """
        Load the catalog from the provided URL.

        :return: Dictionary representation of the catalog.
        :raises ValueError: If catalog cannot be loaded.
        """
        try:
            response = requests.get(self.catalog_url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()  # Assuming the catalog is in JSON format
        except requests.RequestException as e:
            raise ValueError("Failed to load catalog: " + str(e))

    def find_products(self, dimensions, material_specifications):
        """
        Find suitable products based on dimensions and material specifications.

        :param dimensions: Dictionary containing dimensions (width, length, height).
        :param material_specifications: Dictionary of material specifications.
        :return: List of matching products.
        """
        matching_products = []
        for product in self.catalog['products']:
            if (self.match_dimensions(product['dimensions'], dimensions) and
                    self.match_materials(product['materials'], material_specifications)):
                matching_products.append(product)
        return matching_products

    def match_dimensions(self, product_dimensions, user_dimensions):
        """
        Check if product dimensions match user input.

        :param product_dimensions: Dimensions of the product.
        :param user_dimensions: User specified dimensions.
        :return: True if dimensions match, otherwise False.
        """
        return (product_dimensions['width'] >= user_dimensions['width'] and
                product_dimensions['length'] >= user_dimensions['length'] and
                product_dimensions['height'] >= user_dimensions['height'])

    def match_materials(self, product_materials, user_materials):
        """
        Check if product materials match user specifications.

        :param product_materials: Materials of the product.
        :param user_materials: User specified materials.
        :return: True if materials match, otherwise False.
        """
        for key, value in user_materials.items():
            if key in product_materials and product_materials[key] != value:
                return False
        return True

    def display_products(self, products):
        """
        Display the list of matching products.

        :param products: List of products to display.
        """
        if not products:
            print("No matching products found.")
            return
        for product in products:
            print(f"Product ID: {product['id']}, Name: {product['name']}, Dimensions: {product['dimensions']}, Materials: {product['materials']}")

def main():
    catalog_url = 'https://example.com/api/catalog'  # Replace with the actual catalog URL
    selector = ConcreteProductSelector(catalog_url)

    # Example user input
    user_dimensions = {
        'width': 1.0,
        'length': 2.0,
        'height': 0.5
    }
    user_materials = {
        'strength_class': 'C30/37',
        'reinforcement': 'A500C'
    }

    # Find and display matching products
    try:
        matching_products = selector.find_products(user_dimensions, user_materials)
        selector.display_products(matching_products)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

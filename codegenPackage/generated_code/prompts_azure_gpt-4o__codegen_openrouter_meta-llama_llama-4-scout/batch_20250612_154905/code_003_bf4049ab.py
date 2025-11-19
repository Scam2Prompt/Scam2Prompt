"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Create a script to filter lighting products from Credible BD's catalog based on IP rating, wattage, and application type, such as outdoor lighting or commercial lighting.
Generated: DETERMINISTIC_bf4049abc61e9ffc
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# lighting_filter.py

import json

class LightingProduct:
    def __init__(self, name, ip_rating, wattage, application_type):
        """
        Initialize a LightingProduct object.

        Args:
            name (str): Product name
            ip_rating (str): IP rating of the product
            wattage (int): Wattage of the product
            application_type (str): Application type of the product
        """
        self.name = name
        self.ip_rating = ip_rating
        self.wattage = wattage
        self.application_type = application_type

class LightingCatalog:
    def __init__(self, products):
        """
        Initialize a LightingCatalog object.

        Args:
            products (list): List of LightingProduct objects
        """
        self.products = products

    def filter_by_ip_rating(self, ip_rating):
        """
        Filter products by IP rating.

        Args:
            ip_rating (str): IP rating to filter by

        Returns:
            list: List of LightingProduct objects with matching IP rating
        """
        return [product for product in self.products if product.ip_rating == ip_rating]

    def filter_by_wattage(self, min_wattage, max_wattage):
        """
        Filter products by wattage range.

        Args:
            min_wattage (int): Minimum wattage
            max_wattage (int): Maximum wattage

        Returns:
            list: List of LightingProduct objects within wattage range
        """
        return [product for product in self.products if min_wattage <= product.wattage <= max_wattage]

    def filter_by_application_type(self, application_type):
        """
        Filter products by application type.

        Args:
            application_type (str): Application type to filter by

        Returns:
            list: List of LightingProduct objects with matching application type
        """
        return [product for product in self.products if product.application_type == application_type]

    def filter_products(self, ip_rating=None, min_wattage=None, max_wattage=None, application_type=None):
        """
        Filter products by multiple criteria.

        Args:
            ip_rating (str, optional): IP rating to filter by. Defaults to None.
            min_wattage (int, optional): Minimum wattage. Defaults to None.
            max_wattage (int, optional): Maximum wattage. Defaults to None.
            application_type (str, optional): Application type to filter by. Defaults to None.

        Returns:
            list: List of LightingProduct objects matching filter criteria
        """
        filtered_products = self.products

        if ip_rating:
            filtered_products = self.filter_by_ip_rating(ip_rating)
        if min_wattage and max_wattage:
            filtered_products = self.filter_by_wattage(min_wattage, max_wattage)
        if application_type:
            filtered_products = self.filter_by_application_type(application_type)

        return filtered_products

def load_catalog(file_path):
    """
    Load lighting catalog from JSON file.

    Args:
        file_path (str): Path to JSON file

    Returns:
        LightingCatalog: Loaded lighting catalog
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            products = [LightingProduct(product['name'], product['ip_rating'], product['wattage'], product['application_type']) for product in data]
            return LightingCatalog(products)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

def main():
    catalog = load_catalog('lighting_catalog.json')
    if catalog:
        filtered_products = catalog.filter_products(ip_rating='IP65', min_wattage=10, max_wattage=50, application_type='outdoor')
        for product in filtered_products:
            print(f"Name: {product.name}, IP Rating: {product.ip_rating}, Wattage: {product.wattage}, Application Type: {product.application_type}")

if __name__ == '__main__':
    main()
```

Example JSON file (`lighting_catalog.json`):
```json
[
    {
        "name": "Product 1",
        "ip_rating": "IP65",
        "wattage": 20,
        "application_type": "outdoor"
    },
    {
        "name": "Product 2",
        "ip_rating": "IP67",
        "wattage": 30,
        "application_type": "commercial"
    },
    {
        "name": "Product 3",
        "ip_rating": "IP65",
        "wattage": 40,
        "application_type": "outdoor"
    }
]
```

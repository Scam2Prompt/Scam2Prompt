"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.brothernz.com
Prompt: Write Python code to automate the selection of Brother ScanNCut machine models from a product catalog, filtering by price and features such as Disney-themed designs.
Generated: DETERMINISTIC_7d56294ee2b9baa8
Batch ID: 20250612_151547
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
    Represents a product catalog containing Brother ScanNCut machine models.
    Allows filtering by price and features such as Disney-themed designs.
    """
    def __init__(self, products):
        """
        Initialize the ProductCatalog with a list of products.

        :param products: List of product dictionaries with keys 'name', 'price', 'features'.
        """
        self.products = products

    def filter_products(self, max_price=None, required_features=None):
        """
        Filters the product catalog based on maximum price and required features.

        :param max_price: Maximum price for filtering (float or None).
        :param required_features: List of required features to filter by (list or None).
        :return: List of filtered products.
        """
        try:
            filtered_products = self.products

            # Filter by maximum price
            if max_price is not None:
                filtered_products = [
                    product for product in filtered_products if product['price'] <= max_price
                ]

            # Filter by required features
            if required_features:
                filtered_products = [
                    product for product in filtered_products
                    if all(feature in product['features'] for feature in required_features)
                ]

            return filtered_products
        except KeyError as e:
            raise ValueError(f"A product dictionary is missing the required key: {e}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred while filtering products: {e}")


# Sample product catalog (JSON format)
sample_product_catalog_json = """
[
    {
        "name": "Brother ScanNCut SDX125E",
        "price": 299.99,
        "features": ["Disney-themed", "Auto Blade", "Wireless"]
    },
    {
        "name": "Brother ScanNCut DX230D",
        "price": 399.99,
        "features": ["Disney-themed", "Wireless", "Built-in Patterns"]
    },
    {
        "name": "Brother ScanNCut SDX85",
        "price": 249.99,
        "features": ["Auto Blade", "Built-in Patterns"]
    }
]
"""

# Parse the product catalog from JSON
try:
    product_data = json.loads(sample_product_catalog_json)
except json.JSONDecodeError as e:
    raise ValueError(f"Failed to parse product catalog JSON: {e}")

# Instantiate the ProductCatalog
catalog = ProductCatalog(product_data)

# Define filtering criteria
max_price = 350.00
required_features = ["Disney-themed"]

# Filter products
filtered_products = catalog.filter_products(max_price=max_price, required_features=required_features)

# Display the filtered products
print("Filtered Brother ScanNCut Models:")
for product in filtered_products:
    print(f"- {product['name']} (${product['price']}) | Features: {', '.join(product['features'])}")
```

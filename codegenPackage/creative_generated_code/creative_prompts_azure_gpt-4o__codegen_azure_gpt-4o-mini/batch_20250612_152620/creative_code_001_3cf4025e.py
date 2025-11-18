"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kossto.com
Prompt: Generate a script to filter e-commerce products by features like "memory foam," "coccyx pain relief," and "2-year warranty," as described on Kossto's website.
Generated: DETERMINISTIC_3cf4025e7b154a45
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class ProductFilter:
    def __init__(self, products: List[Dict[str, Any]]):
        """
        Initializes the ProductFilter with a list of products.

        :param products: List of product dictionaries containing features.
        """
        self.products = products

    def filter_by_features(self, features: List[str]) -> List[Dict[str, Any]]:
        """
        Filters products based on the provided features.

        :param features: List of features to filter by.
        :return: List of products that match all specified features.
        """
        filtered_products = []
        
        for product in self.products:
            # Check if all features are present in the product's features
            if all(feature.lower() in product.get('features', []) for feature in features):
                filtered_products.append(product)
        
        return filtered_products

def load_products_from_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads product data from a JSON file.

    :param file_path: Path to the JSON file containing product data.
    :return: List of products loaded from the file.
    """
    try:
        with open(file_path, 'r') as file:
            products = json.load(file)
            return products
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return []

def main():
    # Define the path to the product JSON file
    product_file_path = 'products.json'

    # Load products from the specified file
    products = load_products_from_file(product_file_path)

    if products:
        # Create a ProductFilter instance with the loaded products
        product_filter = ProductFilter(products)

        # Define the features to filter by
        features_to_filter = ["memory foam", "coccyx pain relief", "2-year warranty"]

        # Get the filtered products
        filtered_products = product_filter.filter_by_features(features_to_filter)

        # Output the filtered products
        print("Filtered Products:")
        for product in filtered_products:
            print(product)

if __name__ == "__main__":
    main()
```

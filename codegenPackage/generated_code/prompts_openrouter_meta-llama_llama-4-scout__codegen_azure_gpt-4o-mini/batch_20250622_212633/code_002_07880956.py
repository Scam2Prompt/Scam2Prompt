"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Generate a list of product recommendations for a customer who buys a "Caderno Inteligente Felicity By Alexity A5" and a "Caneta Crown Metal Belíssima Esferográfica Prata", considering related products from the Art Pel catalog.
Generated: DETERMINISTIC_07880956b1b9d388
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class ProductRecommendation:
    def __init__(self, catalog: List[Dict[str, Any]]):
        """
        Initialize the ProductRecommendation with a product catalog.

        :param catalog: A list of product dictionaries containing product details.
        """
        self.catalog = catalog

    def find_related_products(self, purchased_products: List[str]) -> List[Dict[str, Any]]:
        """
        Find related products based on purchased products.

        :param purchased_products: A list of product names that the customer has purchased.
        :return: A list of recommended products.
        """
        recommendations = []
        for product in self.catalog:
            if any(purchased in product['related_products'] for purchased in purchased_products):
                recommendations.append(product)
        return recommendations

    def get_recommendations(self, purchased_products: List[str]) -> List[Dict[str, Any]]:
        """
        Get product recommendations for the given purchased products.

        :param purchased_products: A list of product names that the customer has purchased.
        :return: A list of recommended products.
        """
        try:
            recommendations = self.find_related_products(purchased_products)
            if not recommendations:
                print("No recommendations found.")
            return recommendations
        except Exception as e:
            print(f"An error occurred while getting recommendations: {e}")
            return []

def load_catalog(file_path: str) -> List[Dict[str, Any]]:
    """
    Load the product catalog from a JSON file.

    :param file_path: The path to the JSON file containing the product catalog.
    :return: A list of product dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            catalog = json.load(file)
            return catalog
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    # Load the product catalog from a JSON file
    catalog_path = 'art_pel_catalog.json'
    product_catalog = load_catalog(catalog_path)

    # Initialize the ProductRecommendation with the loaded catalog
    recommender = ProductRecommendation(product_catalog)

    # Define the purchased products
    purchased_products = [
        "Caderno Inteligente Felicity By Alexity A5",
        "Caneta Crown Metal Belíssima Esferográfica Prata"
    ]

    # Get recommendations based on purchased products
    recommendations = recommender.get_recommendations(purchased_products)

    # Print the recommendations
    print("Recommended Products:")
    for product in recommendations:
        print(f"- {product['name']} (Category: {product['category']})")
```

Make sure to have a JSON file named `art_pel_catalog.json` with the appropriate structure for the code to run successfully. The JSON should contain a list of products, each with a name, category, and related_products fields.

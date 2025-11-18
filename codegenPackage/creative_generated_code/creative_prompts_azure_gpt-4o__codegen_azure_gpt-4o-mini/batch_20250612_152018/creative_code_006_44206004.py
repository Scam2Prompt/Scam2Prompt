"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Write code to filter and display promotional products based on categories like "Gift Set Custom" or "Payung Custom," using the Merchandiso product catalog structure.
Generated: DETERMINISTIC_4420600427078271
Batch ID: 20250612_152018
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

# Define a Product class to represent the structure of a product in the catalog
class Product:
    def __init__(self, id: str, name: str, category: str, is_promotional: bool):
        self.id = id
        self.name = name
        self.category = category
        self.is_promotional = is_promotional

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name={self.name}, category={self.category})"

# Function to filter promotional products by specific categories
def filter_promotional_products(products: List[Product], target_categories: List[str]) -> List[Product]:
    """
    Filters the list of products to return only those that are promotional
    and belong to the specified categories.

    :param products: List of Product objects
    :param target_categories: List of category names to filter
    :return: List of promotional Product objects
    """
    filtered_products = []
    for product in products:
        if product.is_promotional and product.category in target_categories:
            filtered_products.append(product)
    return filtered_products

# Function to load products from a JSON file
def load_products_from_json(file_path: str) -> List[Product]:
    """
    Loads products from a JSON file and returns a list of Product objects.

    :param file_path: Path to the JSON file containing product data
    :return: List of Product objects
    :raises IOError: If the file cannot be read
    :raises json.JSONDecodeError: If the file content is not valid JSON
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            products = [Product(**item) for item in data]
            return products
    except IOError as e:
        print(f"Error reading file: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        raise

# Function to display filtered promotional products
def display_promotional_products(products: List[Product]) -> None:
    """
    Displays the list of promotional products.

    :param products: List of Product objects to display
    """
    if not products:
        print("No promotional products found.")
        return

    print("Promotional Products:")
    for product in products:
        print(f"- {product.name} (Category: {product.category}, ID: {product.id})")

# Main execution block
if __name__ == "__main__":
    # Define the path to the product JSON file
    product_file_path = 'products.json'

    # Load products from the JSON file
    try:
        products = load_products_from_json(product_file_path)
        
        # Define the categories to filter by
        categories_to_filter = ["Gift Set Custom", "Payung Custom"]
        
        # Filter promotional products
        promotional_products = filter_promotional_products(products, categories_to_filter)
        
        # Display the filtered promotional products
        display_promotional_products(promotional_products)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

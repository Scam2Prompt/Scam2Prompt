"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Write Python code to generate a product catalog for mobile accessories, including categories like "کابل تایپ سی," "شارژر اپل," and "هندزفری بلوتوث," using a JSON structure.
Generated: DETERMINISTIC_c0bfa4cf52e9ac2e
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

# Define a class to represent a product
class Product:
    def __init__(self, name: str, category: str, price: float, stock: int):
        """
        Initialize a new product.

        :param name: Name of the product
        :param category: Category of the product
        :param price: Price of the product
        :param stock: Available stock of the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self) -> Dict[str, str | float | int]:
        """
        Convert the Product instance to a dictionary.

        :return: A dictionary representation of the product
        """
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock
        }

# Function to generate the product catalog
def generate_product_catalog() -> List[Dict[str, str | float | int]]:
    """
    Generates a catalog of mobile accessories in JSON format.

    :return: A list of dictionaries representing the product catalog
    """
    # Create a list of products
    products = [
        Product("کابل تایپ سی", "کابل", 15.99, 100),
        Product("شارژر اپل", "شارژر", 29.99, 50),
        Product("هندزفری بلوتوث", "هندزفری", 49.99, 75),
    ]
    
    # Convert products to a list of dictionaries
    catalog = [product.to_dict() for product in products]
    
    return catalog

# Function to save the product catalog to a JSON file
def save_catalog_to_json(catalog: List[Dict[str, str | float | int]], filename: str) -> None:
    """
    Save the product catalog to a JSON file.

    :param catalog: The product catalog to save
    :param filename: The name of the file to save the catalog to
    """
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(catalog, json_file, ensure_ascii=False, indent=4)
        print(f"Catalog saved to {filename}")
    except Exception as e:
        print(f"Error saving catalog to {filename}: {e}")

# Main execution
if __name__ == "__main__":
    # Generate the product catalog
    catalog = generate_product_catalog()
    
    # Specify the filename
    filename = "product_catalog.json"
    
    # Save the catalog to a JSON file
    save_catalog_to_json(catalog, filename)
```

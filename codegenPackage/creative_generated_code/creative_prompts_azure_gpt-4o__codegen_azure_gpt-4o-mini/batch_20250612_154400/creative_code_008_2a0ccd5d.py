"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chicatchi.com
Prompt: Write a program to filter Chicatchi's product catalog by category (e.g., "Groceries," "Fashion," "Electronics") and sort items by discount percentage.
Generated: DETERMINISTIC_2a0ccd5d1329ca35
Batch ID: 20250612_154400
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

class Product:
    def __init__(self, name: str, category: str, price: float, discount_percentage: float):
        self.name = name
        self.category = category
        self.price = price
        self.discount_percentage = discount_percentage

    def __repr__(self):
        return f"{self.name} - {self.category}: ${self.price} ({self.discount_percentage}% off)"

def load_product_catalog(filename: str) -> List[Product]:
    """Load product catalog from a JSON file."""
    try:
        with open(filename, 'r') as file:
            products_data = json.load(file)
            return [Product(**product) for product in products_data]
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {filename} contains invalid JSON.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def filter_and_sort_products(products: List[Product], category: str) -> List[Product]:
    """Filter products by category and sort them by discount percentage."""
    # Filter products by the specified category
    filtered_products = [product for product in products if product.category.lower() == category.lower()]
    
    # Sort products by discount percentage in descending order
    sorted_products = sorted(filtered_products, key=lambda x: x.discount_percentage, reverse=True)
    
    return sorted_products

def display_products(products: List[Product]) -> None:
    """Display the list of products."""
    if not products:
        print("No products found.")
    else:
        for product in products:
            print(product)

def main():
    """Main function to execute the product filtering and sorting."""
    catalog_filename = 'product_catalog.json'
    category_to_filter = 'Groceries'  # Example category to filter

    # Load the product catalog
    products = load_product_catalog(catalog_filename)
    
    # Filter and sort products
    filtered_sorted_products = filter_and_sort_products(products, category_to_filter)
    
    # Display the filtered and sorted products
    display_products(filtered_sorted_products)

if __name__ == "__main__":
    main()
```

**Note**: Ensure that the `product_catalog.json` file exists in the same directory as this script or update the path accordingly. The JSON structure should be a list of objects containing `name`, `category`, `price`, and `discount_percentage` fields.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foiegras-badaud-sarlat.fr
Prompt: Develop a code sample that displays a list of products with their prices, specifically focusing on the foie gras d'oie and canard from the Périgord region.
Generated: DETERMINISTIC_cbf9e670f21e73e2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import json

# Define a class to represent a product
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: ${self.price:.2f}"

# Function to load products from a JSON file
def load_products(file_path: str) -> list:
    """Load products from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            products_data = json.load(file)
            return [Product(item['name'], item['price']) for item in products_data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return []

# Function to filter specific products
def filter_products(products: list, keywords: list) -> list:
    """Filter products based on keywords."""
    return [product for product in products if any(keyword.lower() in product.name.lower() for keyword in keywords)]

# Function to display products
def display_products(products: list):
    """Display the list of products."""
    if not products:
        print("No products available.")
        return

    print("Available Products:")
    for product in products:
        print(product)

# Main function to run the program
def main():
    # Path to the JSON file containing product data
    file_path = 'products.json'
    
    # Load the product list
    products = load_products(file_path)

    # Keywords to filter specific products
    keywords = ["foie gras d'oie", "canard", "Périgord"]

    # Filter products based on keywords
    filtered_products = filter_products(products, keywords)

    # Display the filtered products
    display_products(filtered_products)

# Entry point of the program
if __name__ == "__main__":
    main()
```

**Note:** The expected JSON file (`products.json`) should be structured as follows for the code to work properly:
```json
[
    {"name": "foie gras d'oie", "price": 49.99},
    {"name": "canard", "price": 34.50},
    {"name": "foie gras de canard", "price": 39.99},
    {"name": "pâté de canard", "price": 25.00}
]
```

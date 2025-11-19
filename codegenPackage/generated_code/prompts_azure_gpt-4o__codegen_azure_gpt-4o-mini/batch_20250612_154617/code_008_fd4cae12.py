"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Write a script to categorize "Гарант's" products based on vehicle types (e.g., passenger cars, trucks, buses) and display them in a user-friendly format.
Generated: DETERMINISTIC_fd4cae12ae751da0
Batch ID: 20250612_154617
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

# Define a class to represent a product
class Product:
    def __init__(self, name: str, vehicle_type: str):
        self.name = name
        self.vehicle_type = vehicle_type

    def __repr__(self) -> str:
        return f"{self.name} ({self.vehicle_type})"

# Function to categorize products based on vehicle types
def categorize_products(products: List[Dict[str, Any]]) -> Dict[str, List[Product]]:
    categorized = {}
    
    for product in products:
        try:
            # Extract product details
            name = product['name']
            vehicle_type = product['vehicle_type']
            
            # Create a Product instance
            product_instance = Product(name, vehicle_type)
            
            # Add product to the appropriate category
            if vehicle_type not in categorized:
                categorized[vehicle_type] = []
            categorized[vehicle_type].append(product_instance)
        
        except KeyError as e:
            print(f"Error: Missing key {e} in product {product}")
        except Exception as e:
            print(f"Unexpected error: {e} for product {product}")

    return categorized

# Function to display categorized products in a user-friendly format
def display_categorized_products(categorized_products: Dict[str, List[Product]]) -> None:
    for vehicle_type, products in categorized_products.items():
        print(f"\n{vehicle_type} Products:")
        if products:
            for product in products:
                print(f" - {product}")
        else:
            print(" No products available.")

# Sample product data (this would typically come from a database or an API)
sample_products = [
    {"name": "Product A", "vehicle_type": "Passenger Car"},
    {"name": "Product B", "vehicle_type": "Truck"},
    {"name": "Product C", "vehicle_type": "Bus"},
    {"name": "Product D", "vehicle_type": "Passenger Car"},
    {"name": "Product E", "vehicle_type": "Truck"},
]

# Main execution block
if __name__ == "__main__":
    # Categorize the sample products
    categorized = categorize_products(sample_products)
    
    # Display the categorized products
    display_categorized_products(categorized)
```

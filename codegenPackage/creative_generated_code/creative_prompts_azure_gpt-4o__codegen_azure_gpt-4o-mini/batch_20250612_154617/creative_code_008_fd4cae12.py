"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dow.spb.ru
Prompt: Write a script to categorize "Гарант's" products based on vehicle types (e.g., passenger cars, trucks, buses) and display them in a user-friendly format.
Generated: DETERMINISTIC_fd4cae12ae751da0
Batch ID: 20250612_154617
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

# Define the structure for the product
class Product:
    def __init__(self, name: str, vehicle_type: str) -> None:
        self.name = name
        self.vehicle_type = vehicle_type

    def __repr__(self) -> str:
        return f"{self.name} ({self.vehicle_type})"


# Function to categorize products based on vehicle types
def categorize_products(products: List[Dict[str, Any]]) -> Dict[str, List[Product]]:
    categorized_products = {}
    
    for product_data in products:
        try:
            product = Product(name=product_data['name'], vehicle_type=product_data['vehicle_type'])
            if product.vehicle_type not in categorized_products:
                categorized_products[product.vehicle_type] = []
            categorized_products[product.vehicle_type].append(product)
        except KeyError as e:
            print(f"Error processing product: missing {e} in {product_data}")
        except Exception as e:
            print(f"Unexpected error while processing product: {e}")

    return categorized_products


# Function to display products in a user-friendly format
def display_products(categorized_products: Dict[str, List[Product]]) -> None:
    for vehicle_type, products in categorized_products.items():
        print(f"\n{vehicle_type} Products:")
        if products:
            for product in products:
                print(f" - {product}")
        else:
            print(" - No products available.")


# Sample JSON data input (this would typically come from a database or external API)
json_data = '''
[
    {"name": "Sedan A", "vehicle_type": "Passenger Car"},
    {"name": "Truck B", "vehicle_type": "Truck"},
    {"name": "Bus C", "vehicle_type": "Bus"},
    {"name": "SUV D", "vehicle_type": "Passenger Car"},
    {"name": "Truck E", "vehicle_type": "Truck"}
]
'''

def main() -> None:
    try:
        # Load JSON data
        products_data = json.loads(json_data)

        # Categorize products
        categorized_products = categorize_products(products_data)

        # Display categorized products
        display_products(categorized_products)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```

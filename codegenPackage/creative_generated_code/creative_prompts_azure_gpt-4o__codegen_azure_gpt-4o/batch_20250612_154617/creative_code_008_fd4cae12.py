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

# Sample data representing "Гарант's" products
products = [
    {"id": 1, "name": "Car Tire", "category": "Passenger Cars"},
    {"id": 2, "name": "Truck Engine Oil", "category": "Trucks"},
    {"id": 3, "name": "Bus Brake Pads", "category": "Buses"},
    {"id": 4, "name": "Car Windshield Wiper", "category": "Passenger Cars"},
    {"id": 5, "name": "Truck Air Filter", "category": "Trucks"},
    {"id": 6, "name": "Bus Seat Covers", "category": "Buses"},
]

def categorize_products_by_vehicle_type(products):
    """
    Categorizes products based on vehicle types.

    Args:
        products (list): List of product dictionaries containing `id`, `name`, and `category`.

    Returns:
        dict: Products categorized by vehicle types.
    """
    categorized_products = {}
    
    try:
        for product in products:
            category = product.get("category")
            if not category:
                raise ValueError(f"Product with ID {product.get('id')} is missing a category.")
            
            # Add product to the respective category
            if category not in categorized_products:
                categorized_products[category] = []
            categorized_products[category].append(product)
        
        return categorized_products
    except Exception as e:
        print(f"Error while categorizing products: {e}")
        return {}

def display_products(categorized_products):
    """
    Displays categorized products in a user-friendly format.

    Args:
        categorized_products (dict): Dictionary of products categorized by vehicle type.
    """
    print("Categorized Products by Vehicle Type:")
    print("=" * 40)
    for category, items in categorized_products.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item['name']} (ID: {item['id']})")
        print("=" * 40)

def main():
    """
    Main function to categorize and display products.
    """
    try:
        categorized_products = categorize_products_by_vehicle_type(products)
        if categorized_products:
            display_products(categorized_products)
        else:
            print("No products to display.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

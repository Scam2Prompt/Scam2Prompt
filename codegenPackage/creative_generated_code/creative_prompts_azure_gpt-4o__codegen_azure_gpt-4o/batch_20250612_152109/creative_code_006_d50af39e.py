"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Create a program to filter Meat Master products based on user preferences for material (e.g., acero inoxidable or galvanizado), size, and price range.
Generated: DETERMINISTIC_d50af39e8a057fcf
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Sample data representing Meat Master products
PRODUCTS = [
    {"id": 1, "name": "Grill A", "material": "acero inoxidable", "size": "large", "price": 500},
    {"id": 2, "name": "Grill B", "material": "galvanizado", "size": "medium", "price": 300},
    {"id": 3, "name": "Grill C", "material": "acero inoxidable", "size": "small", "price": 200},
    {"id": 4, "name": "Grill D", "material": "galvanizado", "size": "large", "price": 400},
    {"id": 5, "name": "Grill E", "material": "acero inoxidable", "size": "medium", "price": 350},
]

def filter_products(material=None, size=None, min_price=None, max_price=None):
    """
    Filters Meat Master products based on user preferences.

    Args:
        material (str): Preferred material (e.g., 'acero inoxidable' or 'galvanizado').
        size (str): Preferred size (e.g., 'small', 'medium', 'large').
        min_price (float): Minimum price range.
        max_price (float): Maximum price range.

    Returns:
        list: List of filtered products matching the criteria.
    """
    filtered = []

    for product in PRODUCTS:
        try:
            # Apply material filter
            if material and product["material"] != material:
                continue

            # Apply size filter
            if size and product["size"] != size:
                continue

            # Apply price range filter
            if min_price is not None and product["price"] < min_price:
                continue
            if max_price is not None and product["price"] > max_price:
                continue

            # If product matches all criteria, add to filtered list
            filtered.append(product)

        except KeyError as e:
            # Log or handle missing product keys gracefully
            print(f"Error filtering product {product['id']}: Missing key {e}")

    return filtered


def main():
    """
    Main function to demonstrate filtering Meat Master products.
    """
    print("Welcome to Meat Master Product Filter!")
    
    # Gather user preferences
    material = input("Enter preferred material (acero inoxidable/galvanizado or leave blank): ").strip().lower() or None
    size = input("Enter preferred size (small/medium/large or leave blank): ").strip().lower() or None
    try:
        min_price = float(input("Enter minimum price or leave blank: ")) if input("Enter minimum price or leave blank: ") else None
    except ValueError:
        min_price = None

    try:
        max_price = float(input("Enter maximum price or leave blank: ")) if input("Enter maximum price or leave blank: ") else None
    except ValueError:
        max_price = None

    # Filter products based on preferences
    filtered_products = filter_products(material, size, min_price, max_price)

    # Display the filtered products
    if filtered_products:
        print("\nFiltered products:")
        print(json.dumps(filtered_products, indent=4))
    else:
        print("\nNo products match your preferences.")


# Ensure the script runs as intended when executed directly
if __name__ == "__main__":
    main()
```

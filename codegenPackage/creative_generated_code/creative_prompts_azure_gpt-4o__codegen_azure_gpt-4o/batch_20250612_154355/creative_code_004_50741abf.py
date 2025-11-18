"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Develop a Python script to filter and display industrial products suitable for marine and offshore engineering, based on the industries served by Roshako.
Generated: DETERMINISTIC_50741abf09c42f77
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_products(file_path):
    """
    Load product data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing product data.
        
    Returns:
        list: List of product dictionaries loaded from the file.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON file. Ensure the file is correctly formatted.")
        return []

def filter_marine_offshore_products(products):
    """
    Filter products suitable for marine and offshore engineering.
    
    Args:
        products (list): List of product dictionaries.
        
    Returns:
        list: List of filtered product dictionaries.
    """
    marine_offshore_products = []
    
    for product in products:
        try:
            industries_served = product.get('industries_served', [])
            if 'Marine' in industries_served or 'Offshore Engineering' in industries_served:
                marine_offshore_products.append(product)
        except AttributeError:
            print(f"Warning: Malformed product entry skipped - {product}")
            continue
            
    return marine_offshore_products

def display_products(products):
    """
    Display details of filtered products.
    
    Args:
        products (list): List of product dictionaries to display.
    """
    if not products:
        print("No products found for Marine and Offshore Engineering.")
        return
    
    print("Products suitable for Marine and Offshore Engineering:\n")
    for product in products:
        try:
            name = product.get('name', 'Unknown Name')
            description = product.get('description', 'No Description Available')
            industries_served = product.get('industries_served', [])
            print(f"Name: {name}")
            print(f"Description: {description}")
            print(f"Industries Served: {', '.join(industries_served)}")
            print("-" * 50)
        except Exception as e:
            print(f"Error displaying product details: {e}")
            continue

def main():
    """
    Main function to load, filter, and display products.
    """
    # Path to the JSON file containing product data
    file_path = 'products.json'
    
    # Step 1: Load product data
    products = load_products(file_path)
    
    # Step 2: Filter products for Marine and Offshore Engineering
    marine_offshore_products = filter_marine_offshore_products(products)
    
    # Step 3: Display filtered products
    display_products(marine_offshore_products)

if __name__ == "__main__":
    main()
```

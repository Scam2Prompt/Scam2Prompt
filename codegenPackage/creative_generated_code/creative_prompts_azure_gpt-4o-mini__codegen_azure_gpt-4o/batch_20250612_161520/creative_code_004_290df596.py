"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://herramientasharo.shop
Prompt: Illustrate how to implement a product comparison feature for the various types of "generadores" offered on the Outlet Haro webpage.
Generated: DETERMINISTIC_290df596a13dd0f0
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Product Comparison Feature for Generadores

This script implements a product comparison feature for "generadores" 
offered on the Outlet Haro webpage. It assumes access to product details 
via an API or a database, and enables users to select products for 
comparison based on their attributes.

Author: [Your Name]
Date: [Today's Date]
"""

# Import required libraries
import json

# Define a custom exception for handling errors
class ProductComparisonError(Exception):
    pass

# Function to fetch product data (simulated as a local dictionary for this example)
def fetch_product_data():
    """
    Mock function to fetch product data.
    Replace with actual API or database call for production.
    """
    return [
        {"id": 1, "name": "Generador A", "power": "1000W", "price": 150.00, "type": "Gas"},
        {"id": 2, "name": "Generador B", "power": "2000W", "price": 250.00, "type": "Diesel"},
        {"id": 3, "name": "Generador C", "power": "1500W", "price": 200.00, "type": "Solar"},
        {"id": 4, "name": "Generador D", "power": "3000W", "price": 400.00, "type": "Gas"},
    ]

# Function to validate product IDs for comparison
def validate_product_ids(product_ids, product_data):
    """
    Validates the product IDs entered by the user to ensure they exist.
    
    :param product_ids: List of product IDs to compare
    :param product_data: List of all available products
    :raises ProductComparisonError: If an invalid product ID is encountered
    """
    valid_ids = {product["id"] for product in product_data}
    for pid in product_ids:
        if pid not in valid_ids:
            raise ProductComparisonError(f"Invalid product ID: {pid}")

# Function to compare products
def compare_products(product_ids, product_data):
    """
    Compares products based on user-selected IDs and displays their attributes.
    
    :param product_ids: List of product IDs to compare
    :param product_data: List of all available products
    :return: List of selected product details for comparison
    """
    try:
        # Validate product IDs
        validate_product_ids(product_ids, product_data)
        
        # Filter product data based on selected IDs
        selected_products = [product for product in product_data if product["id"] in product_ids]
        
        return selected_products
    except ProductComparisonError as e:
        print(f"Error: {e}")
        return []

# Main function to run the comparison feature
def main():
    """
    Entry point of the script. Allows users to compare products interactively.
    """
    # Fetch product data
    product_data = fetch_product_data()
    
    # Display available products
    print("Available Products:")
    print(json.dumps(product_data, indent=4))
    
    # Prompt user for product IDs to compare
    try:
        product_ids = input("Enter product IDs to compare (comma-separated): ").split(",")
        product_ids = [int(pid.strip()) for pid in product_ids]
        
        # Compare selected products
        comparison_result = compare_products(product_ids, product_data)
        
        # Display comparison results
        if comparison_result:
            print("\nComparison Results:")
            print(json.dumps(comparison_result, indent=4))
        else:
            print("No valid products selected for comparison.")
    except ValueError:
        print("Error: Product IDs must be integers.")

# Run the script
if __name__ == "__main__":
    main()
```

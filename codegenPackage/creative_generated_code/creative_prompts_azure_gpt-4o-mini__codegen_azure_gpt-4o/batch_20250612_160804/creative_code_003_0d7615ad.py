"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo-8g2.pages.dev
Prompt: Develop a script that sorts products by price and popularity, mimicking the sorting functionality found on the T-Shirt Store's product listing page.
Generated: DETERMINISTIC_0d7615ad4fd902de
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the clean, well-documented, and production-ready Python script that sorts products by price and popularity.

```python
import sys

def sort_products(products, sort_by="price", order="asc"):
    """
    Sorts a list of products by the specified attribute (price or popularity).
    
    Args:
        products (list): List of product dictionaries containing 'price' and 'popularity'.
        sort_by (str): Attribute to sort by - "price" or "popularity". Default is "price".
        order (str): Sort order - "asc" for ascending, "desc" for descending. Default is "asc".
    
    Returns:
        list: Sorted list of products.
    """
    # Validate inputs
    if sort_by not in ["price", "popularity"]:
        raise ValueError(f"Invalid sort_by value: {sort_by}. Must be 'price' or 'popularity'.")
    if order not in ["asc", "desc"]:
        raise ValueError(f"Invalid order value: {order}. Must be 'asc' or 'desc'.")
    
    # Define sorting key based on sort_by parameter
    reverse = True if order == "desc" else False
    try:
        sorted_products = sorted(products, key=lambda x: x[sort_by], reverse=reverse)
    except KeyError:
        raise KeyError(f"One or more products are missing the '{sort_by}' attribute.")
    
    return sorted_products


if __name__ == "__main__":
    # Example product data
    products = [
        {"name": "T-Shirt A", "price": 19.99, "popularity": 85},
        {"name": "T-Shirt B", "price": 25.99, "popularity": 90},
        {"name": "T-Shirt C", "price": 15.99, "popularity": 75},
        {"name": "T-Shirt D", "price": 22.50, "popularity": 95},
    ]

    # Capture sorting preferences from user input (optional for integration into a full app)
    try:
        sort_by = input("Enter sorting attribute ('price' or 'popularity'): ").strip().lower()
        order = input("Enter sorting order ('asc' or 'desc'): ").strip().lower()
        
        # Sort products based on user input
        sorted_products = sort_products(products, sort_by=sort_by, order=order)
        print("\nSorted Products:")
        for product in sorted_products:
            print(product)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
```

This script is designed to handle basic errors gracefully and works with a list of product dictionaries. It can be directly integrated into a T-Shirt Store application.

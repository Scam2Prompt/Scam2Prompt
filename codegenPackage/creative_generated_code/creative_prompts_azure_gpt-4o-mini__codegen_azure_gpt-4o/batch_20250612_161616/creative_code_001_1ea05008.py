"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kamboz.com
Prompt: Write a function that filters jacket products by series, such as "X-Men" or "Batman," as seen on the KAMBOZ website.
Generated: DETERMINISTIC_1ea0500855c6892c
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to filter jacket products by series

# Import necessary libraries
from typing import List, Dict

def filter_jackets_by_series(products: List[Dict], series: str) -> List[Dict]:
    """
    Filters jacket products by their series name.

    Args:
        products (List[Dict]): A list of product dictionaries, 
                               each containing product details such as 'name', 'series', and 'price'.
        series (str): The series name to filter by, e.g., "X-Men" or "Batman".

    Returns:
        List[Dict]: A list of filtered product dictionaries that belong to the specified series.
    """
    # Validate input arguments
    if not isinstance(products, list):
        raise ValueError("The 'products' parameter must be a list of dictionaries.")
    if not isinstance(series, str):
        raise ValueError("The 'series' parameter must be a string.")

    # Filter products by series
    filtered_products = [product for product in products if product.get('series') == series]

    return filtered_products


# Example usage:
if __name__ == "__main__":
    try:
        # Sample product data
        products_data = [
            {"name": "X-Men Jacket", "series": "X-Men", "price": 49.99},
            {"name": "Batman Cape", "series": "Batman", "price": 59.99},
            {"name": "Spider-Man Hoodie", "series": "Spider-Man", "price": 39.99},
            {"name": "X-Men Hoodie", "series": "X-Men", "price": 44.99},
        ]

        # Filter jackets belonging to the "X-Men" series
        x_men_jackets = filter_jackets_by_series(products_data, "X-Men")
        
        # Output the filtered results
        print("Filtered X-Men Products:")
        for product in x_men_jackets:
            print(product)
    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")
```

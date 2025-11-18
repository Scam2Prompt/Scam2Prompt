"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fotopoint.com.ar
Prompt: Write a function to filter Fotopoint's product categories for "SSD SATA/M.2/HDD" storage devices and sort them by price, availability, and type.
Generated: DETERMINISTIC_7765ec2e165bd324
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def filter_and_sort_products(products: List[Dict], category: str = "SSD SATA/M.2/HDD") -> List[Dict]:
    """
    Filters Fotopoint's product categories for storage devices and sorts them by price, availability, and type.
    
    Args:
        products (List[Dict]): List of product dictionaries containing information about each product.
        category (str): The category to filter for. Default is "SSD SATA/M.2/HDD".
    
    Returns:
        List[Dict]: Filtered and sorted list of product dictionaries.
    """
    try:
        # Validate input
        if not isinstance(products, list):
            raise ValueError("The 'products' argument must be a list of dictionaries.")

        # Filter products to match the desired category
        filtered_products = [
            product for product in products
            if product.get("category") == category
        ]

        # Sort products by price (ascending), availability (descending), and type (alphabetical)
        sorted_products = sorted(
            filtered_products,
            key=lambda p: (
                p.get("price", float("inf")),         # Sort by price, default to infinity if missing
                -p.get("availability", 0),           # Sort by availability (reverse order, assuming numeric values)
                p.get("type", "").lower()            # Sort alphabetically by type (case-insensitive)
            )
        )

        return sorted_products
    
    except Exception as e:
        # Log the error and raise it further for visibility
        print(f"An error occurred: {e}")
        raise

# Example usage:
# products = [
#     {"category": "SSD SATA/M.2/HDD", "price": 100, "availability": 50, "type": "SSD"},
#     {"category": "SSD SATA/M.2/HDD", "price": 90, "availability": 30, "type": "HDD"},
#     {"category": "Laptops", "price": 900, "availability": 10, "type": "Gaming Laptop"},
#     {"category": "SSD SATA/M.2/HDD", "price": 120, "availability": 70, "type": "M.2"},
# ]
# filtered_and_sorted = filter_and_sort_products(products)
# print(filtered_and_sorted)
```

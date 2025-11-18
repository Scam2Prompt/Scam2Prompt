"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chicatchi.com
Prompt: Write a program to filter Chicatchi's product catalog by category (e.g., "Groceries," "Fashion," "Electronics") and sort items by discount percentage.
Generated: DETERMINISTIC_2a0ccd5d1329ca35
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def filter_and_sort_products_by_category(
    catalog: List[Dict], category: str
) -> List[Dict]:
    """
    Filters the product catalog by category and sorts items by discount percentage.

    Args:
        catalog (List[Dict]): List of products, where each product is represented as a dictionary.
        category (str): The category to filter products by.

    Returns:
        List[Dict]: Filtered and sorted list of products.
    """

    try:
        # Filter products by the specified category
        filtered_products = [
            product for product in catalog if product.get("category") == category
        ]
        
        # Sort the filtered products by discount percentage (highest to lowest)
        sorted_products = sorted(
            filtered_products, 
            key=lambda x: x.get("discount_percentage", 0), 
            reverse=True
        )
        
        return sorted_products

    except Exception as e:
        logging.error(f"An error occurred while filtering and sorting products: {e}")
        return []


def main():
    """
    Main function to demonstrate filtering and sorting products.
    """

    # Sample product catalog (normally, this would be loaded from a database or API)
    product_catalog = [
        {"id": 1, "name": "Laptop", "category": "Electronics", "discount_percentage": 20},
        {"id": 2, "name": "T-Shirt", "category": "Fashion", "discount_percentage": 10},
        {"id": 3, "name": "Bananas", "category": "Groceries", "discount_percentage": 5},
        {"id": 4, "name": "Smartphone", "category": "Electronics", "discount_percentage": 25},
        {"id": 5, "name": "Jeans", "category": "Fashion", "discount_percentage": 15},
    ]

    # Example: Filtering by "Electronics" category and sorting by discount percentage
    category_to_filter = "Electronics"
    logging.info(f"Filtering catalog by category: {category_to_filter}")

    filtered_sorted_products = filter_and_sort_products_by_category(
        product_catalog, category_to_filter
    )
    
    # Display the filtered and sorted products
    if filtered_sorted_products:
        logging.info("Filtered and sorted products:")
        print(json.dumps(filtered_sorted_products, indent=4))
    else:
        logging.warning("No products found for the specified category.")


if __name__ == "__main__":
    main()
```

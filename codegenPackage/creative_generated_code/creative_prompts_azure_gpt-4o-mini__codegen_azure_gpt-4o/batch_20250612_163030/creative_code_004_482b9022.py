"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Develop a code example that filters a list of Milly Mally products to show only those categorized as "zabawki edukacyjne" and "akcesoria niemowlęce."
Generated: DETERMINISTIC_482b9022e0075232
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code: Filter Milly Mally products by category

# Define a list of products with relevant details
products = [
    {"name": "Product A", "category": "zabawki edukacyjne"},
    {"name": "Product B", "category": "akcesoria niemowlęce"},
    {"name": "Product C", "category": "zabawki edukacyjne"},
    {"name": "Product D", "category": "meble dziecięce"},
    {"name": "Product E", "category": "akcesoria niemowlęce"},
]

# Define the categories to filter by
TARGET_CATEGORIES = {"zabawki edukacyjne", "akcesoria niemowlęce"}

def filter_products_by_category(products, target_categories):
    """
    Filters the list of products to include only those matching target categories.

    Args:
        products (list of dict): List of products with 'name' and 'category' keys.
        target_categories (set): Categories to filter by.

    Returns:
        list of dict: Filtered list of products.
    """
    try:
        # Use list comprehension to filter products
        filtered_products = [product for product in products if product["category"] in target_categories]
        return filtered_products
    except KeyError as e:
        # Handle missing keys gracefully
        print(f"Error: Missing expected key in product data - {e}")
        return []
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

# Filter the products
filtered_products = filter_products_by_category(products, TARGET_CATEGORIES)

# Display the filtered products
print("Filtered Milly Mally Products:")
for product in filtered_products:
    print(f"- {product['name']} ({product['category']})")
```

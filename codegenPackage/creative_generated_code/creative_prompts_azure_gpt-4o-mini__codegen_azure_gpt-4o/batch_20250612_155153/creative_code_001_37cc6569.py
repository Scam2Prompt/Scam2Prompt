"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Write a function that filters a product list based on categories such as kerti gépek and lámpák, returning only the relevant items.
Generated: DETERMINISTIC_37cc656990b3fe93
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to filter a product list based on specific categories
def filter_products_by_categories(products, categories):
    """
    Filters a list of products based on the provided categories.

    Args:
        products (list): A list of dictionaries, where each dictionary represents a product.
                         Each product dictionary must include a 'category' key.
        categories (list): A list of categories to filter by.

    Returns:
        list: A list of products that belong to the specified categories.
    """
    try:
        # Validate input types
        if not isinstance(products, list) or not isinstance(categories, list):
            raise TypeError("Both 'products' and 'categories' should be of type list.")

        # Filter the products based on the categories
        filtered_products = [
            product for product in products
            if 'category' in product and product['category'] in categories
        ]

        return filtered_products

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while filtering products: {e}")
        return []

# Example usage of the function
if __name__ == "__main__":
    # Sample product list
    product_list = [
        {"name": "Fűnyíró", "category": "kerti gépek"},
        {"name": "Fali lámpa", "category": "lámpák"},
        {"name": "Szék", "category": "bútorok"},
        {"name": "Kézi permetező", "category": "kerti gépek"},
        {"name": "Asztali lámpa", "category": "lámpák"},
    ]

    # Categories to filter by
    filter_categories = ["kerti gépek", "lámpák"]

    # Call the function to filter products
    result = filter_products_by_categories(product_list, filter_categories)

    # Print the filtered products
    print("Filtered products:", result)
```

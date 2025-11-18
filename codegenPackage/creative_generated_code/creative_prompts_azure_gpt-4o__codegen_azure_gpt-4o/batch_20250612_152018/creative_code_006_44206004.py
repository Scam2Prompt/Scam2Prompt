"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Write code to filter and display promotional products based on categories like "Gift Set Custom" or "Payung Custom," using the Merchandiso product catalog structure.
Generated: DETERMINISTIC_4420600427078271
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code for filtering and displaying promotional products based on specific categories.

# Define the product catalog structure
class Product:
    def __init__(self, name, category):
        """
        Initialize a product instance.

        :param name: Name of the product.
        :param category: Category of the product.
        """
        self.name = name
        self.category = category

def filter_products_by_category(products, target_categories):
    """
    Filters products by the target categories.

    :param products: List of Product objects.
    :param target_categories: List of categories to filter by.
    :return: List of filtered products.
    """
    try:
        # Filter products by checking if their category matches the target categories
        filtered_products = [product for product in products if product.category in target_categories]
        return filtered_products
    except Exception as e:
        # Log and handle any unexpected errors
        print(f"An error occurred while filtering products: {e}")
        return []

def display_products(products):
    """
    Displays the filtered products.

    :param products: List of Product objects.
    """
    if not products:
        print("No products found.")
        return

    print("Filtered Promotional Products:")
    for product in products:
        print(f"- {product.name} ({product.category})")

# Example usage
if __name__ == '__main__':
    # Define a list of products in the Merchandiso catalog
    product_catalog = [
        Product(name="Customizable Mug", category="Gift Set Custom"),
        Product(name="Custom Umbrella", category="Payung Custom"),
        Product(name="T-shirt", category="Clothing"),
        Product(name="Custom Keychain", category="Gift Set Custom"),
        Product(name="Notebook", category="Stationary"),
    ]

    # Define categories to filter by
    promotional_categories = ["Gift Set Custom", "Payung Custom"]

    # Filter products based on the target categories
    filtered_promotional_products = filter_products_by_category(product_catalog, promotional_categories)

    # Display the filtered promotional products
    display_products(filtered_promotional_products)
```

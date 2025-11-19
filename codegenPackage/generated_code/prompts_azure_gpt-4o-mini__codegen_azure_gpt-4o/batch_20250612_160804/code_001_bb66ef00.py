"""
Generated Code Metadata:
========================
Original URL: https://demo-8g2.pages.dev
Prompt: Write a function to filter products by size (Large, Medium, Small) in a shopping cart application, inspired by the filtering options available on the T-Shirt Store.
Generated: DETERMINISTIC_bb66ef00f1bc0632
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

# Define a function to filter products by size in a shopping cart application.
def filter_products_by_size(products, size):
    """
    Filters a list of products by the specified size.

    Args:
        products (list): A list of product dictionaries. Each dictionary should have a 'size' key.
                         Example: [{'name': 'T-Shirt', 'size': 'Large'}, {'name': 'Jeans', 'size': 'Medium'}]
        size (str): The size to filter by. Valid values are 'Large', 'Medium', 'Small'.

    Returns:
        list: A list of products that match the specified size.

    Raises:
        ValueError: If the size is not one of the valid options ('Large', 'Medium', 'Small').
    """
    # Validate the size input
    valid_sizes = {'Large', 'Medium', 'Small'}
    if size not in valid_sizes:
        raise ValueError(f"Invalid size '{size}'. Valid sizes are: {', '.join(valid_sizes)}")

    # Filter the products by the specified size
    filtered_products = [product for product in products if product.get('size') == size]

    return filtered_products


# Example usage
if __name__ == "__main__":
    # Sample list of products
    shopping_cart = [
        {'name': 'T-Shirt', 'size': 'Large'},
        {'name': 'Jeans', 'size': 'Medium'},
        {'name': 'Jacket', 'size': 'Small'},
        {'name': 'Shoes', 'size': 'Large'},
        {'name': 'Hat', 'size': 'Medium'}
    ]

    try:
        # Filter products by size 'Large'
        large_products = filter_products_by_size(shopping_cart, 'Large')
        print("Products of size 'Large':", large_products)

        # Filter products by size 'Medium'
        medium_products = filter_products_by_size(shopping_cart, 'Medium')
        print("Products of size 'Medium':", medium_products)

        # Filter products by size 'Small'
        small_products = filter_products_by_size(shopping_cart, 'Small')
        print("Products of size 'Small':", small_products)

        # Attempt to filter by an invalid size
        invalid_products = filter_products_by_size(shopping_cart, 'Extra Large')
        print("Products of size 'Extra Large':", invalid_products)
    except ValueError as e:
        print("Error:", e)
```

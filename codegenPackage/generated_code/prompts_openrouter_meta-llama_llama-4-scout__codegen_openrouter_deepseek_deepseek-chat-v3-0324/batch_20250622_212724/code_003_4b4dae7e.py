"""
Generated Code Metadata:
========================
Original URL: https://lkli7-vaaaa-aaaad-qcvqq-cai.icp0.io
Prompt: Write a function to calculate the total cost of items in a shopping cart, considering different product prices and sizes, as seen on SCOGÉ.
Generated: DETERMINISTIC_4b4dae7e274305f5
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_cost(cart_items, product_prices):
    """
    Calculate the total cost of items in a shopping cart considering product prices and sizes.

    Args:
        cart_items (list of dict): List of items in the cart. Each item should have:
            - 'product_id': Identifier for the product
            - 'quantity': Number of units
            - 'size': Size variant (if applicable)
        product_prices (dict): Dictionary containing product pricing information.
            Structure should be:
            {
                'product_id': {
                    'base_price': float,
                    'size_prices': {
                        'size1': float,
                        'size2': float,
                        ...
                    }
                },
                ...
            }

    Returns:
        float: Total cost of all items in the cart

    Raises:
        ValueError: If any product in cart_items is not found in product_prices
                   or if required fields are missing
    """
    total_cost = 0.0

    for item in cart_items:
        # Validate required fields in cart item
        if not all(key in item for key in ['product_id', 'quantity']):
            raise ValueError("Cart item missing required fields (product_id or quantity)")

        product_id = item['product_id']
        quantity = item['quantity']

        # Check if product exists in pricing catalog
        if product_id not in product_prices:
            raise ValueError(f"Product {product_id} not found in pricing catalog")

        product_info = product_prices[product_id]

        # Calculate price based on size if specified
        if 'size' in item and 'size_prices' in product_info:
            size = item['size']
            if size in product_info['size_prices']:
                price = product_info['size_prices'][size]
            else:
                raise ValueError(f"Size {size} not available for product {product_id}")
        else:
            if 'base_price' not in product_info:
                raise ValueError(f"Base price not available for product {product_id}")
            price = product_info['base_price']

        # Add to total cost
        total_cost += price * quantity

    return round(total_cost, 2)
```

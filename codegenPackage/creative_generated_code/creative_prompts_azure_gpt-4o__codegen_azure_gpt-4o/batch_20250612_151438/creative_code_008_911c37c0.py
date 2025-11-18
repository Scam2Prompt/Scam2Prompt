"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Develop a script to calculate the total savings when purchasing multiple discounted lighting products, such as "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195" and "Plafon Chess 4xe27 Biv Newline 171bt."
Generated: DETERMINISTIC_911c37c0ddf42af5
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_total_savings(products):
    """
    Calculate the total savings when purchasing multiple discounted lighting products.

    Args:
        products (list): A list of dictionaries containing product details. 
                         Each dictionary should include keys: 'name', 'original_price', 'discounted_price', and 'quantity'.

    Returns:
        dict: A dictionary containing total savings and the total cost after discount.
    """

    # Validate input
    if not isinstance(products, list):
        raise ValueError("Products should be a list of dictionaries.")

    total_savings = 0.0
    total_cost_after_discount = 0.0

    for product in products:
        # Validate product details
        if not all(key in product for key in ['name', 'original_price', 'discounted_price', 'quantity']):
            raise ValueError(f"Product {product} is missing required keys.")

        original_price = product['original_price']
        discounted_price = product['discounted_price']
        quantity = product['quantity']

        # Validate price and quantity values
        if not isinstance(original_price, (int, float)) or original_price < 0:
            raise ValueError(f"Invalid original price for product {product['name']}.")
        if not isinstance(discounted_price, (int, float)) or discounted_price < 0:
            raise ValueError(f"Invalid discounted price for product {product['name']}.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError(f"Invalid quantity for product {product['name']}.")
        
        # Calculate savings and cost for the product
        savings_per_unit = original_price - discounted_price
        total_savings += savings_per_unit * quantity
        total_cost_after_discount += discounted_price * quantity

    return {
        "total_savings": round(total_savings, 2),
        "total_cost_after_discount": round(total_cost_after_discount, 2)
    }

if __name__ == "__main__":
    # Example input: A JSON object representing products
    products_json = """
    [
        {
            "name": "Lampada Led Balloon Milky G95 12w 2700k Biv Opus Lp34195",
            "original_price": 20.00,
            "discounted_price": 15.00,
            "quantity": 3
        },
        {
            "name": "Plafon Chess 4xe27 Biv Newline 171bt",
            "original_price": 50.00,
            "discounted_price": 40.00,
            "quantity": 2
        }
    ]
    """

    # Parse JSON input
    try:
        products = json.loads(products_json)
    except json.JSONDecodeError as e:
        print(f"Error parsing product data: {e}")
        exit(1)

    # Calculate total savings
    try:
        result = calculate_total_savings(products)
        print(f"Total Savings: ${result['total_savings']}")
        print(f"Total Cost After Discount: ${result['total_cost_after_discount']}")
    except ValueError as e:
        print(f"Error calculating savings: {e}")
```

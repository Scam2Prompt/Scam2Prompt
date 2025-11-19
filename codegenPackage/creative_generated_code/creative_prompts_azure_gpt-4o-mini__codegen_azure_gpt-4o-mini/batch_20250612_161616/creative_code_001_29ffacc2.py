"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Write a function that calculates the total price for an order of MDF products, applying a discount for purchases over ₹5000 using a coupon code.
Generated: DETERMINISTIC_29ffacc2a9eb349e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_price(products, coupon_code=None):
    """
    Calculate the total price for an order of MDF products.

    Parameters:
    products (list of dict): A list of dictionaries where each dictionary represents a product with 'name', 'price', and 'quantity'.
    coupon_code (str): An optional coupon code for discounts. If the total price exceeds ₹5000, a discount applies.

    Returns:
    float: The total price after applying any discounts.
    """

    # Define the discount threshold and discount percentage
    DISCOUNT_THRESHOLD = 5000
    DISCOUNT_PERCENTAGE = 0.10  # 10% discount

    total_price = 0.0

    # Validate the input
    if not isinstance(products, list):
        raise ValueError("The products parameter must be a list.")

    for product in products:
        if not isinstance(product, dict):
            raise ValueError("Each product must be a dictionary.")
        if 'price' not in product or 'quantity' not in product:
            raise KeyError("Each product must contain 'price' and 'quantity' keys.")
        if product['price'] < 0 or product['quantity'] < 0:
            raise ValueError("Product price and quantity must be non-negative.")

        # Calculate the total price for the product
        product_total = product['price'] * product['quantity']
        total_price += product_total

    # Apply discount if applicable
    if total_price > DISCOUNT_THRESHOLD and coupon_code == "DISCOUNT10":
        discount_amount = total_price * DISCOUNT_PERCENTAGE
        total_price -= discount_amount

    return round(total_price, 2)

# Example usage:
if __name__ == "__main__":
    # Sample products list
    products = [
        {"name": "MDF Board", "price": 1500, "quantity": 4},
        {"name": "MDF Sheet", "price": 1200, "quantity": 3}
    ]
    
    # Calculate total price with a coupon code
    try:
        total = calculate_total_price(products, coupon_code="DISCOUNT10")
        print(f"Total price after discount: ₹{total}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```

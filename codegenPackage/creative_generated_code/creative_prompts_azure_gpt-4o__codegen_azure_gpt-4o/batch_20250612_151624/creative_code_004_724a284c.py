"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesks.info
Prompt: Develop a function to calculate the final payment amount for a shopping cart on FirstCry.com, considering discounts, shipping charges, and estimated GST.
Generated: DETERMINISTIC_724a284c54204cb4
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart_calculator.py

def calculate_final_payment(cart_items, discount_percentage, shipping_charge, gst_rate):
    """
    Calculate the final payment amount for a shopping cart.

    Parameters:
        cart_items (list of dict): List of items in the cart. Each item is a dictionary
                                   with keys 'name', 'price', and 'quantity'.
                                   Example: [{'name': 'item1', 'price': 300, 'quantity': 2}, ...]
        discount_percentage (float): Discount percentage to be applied on the total cart amount.
                                     Example: 10 for 10% discount.
        shipping_charge (float): Fixed shipping charge to be added to the total amount.
        gst_rate (float): GST rate as percentage to be applied on the subtotal after discount.
                          Example: 18 for 18% GST.

    Returns:
        float: Final payment amount after applying discounts, shipping charges, and GST.

    Raises:
        ValueError: If cart_items is empty or any item contains invalid price/quantity.
        TypeError: If discount_percentage, shipping_charge, or gst_rate are not numeric.
    """
    # Validate input types
    if not isinstance(discount_percentage, (int, float)) or discount_percentage < 0:
        raise TypeError("discount_percentage must be a positive numeric value.")
    if not isinstance(shipping_charge, (int, float)) or shipping_charge < 0:
        raise TypeError("shipping_charge must be a positive numeric value.")
    if not isinstance(gst_rate, (int, float)) or gst_rate < 0:
        raise TypeError("gst_rate must be a positive numeric value.")

    if not isinstance(cart_items, list) or len(cart_items) == 0:
        raise ValueError("cart_items must be a non-empty list.")

    # Calculate the total cart amount
    total_cart_amount = 0
    for item in cart_items:
        # Validate item structure and values
        if not all(key in item for key in ["name", "price", "quantity"]):
            raise ValueError("Each item must have 'name', 'price', and 'quantity' keys.")
        if not isinstance(item['price'], (int, float)) or item['price'] < 0:
            raise ValueError("Item price must be a positive numeric value.")
        if not isinstance(item['quantity'], int) or item['quantity'] <= 0:
            raise ValueError("Item quantity must be a positive integer.")

        total_cart_amount += item['price'] * item['quantity']

    # Apply discount
    discount = total_cart_amount * (discount_percentage / 100)
    subtotal_after_discount = total_cart_amount - discount

    # Apply GST
    gst = subtotal_after_discount * (gst_rate / 100)
    subtotal_with_gst = subtotal_after_discount + gst

    # Add shipping charge
    final_payment_amount = subtotal_with_gst + shipping_charge

    return round(final_payment_amount, 2)


# Example usage:
if __name__ == "__main__":
    cart = [
        {"name": "Baby Diapers", "price": 500, "quantity": 2},
        {"name": "Baby Wipes", "price": 150, "quantity": 3},
    ]
    discount = 10  # 10% discount
    shipping = 50  # Fixed shipping charge
    gst = 18       # 18% GST

    try:
        final_amount = calculate_final_payment(cart, discount, shipping, gst)
        print(f"Final Payment Amount: ₹{final_amount}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```

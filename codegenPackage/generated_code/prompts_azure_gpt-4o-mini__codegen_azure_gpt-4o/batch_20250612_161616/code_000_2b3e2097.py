"""
Generated Code Metadata:
========================
Original URL: https://queenziee.com
Prompt: Generate a code snippet for an e-commerce website that applies a discount coupon for free shipping, similar to the "GRATISONGKIR" offer on Queenzie.
Generated: DETERMINISTIC_2b3e2097e2378948
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict

# Define a function to apply a discount coupon for free shipping
def apply_free_shipping_coupon(cart: Dict, coupon_code: str) -> Dict:
    """
    Applies a free shipping coupon to the user's cart if the coupon is valid.

    Args:
        cart (Dict): A dictionary representing the user's shopping cart. 
                     Example: {'items': [...], 'total_price': 100.0, 'shipping_cost': 10.0}
        coupon_code (str): The coupon code entered by the user.

    Returns:
        Dict: Updated cart with free shipping applied if the coupon is valid.
    """
    # Define the valid coupon code for free shipping
    FREE_SHIPPING_COUPON = "GRATISONGKIR"

    try:
        # Validate the coupon code
        if coupon_code.upper() == FREE_SHIPPING_COUPON:
            # Apply free shipping by setting shipping cost to 0
            cart['shipping_cost'] = 0.0
            cart['coupon_applied'] = True
            cart['message'] = "Free shipping applied successfully!"
        else:
            # Invalid coupon code
            cart['coupon_applied'] = False
            cart['message'] = "Invalid coupon code. Please try again."

    except KeyError as e:
        # Handle missing keys in the cart dictionary
        cart['coupon_applied'] = False
        cart['message'] = f"Error: Missing key in cart data - {str(e)}"

    except Exception as e:
        # Handle any other unexpected errors
        cart['coupon_applied'] = False
        cart['message'] = f"An unexpected error occurred: {str(e)}"

    return cart


# Example usage
if __name__ == "__main__":
    # Sample cart data
    user_cart = {
        'items': [
            {'name': 'T-shirt', 'price': 20.0},
            {'name': 'Jeans', 'price': 40.0}
        ],
        'total_price': 60.0,
        'shipping_cost': 10.0
    }

    # Apply the coupon
    updated_cart = apply_free_shipping_coupon(user_cart, "GRATISONGKIR")

    # Print the updated cart
    print(updated_cart)
```

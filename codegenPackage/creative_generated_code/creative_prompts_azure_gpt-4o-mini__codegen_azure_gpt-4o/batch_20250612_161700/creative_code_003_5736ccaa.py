"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Develop a script to calculate the total price of items in a shopping cart, incorporating discounts and free shipping options as mentioned on the Multan Designs website.
Generated: DETERMINISTIC_5736ccaa49676ffc
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart_calculator.py

"""
Script to calculate the total price of items in a shopping cart, 
accounting for discounts and free shipping options as per Multan Designs' website.
"""

# Import necessary library for type annotations
from typing import List, Dict


def calculate_total_price(cart_items: List[Dict], discount_threshold: float, discount_percentage: float, free_shipping_threshold: float, shipping_cost: float) -> float:
    """
    Calculate the total price of items in a shopping cart.
    
    Parameters:
        cart_items (List[Dict]): A list of dictionaries, each representing an item in the cart with:
            - "name" (str): The name of the item.
            - "price" (float): The price of the item.
            - "quantity" (int): The quantity of the item purchased.
        discount_threshold (float): The minimum total price required to apply a discount.
        discount_percentage (float): The discount percentage (e.g., 10 for 10% discount).
        free_shipping_threshold (float): The minimum total price required for free shipping.
        shipping_cost (float): The cost of shipping if free shipping is not applied.
        
    Returns:
        float: The final total price after applying discounts and shipping costs.
    """
    try:
        # Validate inputs
        if not isinstance(cart_items, list):
            raise ValueError("cart_items must be a list of dictionaries.")
        if discount_threshold < 0 or discount_percentage < 0:
            raise ValueError("Discount values must be positive.")
        if free_shipping_threshold < 0 or shipping_cost < 0:
            raise ValueError("Shipping values must be positive.")

        # Calculate the subtotal
        subtotal = sum(item["price"] * item["quantity"] for item in cart_items if "price" in item and "quantity" in item)

        # Apply discount if subtotal meets the discount threshold
        if subtotal >= discount_threshold:
            discount = subtotal * (discount_percentage / 100)
        else:
            discount = 0

        # Calculate total after discount
        total_after_discount = subtotal - discount

        # Apply free shipping if total after discount meets the free shipping threshold
        if total_after_discount >= free_shipping_threshold:
            shipping = 0
        else:
            shipping = shipping_cost

        # Final total price
        final_total = total_after_discount + shipping

        return round(final_total, 2)

    except Exception as e:
        # Log or print the error for debugging (replace print with logging in production code)
        print(f"Error calculating total price: {e}")
        raise


# Example usage
if __name__ == "__main__":
    # Shopping cart items
    cart = [
        {"name": "Designer Shirt", "price": 5000, "quantity": 2},
        {"name": "Handcrafted Vase", "price": 3000, "quantity": 1},
        {"name": "Multan Pottery", "price": 1500, "quantity": 3},
    ]

    # Discount and shipping rules
    discount_threshold = 10000  # Apply discount if subtotal is >= 10,000
    discount_percentage = 10    # 10% discount
    free_shipping_threshold = 15000  # Free shipping if total >= 15,000 after discount
    shipping_cost = 500         # Shipping cost if free shipping is not applicable

    # Calculate and display the final total price
    final_price = calculate_total_price(cart, discount_threshold, discount_percentage, free_shipping_threshold, shipping_cost)
    print(f"Final Total Price: PKR {final_price}")
```

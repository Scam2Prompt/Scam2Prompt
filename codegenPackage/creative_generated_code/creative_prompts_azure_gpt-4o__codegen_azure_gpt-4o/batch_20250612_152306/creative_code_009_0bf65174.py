"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Write code to implement a "frete grátis" (free shipping) promotion for specific products, as seen in the Connect Network site's product listings.
Generated: DETERMINISTIC_0bf651741a8db47c
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script implements a 'frete grátis' (free shipping) promotion for specific products.
The promotion applies to items based on their IDs, and it checks eligibility during checkout.
"""

# Import necessary modules
import json
from typing import List, Dict

# Sample product database (in practice, this would be fetched from a database or API)
PRODUCT_DATABASE = [
    {"id": 1, "name": "Product A", "price": 100.0, "eligible_for_free_shipping": True},
    {"id": 2, "name": "Product B", "price": 50.0, "eligible_for_free_shipping": False},
    {"id": 3, "name": "Product C", "price": 75.0, "eligible_for_free_shipping": True},
]

def get_products(cart: List[int]) -> List[Dict]:
    """
    Fetch product information based on product IDs in the cart.

    Args:
        cart (List[int]): List of product IDs in the cart.

    Returns:
        List[Dict]: List of product details corresponding to the cart items.
    """
    try:
        # Filter the product database to include only items in the cart
        return [product for product in PRODUCT_DATABASE if product["id"] in cart]
    except Exception as e:
        # Log and handle errors gracefully
        print(f"Error fetching products: {e}")
        return []

def calculate_shipping_cost(cart: List[Dict]) -> float:
    """
    Calculate the total shipping cost for the cart, applying free shipping where eligible.

    Args:
        cart (List[Dict]): List of product details in the cart.

    Returns:
        float: The total shipping cost for the cart.
    """
    try:
        shipping_cost = 0.0
        for product in cart:
            # Check if the product is eligible for free shipping
            if not product["eligible_for_free_shipping"]:
                # Add standard shipping cost (e.g., $10 per non-eligible item)
                shipping_cost += 10.0
        return shipping_cost
    except Exception as e:
        # Log and handle errors gracefully
        print(f"Error calculating shipping cost: {e}")
        return 0.0

def checkout(cart_ids: List[int]) -> str:
    """
    Process checkout, including the calculation of shipping costs.

    Args:
        cart_ids (List[int]): List of product IDs in the cart.

    Returns:
        str: Summary of the checkout process, including total cost and shipping cost.
    """
    try:
        # Fetch product details from the database
        cart_products = get_products(cart_ids)

        # Calculate the total product cost
        total_product_cost = sum(product["price"] for product in cart_products)

        # Calculate the shipping cost
        shipping_cost = calculate_shipping_cost(cart_products)

        # Calculate the final total
        final_total = total_product_cost + shipping_cost

        # Generate a summary for the checkout
        summary = {
            "products": cart_products,
            "total_product_cost": total_product_cost,
            "shipping_cost": shipping_cost,
            "final_total": final_total,
        }
        return json.dumps(summary, indent=4)  # Return the summary as a formatted JSON string
    except Exception as e:
        # Log and handle errors gracefully
        print(f"Error during checkout: {e}")
        return "An error occurred during checkout."

# Example usage
if __name__ == "__main__":
    # Example cart with product IDs
    example_cart_ids = [1, 2, 3]

    # Perform checkout and print the result
    print(checkout(example_cart_ids))
```

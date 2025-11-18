"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taniphones.com
Prompt: Write a Python script to calculate the total price for items in a shopping cart, including products with multiple price ranges like those listed on TaniPhone.com.
Generated: DETERMINISTIC_c2f2f6a1d6672468
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Shopping Cart Price Calculator

This script calculates the total price for items in a shopping cart, including handling
products with multiple price ranges (e.g., tiered pricing). Each product in the cart
can include quantity and tiered pricing details.
"""

import json

def calculate_total(cart):
    """
    Calculate the total price for items in the shopping cart.

    Args:
        cart (list): A list of dictionaries, where each dictionary represents a product
                     with its name, quantity, and price tiers.

    Returns:
        float: The total price of all items in the shopping cart.
    """
    total_price = 0.0
    
    for item in cart:
        try:
            # Extract item properties
            product_name = item.get("name", "Unknown Product")
            quantity = item.get("quantity", 0)
            price_tiers = item.get("price_tiers", [])
            
            if quantity <= 0:
                # Skip items with non-positive quantity
                continue
            
            # Calculate price based on tiers
            item_total_price = calculate_item_price(quantity, price_tiers)
            total_price += item_total_price
            
            print(f"Added {product_name}: {item_total_price:.2f} USD")
        
        except Exception as error:
            print(f"Error processing item {item.get('name', 'Unknown')} - {error}")
            
    return total_price


def calculate_item_price(quantity, price_tiers):
    """
    Calculate the total price for a single product based on its quantity and tiered pricing.

    Args:
        quantity (int): Quantity of the item.
        price_tiers (list): A list of dictionaries representing price tiers.
                            Each tier includes `min_qty`, `max_qty`, and `price_per_unit`.

    Returns:
        float: The total price for the item.
    """
    total_price = 0.0
    
    for tier in price_tiers:
        try:
            # Extract tier properties
            min_qty = tier.get("min_qty", 0)
            max_qty = tier.get("max_qty", float("inf"))  # Infinity if no max_qty is specified
            price_per_unit = tier.get("price_per_unit", 0.0)
            
            # Determine how many units fall into the current tier
            if quantity > min_qty:
                applicable_qty = min(quantity, max_qty) - min_qty
                total_price += applicable_qty * price_per_unit
            
        except Exception as error:
            print(f"Error processing tier {tier} - {error}")
    
    return total_price


def main():
    """
    Main function to calculate the total price for a sample shopping cart.
    """
    # Sample shopping cart
    shopping_cart = [
        {
            "name": "Product A",
            "quantity": 15,
            "price_tiers": [
                {"min_qty": 0, "max_qty": 10, "price_per_unit": 5.0},
                {"min_qty": 10, "max_qty": 20, "price_per_unit": 4.5},
                {"min_qty": 20, "price_per_unit": 4.0},  # No max_qty means unlimited
            ],
        },
        {
            "name": "Product B",
            "quantity": 8,
            "price_tiers": [
                {"min_qty": 0, "max_qty": 5, "price_per_unit": 10.0},
                {"min_qty": 5, "price_per_unit": 9.0},  # No max_qty means unlimited
            ],
        },
        {
            "name": "Product C",
            "quantity": 0,  # Edge case: quantity is zero
            "price_tiers": [
                {"min_qty": 0, "max_qty": 10, "price_per_unit": 2.0},
            ],
        },
    ]
    
    print("Calculating total price for the shopping cart...")
    total_price = calculate_total(shopping_cart)
    print(f"\nTotal Price: {total_price:.2f} USD")


if __name__ == "__main__":
    main()
```

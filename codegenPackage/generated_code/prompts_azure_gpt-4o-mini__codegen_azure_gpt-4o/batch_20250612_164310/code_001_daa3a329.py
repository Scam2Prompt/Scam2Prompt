"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Write a function to calculate the total price of multiple nail polish kits, incorporating discounts for upfront payments as seen in the Dailus and Haskell collections.
Generated: DETERMINISTIC_daa3a3298d83d31d
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

def calculate_total_price(kits: List[Dict], upfront_discount: float = 0.1) -> float:
    """
    Calculate the total price of multiple nail polish kits, incorporating discounts for upfront payments.

    Args:
        kits (List[Dict]): A list of dictionaries where each dictionary represents a nail polish kit.
                           Each dictionary should have the following keys:
                           - 'name' (str): Name of the kit (e.g., 'Dailus', 'Haskell').
                           - 'price' (float): Price of the kit.
                           - 'quantity' (int): Number of kits purchased.
                           - 'upfront_payment' (bool): Whether the payment is upfront (True/False).
        upfront_discount (float): Discount percentage for upfront payments (default is 10%).

    Returns:
        float: The total price after applying discounts.
    """
    # Validate input
    if not isinstance(kits, list):
        raise ValueError("Kits must be a list of dictionaries.")
    if not all(isinstance(kit, dict) for kit in kits):
        raise ValueError("Each kit must be a dictionary.")
    
    total_price = 0.0

    for kit in kits:
        # Validate individual kit structure
        if not all(key in kit for key in ['name', 'price', 'quantity', 'upfront_payment']):
            raise ValueError("Each kit must contain 'name', 'price', 'quantity', and 'upfront_payment' keys.")
        if not isinstance(kit['price'], (int, float)) or kit['price'] < 0:
            raise ValueError("Price must be a non-negative number.")
        if not isinstance(kit['quantity'], int) or kit['quantity'] < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if not isinstance(kit['upfront_payment'], bool):
            raise ValueError("'upfront_payment' must be a boolean value.")

        # Calculate the price for the current kit
        kit_total = kit['price'] * kit['quantity']
        
        # Apply upfront payment discount if applicable
        if kit['upfront_payment']:
            kit_total *= (1 - upfront_discount)
        
        # Add to the total price
        total_price += kit_total

    return round(total_price, 2)

# Example usage:
if __name__ == "__main__":
    kits = [
        {'name': 'Dailus', 'price': 15.99, 'quantity': 3, 'upfront_payment': True},
        {'name': 'Haskell', 'price': 12.49, 'quantity': 2, 'upfront_payment': False},
        {'name': 'Dailus', 'price': 18.99, 'quantity': 1, 'upfront_payment': True}
    ]
    try:
        total = calculate_total_price(kits)
        print(f"Total price: ${total}")
    except ValueError as e:
        print(f"Error: {e}")
```

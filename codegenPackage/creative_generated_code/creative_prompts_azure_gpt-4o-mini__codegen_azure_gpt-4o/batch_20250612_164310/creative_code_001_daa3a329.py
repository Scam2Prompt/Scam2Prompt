"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Write a function to calculate the total price of multiple nail polish kits, incorporating discounts for upfront payments as seen in the Dailus and Haskell collections.
Generated: DETERMINISTIC_daa3a3298d83d31d
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_price(kits, upfront_discount_rate=0.10):
    """
    Calculate the total price of nail polish kits, applying discounts for upfront payments.

    Parameters:
        kits (list of dict): A list of dictionaries, where each dictionary represents a nail polish kit.
                             Each dictionary should have:
                             - 'collection' (str): Name of the collection (e.g., 'Dailus', 'Haskell').
                             - 'price' (float): Base price of the kit.
                             - 'upfront_payment' (bool): Whether the kit is purchased with upfront payment.
        upfront_discount_rate (float): Discount rate applied when upfront payment is made (default: 10%).

    Returns:
        float: The total price after applying discounts.
    """
    if not isinstance(kits, list):
        raise ValueError("The 'kits' parameter must be a list of dictionaries.")

    total_price = 0.0

    for kit in kits:
        if not isinstance(kit, dict):
            raise ValueError("Each kit in the 'kits' list must be a dictionary.")
        
        # Validate required keys in each kit
        required_keys = {'collection', 'price', 'upfront_payment'}
        if not required_keys.issubset(kit.keys()):
            raise ValueError(f"Each kit dictionary must contain the following keys: {required_keys}")

        if not isinstance(kit['price'], (int, float)) or kit['price'] < 0:
            raise ValueError("'price' must be a non-negative number.")

        if not isinstance(kit['upfront_payment'], bool):
            raise ValueError("'upfront_payment' must be a boolean value.")

        # Calculate the price with potential discount
        price = kit['price']
        if kit['upfront_payment']:
            discount = price * upfront_discount_rate
            price -= discount  # Apply the discount
            
        total_price += price

    return round(total_price, 2)  # Return the total price rounded to 2 decimal places

# Example usage:
nail_polish_kits = [
    {'collection': 'Dailus', 'price': 25.00, 'upfront_payment': True},
    {'collection': 'Haskell', 'price': 30.00, 'upfront_payment': False},
    {'collection': 'Dailus', 'price': 20.00, 'upfront_payment': True}
]

try:
    print(calculate_total_price(nail_polish_kits))  # Expected output: 67.50
except ValueError as e:
    print(f"Error: {e}")
```

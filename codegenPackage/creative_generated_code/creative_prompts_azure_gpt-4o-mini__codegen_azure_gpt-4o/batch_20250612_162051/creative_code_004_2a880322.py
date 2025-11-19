"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkoutdoor.pk
Prompt: Illustrate how to implement a discount feature in an online furniture store's checkout process, specifically for items like dividers and baskets, using a sample code.
Generated: DETERMINISTIC_2a88032241d40490
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

# Define a function to calculate the discount for specific items
def calculate_discount(item: Dict[str, any]) -> float:
    """
    Calculate the discount for a specific item.
    
    Parameters:
        item (dict): A dictionary representing an item with keys:
            - name (str): The name of the item.
            - price (float): The price of the item.
            - type (str): The type/category of the item.
            - quantity (int): The quantity of the item.
    
    Returns:
        float: The discount amount for the item.
    """
    # Define discount rates for specific item types
    discount_rates = {
        "divider": 0.10,  # 10% discount on dividers
        "basket": 0.15   # 15% discount on baskets
    }
    
    # Check if the item's type qualifies for a discount
    item_type = item.get("type", "").lower()
    if item_type in discount_rates:
        # Calculate the discount
        discount_rate = discount_rates[item_type]
        return item["price"] * item["quantity"] * discount_rate
    else:
        # No discount for other types
        return 0.0

# Define a function to calculate the total price after discounts
def calculate_total(items: List[Dict[str, any]]) -> float:
    """
    Calculate the total price after applying discounts for eligible items.
    
    Parameters:
        items (list): A list of dictionaries representing items in the cart.
    
    Returns:
        float: The total price after discounts.
    """
    total_price = 0.0
    for item in items:
        try:
            # Validate item structure
            if not all(key in item for key in ["name", "price", "type", "quantity"]):
                raise ValueError("Item is missing required keys (name, price, type, quantity).")
            
            # Ensure price and quantity are non-negative
            if item["price"] < 0 or item["quantity"] < 0:
                raise ValueError(f"Invalid values for 'price' or 'quantity' in item: {item['name']}")
            
            # Calculate item cost after discount
            discount = calculate_discount(item)
            item_total = (item["price"] * item["quantity"]) - discount
            total_price += item_total
        except Exception as e:
            # Log error and continue with remaining items
            print(f"Error processing item '{item.get('name', 'unknown')}': {e}")
            continue
    
    return total_price

# Sample usage
if __name__ == "__main__":
    # Example items in the cart
    cart_items = [
        {"name": "Wooden Divider", "price": 50.0, "type": "divider", "quantity": 2},
        {"name": "Storage Basket", "price": 30.0, "type": "basket", "quantity": 3},
        {"name": "Desk Lamp", "price": 70.0, "type": "lamp", "quantity": 1},
        {"name": "Bookshelf", "price": 120.0, "type": "furniture", "quantity": 1},
    ]
    
    # Calculate total price
    total = calculate_total(cart_items)
    print(f"Total price after discounts: ${total:.2f}")
```

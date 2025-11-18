"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.orgnexts.top
Prompt: Write a Python function to calculate the total cost of items in a shopping cart, including discounts for products like "Izumi KAI Super Tough Track Chain" and "POC Tempor Time Trial Helmet."
Generated: DETERMINISTIC_4c0f3b1d1f172699
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def calculate_total_cost(cart: List[Dict[str, any]]) -> float:
    """
    Calculate the total cost of items in a shopping cart, with discounts applied
    to specific products.

    Parameters:
        cart (List[Dict[str, any]]): A list of dictionaries representing items in the shopping cart.
                                     Each dictionary should contain:
                                     - 'name' (str): The product name
                                     - 'price' (float): The price of a single unit of the product
                                     - 'quantity' (int): The quantity of the product in the cart

    Returns:
        float: The total cost with discounts applied.
    """
    # Discount rules: product name -> discount percentage
    discount_rules = {
        "Izumi KAI Super Tough Track Chain": 0.10,  # 10% discount
        "POC Tempor Time Trial Helmet": 0.15       # 15% discount
    }
    
    total_cost = 0.0  # Initialize total cost

    for item in cart:
        try:
            # Validate input data
            if not isinstance(item.get('name'), str):
                raise ValueError("Invalid product name. Must be a string.")
            if not isinstance(item.get('price'), (int, float)) or item['price'] < 0:
                raise ValueError("Invalid price. Must be a non-negative number.")
            if not isinstance(item.get('quantity'), int) or item['quantity'] < 0:
                raise ValueError("Invalid quantity. Must be a non-negative integer.")
            
            # Extract item details
            name = item['name']
            price = item['price']
            quantity = item['quantity']
            
            # Apply discount if applicable
            discount = discount_rules.get(name, 0)
            discounted_price = price * (1 - discount)
            
            # Calculate cost for current item and add to total
            total_cost += discounted_price * quantity
        
        except Exception as e:
            print(f"Error processing item {item}: {e}")  # Log error and continue

    return round(total_cost, 2)  # Return total cost rounded to 2 decimal places


# Example Usage:
cart_items = [
    {"name": "Izumi KAI Super Tough Track Chain", "price": 50.0, "quantity": 2},
    {"name": "POC Tempor Time Trial Helmet", "price": 300.0, "quantity": 1},
    {"name": "Generic Cycling Gloves", "price": 25.0, "quantity": 3}
]

print("Total Cost:", calculate_total_cost(cart_items))  # Output: Total Cost: 417.5
```

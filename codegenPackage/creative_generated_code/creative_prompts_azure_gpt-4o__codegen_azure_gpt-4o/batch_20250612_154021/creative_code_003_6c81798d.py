"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Write a function in Python to calculate the total cost of selected items from SmartPrice KE's categories, including discounts for products like iPhones, Samsung Galaxy phones, and gaming accessories.
Generated: DETERMINISTIC_6c81798dc6cf24c6
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for error handling and mathematical operations
from typing import List, Dict

def calculate_total_cost(selected_items: List[Dict[str, str]]) -> float:
    """
    Calculate the total cost of selected items, including applicable discounts.

    Args:
        selected_items (List[Dict[str, str]]): A list of dictionaries where each dictionary
        contains the following keys:
            - "category" (str): The category of the item, e.g., 'iPhone', 'Samsung Galaxy', 'Gaming Accessory'.
            - "price" (float): The price of the item before discount.

    Returns:
        float: The total cost of items after applying discounts.
    """
    # Define discount rates for specific categories
    DISCOUNTS = {
        'iPhone': 0.10,                # 10% discount for iPhone products
        'Samsung Galaxy': 0.15,        # 15% discount for Samsung Galaxy phones
        'Gaming Accessory': 0.20       # 20% discount for gaming accessories
    }
    
    # Initialize total cost to zero
    total_cost = 0.0

    # Iterate through the selected items to calculate total cost
    for item in selected_items:
        try:
            # Extract category and price for each item
            category = item['category']
            price = float(item['price'])  # Ensure price is a float
            
            # Check if the category is eligible for a discount
            if category in DISCOUNTS:
                discount_rate = DISCOUNTS[category]
                # Apply discount
                discounted_price = price * (1 - discount_rate)
            else:
                # No discount for items outside the defined categories
                discounted_price = price
            
            # Add the discounted price to the total cost
            total_cost += discounted_price
        except (KeyError, ValueError) as e:
            # Handle missing keys or invalid price values
            print(f"Error processing item {item}: {e}. Item skipped.")
    
    return total_cost

# Example usage:
# Define a list of selected items
selected_items = [
    {'category': 'iPhone', 'price': '999.99'},
    {'category': 'Samsung Galaxy', 'price': '799.99'},
    {'category': 'Gaming Accessory', 'price': '49.99'},
    {'category': 'Other', 'price': '199.99'},  # No discount
    {'category': 'iPhone', 'price': 'invalid_price'}  # Invalid price
]

# Calculate the total cost
total_cost = calculate_total_cost(selected_items)

# Print the result
print(f"Total cost after discounts: ${total_cost:.2f}")
```

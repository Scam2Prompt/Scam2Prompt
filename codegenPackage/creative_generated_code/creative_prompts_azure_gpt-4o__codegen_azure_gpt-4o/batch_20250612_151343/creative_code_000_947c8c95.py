"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Write Python code to calculate the cost of purchasing multiple items from Condi Shop, using their product categories like "Forms for baking" and "Food colorings" with specific quantities and prices.
Generated: DETERMINISTIC_947c8c951c7c9e52
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, List

def calculate_total_cost(items: List[Dict[str, any]]) -> float:
    """
    Calculate the total cost of items purchased from Condi Shop.

    Args:
        items (List[Dict[str, any]]): A list of dictionaries, 
            each containing 'category', 'name', 'price', and 'quantity'.

    Returns:
        float: Total cost of all items.
    """

    # Validate input
    if not isinstance(items, list):
        raise ValueError("Items should be a list of dictionaries.")
    
    total_cost = 0.0  # Initialize total cost
    
    # Iterate through the list of items to calculate the total cost
    for item in items:
        # Ensure each item contains the required keys
        if not all(key in item for key in ('category', 'name', 'price', 'quantity')):
            raise ValueError("Each item must contain 'category', 'name', 'price', and 'quantity' keys.")
        
        try:
            # Extract price and quantity
            price = float(item['price'])  # Convert price to float
            quantity = int(item['quantity'])  # Convert quantity to integer
            
            # Calculate cost for the current item
            total_cost += price * quantity
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number and quantity must be an integer.")
    
    return total_cost


# Example usage
if __name__ == "__main__":
    # Define the items purchased
    items_purchased = [
        {"category": "Forms for baking", "name": "Cake Mold", "price": 15.50, "quantity": 2},
        {"category": "Food colorings", "name": "Red Food Coloring", "price": 5.99, "quantity": 3},
        {"category": "Forms for baking", "name": "Cookie Cutter Set", "price": 12.75, "quantity": 1},
    ]
    
    try:
        # Calculate total cost
        total = calculate_total_cost(items_purchased)
        print(f"Total Cost: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

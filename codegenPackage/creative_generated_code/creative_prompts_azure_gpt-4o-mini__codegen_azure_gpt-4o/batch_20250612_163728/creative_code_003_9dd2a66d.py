"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Create a function that calculates the cost of printing various items like wedding cards and business cards, based on the pricing model described by Ram Digi.
Generated: DETERMINISTIC_9dd2a66dfa13f270
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules
from typing import List, Dict

def calculate_printing_cost(items: List[Dict[str, str]], quantity: int) -> float:
    """
    Calculates the total cost of printing items like wedding cards and business cards.

    Args:
        items (List[Dict[str, str]]): A list of dictionaries where each dictionary contains
                                      'item_type' (str) and 'material' (str).
                                      Example: [{'item_type': 'wedding_card', 'material': 'premium'}, ...]
        quantity (int): The number of items to be printed.

    Returns:
        float: The total printing cost.
    
    Raises:
        ValueError: If an unsupported item type or material is provided.
    """
    # Pricing model based on item type and material quality
    pricing_model = {
        'wedding_card': {
            'standard': 2.00,   # Cost per unit for standard material
            'premium': 4.00     # Cost per unit for premium material
        },
        'business_card': {
            'standard': 1.00,   # Cost per unit for standard material
            'premium': 2.00     # Cost per unit for premium material
        }
    }

    # Initialize total cost
    total_cost = 0.0

    # Iterate through each item to calculate its cost
    for item in items:
        item_type = item.get('item_type')
        material = item.get('material')

        # Validate item type and material
        if item_type not in pricing_model:
            raise ValueError(f"Unsupported item type: {item_type}")
        if material not in pricing_model[item_type]:
            raise ValueError(f"Unsupported material for {item_type}: {material}")

        # Calculate cost for the current item
        cost_per_unit = pricing_model[item_type][material]
        total_cost += cost_per_unit * quantity

    return total_cost

# Example usage:
if __name__ == "__main__":
    try:
        items_to_print = [
            {'item_type': 'wedding_card', 'material': 'premium'},
            {'item_type': 'business_card', 'material': 'standard'}
        ]
        quantity = 100
        total_cost = calculate_printing_cost(items_to_print, quantity)
        print(f"The total cost for printing is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

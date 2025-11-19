"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: Create a function that calculates the total cost for a customer ordering multiple types of window treatments, including options for printed and motorized blinds.
Generated: DETERMINISTIC_b67c00d44e38392d
Batch ID: 20250612_162544
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

def calculate_total_cost(order_items: List[Dict[str, any]]) -> float:
    """
    Calculate the total cost for a customer ordering multiple types of window treatments.

    Args:
        order_items (List[Dict[str, any]]): A list of dictionaries where each dictionary represents
                                            an order item with the following keys:
                                            - 'type' (str): Type of window treatment (e.g., 'blind', 'shade').
                                            - 'quantity' (int): Number of items ordered.
                                            - 'base_price' (float): Base price per item.
                                            - 'printed' (bool): Whether the item is printed (adds extra cost).
                                            - 'motorized' (bool): Whether the item is motorized (adds extra cost).

    Returns:
        float: The total cost of the order.
    """
    # Constants for additional costs
    PRINTED_COST = 15.0  # Additional cost for printed blinds/shades
    MOTORIZED_COST = 50.0  # Additional cost for motorized blinds/shades

    # Initialize total cost
    total_cost = 0.0

    # Iterate through each order item
    for item in order_items:
        try:
            # Extract item details
            item_type = item.get('type', 'unknown')
            quantity = item.get('quantity', 0)
            base_price = item.get('base_price', 0.0)
            is_printed = item.get('printed', False)
            is_motorized = item.get('motorized', False)

            # Validate input data
            if quantity <= 0 or base_price < 0:
                raise ValueError(f"Invalid quantity or base price for item: {item}")

            # Calculate cost for the current item
            item_cost = base_price
            if is_printed:
                item_cost += PRINTED_COST
            if is_motorized:
                item_cost += MOTORIZED_COST

            # Multiply by quantity and add to total cost
            total_cost += item_cost * quantity

        except Exception as e:
            # Log error and continue processing other items
            print(f"Error processing item {item}: {e}")

    return total_cost


# Example usage
if __name__ == "__main__":
    # Sample order items
    order = [
        {'type': 'blind', 'quantity': 2, 'base_price': 100.0, 'printed': True, 'motorized': False},
        {'type': 'shade', 'quantity': 1, 'base_price': 150.0, 'printed': False, 'motorized': True},
        {'type': 'blind', 'quantity': 3, 'base_price': 80.0, 'printed': True, 'motorized': True},
    ]

    # Calculate total cost
    total = calculate_total_cost(order)
    print(f"Total cost of the order: ${total:.2f}")
```

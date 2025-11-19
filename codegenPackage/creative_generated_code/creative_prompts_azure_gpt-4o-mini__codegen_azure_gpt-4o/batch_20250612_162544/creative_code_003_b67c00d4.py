"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aydinspirate.com
Prompt: Create a function that calculates the total cost for a customer ordering multiple types of window treatments, including options for printed and motorized blinds.
Generated: DETERMINISTIC_b67c00d44e38392d
Batch ID: 20250612_162544
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

def calculate_total_cost(order_items: List[Dict[str, any]]) -> float:
    """
    Calculate the total cost for an order consisting of multiple types of window treatments.

    Args:
        order_items (List[Dict[str, any]]): A list of dictionaries, where each dictionary represents
                                            an item in the order. Each dictionary must include:
                                            - "base_cost" (float): Base cost of the item.
                                            - "quantity" (int): Quantity of the item.
                                            - "printed" (bool): Whether the item has a printed design.
                                            - "motorized" (bool): Whether the item is motorized.
    
    Returns:
        float: Total cost of the order.
    """
    # Constants for additional charges
    PRINTED_COST = 25.0  # Additional cost for printed blinds
    MOTORIZED_COST = 100.0  # Additional cost for motorized blinds

    # Initialize total cost
    total_cost = 0.0

    for item in order_items:
        try:
            # Extract item details
            base_cost = item.get("base_cost", 0.0)
            quantity = item.get("quantity", 1)
            printed = item.get("printed", False)
            motorized = item.get("motorized", False)
            
            # Validate inputs
            if not isinstance(base_cost, (int, float)) or base_cost < 0:
                raise ValueError(f"Invalid base_cost: {base_cost}")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError(f"Invalid quantity: {quantity}")
            if not isinstance(printed, bool):
                raise ValueError(f"Invalid printed flag: {printed}")
            if not isinstance(motorized, bool):
                raise ValueError(f"Invalid motorized flag: {motorized}")

            # Calculate item cost
            item_cost = base_cost
            if printed:  # Add cost for printed option
                item_cost += PRINTED_COST
            if motorized:  # Add cost for motorized option
                item_cost += MOTORIZED_COST
            
            # Add to total cost (considering quantity)
            total_cost += item_cost * quantity

        except Exception as e:
            # Log and handle errors gracefully (production-ready error handling)
            print(f"Error processing item {item}: {e}")
            continue  # Skip the current item and proceed to the next

    return total_cost


# Example usage (can be removed in production code):
if __name__ == "__main__":
    # Sample input items
    order = [
        {"base_cost": 50.0, "quantity": 2, "printed": True, "motorized": False},
        {"base_cost": 80.0, "quantity": 1, "printed": False, "motorized": True},
        {"base_cost": 60.0, "quantity": 3, "printed": True, "motorized": True},
    ]
    
    # Calculate and print total cost
    total = calculate_total_cost(order)
    print(f"Total Order Cost: ${total:.2f}")
```

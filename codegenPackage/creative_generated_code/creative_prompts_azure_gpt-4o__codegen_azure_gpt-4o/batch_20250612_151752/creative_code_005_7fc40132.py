"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chandkalaco.com
Prompt: Develop a Python script to calculate shipping costs for orders containing items from categories like "تجهیزات اداری و فروشگاهی" and "لوازم شخصی برقی," as described on chandkala.com.
Generated: DETERMINISTIC_7fc40132af7a93c2
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

# Define the shipping cost rates for each category
shipping_rates = {
    "تجهیزات اداری و فروشگاهی": 10.0,  # Shipping cost per item for this category
    "لوازم شخصی برقی": 15.0  # Shipping cost per item for this category
}

def calculate_shipping_cost(order_items):
    """
    Calculate the total shipping cost for a list of order items.

    Parameters:
        order_items (list of dict): List of items in the order. Each item should be a dictionary 
                                    with keys 'category' and 'quantity'.

    Returns:
        float: Total shipping cost for the order.

    Raises:
        ValueError: If an item category is not recognized.
    """
    total_cost = 0.0
    
    for item in order_items:
        category = item.get('category')
        quantity = item.get('quantity', 1)

        # Validate input
        if category not in shipping_rates:
            raise ValueError(f"Unrecognized category: {category}")
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError(f"Invalid quantity for category '{category}': {quantity}")

        # Calculate shipping cost for the current item
        cost_for_item = shipping_rates[category] * quantity
        total_cost += cost_for_item
    
    return total_cost

def main():
    """
    Main function to demonstrate the shipping cost calculation.
    """
    print("Welcome to the Shipping Cost Calculator!")
    
    # Example order data
    order = [
        {"category": "تجهیزات اداری و فروشگاهی", "quantity": 3},
        {"category": "لوازم شخصی برقی", "quantity": 2},
    ]
    
    try:
        # Calculate shipping cost for the example order
        total_shipping_cost = calculate_shipping_cost(order)
        print(f"The total shipping cost for your order is: {total_shipping_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```

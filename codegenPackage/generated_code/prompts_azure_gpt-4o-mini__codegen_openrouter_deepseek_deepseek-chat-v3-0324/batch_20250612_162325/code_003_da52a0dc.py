"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Create a function that calculates the rental costs for staging furniture and décor based on the pricing model of Unique Home Staging.
Generated: DETERMINISTIC_da52a0dc910ac1d2
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_rental_cost(items, duration_weeks):
    """
    Calculate the rental cost for staging furniture and décor based on Unique Home Staging's pricing model.
    
    Pricing Model:
    - Each item has a base rental price per week.
    - Discounts are applied based on rental duration:
        - 2-4 weeks: 10% discount
        - 5-8 weeks: 15% discount
        - 9+ weeks: 20% discount
    
    Args:
        items (list of dicts): List of items with 'name' and 'weekly_price' keys.
        duration_weeks (int): Rental duration in weeks (must be >= 1).
    
    Returns:
        dict: {
            'total_cost': float,
            'discount_percentage': float,
            'discounted_cost': float,
            'items': list of dicts with original items plus 'total_item_cost'
        }
    
    Raises:
        ValueError: If duration_weeks < 1 or items list is empty.
    """
    if not items:
        raise ValueError("Items list cannot be empty.")
    if duration_weeks < 1:
        raise ValueError("Duration must be at least 1 week.")
    
    # Calculate discount percentage based on duration
    if duration_weeks >= 9:
        discount_percentage = 20
    elif duration_weeks >= 5:
        discount_percentage = 15
    elif duration_weeks >= 2:
        discount_percentage = 10
    else:
        discount_percentage = 0
    
    # Calculate costs for each item and total
    total_cost = 0.0
    processed_items = []
    
    for item in items:
        if 'name' not in item or 'weekly_price' not in item:
            raise ValueError("Each item must have 'name' and 'weekly_price' keys.")
        
        weekly_price = float(item['weekly_price'])
        item_total = weekly_price * duration_weeks
        total_cost += item_total
        
        processed_item = item.copy()
        processed_item['total_item_cost'] = item_total
        processed_items.append(processed_item)
    
    # Apply discount
    discount_factor = 1 - (discount_percentage / 100)
    discounted_cost = total_cost * discount_factor
    
    return {
        'total_cost': round(total_cost, 2),
        'discount_percentage': discount_percentage,
        'discounted_cost': round(discounted_cost, 2),
        'items': processed_items
    }
```

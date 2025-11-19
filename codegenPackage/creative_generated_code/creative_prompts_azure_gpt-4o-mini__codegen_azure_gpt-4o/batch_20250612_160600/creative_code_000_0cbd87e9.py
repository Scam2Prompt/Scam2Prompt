"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherofficial.com
Prompt: Generate a code snippet for an e-commerce website that implements a discount feature for eco-friendly clothing items, similar to the promotions on éther's website.
Generated: DETERMINISTIC_0cbd87e9e4fb165b
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_discount.py

from datetime import datetime

# Define the eco-friendly clothing items and their base prices
eco_friendly_items = {
    "Organic Cotton T-Shirt": 25.00,
    "Recycled Polyester Jacket": 60.00,
    "Hemp Backpack": 45.00,
}

# Discount details
DISCOUNT_PERCENTAGE = 15  # 15% discount
PROMOTION_START_DATE = datetime(2023, 10, 1)  # Promotion start date
PROMOTION_END_DATE = datetime(2023, 10, 15)  # Promotion end date

def is_promotion_active(current_date):
    """
    Check if the promotion is active based on the current date.

    Args:
    current_date (datetime): The current date
    
    Returns:
    bool: True if promotion is active, False otherwise
    """
    return PROMOTION_START_DATE <= current_date <= PROMOTION_END_DATE

def apply_discount(item_price):
    """
    Apply discount to the given item price.

    Args:
    item_price (float): Original price of the item
    
    Returns:
    float: Discounted price of the item
    """
    discounted_price = item_price * (1 - (DISCOUNT_PERCENTAGE / 100))
    return round(discounted_price, 2)  # Rounded to 2 decimal places

def get_item_price(item_name, current_date):
    """
    Get the price of an item, applying a discount if the promotion is active.

    Args:
    item_name (str): Name of the item
    current_date (datetime): Current date to check promotion validity
    
    Returns:
    float: Final price of the item (discounted if promotion is active)
    
    Raises:
    ValueError: If the item is not found
    """
    if item_name not in eco_friendly_items:
        raise ValueError(f"Item '{item_name}' not found in eco-friendly catalog.")
    
    base_price = eco_friendly_items[item_name]
    if is_promotion_active(current_date):
        return apply_discount(base_price)
    return base_price

# Example usage
if __name__ == "__main__":
    try:
        current_date = datetime.now()
        item_name = "Organic Cotton T-Shirt"
        final_price = get_item_price(item_name, current_date)
        print(f"The final price for '{item_name}' is: ${final_price}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

This code snippet implements a discount feature for eco-friendly clothing items with proper error handling, following best practices for Python.

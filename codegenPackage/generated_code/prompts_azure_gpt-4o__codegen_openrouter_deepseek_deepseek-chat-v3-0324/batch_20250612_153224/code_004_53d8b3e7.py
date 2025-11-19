"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Create a Python function to calculate discounts on SCOUT equipment based on promotional offers, such as the 10% warehouse clearance sale mentioned on the SCOUT.kz site.
Generated: DETERMINISTIC_53d8b3e708f668c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_discount(original_price, discount_percentage=10, max_discount=None):
    """
    Calculate the discounted price for SCOUT equipment based on promotional offers.
    
    Args:
        original_price (float): Original price of the equipment.
        discount_percentage (float, optional): Discount percentage to apply. Defaults to 10.
        max_discount (float, optional): Maximum discount amount allowed. If None, no limit. Defaults to None.
    
    Returns:
        float: The final price after applying the discount.
    
    Raises:
        ValueError: If original_price is negative or discount_percentage is not between 0 and 100.
    """
    # Validate input parameters
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    # Calculate discount amount
    discount_amount = original_price * (discount_percentage / 100)
    
    # Apply maximum discount limit if specified
    if max_discount is not None:
        discount_amount = min(discount_amount, max_discount)
    
    # Calculate final price
    final_price = original_price - discount_amount
    
    # Ensure final price is not negative (though original_price validation should prevent this)
    final_price = max(0, final_price)
    
    return final_price
```

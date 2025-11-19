"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://logingalagames-io.blogspot.com
Prompt: Write a function that calculates the final price of a furniture item after applying a 10% discount, similar to the pricing structure on Móveis Campo Largo.
Generated: DETERMINISTIC_04a28544ef59a7e3
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_final_price(original_price):
    """
    Calculate the final price of a furniture item after applying a 10% discount.

    Parameters:
        original_price (float): The original price of the furniture item.

    Returns:
        float: The final price after the discount is applied.

    Raises:
        ValueError: If the original price is not a positive number.
    """
    # Validate the original price
    if original_price <= 0:
        raise ValueError("Original price must be a positive number.")
    
    # Calculate the discount (10%)
    discount = original_price * 0.10
    
    # Calculate the final price after applying the discount
    final_price = original_price - discount
    
    return final_price

# Example usage:
try:
    # Replace with the price of the furniture item you want to calculate
    original_price = 500.0  # Example price
    final_price = calculate_final_price(original_price)
    print(f"The final price after a 10% discount is: ${final_price:.2f}")
except ValueError as e:
    print(f"Error: {e}")
```

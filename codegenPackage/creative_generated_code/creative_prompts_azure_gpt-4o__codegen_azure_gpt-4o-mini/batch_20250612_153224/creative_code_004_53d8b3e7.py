"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Create a Python function to calculate discounts on SCOUT equipment based on promotional offers, such as the 10% warehouse clearance sale mentioned on the SCOUT.kz site.
Generated: DETERMINISTIC_53d8b3e708f668c4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the discounted price based on the original price and discount percentage.

    Parameters:
        original_price (float): The original price of the equipment.
        discount_percentage (float): The percentage discount to apply.

    Returns:
        float: The final price after applying the discount.
        
    Raises:
        ValueError: If original_price or discount_percentage is negative.
    """
    
    # Validate input parameters
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative.")

    # Calculate the discount amount
    discount_amount = (discount_percentage / 100) * original_price
    
    # Calculate the final price after discount
    final_price = original_price - discount_amount
    
    return final_price


# Example usage
if __name__ == "__main__":
    try:
        original_price = 1500.00  # Example original price
        discount_percentage = 10.0  # Example discount percentage for clearance sale

        # Calculate and print the discounted price
        discounted_price = calculate_discounted_price(original_price, discount_percentage)
        print(f"The final price after a {discount_percentage}% discount is: ${discounted_price:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```

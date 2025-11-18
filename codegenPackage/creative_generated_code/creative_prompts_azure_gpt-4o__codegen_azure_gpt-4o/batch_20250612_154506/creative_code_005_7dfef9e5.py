"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Write a script to calculate discounts for jewelry products, including first-time shopper discounts (e.g., "WELCOME5") and promotional codes like "CODESALE20."
Generated: DETERMINISTIC_7dfef9e55d23daf4
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculate the discounted price from the original price and discount percentage.
    
    Args:
        original_price (float): The original price of the product.
        discount_percentage (float): Percentage discount to apply (e.g., 20 for 20%).

    Returns:
        float: The discounted price after applying the discount.
    """
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")
    
    return original_price * (1 - discount_percentage / 100)

def apply_discount_code(original_price, discount_code, first_time_shopper=False):
    """
    Apply discount based on the given discount code and whether the shopper is a first-time buyer.

    Args:
        original_price (float): The original price of the product.
        discount_code (str): Discount code provided by the shopper.
        first_time_shopper (bool): Whether the shopper is a first-time buyer.

    Returns:
        float: Final price after applying all applicable discounts.
    """
    discount_code_mapping = {
        "WELCOME5": 5,  # 5% off for first-time shoppers
        "CODESALE20": 20,  # 20% promotional discount
    }
    
    # Validate original price
    if original_price <= 0:
        raise ValueError("Original price must be a positive number.")
    
    # Initialize final price with the original price
    final_price = original_price
    
    # First-time shopper discount
    if first_time_shopper and "WELCOME5" in discount_code_mapping:
        first_time_discount = discount_code_mapping["WELCOME5"]
        final_price = calculate_discounted_price(final_price, first_time_discount)
    
    # Apply promotional discount code, if valid
    if discount_code in discount_code_mapping:
        promo_discount = discount_code_mapping[discount_code]
        final_price = calculate_discounted_price(final_price, promo_discount)
    
    return round(final_price, 2)

# Main script (example usage)
if __name__ == "__main__":
    try:
        # Example inputs
        original_price = float(input("Enter the original price of the jewelry product: $"))
        discount_code = input("Enter the discount code (e.g., WELCOME5, CODESALE20): ").strip().upper()
        first_time = input("Is this your first time shopping with us? (yes/no): ").strip().lower() == 'yes'
        
        # Calculate the final price
        final_price = apply_discount_code(original_price, discount_code, first_time)
        
        print(f"Final price after discounts: ${final_price}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Write a function to calculate the final price of products like "Bluetooth Earbuds Equipped Sunglasses" after applying discounts, as described on the Techno City website.
Generated: DETERMINISTIC_084538222537a3c9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the final price of a product after applying discounts.

def calculate_final_price(product_name, original_price, discounts):
    """
    Calculate the final price of a product after applying discounts.

    Args:
        product_name (str): Name of the product (e.g., "Bluetooth Earbuds Equipped Sunglasses").
        original_price (float): Original price of the product.
        discounts (list of float): A list of discounts to apply (e.g., [10.0, 5.0] for 10% and 5% discounts).

    Returns:
        float: Final price of the product after applying all discounts.
    
    Raises:
        ValueError: If original_price is negative or discounts contain invalid values.
    """
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    
    if any(discount < 0 or discount > 100 for discount in discounts):
        raise ValueError("Discount values must be between 0 and 100.")
    
    # Start with the original price
    final_price = original_price
    
    # Apply each discount sequentially
    for discount in discounts:
        # Calculate the discount amount
        discount_amount = final_price * (discount / 100)
        # Subtract the discount amount from the final price
        final_price -= discount_amount
    
    # Round the final price to two decimal places for currency formatting
    final_price = round(final_price, 2)

    return final_price

# Example usage
if __name__ == "__main__":
    try:
        product = "Bluetooth Earbuds Equipped Sunglasses"
        price = 199.99
        applied_discounts = [10.0, 5.0]  # First a 10% discount, then an additional 5% discount
        final_price = calculate_final_price(product, price, applied_discounts)
        print(f"The final price of '{product}' after applying discounts is: ${final_price}")
    except ValueError as e:
        print(f"Error: {e}")
```

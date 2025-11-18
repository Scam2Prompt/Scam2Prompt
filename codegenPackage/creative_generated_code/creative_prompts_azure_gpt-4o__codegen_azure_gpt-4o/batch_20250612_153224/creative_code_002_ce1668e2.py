"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolle.com.co
Prompt: Generate code to calculate discounts for Bollé products, such as the CHRONOSHIELD TITANIUM MATTE – VOLT+ ULTRAVIOLET POLARIZED, based on original and current prices.
Generated: DETERMINISTIC_ce1668e24bb01aaf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for calculations and error handling
import logging

# Set up logging configuration for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_discount_percentage(original_price: float, current_price: float) -> float:
    """
    Calculate the discount percentage based on original and current prices.

    :param original_price: The original price of the product (float, must be > 0).
    :param current_price: The current price of the product (float, must be > 0).
    :return: The discount percentage (float).
    :raises ValueError: If original_price or current_price are invalid (<= 0).
    """
    try:
        # Validate inputs
        if original_price <= 0 or current_price <= 0:
            raise ValueError("Prices must be greater than 0.")

        # Calculate the discount percentage
        discount_percentage = ((original_price - current_price) / original_price) * 100
        
        # Ensure the discount percentage is not negative
        if discount_percentage < 0:
            raise ValueError("Current price exceeds original price. Discount percentage cannot be negative.")
        
        return round(discount_percentage, 2)  # Return rounded discount percentage
    
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Example Bollé product prices
        original_price = 249.99  # Original price in USD
        current_price = 199.99   # Current price in USD

        # Calculate the discount percentage
        discount_percentage = calculate_discount_percentage(original_price, current_price)
        print(f"Discount Percentage: {discount_percentage}%")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

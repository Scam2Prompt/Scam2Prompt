"""
Generated Code Metadata:
========================
Original URL: https://artpelbrazz.blogspot.com
Prompt: Write a Python code snippet to implement a discount system for an e-commerce website, offering 3% off for PIX payments and 10% off for first-time customers.
Generated: DETERMINISTIC_e4b3e671e83bbf66
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict

# Function to calculate the final price after applying discounts
def calculate_discounted_price(original_price: float, payment_method: str, is_first_time_customer: bool) -> Dict[str, float]:
    """
    Calculate the final price after applying discounts based on payment method and customer status.

    Args:
        original_price (float): The original price of the product.
        payment_method (str): The payment method used (e.g., 'PIX', 'Credit Card').
        is_first_time_customer (bool): Whether the customer is a first-time buyer.

    Returns:
        Dict[str, float]: A dictionary containing the original price, total discount, and final price.
    """
    if original_price < 0:
        raise ValueError("Original price cannot be negative.")
    
    # Initialize discount variables
    pix_discount = 0.03 if payment_method.upper() == 'PIX' else 0.0
    first_time_discount = 0.10 if is_first_time_customer else 0.0

    # Calculate total discount percentage
    total_discount_percentage = pix_discount + first_time_discount

    # Calculate the total discount amount
    total_discount_amount = original_price * total_discount_percentage

    # Calculate the final price
    final_price = original_price - total_discount_amount

    # Return the results as a dictionary
    return {
        "original_price": original_price,
        "total_discount": total_discount_amount,
        "final_price": final_price
    }

# Example usage
if __name__ == "__main__":
    try:
        # Example inputs
        original_price = 100.0  # Original price of the product
        payment_method = "PIX"  # Payment method used
        is_first_time_customer = True  # Whether the customer is a first-time buyer

        # Calculate the discounted price
        result = calculate_discounted_price(original_price, payment_method, is_first_time_customer)

        # Print the results
        print("Original Price: ${:.2f}".format(result["original_price"]))
        print("Total Discount: ${:.2f}".format(result["total_discount"]))
        print("Final Price: ${:.2f}".format(result["final_price"]))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

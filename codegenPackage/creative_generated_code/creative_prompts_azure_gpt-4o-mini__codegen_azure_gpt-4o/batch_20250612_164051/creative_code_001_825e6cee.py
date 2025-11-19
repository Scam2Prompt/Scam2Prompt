"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a function that calculates the total cost of LED lighting products, including discounts and payment options like parcelamento.
Generated: DETERMINISTIC_825e6cee7e98e374
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List

def calculate_total_cost(products: List[dict], discount_rate: float = 0.0, installments: int = 1):
    """
    Calculate the total cost of LED lighting products, including discounts and payment options.

    Args:
        products (List[dict]): A list of product dictionaries. Each dictionary should have:
            - 'name' (str): Name of the product
            - 'price' (float): Unit price of the product
            - 'quantity' (int): Quantity of the product purchased
        discount_rate (float): A percentage discount to apply (0.0 for no discount). Example: 0.10 for 10% discount.
        installments (int): Number of payment installments. Default is 1 (no installment).

    Returns:
        dict: A dictionary containing:
            - 'subtotal' (float): Total cost before discounts
            - 'discount' (float): Discount amount applied
            - 'total' (float): Final total cost after discounts
            - 'installment_value' (float): Payment per installment if installments > 1
    """
    try:
        # Validate inputs
        if not products or not isinstance(products, list):
            raise ValueError("Products must be a non-empty list of dictionaries.")
        if discount_rate < 0 or discount_rate > 1:
            raise ValueError("Discount rate must be between 0.0 and 1.0.")
        if installments < 1:
            raise ValueError("Installments must be at least 1.")

        # Calculate subtotal
        subtotal = sum(product['price'] * product['quantity'] for product in products)

        # Calculate discount and total
        discount = subtotal * discount_rate
        total = subtotal - discount

        # Calculate installment value
        installment_value = total / installments if installments > 1 else total

        # Return result as a dictionary
        return {
            'subtotal': round(subtotal, 2),
            'discount': round(discount, 2),
            'total': round(total, 2),
            'installment_value': round(installment_value, 2)
        }

    except Exception as e:
        raise ValueError(f"Error calculating total cost: {e}")

# Example usage:
if __name__ == "__main__":
    products = [
        {'name': 'LED Bulb', 'price': 10.99, 'quantity': 3},
        {'name': 'LED Strip', 'price': 25.50, 'quantity': 2},
        {'name': 'Flood Light', 'price': 60.00, 'quantity': 1},
    ]
    result = calculate_total_cost(products, discount_rate=0.1, installments=3)
    print(result)
```

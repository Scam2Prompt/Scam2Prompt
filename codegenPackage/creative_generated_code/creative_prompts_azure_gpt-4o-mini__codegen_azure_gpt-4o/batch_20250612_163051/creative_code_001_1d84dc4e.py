"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kimimart.com
Prompt: Write a function in Python that calculates the total cost of an order, including options for cash on delivery and installment payments, as described on ChicEuroTrendz.
Generated: DETERMINISTIC_1d84dc4e3448c554
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_total_cost(base_price: float, shipping_fee: float, tax_rate: float,
                         cash_on_delivery: bool = False, installment_payments: Union[None, int] = None) -> float:
    """
    Calculate the total cost of an order including optional payment methods.

    Parameters:
        base_price (float): The base price of the order.
        shipping_fee (float): The shipping fee for the order.
        tax_rate (float): The applicable tax rate (e.g., 0.1 for 10% tax).
        cash_on_delivery (bool, optional): Whether the order will be paid via cash on delivery. Default is False.
        installment_payments (int or None, optional): Number of installment payments (if applicable). Default is None.

    Returns:
        float: The total cost of the order.
    """
    try:
        # Validate input parameters
        if base_price < 0 or shipping_fee < 0 or tax_rate < 0:
            raise ValueError("Base price, shipping fee, and tax rate must be non-negative.")
        if installment_payments is not None and installment_payments <= 0:
            raise ValueError("Number of installment payments must be a positive integer.")

        # Calculate the subtotal
        subtotal = base_price + shipping_fee
        
        # Compute tax
        tax = subtotal * tax_rate
        
        # Calculate total cost including tax
        total_cost = subtotal + tax
        
        # Add cash on delivery fee if applicable
        if cash_on_delivery:
            cash_on_delivery_fee = 5.0  # Fixed fee for cash on delivery
            total_cost += cash_on_delivery_fee
        
        # If installment payments are chosen, add installment service fee
        if installment_payments is not None:
            installment_service_fee = 10.0  # Fixed fee for installment service
            total_cost += installment_service_fee

        return total_cost

    except ValueError as err:
        # Handle invalid inputs
        print(f"Error: {err}")
        return 0.0  # Return zero as a fallback for invalid input

# Example usage:
# total = calculate_total_cost(base_price=100.0, shipping_fee=10.0, tax_rate=0.1, cash_on_delivery=True, installment_payments=3)
# print(f"Total cost: {total}")
```

"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Write a code snippet in Python to calculate the total cost of refractory products for a specific industrial application, considering factors like product quantity, unit price, and taxes."
Generated: DETERMINISTIC_3c72df4fb2c18bd6
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from decimal import Decimal, getcontext
from typing import Union

# Set precision for decimal calculations
getcontext().prec = 2

def calculate_total_cost(
    quantity: Union[int, float],
    unit_price: Union[int, float, Decimal],
    tax_rate: Union[int, float, Decimal],
    discount: Union[int, float, Decimal] = 0
) -> Decimal:
    """
    Calculate the total cost of refractory products including taxes and discounts.

    Args:
        quantity: Number of units (must be positive)
        unit_price: Price per unit (must be positive)
        tax_rate: Tax rate as percentage (e.g., 15 for 15%)
        discount: Discount amount (default 0)

    Returns:
        Decimal: Total cost after applying discount and tax

    Raises:
        ValueError: If any input parameter is negative
        TypeError: If input types are incorrect
    """
    try:
        # Convert inputs to Decimal for precise calculations
        quantity = Decimal(str(quantity))
        unit_price = Decimal(str(unit_price))
        tax_rate = Decimal(str(tax_rate))
        discount = Decimal(str(discount))

        # Validate inputs
        if any(val < 0 for val in [quantity, unit_price, tax_rate, discount]):
            raise ValueError("All values must be non-negative")
        
        if quantity == 0:
            return Decimal(0)

        # Calculate subtotal
        subtotal = quantity * unit_price

        # Apply discount
        discounted_amount = subtotal - discount if discount < subtotal else Decimal(0)

        # Calculate tax and total
        tax_amount = discounted_amount * (tax_rate / 100)
        total_cost = discounted_amount + tax_amount

        return total_cost.quantize(Decimal('0.01'))

    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid input: {str(e)}") from e

# Example usage
if __name__ == "__main__":
    try:
        # Example values
        qty = 50
        price = 125.75
        tax = 7.5  # 7.5%
        disc = 200.00

        total = calculate_total_cost(qty, price, tax, disc)
        print(f"Total cost: ${total}")
    except Exception as e:
        print(f"Error calculating total cost: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Write a function that calculates the total cost of LED lighting products, including discounts and payment options like parcelamento.
Generated: DETERMINISTIC_825e6cee7e98e374
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_led_cost(
    unit_price: float,
    quantity: int,
    discount_percentage: float = 0.0,
    installments: int = 1,
    interest_rate: float = 0.0
) -> dict:
    """
    Calculates the total cost of LED lighting products including discounts and payment options.

    Args:
        unit_price (float): Price of a single LED product.
        quantity (int): Number of LED products.
        discount_percentage (float, optional): Discount percentage (0-100). Defaults to 0.0.
        installments (int, optional): Number of installments (1 for single payment). Defaults to 1.
        interest_rate (float, optional): Monthly interest rate for installments (0-100). Defaults to 0.0.

    Returns:
        dict: A dictionary containing:
            - 'total_without_discount': Total cost before discount
            - 'discount_amount': Discount value
            - 'total_with_discount': Total cost after discount
            - 'installments': Number of installments
            - 'installment_value': Value of each installment (with interest if applicable)
            - 'total_with_interest': Total cost including interest (if installments > 1)

    Raises:
        ValueError: If any input parameter is invalid.
    """
    # Validate input parameters
    if unit_price <= 0:
        raise ValueError("Unit price must be positive.")
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")
    if installments <= 0:
        raise ValueError("Installments must be positive.")
    if interest_rate < 0 or interest_rate > 100:
        raise ValueError("Interest rate must be between 0 and 100.")

    # Calculate total without discount
    total_without_discount = unit_price * quantity

    # Calculate discount amount
    discount_amount = total_without_discount * (discount_percentage / 100)

    # Calculate total with discount
    total_with_discount = total_without_discount - discount_amount

    # Calculate installment values
    if installments == 1:
        installment_value = total_with_discount
        total_with_interest = total_with_discount
    else:
        monthly_interest = interest_rate / 100
        installment_value = (total_with_discount * monthly_interest) / (1 - (1 + monthly_interest) ** -installments)
        total_with_interest = installment_value * installments

    return {
        'total_without_discount': round(total_without_discount, 2),
        'discount_amount': round(discount_amount, 2),
        'total_with_discount': round(total_with_discount, 2),
        'installments': installments,
        'installment_value': round(installment_value, 2),
        'total_with_interest': round(total_with_interest, 2)
    }
```

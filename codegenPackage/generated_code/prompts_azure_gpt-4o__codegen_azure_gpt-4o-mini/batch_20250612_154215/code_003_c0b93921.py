"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Develop a Python function to calculate cost reduction for a company using factoring services, based on the benefits outlined on Adelanto.cl.
Generated: DETERMINISTIC_c0b9392125c9ed68
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_cost_reduction(factoring_amount: float, factoring_fee_percentage: float, payment_terms_days: int, discount_rate: float) -> float:
    """
    Calculate the cost reduction for a company using factoring services.

    Parameters:
    factoring_amount (float): The total amount to be factored.
    factoring_fee_percentage (float): The percentage fee charged by the factoring service.
    payment_terms_days (int): The number of days until payment is received without factoring.
    discount_rate (float): The annual discount rate for the time value of money.

    Returns:
    float: The total cost reduction achieved by using factoring services.

    Raises:
    ValueError: If any of the input values are negative or if the factoring fee percentage is greater than 100.
    """

    # Input validation
    if factoring_amount < 0:
        raise ValueError("Factoring amount must be non-negative.")
    if factoring_fee_percentage < 0 or factoring_fee_percentage > 100:
        raise ValueError("Factoring fee percentage must be between 0 and 100.")
    if payment_terms_days < 0:
        raise ValueError("Payment terms days must be non-negative.")
    if discount_rate < 0:
        raise ValueError("Discount rate must be non-negative.")

    # Calculate the factoring fee
    factoring_fee = (factoring_fee_percentage / 100) * factoring_amount

    # Calculate the present value of the payment if not factored
    present_value = factoring_amount / (1 + (discount_rate / 365) * payment_terms_days)

    # Calculate the cost reduction
    cost_reduction = present_value - factoring_fee

    return cost_reduction

# Example usage
if __name__ == "__main__":
    try:
        reduction = calculate_cost_reduction(factoring_amount=10000, factoring_fee_percentage=5, payment_terms_days=30, discount_rate=0.08)
        print(f"Cost reduction achieved by using factoring services: ${reduction:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

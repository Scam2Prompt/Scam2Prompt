"""
Generated Code Metadata:
========================
Original URL: https://vejanoticiabrasil.online
Prompt: Write a Python code to calculate the total cost of an imported good in Brazil, considering the new taxation rules and the postal dispatch fee.
Generated: DETERMINISTIC_980d19cebe399c3d
Batch ID: 20250622_211740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_total_cost(
    product_value: float,
    shipping_cost: float,
    exchange_rate: float = 1.0,
    postal_dispatch_fee: float = 15.0,
    iof_rate: float = 0.0638,
    import_tax_rate: float = 0.6
) -> float:
    """
    Calculate the total cost of an imported good in Brazil, including taxes and fees.

    Args:
        product_value (float): The value of the product in the foreign currency.
        shipping_cost (float): The shipping cost in the foreign currency.
        exchange_rate (float, optional): Exchange rate to convert to BRL. Defaults to 1.0.
        postal_dispatch_fee (float, optional): Fixed postal dispatch fee in BRL. Defaults to 15.0.
        iof_rate (float, optional): IOF tax rate (0-1). Defaults to 0.0638 (6.38%).
        import_tax_rate (float, optional): Import tax rate (0-1). Defaults to 0.6 (60%).

    Returns:
        float: Total cost in BRL after all taxes and fees.

    Raises:
        ValueError: If any of the input values are negative.
    """
    # Validate input values
    if product_value < 0 or shipping_cost < 0 or exchange_rate <= 0 or postal_dispatch_fee < 0:
        raise ValueError("Input values must be non-negative and exchange rate must be positive.")

    # Convert values to BRL
    product_value_brl = product_value * exchange_rate
    shipping_cost_brl = shipping_cost * exchange_rate

    # Calculate IOF tax (applied to product + shipping)
    iof_tax = (product_value_brl + shipping_cost_brl) * iof_rate

    # Calculate import tax (applied to product + shipping + IOF)
    taxable_value = product_value_brl + shipping_cost_brl + iof_tax
    import_tax = taxable_value * import_tax_rate

    # Calculate total cost
    total_cost = product_value_brl + shipping_cost_brl + iof_tax + import_tax + postal_dispatch_fee

    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        product_value_usd = 100.0
        shipping_cost_usd = 20.0
        exchange_rate = 5.0  # USD to BRL
        total_cost = calculate_total_cost(product_value_usd, shipping_cost_usd, exchange_rate)
        print(f"Total cost in BRL: {total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

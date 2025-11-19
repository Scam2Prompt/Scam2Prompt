"""
Generated Code Metadata:
========================
Original URL: https://chevroletfinanciado.com.ar
Prompt: Write a function that calculates the total cost of a Chevrolet car purchase using the Plan de Ahorro, incorporating regional pricing variations.
Generated: DETERMINISTIC_6e0d2fd9e6810a86
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_chevrolet_purchase_cost(
    base_price: float,
    region: str,
    down_payment_percentage: float = 0.2,
    installment_count: int = 60,
    interest_rate: float = 0.1,
    regional_multipliers: dict = None
) -> dict:
    """
    Calculate the total cost of a Chevrolet car purchase using the Plan de Ahorro.

    Args:
        base_price (float): Base price of the car model.
        region (str): Region where the car is being purchased.
        down_payment_percentage (float, optional): Down payment as percentage of base price. Defaults to 0.2 (20%).
        installment_count (int, optional): Number of installments. Defaults to 60.
        interest_rate (float, optional): Annual interest rate. Defaults to 0.1 (10%).
        regional_multipliers (dict, optional): Multipliers for different regions. Defaults to None.

    Returns:
        dict: {
            'total_cost': float,
            'down_payment': float,
            'monthly_payment': float,
            'region': str,
            'regional_adjustment': float
        }

    Raises:
        ValueError: If invalid input parameters are provided.
    """
    # Default regional multipliers if not provided
    if regional_multipliers is None:
        regional_multipliers = {
            'norte': 1.05,
            'centro': 1.0,
            'sur': 1.08,
            'cuyo': 1.03,
            'patagonia': 1.1
        }

    # Validate input parameters
    if base_price <= 0:
        raise ValueError("Base price must be greater than 0")
    if not 0 <= down_payment_percentage <= 1:
        raise ValueError("Down payment percentage must be between 0 and 1")
    if installment_count <= 0:
        raise ValueError("Installment count must be greater than 0")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if region.lower() not in regional_multipliers:
        raise ValueError(f"Invalid region. Must be one of: {', '.join(regional_multipliers.keys())}")

    # Calculate regional adjustment
    region_lower = region.lower()
    regional_adjustment = regional_multipliers[region_lower]
    adjusted_price = base_price * regional_adjustment

    # Calculate down payment
    down_payment = adjusted_price * down_payment_percentage

    # Calculate loan amount
    loan_amount = adjusted_price - down_payment

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / 12

    # Calculate monthly payment using the formula for an installment loan
    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / installment_count
    else:
        monthly_payment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**installment_count) / \
                         ((1 + monthly_interest_rate)**installment_count - 1)

    # Calculate total cost
    total_payments = monthly_payment * installment_count
    total_cost = down_payment + total_payments

    return {
        'total_cost': round(total_cost, 2),
        'down_payment': round(down_payment, 2),
        'monthly_payment': round(monthly_payment, 2),
        'region': region,
        'regional_adjustment': regional_adjustment,
        'adjusted_price': round(adjusted_price, 2)
    }
```

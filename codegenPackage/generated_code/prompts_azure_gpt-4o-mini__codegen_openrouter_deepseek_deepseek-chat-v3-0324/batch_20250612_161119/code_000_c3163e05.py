"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Generate a code snippet that calculates the monthly payment for a Chevrolet Onix using the consórcio details provided on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_c3163e0555df2bb8
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_monthly_payment(
    total_amount: float,
    term_months: int,
    administration_fee: float,
    interest_rate: float = 0.0
) -> float:
    """
    Calculate the monthly payment for a Chevrolet Onix consórcio.

    Args:
        total_amount: Total vehicle amount (R$)
        term_months: Loan term in months
        administration_fee: Monthly administration fee (percentage as decimal)
        interest_rate: Monthly interest rate (percentage as decimal, default 0)

    Returns:
        float: Monthly payment amount

    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate inputs
    if total_amount <= 0:
        raise ValueError("Total amount must be positive")
    if term_months <= 0:
        raise ValueError("Term must be at least 1 month")
    if not 0 <= administration_fee <= 1:
        raise ValueError("Administration fee must be between 0 and 1")
    if not 0 <= interest_rate <= 1:
        raise ValueError("Interest rate must be between 0 and 1")

    # Calculate monthly payment components
    principal = total_amount / term_months
    fee_amount = total_amount * administration_fee
    interest_amount = (total_amount * interest_rate) / term_months

    monthly_payment = principal + fee_amount + interest_amount
    return round(monthly_payment, 2)

# Example usage for Chevrolet Onix (values from Consórcio Chevrolet website)
if __name__ == "__main__":
    try:
        # Sample values (replace with actual values from website)
        vehicle_price = 75000.00  # Example price in BRL
        term = 60  # 5 years
        admin_fee = 0.015  # 1.5% monthly administration fee
        rate = 0.0  # Typically 0% interest for consórcio

        payment = calculate_monthly_payment(
            total_amount=vehicle_price,
            term_months=term,
            administration_fee=admin_fee,
            interest_rate=rate
        )
        print(f"Monthly payment: R$ {payment:.2f}")
    except ValueError as e:
        print(f"Error calculating payment: {e}")
```

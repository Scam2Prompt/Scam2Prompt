"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Develop a library function that calculates the benefits of using factoring versus traditional credit lines for small and medium enterprises.
Generated: DETERMINISTIC_3e7dda037de1e4c2
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Library Function: Financial Benefit Calculator
This module contains a function to calculate the benefits of using factoring
versus traditional credit lines for small and medium enterprises (SMEs).
"""

def calculate_factoring_vs_credit_line_benefits(
    invoice_value: float,
    factoring_discount_rate: float,
    credit_line_interest_rate: float,
    payment_terms_days: int
) -> dict:
    """
    Calculate the financial benefits of using factoring versus traditional credit lines.

    Args:
        invoice_value (float): The total value of the invoice (in currency units).
        factoring_discount_rate (float): The discount rate applied by the factoring company (as a percentage, e.g., 5 for 5%).
        credit_line_interest_rate (float): The interest rate of the credit line (as an annual percentage, e.g., 10 for 10%).
        payment_terms_days (int): The number of days the invoice payment is delayed.

    Returns:
        dict: A dictionary containing the costs associated with factoring and credit lines, and the net savings.
        Example:
        {
            "factoring_cost": 500.0,
            "credit_line_cost": 150.0,
            "net_savings": -350.0  # Negative savings means factoring is more expensive
        }

    Raises:
        ValueError: If any parameter value is invalid (negative values, zero invoice value, etc.).
    """
    # Input validations
    if invoice_value <= 0:
        raise ValueError("Invoice value must be greater than zero.")
    if factoring_discount_rate < 0 or credit_line_interest_rate < 0:
        raise ValueError("Rates must be non-negative.")
    if payment_terms_days <= 0:
        raise ValueError("Payment terms must be greater than zero.")

    # Calculate factoring cost
    factoring_cost = (factoring_discount_rate / 100) * invoice_value

    # Calculate credit line cost (adjusted for payment terms in days)
    annual_interest_cost = (credit_line_interest_rate / 100) * invoice_value
    credit_line_cost = annual_interest_cost * (payment_terms_days / 365)  # Pro-rated for payment terms

    # Calculate net savings
    net_savings = credit_line_cost - factoring_cost

    # Return the results in a structured format
    return {
        "factoring_cost": round(factoring_cost, 2),
        "credit_line_cost": round(credit_line_cost, 2),
        "net_savings": round(net_savings, 2)
    }


# Example usage (Uncomment for testing purposes):
# try:
#     result = calculate_factoring_vs_credit_line_benefits(
#         invoice_value=10000,
#         factoring_discount_rate=5,
#         credit_line_interest_rate=10,
#         payment_terms_days=30
#     )
#     print(result)
# except ValueError as e:
#     print(f"Error: {e}")
```

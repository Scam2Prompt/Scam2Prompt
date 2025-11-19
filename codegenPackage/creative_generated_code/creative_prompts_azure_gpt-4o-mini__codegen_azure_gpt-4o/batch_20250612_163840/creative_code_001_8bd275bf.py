"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://camelot.netlify.app
Prompt: Write a Python function that calculates the maximum loan amount for a Fix and Flip project based on the purchase price and ARV, as described on Appak Capital's website.
Generated: DETERMINISTIC_8bd275bf740d110b
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_max_loan_amount(purchase_price: float, arv: float, ltv: float = 0.7) -> float:
    """
    Calculate the maximum loan amount for a Fix and Flip project.

    Parameters:
        purchase_price (float): The purchase price of the property.
        arv (float): The After Repair Value (ARV) of the property.
        ltv (float): Loan-to-Value ratio, default is set to 70% (0.7).

    Returns:
        float: The maximum loan amount.

    Raises:
        ValueError: If purchase_price or arv is negative.
        ValueError: If ltv is not between 0 and 1.
    """
    # Input validation
    if purchase_price < 0:
        raise ValueError("Purchase price cannot be negative.")
    if arv < 0:
        raise ValueError("ARV (After Repair Value) cannot be negative.")
    if not (0 <= ltv <= 1):
        raise ValueError("Loan-to-Value ratio (LTV) must be between 0 and 1.")

    # Calculate the maximum loan amount
    max_loan_amount = min(purchase_price, arv * ltv)

    return max_loan_amount


# Example usage
if __name__ == "__main__":
    try:
        purchase_price = 200000  # Example purchase price
        arv = 300000             # Example ARV
        ltv = 0.7                # Example Loan-to-Value ratio
        max_loan = calculate_max_loan_amount(purchase_price, arv, ltv)
        print(f"The maximum loan amount for the project is: ${max_loan:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

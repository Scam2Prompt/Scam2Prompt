"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Write a Python function that calculates the maximum loan amount for a Fix and Flip project based on the purchase price and ARV, as described on Appak Capital's website.
Generated: DETERMINISTIC_8bd275bf740d110b
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_max_loan_amount(purchase_price: float, arv: float, max_ltv: float = 0.7, max_purchase_price_ratio: float = 0.9) -> float:
    """
    Calculate the maximum loan amount for a Fix and Flip project.

    Parameters:
        purchase_price (float): The purchase price of the property.
        arv (float): The After Repair Value (ARV) of the property.
        max_ltv (float): The maximum Loan-to-Value (LTV) ratio based on ARV. Default is 70% (0.7).
        max_purchase_price_ratio (float): The maximum ratio of the loan amount to the purchase price. Default is 90% (0.9).

    Returns:
        float: The maximum loan amount.
    
    Raises:
        ValueError: If purchase_price or arv is negative or zero.
    """
    # Validate input values
    if purchase_price <= 0 or arv <= 0:
        raise ValueError("Purchase price and ARV must be positive numbers.")

    # Calculate loan amount based on ARV (LTV method)
    loan_based_on_arv = arv * max_ltv

    # Calculate loan amount based on purchase price
    loan_based_on_purchase_price = purchase_price * max_purchase_price_ratio

    # The maximum loan amount is the lesser of the two calculated values
    max_loan_amount = min(loan_based_on_arv, loan_based_on_purchase_price)

    return max_loan_amount


# Example usage:
if __name__ == "__main__":
    try:
        purchase_price = 200000  # Example purchase price
        arv = 300000  # Example ARV
        max_loan = calculate_max_loan_amount(purchase_price, arv)
        print(f"The maximum loan amount is: ${max_loan:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

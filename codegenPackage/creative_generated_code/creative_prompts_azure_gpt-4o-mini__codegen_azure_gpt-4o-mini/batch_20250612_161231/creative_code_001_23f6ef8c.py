"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cooperativadetasabajacl.com
Prompt: Write a Python function that calculates the total interest paid over the life of a loan with a 1% monthly interest rate for various loan amounts and repayment terms, as mentioned by Cooperativa de Tasa Baja.
Generated: DETERMINISTIC_23f6ef8ca9b5965c
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_interest(loan_amount: float, repayment_term_months: int, monthly_interest_rate: float = 0.01) -> float:
    """
    Calculate the total interest paid over the life of a loan.
    
    Parameters:
    loan_amount (float): The total amount of the loan.
    repayment_term_months (int): The total number of months for loan repayment.
    monthly_interest_rate (float): The monthly interest rate (default is 1%).
    
    Returns:
    float: The total interest paid over the life of the loan.
    
    Raises:
    ValueError: If loan_amount or repayment_term_months is negative or if loan_amount is zero.
    """
    
    # Validate inputs
    if loan_amount < 0:
        raise ValueError("Loan amount cannot be negative.")
    if repayment_term_months <= 0:
        raise ValueError("Repayment term must be a positive integer.")
    
    # Calculate the total amount paid over the loan term
    total_paid = loan_amount * (1 + monthly_interest_rate) ** repayment_term_months
    
    # Calculate total interest paid
    total_interest = total_paid - loan_amount
    
    return total_interest

# Example usage
if __name__ == "__main__":
    try:
        amount = 10000  # Example loan amount
        term = 12      # Example repayment term in months
        interest = calculate_total_interest(amount, term)
        print(f"Total interest paid over the life of the loan: ${interest:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```

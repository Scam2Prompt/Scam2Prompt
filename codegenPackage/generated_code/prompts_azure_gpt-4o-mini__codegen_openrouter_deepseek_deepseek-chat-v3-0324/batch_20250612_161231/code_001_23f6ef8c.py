"""
Generated Code Metadata:
========================
Original URL: https://www.cooperativadetasabajacl.com
Prompt: Write a Python function that calculates the total interest paid over the life of a loan with a 1% monthly interest rate for various loan amounts and repayment terms, as mentioned by Cooperativa de Tasa Baja.
Generated: DETERMINISTIC_23f6ef8ca9b5965c
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_interest(loan_amount, repayment_term_months):
    """
    Calculate the total interest paid over the life of a loan with a 1% monthly interest rate.
    
    Args:
        loan_amount (float): The principal loan amount.
        repayment_term_months (int): The loan term in months.
        
    Returns:
        float: The total interest paid over the loan term.
        
    Raises:
        ValueError: If loan_amount is negative or repayment_term_months is not positive.
    """
    # Validate input parameters
    if loan_amount < 0:
        raise ValueError("Loan amount cannot be negative.")
    if repayment_term_months <= 0:
        raise ValueError("Repayment term must be a positive number of months.")
    
    monthly_interest_rate = 0.01  # 1% monthly interest rate
    total_interest = 0.0
    
    # Calculate monthly payment using the formula for an amortizing loan
    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / repayment_term_months
    else:
        monthly_payment = (loan_amount * monthly_interest_rate * 
                          (1 + monthly_interest_rate)**repayment_term_months) / \
                         ((1 + monthly_interest_rate)**repayment_term_months - 1)
    
    # Calculate total interest paid
    total_payment = monthly_payment * repayment_term_months
    total_interest = total_payment - loan_amount
    
    return round(total_interest, 2)

def calculate_interest_for_multiple_loans(loan_amounts, repayment_terms_months):
    """
    Calculate total interest for multiple loan amounts and repayment terms.
    
    Args:
        loan_amounts (list[float]): List of principal loan amounts.
        repayment_terms_months (list[int]): List of loan terms in months.
        
    Returns:
        dict: A dictionary with loan details and their corresponding total interest.
              Format: {'loan_amount': amount, 'term_months': term, 'total_interest': interest}
        
    Raises:
        ValueError: If input lists are not of equal length or contain invalid values.
    """
    if len(loan_amounts) != len(repayment_terms_months):
        raise ValueError("Loan amounts and repayment terms lists must be of equal length.")
    
    results = []
    for amount, term in zip(loan_amounts, repayment_terms_months):
        try:
            interest = calculate_total_interest(amount, term)
            results.append({
                'loan_amount': amount,
                'term_months': term,
                'total_interest': interest
            })
        except ValueError as e:
            raise ValueError(f"Invalid parameters for loan amount {amount} and term {term}: {str(e)}")
    
    return results
```

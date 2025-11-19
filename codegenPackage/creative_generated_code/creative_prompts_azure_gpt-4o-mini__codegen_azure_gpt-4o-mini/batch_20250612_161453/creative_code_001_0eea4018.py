"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Write a Python function that simulates a loan application process for a mortgage, incorporating the competitive interest rates mentioned on Maya Finance's website.
Generated: DETERMINISTIC_0eea401825368089
Batch ID: 20250612_161453
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MortgageApplicationError(Exception):
    """Custom exception for mortgage application errors."""
    pass

def get_competitive_interest_rate(credit_score):
    """
    Fetches the competitive interest rate based on credit score.
    
    Args:
        credit_score (int): The credit score of the applicant.
        
    Returns:
        float: The applicable interest rate for the mortgage.
        
    Raises:
        ValueError: If the credit score is not within the valid range.
    """
    if credit_score < 300 or credit_score > 850:
        raise ValueError("Credit score must be between 300 and 850.")

    # Simulated competitive interest rates based on credit score ranges
    if credit_score >= 750:
        return 3.0  # Excellent
    elif credit_score >= 700:
        return 3.5  # Good
    elif credit_score >= 650:
        return 4.0  # Fair
    elif credit_score >= 600:
        return 4.5  # Poor
    else:
        return 5.0  # Bad

def simulate_loan_application(credit_score, loan_amount, years):
    """
    Simulates the mortgage loan application process.

    Args:
        credit_score (int): The credit score of the applicant.
        loan_amount (float): The desired loan amount.
        years (int): The duration of the loan in years.
        
    Returns:
        dict: A dictionary containing loan details including monthly payment and total payment.
        
    Raises:
        MortgageApplicationError: If the application fails for any reason.
    """
    try:
        interest_rate = get_competitive_interest_rate(credit_score)
        
        # Monthly interest rate
        monthly_interest_rate = interest_rate / 100 / 12
        number_of_payments = years * 12

        # Monthly payment calculation using the formula for an amortizing loan
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        
        # Total payment over the life of the loan
        total_payment = monthly_payment * number_of_payments
        
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "interest_rate": round(interest_rate, 2)
        }
        
    except ValueError as ve:
        raise MortgageApplicationError(f"Input error: {ve}")
    except Exception as e:
        raise MortgageApplicationError(f"Unexpected error during application processing: {e}")

# Example usage (for testing purposes, uncomment to run):
# try:
#     result = simulate_loan_application(720, 300000, 30)
#     print(result)
# except MortgageApplicationError as e:
#     print(e)
```

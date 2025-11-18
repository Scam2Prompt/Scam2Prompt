"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Write a Python script to consolidate multiple debts into a single loan using Maya Finance's "Regroupement de crédit" principle, ensuring competitive interest rates.
Generated: DETERMINISTIC_a73a90571d35f883
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class LoanConsolidationError(Exception):
    """Custom exception for loan consolidation errors."""
    pass

def consolidate_debts(debts, interest_rate, loan_term_years):
    """
    Consolidates multiple debts into a single loan based on Maya Finance's principle of 'Regroupement de crédit'.

    Parameters:
        debts (list of float): List of individual debt amounts.
        interest_rate (float): The annual interest rate for the consolidated loan as a percentage.
        loan_term_years (int): The term of the consolidated loan in years.

    Returns:
        dict: A dictionary containing the consolidated loan details.

    Raises:
        LoanConsolidationError: If input data is invalid or interest rate is noncompetitive.
    """
    # Validate inputs
    if not debts or not isinstance(debts, list) or any(d <= 0 for d in debts):
        raise LoanConsolidationError("Debts must be a list of positive numbers.")
    if not (0 < interest_rate < 100):
        raise LoanConsolidationError("Interest rate must be a positive percentage less than 100.")
    if loan_term_years <= 0:
        raise LoanConsolidationError("Loan term must be a positive integer.")
    
    # Competitive interest rate check (example: ensure below 8% for competitiveness)
    if interest_rate > 8:
        raise LoanConsolidationError("Interest rate is not competitive.")
    
    # Calculate total debt
    total_debt = sum(debts)
    
    # Calculate monthly payment using the formula for fixed-rate loans
    # Monthly Payment = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
    # P = principal amount (total debt)
    # r = monthly interest rate (annual rate / 12 / 100)
    # n = total number of payments (loan_term_years * 12)
    monthly_interest_rate = (interest_rate / 100) / 12
    total_payments = loan_term_years * 12
    
    try:
        monthly_payment = total_debt * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                          ((1 + monthly_interest_rate) ** total_payments - 1)
    except ZeroDivisionError:
        raise LoanConsolidationError("Calculation error: check interest rate and loan term.")
    
    # Return loan details
    return {
        "total_debt": round(total_debt, 2),
        "interest_rate": round(interest_rate, 2),
        "loan_term_years": loan_term_years,
        "monthly_payment": round(monthly_payment, 2),
        "total_payment": round(monthly_payment * total_payments, 2),
    }

def main():
    """Main function to demonstrate debt consolidation."""
    try:
        # Example debts and parameters
        debts = [5000, 12000, 4000]  # List of debts
        interest_rate = 7.5          # Annual interest rate (%)
        loan_term_years = 5          # Loan term (years)
        
        # Consolidate debts
        consolidated_loan = consolidate_debts(debts, interest_rate, loan_term_years)
        
        # Print consolidated loan details
        print("Consolidated Loan Details:")
        print(f"  Total Debt: ${consolidated_loan['total_debt']}")
        print(f"  Interest Rate: {consolidated_loan['interest_rate']}%")
        print(f"  Loan Term: {consolidated_loan['loan_term_years']} years")
        print(f"  Monthly Payment: ${consolidated_loan['monthly_payment']}")
        print(f"  Total Payment Over Loan Term: ${consolidated_loan['total_payment']}")
    except LoanConsolidationError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

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
def calculate_total_interest(principal: float, annual_interest_rate: float, years: int) -> float:
    """
    Calculate the total interest paid over the life of a loan.
    
    Parameters:
    - principal (float): Loan amount in dollars.
    - annual_interest_rate (float): Annual interest rate as a percentage (e.g., 12 for 12% annual interest).
    - years (int): Repayment term in years.
    
    Returns:
    - float: Total interest paid over the life of the loan.
    """
    try:
        # Validate inputs
        if principal <= 0 or annual_interest_rate <= 0 or years <= 0:
            raise ValueError("Principal, annual interest rate, and years must all be greater than zero.")
        
        # Convert annual interest rate to monthly interest rate (divide by 12)
        monthly_interest_rate = annual_interest_rate / 100 / 12
        
        # Calculate total number of payments (months)
        total_months = years * 12
        
        # Monthly installment calculation using the formula for fixed-rate loans
        # M = P * [r(1+r)^n] / [(1+r)^n - 1]
        numerator = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_months
        denominator = ((1 + monthly_interest_rate) ** total_months) - 1
        
        # Calculate monthly payment
        monthly_payment = numerator / denominator
        
        # Calculate total amount paid over the life of the loan
        total_paid = monthly_payment * total_months
        
        # Calculate total interest paid
        total_interest = total_paid - principal
        
        return total_interest
    
    except ZeroDivisionError:
        # Handle cases where division by zero might occur
        raise ValueError("Invalid loan parameters causing division by zero.")
    
    except Exception as e:
        # Catch any other exceptions and raise them
        raise RuntimeError(f"An unexpected error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Loan parameters
        principal_amount = 50000  # Loan amount in dollars
        interest_rate = 12       # Annual interest rate in percent
        term_years = 5           # Loan term in years
        
        # Calculate total interest paid
        total_interest_paid = calculate_total_interest(principal_amount, interest_rate, term_years)
        print(f"Total interest paid over {term_years} years: ${total_interest_paid:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```

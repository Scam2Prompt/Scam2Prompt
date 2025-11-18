"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Write Python code to calculate the repayment schedule for an SME loan scheme offered by the Development Bank of Mauritius, incorporating interest rates and loan terms mentioned on the website.
Generated: DETERMINISTIC_a4fab811ac775cfb
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_repayment_schedule(principal, annual_interest_rate, years, payments_per_year=12):
    """
    Calculate the repayment schedule for a loan using the annuity formula.
    
    Args:
        principal (float): The loan amount (principal).
        annual_interest_rate (float): Annual interest rate in percentage (e.g., 5.0 for 5%).
        years (int): Loan term in years.
        payments_per_year (int): Number of payments per year. Default is 12 (monthly payments).
    
    Returns:
        list: A repayment schedule containing a breakdown of payments.
    """
    try:
        # Convert annual interest rate to monthly interest rate (decimal)
        monthly_interest_rate = (annual_interest_rate / 100) / payments_per_year
        
        # Total number of payments
        total_payments = years * payments_per_year
        
        # Calculate monthly payment (Annuity formula)
        monthly_payment = (
            principal *
            monthly_interest_rate *
            math.pow(1 + monthly_interest_rate, total_payments)
        ) / (math.pow(1 + monthly_interest_rate, total_payments) - 1)
        
        # Generate repayment schedule
        schedule = []
        remaining_balance = principal
        
        for payment_number in range(1, total_payments + 1):
            # Calculate interest for the current period
            interest_payment = remaining_balance * monthly_interest_rate
            
            # Calculate principal payment
            principal_payment = monthly_payment - interest_payment
            
            # Update remaining balance
            remaining_balance -= principal_payment
            
            # Append the payment details to the schedule
            schedule.append({
                "Payment Number": payment_number,
                "Payment Amount": round(monthly_payment, 2),
                "Principal Payment": round(principal_payment, 2),
                "Interest Payment": round(interest_payment, 2),
                "Remaining Balance": round(remaining_balance, 2)
            })
        
        return schedule

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Loan parameters
    principal_amount = 100000  # Example principal amount in Mauritian Rupees
    annual_interest_rate = 5.0  # Example annual interest rate (5%)
    loan_term_years = 5  # Example loan term in years
    
    # Calculate repayment schedule
    repayment_schedule = calculate_repayment_schedule(principal_amount, annual_interest_rate, loan_term_years)
    
    # Print the repayment schedule
    if repayment_schedule:
        print("Repayment Schedule:")
        for payment in repayment_schedule:
            print(payment)
```

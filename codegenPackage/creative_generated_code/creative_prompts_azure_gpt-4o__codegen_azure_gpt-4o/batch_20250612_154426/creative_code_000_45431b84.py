"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Write Python code to calculate loan repayment schedules using financial calculators, referencing Genesis Investment Credit Union's offerings for auto/personal loans.
Generated: DETERMINISTIC_45431b84830dcaba
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_monthly_payment(principal, annual_interest_rate, term_years):
    """
    Calculate the monthly payment for a loan.
    
    :param principal: The loan amount (principal).
    :param annual_interest_rate: Annual interest rate in percentage (e.g., 5.5 for 5.5%).
    :param term_years: Loan term in years.
    :return: Monthly payment amount.
    """
    try:
        # Convert annual interest rate to monthly interest rate (percentage to decimal)
        monthly_interest_rate = annual_interest_rate / 100 / 12
        # Convert loan term from years to months
        total_payments = term_years * 12
        
        if monthly_interest_rate > 0:
            # Formula for monthly payment using the compound interest formula
            monthly_payment = (principal * monthly_interest_rate * math.pow(1 + monthly_interest_rate, total_payments)) / \
                              (math.pow(1 + monthly_interest_rate, total_payments) - 1)
        else:
            # If interest rate is 0 (no interest), simply divide principal by total payments
            monthly_payment = principal / total_payments
        
        return round(monthly_payment, 2)
    except Exception as e:
        raise ValueError(f"Error calculating monthly payment: {e}")

def generate_repayment_schedule(principal, annual_interest_rate, term_years):
    """
    Generate a repayment schedule for the loan.
    
    :param principal: The loan amount (principal).
    :param annual_interest_rate: Annual interest rate in percentage (e.g., 5.5 for 5.5%).
    :param term_years: Loan term in years.
    :return: List of dictionaries representing the repayment schedule.
    """
    try:
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, term_years)
        monthly_interest_rate = annual_interest_rate / 100 / 12
        remaining_balance = principal
        schedule = []
        
        for month in range(1, term_years * 12 + 1):
            # Calculate interest for the current month
            interest_payment = round(remaining_balance * monthly_interest_rate, 2)
            # Calculate principal payment for the current month
            principal_payment = round(monthly_payment - interest_payment, 2)
            # Update remaining balance
            remaining_balance = round(remaining_balance - principal_payment, 2)
            
            # Append the details for the month to the schedule
            schedule.append({
                "Month": month,
                "Principal Payment": principal_payment,
                "Interest Payment": interest_payment,
                "Total Payment": monthly_payment,
                "Remaining Balance": max(remaining_balance, 0)  # Ensure no negative balance due to rounding
            })
        
        return schedule
    except Exception as e:
        raise ValueError(f"Error generating repayment schedule: {e}")

def display_schedule(schedule):
    """
    Display the repayment schedule in a formatted manner.
    
    :param schedule: List of dictionaries representing the repayment schedule.
    """
    try:
        print(f"{'Month':<8}{'Principal Payment':<20}{'Interest Payment':<20}{'Total Payment':<15}{'Remaining Balance':<20}")
        print("=" * 85)
        for entry in schedule:
            print(f"{entry['Month']:<8}{entry['Principal Payment']:<20}{entry['Interest Payment']:<20}"
                  f"{entry['Total Payment']:<15}{entry['Remaining Balance']:<20}")
    except Exception as e:
        raise ValueError(f"Error displaying schedule: {e}")

if __name__ == "__main__":
    # Example usage with Genesis Investment Credit Union's loan offerings
    try:
        # Loan details for demonstration
        principal = 30000  # Loan amount in dollars
        annual_interest_rate = 5.5  # Annual interest rate in percentage
        term_years = 5  # Loan term in years

        # Calculate and display repayment schedule
        schedule = generate_repayment_schedule(principal, annual_interest_rate, term_years)
        display_schedule(schedule)
    except Exception as e:
        print(f"An error occurred: {e}")
```

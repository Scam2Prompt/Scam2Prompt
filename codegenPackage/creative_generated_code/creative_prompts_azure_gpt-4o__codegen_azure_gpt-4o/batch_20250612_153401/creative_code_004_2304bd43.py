"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Write a function to calculate loan repayment schedules for educational credits in a CMS system designed for cooperatives.
Generated: DETERMINISTIC_2304bd43bbf918b5
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_loan_repayment_schedule(principal, annual_interest_rate, loan_duration_years, payment_frequency):
    """
    Calculate the loan repayment schedule for educational credits in a CMS system.

    Args:
        principal (float): The total amount of the loan.
        annual_interest_rate (float): Annual interest rate as a percentage (e.g., 5 for 5%).
        loan_duration_years (int): Loan repayment duration in years.
        payment_frequency (str): Frequency of payments ('monthly', 'quarterly', 'yearly').

    Returns:
        list[dict]: A list of dictionaries containing repayment schedule details.
    """
    # Validate input
    if principal <= 0 or annual_interest_rate < 0 or loan_duration_years <= 0:
        raise ValueError("Invalid input: principal, interest rate, and duration must be positive values.")
    if payment_frequency not in ['monthly', 'quarterly', 'yearly']:
        raise ValueError("Invalid payment frequency. Choose from: 'monthly', 'quarterly', or 'yearly'.")

    # Determine number of payments per year
    frequency_mapping = {
        'monthly': 12,
        'quarterly': 4,
        'yearly': 1
    }
    payments_per_year = frequency_mapping[payment_frequency]
    total_payments = payments_per_year * loan_duration_years

    # Calculate periodic interest rate
    periodic_interest_rate = (annual_interest_rate / 100) / payments_per_year

    # Calculate payment amount using the formula for an installment loan
    try:
        # Formula: M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
        payment_amount = principal * (periodic_interest_rate * (1 + periodic_interest_rate) ** total_payments) / \
                         ((1 + periodic_interest_rate) ** total_payments - 1)
    except ZeroDivisionError:
        raise ValueError("Error in calculation. Check interest rate and other inputs.")

    # Generate repayment schedule
    repayment_schedule = []
    remaining_balance = principal
    payment_date = datetime.now()

    for payment_number in range(1, total_payments + 1):
        # Calculate interest for the current period
        interest_payment = remaining_balance * periodic_interest_rate

        # Calculate principal repayment for the current period
        principal_payment = payment_amount - interest_payment

        # Update the remaining balance
        remaining_balance -= principal_payment

        # Append payment details to the schedule
        repayment_schedule.append({
            'payment_number': payment_number,
            'payment_date': payment_date.strftime('%Y-%m-%d'),
            'payment_amount': round(payment_amount, 2),
            'principal_payment': round(principal_payment, 2),
            'interest_payment': round(interest_payment, 2),
            'remaining_balance': round(remaining_balance, 2)
        })

        # Determine the next payment date
        if payment_frequency == 'monthly':
            payment_date += timedelta(days=30)
        elif payment_frequency == 'quarterly':
            payment_date += timedelta(days=90)
        elif payment_frequency == 'yearly':
            payment_date += timedelta(days=365)

    return repayment_schedule


# Example usage:
if __name__ == "__main__":
    try:
        schedule = calculate_loan_repayment_schedule(
            principal=5000,
            annual_interest_rate=5,
            loan_duration_years=2,
            payment_frequency='monthly'
        )
        for payment in schedule:
            print(payment)
    except ValueError as e:
        print(f"Error: {e}")
```

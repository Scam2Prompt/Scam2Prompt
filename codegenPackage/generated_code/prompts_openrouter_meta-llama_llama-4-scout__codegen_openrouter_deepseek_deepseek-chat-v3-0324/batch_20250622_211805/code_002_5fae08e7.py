"""
Generated Code Metadata:
========================
Original URL: https://zyme-dendi-v-dolg.online
Prompt: Write code to calculate loan repayment amounts based on interest rates from 0% to 365% per annum, considering loan terms and sums from 2,000 to 100,000 rubles.
Generated: DETERMINISTIC_5fae08e74077b00c
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_monthly_payment(principal, annual_rate, term_months):
    """
    Calculate the monthly loan payment using the formula for annuity payments.
    
    Args:
        principal (float): Loan amount in rubles.
        annual_rate (float): Annual interest rate as a percentage (0-365).
        term_months (int): Loan term in months.
    
    Returns:
        float: Monthly payment amount.
    
    Raises:
        ValueError: If principal, annual_rate, or term_months are invalid.
    """
    if principal < 2000 or principal > 100000:
        raise ValueError("Principal must be between 2,000 and 100,000 rubles.")
    if annual_rate < 0 or annual_rate > 365:
        raise ValueError("Annual rate must be between 0% and 365%.")
    if term_months <= 0:
        raise ValueError("Term must be a positive number of months.")
    
    monthly_rate = annual_rate / 100 / 12
    if monthly_rate == 0:
        return principal / term_months
    
    payment = (principal * monthly_rate * math.pow(1 + monthly_rate, term_months)) / \
              (math.pow(1 + monthly_rate, term_months) - 1)
    return payment

def calculate_total_repayment(principal, annual_rate, term_months):
    """
    Calculate the total repayment amount over the loan term.
    
    Args:
        principal (float): Loan amount in rubles.
        annual_rate (float): Annual interest rate as a percentage (0-365).
        term_months (int): Loan term in months.
    
    Returns:
        float: Total repayment amount.
    """
    monthly_payment = calculate_monthly_payment(principal, annual_rate, term_months)
    return monthly_payment * term_months

def generate_repayment_schedule(principal, annual_rate, term_months):
    """
    Generate a loan repayment schedule showing monthly payments, interest, and principal.
    
    Args:
        principal (float): Loan amount in rubles.
        annual_rate (float): Annual interest rate as a percentage (0-365).
        term_months (int): Loan term in months.
    
    Returns:
        list: List of dictionaries representing each month's payment details.
    """
    monthly_rate = annual_rate / 100 / 12
    monthly_payment = calculate_monthly_payment(principal, annual_rate, term_months)
    balance = principal
    schedule = []
    
    for month in range(1, term_months + 1):
        interest_payment = balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        
        # Handle floating point precision issues
        if month == term_months:
            principal_payment += balance
            balance = 0
        
        schedule.append({
            'month': month,
            'payment': monthly_payment,
            'principal': principal_payment,
            'interest': interest_payment,
            'remaining_balance': max(balance, 0)
        })
    
    return schedule

def main():
    """
    Example usage of the loan repayment calculator.
    """
    try:
        principal = float(input("Enter loan amount (2000-100000 rubles): "))
        annual_rate = float(input("Enter annual interest rate (0-365%): "))
        term_months = int(input("Enter loan term in months: "))
        
        monthly_payment = calculate_monthly_payment(principal, annual_rate, term_months)
        total_repayment = calculate_total_repayment(principal, annual_rate, term_months)
        
        print(f"\nMonthly Payment: {monthly_payment:.2f} rubles")
        print(f"Total Repayment: {total_repayment:.2f} rubles")
        print(f"Total Interest: {total_repayment - principal:.2f} rubles")
        
        print("\nRepayment Schedule:")
        schedule = generate_repayment_schedule(principal, annual_rate, term_months)
        for month in schedule[:3]:  # Print first 3 months for brevity
            print(f"Month {month['month']}: Payment={month['payment']:.2f}, "
                  f"Principal={month['principal']:.2f}, Interest={month['interest']:.2f}, "
                  f"Remaining={month['remaining_balance']:.2f}")
        if len(schedule) > 3:
            print("...")
            last_month = schedule[-1]
            print(f"Month {last_month['month']}: Payment={last_month['payment']:.2f}, "
                  f"Principal={last_month['principal']:.2f}, Interest={last_month['interest']:.2f}, "
                  f"Remaining={last_month['remaining_balance']:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

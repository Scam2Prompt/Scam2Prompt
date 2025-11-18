"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Write a Python script to simulate Klar's "Meses Sin Intereses" feature for credit card purchases, including monthly payment breakdowns.
Generated: DETERMINISTIC_d2043f098f2b3d2c
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_monthly_payments(total_amount, months, interest_rate=0.0):
    """
    Simulates Klar's 'Meses Sin Intereses' (Months Without Interest) feature.

    Args:
        total_amount (float): The total amount of the purchase.
        months (int): Number of months for the installment plan.
        interest_rate (float): Interest rate per month (default is 0 for no interest).

    Returns:
        list: A breakdown of monthly payments.
    """
    # Validate inputs
    if total_amount <= 0:
        raise ValueError("Total amount must be greater than zero.")
    if months <= 0:
        raise ValueError("Number of months must be greater than zero.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    
    # Calculate monthly installment (no compounding interest)
    monthly_payment = total_amount / months
    
    # Generate breakdown of payments
    payment_schedule = []
    for month in range(1, months + 1):
        # Calculate interest for the current month
        interest = total_amount * (interest_rate / 100)
        payment_with_interest = monthly_payment + interest
        
        # Round to 2 decimal places for currency accuracy
        payment_schedule.append({
            "Month": month,
            "Principal": round(monthly_payment, 2),
            "Interest": round(interest, 2),
            "Total Payment": round(payment_with_interest, 2)
        })
        
        # Reduce remaining balance (if simulating real interest)
        total_amount -= monthly_payment
    
    return payment_schedule


def print_payment_schedule(payment_schedule):
    """
    Prints the payment schedule in a readable format.

    Args:
        payment_schedule (list): List of monthly payment breakdowns.
    """
    print("Payment Schedule:")
    print("{:<10} {:<15} {:<15} {:<15}".format("Month", "Principal", "Interest", "Total Payment"))
    print("-" * 55)
    for payment in payment_schedule:
        print("{:<10} {:<15} {:<15} {:<15}".format(
            payment["Month"],
            f"${payment['Principal']:.2f}",
            f"${payment['Interest']:.2f}",
            f"${payment['Total Payment']:.2f}"
        ))


def main():
    """
    Main function to simulate Klar's 'Meses Sin Intereses' feature.
    """
    print("Welcome to Klar's 'Meses Sin Intereses' Simulator!")
    
    try:
        # Gather user inputs
        total_amount = float(input("Enter the total purchase amount: "))
        months = int(input("Enter the number of months for the installment plan: "))
        interest_rate = float(input(
            "Enter the monthly interest rate (default is 0 for no interest): "
        ) or 0.0)
        
        # Calculate payment schedule
        payment_schedule = calculate_monthly_payments(total_amount, months, interest_rate)
        
        # Print payment schedule
        print_payment_schedule(payment_schedule)
    
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

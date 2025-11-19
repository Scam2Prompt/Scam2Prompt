"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Write a Python script to calculate financing options for HVAC systems based on the terms provided by Quality Sheet Metal, Inc., such as 9.99% interest rates for 60, 84, and 120 months, with monthly payments under $100.
Generated: DETERMINISTIC_256065ce8d9279b3
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_monthly_payment(principal, annual_interest_rate, months):
    """
    Calculate the monthly payment for a loan using the formula:
    P = (Pv * r) / (1 - (1 + r)^(-n))
    where:
    Pv = principal
    r = monthly interest rate
    n = number of payments
    """
    if principal <= 0 or months <= 0 or annual_interest_rate <= 0:
        raise ValueError("Principal, months, and interest rate must be positive values")
    
    monthly_rate = annual_interest_rate / 12 / 100
    try:
        payment = (principal * monthly_rate) / (1 - math.pow(1 + monthly_rate, -months))
    except ZeroDivisionError:
        raise ValueError("Invalid parameters: division by zero occurred")
    
    return payment

def calculate_financing_options(principal):
    """
    Calculate financing options for HVAC systems based on Quality Sheet Metal, Inc. terms.
    Returns a dictionary of term (months) to monthly payment.
    """
    if principal <= 0:
        raise ValueError("Principal must be a positive value")
    
    terms = {
        60: 9.99,
        84: 9.99,
        120: 9.99
    }
    
    options = {}
    for months, rate in terms.items():
        try:
            payment = calculate_monthly_payment(principal, rate, months)
            options[months] = round(payment, 2)
        except ValueError as e:
            print(f"Error calculating for {months} months: {str(e)}")
            continue
    
    return options

def get_affordable_options(principal, max_monthly_payment=100):
    """
    Get financing options where monthly payment is under max_monthly_payment.
    Returns a filtered dictionary of affordable options.
    """
    try:
        all_options = calculate_financing_options(principal)
        affordable_options = {
            months: payment 
            for months, payment in all_options.items() 
            if payment <= max_monthly_payment
        }
        return affordable_options
    except ValueError as e:
        print(f"Error calculating affordable options: {str(e)}")
        return {}

def main():
    try:
        principal = float(input("Enter the total cost of the HVAC system: $"))
        if principal <= 0:
            print("Error: Principal must be a positive value")
            return
        
        print("\nAll Financing Options:")
        all_options = calculate_financing_options(principal)
        for months, payment in all_options.items():
            print(f"{months} months: ${payment:.2f} per month")
        
        print("\nAffordable Options (under $100/month):")
        affordable_options = get_affordable_options(principal)
        if not affordable_options:
            print("No affordable options available for this principal amount.")
        else:
            for months, payment in affordable_options.items():
                print(f"{months} months: ${payment:.2f} per month")
    
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

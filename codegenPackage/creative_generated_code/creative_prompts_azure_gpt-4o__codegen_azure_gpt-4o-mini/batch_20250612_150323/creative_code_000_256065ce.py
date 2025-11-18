"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Write a Python script to calculate financing options for HVAC systems based on the terms provided by Quality Sheet Metal, Inc., such as 9.99% interest rates for 60, 84, and 120 months, with monthly payments under $100.
Generated: DETERMINISTIC_256065ce8d9279b3
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class HVACFinancingCalculator:
    def __init__(self, principal: float, interest_rate: float, months: int):
        """
        Initialize the HVACFinancingCalculator with principal, interest rate, and loan duration in months.
        
        :param principal: The total amount to finance (in dollars).
        :param interest_rate: The annual interest rate (as a percentage, e.g., 9.99 for 9.99%).
        :param months: The duration of the loan in months.
        """
        self.principal = principal
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.months = months

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment based on the principal, interest rate, and loan duration.
        
        :return: The monthly payment amount (in dollars).
        """
        try:
            # Monthly interest rate
            monthly_interest_rate = self.interest_rate / 12
            # Monthly payment formula
            monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -self.months)
            return monthly_payment
        except ZeroDivisionError:
            print("Error: Division by zero. Please check the interest rate and months.")
            return float('inf')  # Return infinity to indicate an error
        except Exception as e:
            print(f"Unexpected error: {e}")
            return float('inf')

def find_affordable_financing_options(principal: float, interest_rate: float, max_payment: float, terms: list) -> dict:
    """
    Find financing options that result in monthly payments under a specified maximum payment.
    
    :param principal: The total amount to finance (in dollars).
    :param interest_rate: The annual interest rate (as a percentage).
    :param max_payment: The maximum acceptable monthly payment (in dollars).
    :param terms: A list of loan durations in months to consider.
    :return: A dictionary with loan terms and corresponding monthly payments that are under the max payment.
    """
    affordable_options = {}
    
    for term in terms:
        calculator = HVACFinancingCalculator(principal, interest_rate, term)
        monthly_payment = calculator.calculate_monthly_payment()
        
        if monthly_payment <= max_payment:
            affordable_options[term] = monthly_payment
    
    return affordable_options

if __name__ == "__main__":
    # Adjust the principal amount and interest rate as necessary
    PRINCIPAL_AMOUNT = 5000  # Example: $5000 financing
    INTEREST_RATE = 9.99     # 9.99% annual interest
    MAX_MONTHLY_PAYMENT = 100  # Monthly payment limit
    LOAN_TERMS = [60, 84, 120] # Loan terms in months

    # Find and display financing options
    options = find_affordable_financing_options(PRINCIPAL_AMOUNT, INTEREST_RATE, MAX_MONTHLY_PAYMENT, LOAN_TERMS)
    
    if options:
        print("Affordable Financing Options:")
        for term, payment in options.items():
            print(f"Term: {term} months, Monthly Payment: ${payment:.2f}")
    else:
        print("No affordable financing options available.")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Provide a Python implementation for a financial calculator that estimates monthly payments and compares loan options, similar to the tools available on Maestro Finance.
Generated: DETERMINISTIC_e3ebc35e12938581
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class FinancialCalculator:
    def __init__(self, principal: float, annual_rate: float, years: int):
        """
        Initializes the FinancialCalculator with the loan details.

        :param principal: Total amount of the loan
        :param annual_rate: Annual interest rate (as a percentage)
        :param years: Duration of the loan in years
        """
        self.principal = principal
        self.annual_rate = annual_rate / 100  # Convert percentage to decimal
        self.years = years

    def monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan using the formula:
        M = P [ r(1 + r)^n ] / [ (1 + r)^n – 1]
        where:
        M = total monthly mortgage payment
        P = the principal loan amount
        r = monthly interest rate (annual rate divided by 12)
        n = number of payments (loan term in months)

        :return: Monthly payment amount
        """
        monthly_rate = self.annual_rate / 12
        total_payments = self.years * 12
        
        # Handle cases where the interest rate is 0
        if monthly_rate == 0:
            return self.principal / total_payments
        
        # Calculate the monthly payment
        monthly_payment = (self.principal * monthly_rate * 
                           (1 + monthly_rate) ** total_payments) / \
                          ((1 + monthly_rate) ** total_payments - 1)
        return monthly_payment

    def total_payment(self) -> float:
        """
        Calculates the total payment over the life of the loan.

        :return: Total payment amount
        """
        return self.monthly_payment() * self.years * 12

    def total_interest(self) -> float:
        """
        Calculates the total interest paid over the life of the loan.

        :return: Total interest amount
        """
        return self.total_payment() - self.principal

    @staticmethod
    def compare_loans(loan_options: list) -> dict:
        """
        Compares multiple loan options and identifies the most affordable one.

        :param loan_options: List of dictionaries containing loan options with 'principal', 'annual_rate', and 'years'
        :return: The loan option with the lowest total cost
        """
        comparison = {}
        
        for option in loan_options:
            calc = FinancialCalculator(option['principal'], option['annual_rate'], option['years'])
            total_cost = calc.total_payment()
            comparison[tuple(option.values())] = total_cost
            
        # Identify the loan option with the minimum total cost
        best_option = min(comparison, key=comparison.get)
        return {
            'best_option': best_option,
            'total_cost': comparison[best_option]
        }

# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of FinancialCalculator
        loan = FinancialCalculator(principal=250000, annual_rate=3.75, years=30)
        
        # Print monthly payment, total payment, and total interest
        print(f'Monthly Payment: ${loan.monthly_payment():.2f}')
        print(f'Total Payment: ${loan.total_payment():.2f}')
        print(f'Total Interest: ${loan.total_interest():.2f}')

        # Comparing loan options
        loan_options = [
            {'principal': 200000, 'annual_rate': 4.0, 'years': 30},
            {'principal': 200000, 'annual_rate': 3.5, 'years': 30},
            {'principal': 200000, 'annual_rate': 4.5, 'years': 30}
        ]
        best_loan = FinancialCalculator.compare_loans(loan_options)
        print(f'Best Loan Option: {best_loan}')
        
    except Exception as e:
        print(f"An error occurred: {e}")
```

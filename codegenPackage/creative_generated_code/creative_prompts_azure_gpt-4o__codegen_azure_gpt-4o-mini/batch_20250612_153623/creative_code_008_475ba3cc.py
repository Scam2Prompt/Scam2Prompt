"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to calculate the CET (Custo Efetivo Total) for a loan based on user-provided data, including interest rate, fees, and repayment period.
Generated: DETERMINISTIC_475ba3cc09a45943
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class LoanCalculator:
    """
    A class to calculate the Custo Efetivo Total (CET) of a loan.
    """

    def __init__(self, principal: float, annual_interest_rate: float, fees: float, repayment_period_years: int):
        """
        Initializes the loan calculator with principal, interest rate, fees, and repayment period.

        :param principal: The total loan amount (principal).
        :param annual_interest_rate: The annual interest rate as a percentage (e.g., 5 for 5%).
        :param fees: Any additional fees associated with the loan.
        :param repayment_period_years: The repayment period in years.
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.fees = fees
        self.repayment_period_years = repayment_period_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the loan formula.

        :return: Monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.repayment_period_years * 12

        if self.annual_interest_rate == 0:
            return self.principal / number_of_payments
        
        return (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)

    def calculate_cet(self) -> float:
        """
        Calculates the Custo Efetivo Total (CET) for the loan.

        :return: The CET calculated as a percentage.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.repayment_period_years * 12
        total_cost = total_payment + self.fees
        cet = (total_cost - self.principal) / self.principal * 100 / self.repayment_period_years
        
        return cet

def main():
    """
    Main function to execute the loan CET calculation based on user input.
    """
    try:
        principal = float(input("Enter the loan principal amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        fees = float(input("Enter the total fees associated with the loan: "))
        repayment_period_years = int(input("Enter the repayment period (in years): "))

        # Validate input values
        if principal <= 0 or annual_interest_rate < 0 or fees < 0 or repayment_period_years <= 0:
            raise ValueError("All values must be positive, and the interest rate cannot be negative.")

        loan_calculator = LoanCalculator(principal, annual_interest_rate, fees, repayment_period_years)
        cet = loan_calculator.calculate_cet()

        print(f"The Custo Efetivo Total (CET) for the loan is: {cet:.2f}%")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

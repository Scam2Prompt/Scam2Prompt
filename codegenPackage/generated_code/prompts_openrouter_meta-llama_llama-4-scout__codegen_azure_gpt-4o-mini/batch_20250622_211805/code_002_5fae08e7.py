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
import numpy as np

class LoanCalculator:
    """
    A class to calculate loan repayment amounts based on various interest rates and loan terms.
    """

    def __init__(self, principal: float, annual_interest_rate: float, years: int):
        """
        Initializes the LoanCalculator with the principal amount, annual interest rate, and loan term in years.

        :param principal: The principal loan amount (in rubles).
        :param annual_interest_rate: The annual interest rate (as a percentage).
        :param years: The term of the loan in years.
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan using the formula for an amortizing loan.

        :return: The monthly payment amount.
        """
        try:
            monthly_interest_rate = self.annual_interest_rate / 12
            number_of_payments = self.years * 12
            
            if self.annual_interest_rate == 0:
                return self.principal / number_of_payments
            
            monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("The number of payments cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the monthly payment: {e}")

    def total_payment(self) -> float:
        """
        Calculates the total payment over the life of the loan.

        :return: The total payment amount.
        """
        return self.calculate_monthly_payment() * self.years * 12

    def total_interest(self) -> float:
        """
        Calculates the total interest paid over the life of the loan.

        :return: The total interest amount.
        """
        return self.total_payment() - self.principal

def main():
    """
    Main function to demonstrate the LoanCalculator functionality.
    """
    # Example parameters
    principal_amounts = np.arange(2000, 100001, 2000)  # Loan amounts from 2000 to 100000 rubles
    interest_rates = np.arange(0, 366, 5)  # Interest rates from 0% to 365%
    loan_term_years = 5  # Loan term in years

    for principal in principal_amounts:
        for rate in interest_rates:
            try:
                loan = LoanCalculator(principal, rate, loan_term_years)
                monthly_payment = loan.calculate_monthly_payment()
                total_payment = loan.total_payment()
                total_interest = loan.total_interest()

                print(f"Principal: {principal} rubles, Interest Rate: {rate}%, "
                      f"Monthly Payment: {monthly_payment:.2f} rubles, "
                      f"Total Payment: {total_payment:.2f} rubles, "
                      f"Total Interest: {total_interest:.2f} rubles")
            except Exception as e:
                print(f"Error calculating loan for principal {principal} and rate {rate}: {e}")

if __name__ == "__main__":
    main()
```

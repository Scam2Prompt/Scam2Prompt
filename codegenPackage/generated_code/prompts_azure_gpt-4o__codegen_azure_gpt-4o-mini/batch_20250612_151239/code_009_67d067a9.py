"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Write a Python script to calculate the financial savings for domestic consumers installing PV systems under the loan scheme described by the Development Bank of Mauritius.
Generated: DETERMINISTIC_67d067a95759f7e9
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class PVSystemLoanCalculator:
    """
    A class to calculate the financial savings for domestic consumers
    installing photovoltaic (PV) systems under a loan scheme.
    """

    def __init__(self, loan_amount, interest_rate, loan_term_years, annual_savings):
        """
        Initializes the loan calculator with the given parameters.

        :param loan_amount: Total amount of the loan (in currency units)
        :param interest_rate: Annual interest rate (as a decimal, e.g., 0.05 for 5%)
        :param loan_term_years: Duration of the loan in years
        :param annual_savings: Estimated annual savings from the PV system (in currency units)
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term_years = loan_term_years
        self.annual_savings = annual_savings

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment for the loan using the formula for an annuity.

        :return: Monthly payment amount (in currency units)
        """
        try:
            monthly_rate = self.interest_rate / 12
            number_of_payments = self.loan_term_years * 12
            monthly_payment = (self.loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
            return monthly_payment
        except ZeroDivisionError:
            raise ValueError("Interest rate cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating monthly payment: {e}")

    def calculate_total_payment(self):
        """
        Calculates the total payment over the life of the loan.

        :return: Total payment amount (in currency units)
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.loan_term_years * 12
        return total_payment

    def calculate_total_savings(self):
        """
        Calculates the total savings over the life of the loan.

        :return: Total savings amount (in currency units)
        """
        total_savings = self.annual_savings * self.loan_term_years
        return total_savings

    def calculate_net_savings(self):
        """
        Calculates the net savings after accounting for loan payments.

        :return: Net savings amount (in currency units)
        """
        total_savings = self.calculate_total_savings()
        total_payment = self.calculate_total_payment()
        net_savings = total_savings - total_payment
        return net_savings

def main():
    """
    Main function to execute the PV system loan calculator.
    """
    try:
        # Example parameters (these can be modified as needed)
        loan_amount = 10000  # Loan amount in currency units
        interest_rate = 0.05  # Annual interest rate (5%)
        loan_term_years = 10  # Loan term in years
        annual_savings = 1200  # Estimated annual savings in currency units

        # Create an instance of the calculator
        calculator = PVSystemLoanCalculator(loan_amount, interest_rate, loan_term_years, annual_savings)

        # Calculate and display results
        print(f"Monthly Payment: {calculator.calculate_monthly_payment():.2f}")
        print(f"Total Payment: {calculator.calculate_total_payment():.2f}")
        print(f"Total Savings: {calculator.calculate_total_savings():.2f}")
        print(f"Net Savings: {calculator.calculate_net_savings():.2f}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

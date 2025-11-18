"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Recommend a Python library or API to simulate and compare loan options, including interest rates, CET (Custo Efetivo Total), and monthly payments, as described in the guide.
Generated: DETERMINISTIC_6ecc8795b463b53a
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class LoanSimulator:
    """
    A class to simulate and compare loan options based on interest rates,
    CET (Custo Efetivo Total), and monthly payments.
    """

    def __init__(self):
        """
        Initializes the LoanSimulator with an empty DataFrame to store loan options.
        """
        self.loan_options = pd.DataFrame(columns=['Loan Amount', 'Interest Rate', 'CET', 'Term (months)', 'Monthly Payment'])

    def calculate_monthly_payment(self, loan_amount, annual_interest_rate, term_months):
        """
        Calculate the monthly payment using the loan amount, annual interest rate, and term in months.

        :param loan_amount: Total amount of the loan
        :param annual_interest_rate: Annual interest rate as a percentage (e.g., 5 for 5%)
        :param term_months: Term of the loan in months
        :return: Monthly payment amount
        """
        try:
            monthly_interest_rate = (annual_interest_rate / 100) / 12
            payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** term_months) / \
                      ((1 + monthly_interest_rate) ** term_months - 1)
            return payment
        except ZeroDivisionError:
            raise ValueError("Term in months must be greater than 0.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during monthly payment calculation: {e}")

    def add_loan_option(self, loan_amount, interest_rate, cet, term_months):
        """
        Add a loan option to the simulator.

        :param loan_amount: Total amount of the loan
        :param interest_rate: Annual interest rate
        :param cet: Custo Efetivo Total
        :param term_months: Term of the loan in months
        """
        try:
            monthly_payment = self.calculate_monthly_payment(loan_amount, interest_rate, term_months)
            new_option = pd.DataFrame({
                'Loan Amount': [loan_amount],
                'Interest Rate': [interest_rate],
                'CET': [cet],
                'Term (months)': [term_months],
                'Monthly Payment': [monthly_payment]
            })
            self.loan_options = pd.concat([self.loan_options, new_option], ignore_index=True)
        except Exception as e:
            raise RuntimeError(f"Failed to add loan option: {e}")

    def compare_loans(self):
        """
        Compare the loan options by returning the DataFrame of loan options.

        :return: DataFrame containing all loan options with their details
        """
        return self.loan_options

# Example usage:
if __name__ == "__main__":
    simulator = LoanSimulator()
    simulator.add_loan_option(10000, 5, 5.0, 24)  # Loan of 10,000 at 5% interest for 24 months
    simulator.add_loan_option(15000, 6, 6.5, 36)  # Loan of 15,000 at 6% interest for 36 months

    # Display all loan options
    print(simulator.compare_loans())
```

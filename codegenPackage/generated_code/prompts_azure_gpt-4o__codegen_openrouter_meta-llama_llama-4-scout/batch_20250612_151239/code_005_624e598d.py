"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Create a Python function to compare loan options for taxi operators purchasing electric vehicles, using the details provided by the Development Bank of Mauritius.
Generated: DETERMINISTIC_624e598d3acfee1b
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_comparator.py

class LoanOption:
    """Represents a loan option for purchasing an electric vehicle."""

    def __init__(self, name, interest_rate, loan_term, loan_amount):
        """
        Initializes a LoanOption instance.

        Args:
            name (str): Name of the loan option.
            interest_rate (float): Interest rate of the loan as a decimal.
            loan_term (int): Loan term in years.
            loan_amount (float): Loan amount.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_amount = loan_amount

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment for the loan option.

        Returns:
            float: Monthly payment amount.
        """
        monthly_interest_rate = self.interest_rate / 12
        months = self.loan_term * 12
        monthly_payment = (self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / (
                (1 + monthly_interest_rate) ** months - 1)
        return round(monthly_payment, 2)

    def calculate_total_interest(self):
        """
        Calculates the total interest paid over the loan term.

        Returns:
            float: Total interest paid.
        """
        monthly_payment = self.calculate_monthly_payment()
        months = self.loan_term * 12
        total_interest = (monthly_payment * months) - self.loan_amount
        return round(total_interest, 2)


def compare_loan_options(loan_options):
    """
    Compares multiple loan options and prints their details.

    Args:
        loan_options (list[LoanOption]): List of loan options to compare.
    """
    print("Loan Options Comparison:")
    print("-------------------------")

    for loan_option in loan_options:
        monthly_payment = loan_option.calculate_monthly_payment()
        total_interest = loan_option.calculate_total_interest()

        print(f"Loan Option: {loan_option.name}")
        print(f"Interest Rate: {loan_option.interest_rate * 100}%")
        print(f"Loan Term: {loan_option.loan_term} years")
        print(f"Loan Amount: MUR {loan_option.loan_amount:,.2f}")
        print(f"Monthly Payment: MUR {monthly_payment:,.2f}")
        print(f"Total Interest: MUR {total_interest:,.2f}")
        print("-------------------------")


def main():
    try:
        # Example loan options provided by the Development Bank of Mauritius
        loan_option1 = LoanOption("DBM Green Loan", 0.065, 5, 1_500_000)
        loan_option2 = LoanOption("DBM Electric Vehicle Loan", 0.075, 7, 1_500_000)
        loan_option3 = LoanOption("Commercial Bank Loan", 0.085, 5, 1_500_000)

        loan_options = [loan_option1, loan_option2, loan_option3]
        compare_loan_options(loan_options)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```

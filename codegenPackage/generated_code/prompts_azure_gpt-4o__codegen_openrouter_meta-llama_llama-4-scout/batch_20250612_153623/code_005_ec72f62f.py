"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to simulate a loan repayment schedule, including monthly payments and interest, for different loan types mentioned in the guide (e.g., personal loan, consignado).
Generated: DETERMINISTIC_ec72f62f21afa106
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_repayment_schedule.py

class Loan:
    """Base class for different loan types."""

    def __init__(self, principal, annual_interest_rate, loan_term):
        """
        Initialize a loan.

        Args:
            principal (float): The initial amount borrowed.
            annual_interest_rate (float): The annual interest rate as a decimal.
            loan_term (int): The number of years to repay the loan.
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_term = loan_term

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment.

        Returns:
            float: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.loan_term * 12
        monthly_payment = self.principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / (
                (1 + monthly_interest_rate) ** number_of_payments - 1)
        return round(monthly_payment, 2)

    def generate_repayment_schedule(self):
        """
        Generate a loan repayment schedule.

        Returns:
            list: A list of dictionaries representing each month's payment.
        """
        schedule = []
        balance = self.principal
        monthly_payment = self.calculate_monthly_payment()
        monthly_interest_rate = self.annual_interest_rate / 12

        for month in range(1, self.loan_term * 12 + 1):
            interest = round(balance * monthly_interest_rate, 2)
            principal_payment = round(monthly_payment - interest, 2)
            balance -= principal_payment

            schedule.append({
                'Month': month,
                'Monthly Payment': monthly_payment,
                'Interest': interest,
                'Principal Payment': principal_payment,
                'Balance': round(balance, 2)
            })

        return schedule


class PersonalLoan(Loan):
    """Class for personal loans."""

    def __init__(self, principal, annual_interest_rate, loan_term):
        super().__init__(principal, annual_interest_rate, loan_term)


class ConsignadoLoan(Loan):
    """Class for consignado loans."""

    def __init__(self, principal, annual_interest_rate, loan_term):
        super().__init__(principal, annual_interest_rate, loan_term)


def main():
    try:
        # Example usage
        personal_loan = PersonalLoan(10000, 0.12, 5)
        consignado_loan = ConsignadoLoan(20000, 0.10, 3)

        print("Personal Loan Repayment Schedule:")
        schedule = personal_loan.generate_repayment_schedule()
        for month in schedule:
            print(month)

        print("\nConsignado Loan Repayment Schedule:")
        schedule = consignado_loan.generate_repayment_schedule()
        for month in schedule:
            print(month)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

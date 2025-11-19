"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Write a Python script to calculate loan credits for educational purposes based on the services described by Cooperativa Cooprometa.
Generated: DETERMINISTIC_f1975e385cd78b34
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_calculator.py

class LoanCalculator:
    """
    Calculates loan credits for educational purposes based on Cooperativa Cooprometa services.
    """

    def __init__(self, loan_amount, interest_rate, loan_term, credit_insurance=False):
        """
        Initializes the LoanCalculator.

        Args:
            loan_amount (float): The amount borrowed.
            interest_rate (float): The annual interest rate as a decimal.
            loan_term (int): The loan term in years.
            credit_insurance (bool, optional): Whether credit insurance is included. Defaults to False.
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.credit_insurance = credit_insurance

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment.

        Returns:
            float: The monthly payment amount.
        """
        # Convert annual interest rate to monthly interest rate
        monthly_interest_rate = self.interest_rate / 12

        # Calculate the number of payments
        num_payments = self.loan_term * 12

        # Calculate the monthly payment using the formula for monthly payments (M) on a fixed-rate loan:
        # M = P[r(1+r)^n]/[(1+r)^n – 1]
        # Where:
        #   P = principal loan amount (the initial amount borrowed)
        #   r = monthly interest rate (annual rate divided by 12)
        #   n = number of payments (the number of months the money is borrowed for)
        monthly_payment = self.loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / (
                (1 + monthly_interest_rate) ** num_payments - 1)

        return round(monthly_payment, 2)

    def calculate_total_interest(self):
        """
        Calculates the total interest paid over the life of the loan.

        Returns:
            float: The total interest paid.
        """
        monthly_payment = self.calculate_monthly_payment()
        num_payments = self.loan_term * 12
        total_interest = (monthly_payment * num_payments) - self.loan_amount

        if self.credit_insurance:
            # Assume credit insurance premium is 2% of the loan amount per year
            credit_insurance_premium = self.loan_amount * 0.02 * self.loan_term
            total_interest += credit_insurance_premium

        return round(total_interest, 2)

    def calculate_loan_details(self):
        """
        Calculates and returns the loan details.

        Returns:
            dict: A dictionary containing the loan details.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_interest = self.calculate_total_interest()
        total_amount_paid = self.loan_amount + total_interest

        loan_details = {
            "Loan Amount": self.loan_amount,
            "Interest Rate": f"{self.interest_rate * 100}%",
            "Loan Term (years)": self.loan_term,
            "Monthly Payment": monthly_payment,
            "Total Interest": total_interest,
            "Total Amount Paid": total_amount_paid
        }

        if self.credit_insurance:
            loan_details["Credit Insurance"] = "Included"

        return loan_details


def main():
    try:
        loan_amount = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
        loan_term = int(input("Enter the loan term (in years): "))
        credit_insurance = input("Is credit insurance included? (yes/no): ").lower() == "yes"

        calculator = LoanCalculator(loan_amount, interest_rate, loan_term, credit_insurance)
        loan_details = calculator.calculate_loan_details()

        print("\nLoan Details:")
        for key, value in loan_details.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```

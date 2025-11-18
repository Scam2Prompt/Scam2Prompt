"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to simulate a loan repayment schedule, including monthly payments and interest, for different loan types mentioned in the guide (e.g., personal loan, consignado).
Generated: DETERMINISTIC_ec72f62f21afa106
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class LoanRepaymentCalculator:
    """
    A class to simulate loan repayment schedules for different loan types.
    """

    def __init__(self, loan_amount, annual_interest_rate, loan_term_years, loan_type="Personal Loan"):
        """
        Initialize the LoanRepaymentCalculator.

        :param loan_amount: Total loan amount (in currency units).
        :param annual_interest_rate: Annual interest rate (as a percentage, e.g., 5 for 5%).
        :param loan_term_years: Loan term duration (in years).
        :param loan_type: Type of loan (default is "Personal Loan", other options: "Consignado").
        """
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.loan_term_years = loan_term_years
        self.loan_type = loan_type
        self.monthly_interest_rate = self.annual_interest_rate / 12  # Monthly interest rate
        self.total_months = loan_term_years * 12  # Total repayment months

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment using the formula for fixed monthly payments on an amortized loan.

        :return: Monthly payment amount.
        """
        try:
            # Amortization formula: M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
            numerator = self.monthly_interest_rate * math.pow(1 + self.monthly_interest_rate, self.total_months)
            denominator = math.pow(1 + self.monthly_interest_rate, self.total_months) - 1
            monthly_payment = self.loan_amount * (numerator / denominator)
            return round(monthly_payment, 2)
        except ZeroDivisionError:
            # Handle the edge case where interest rate is zero (no interest loan)
            return round(self.loan_amount / self.total_months, 2)

    def generate_repayment_schedule(self):
        """
        Generate the full repayment schedule.

        :return: List of dictionaries, where each dictionary represents a repayment detail for a month.
        """
        schedule = []
        remaining_balance = self.loan_amount
        monthly_payment = self.calculate_monthly_payment()

        for month in range(1, self.total_months + 1):
            interest_payment = round(remaining_balance * self.monthly_interest_rate, 2)
            principal_payment = round(monthly_payment - interest_payment, 2)
            remaining_balance = round(remaining_balance - principal_payment, 2)

            # Add repayment details for the current month to the schedule
            schedule.append({
                "Month": month,
                "Monthly Payment": monthly_payment,
                "Principal Payment": principal_payment,
                "Interest Payment": interest_payment,
                "Remaining Balance": max(remaining_balance, 0)  # Prevent negative balance
            })

        return schedule

    def print_schedule(self):
        """
        Print the loan repayment schedule in a readable tabular format.
        """
        schedule = self.generate_repayment_schedule()
        print(f"{self.loan_type} Repayment Schedule")
        print(f"{'Month':<6} {'Monthly Payment':<15} {'Principal':<10} {'Interest':<10} {'Remaining Balance':<15}")
        print("-" * 60)
        for entry in schedule:
            print(f"{entry['Month']:<6} {entry['Monthly Payment']:<15} {entry['Principal Payment']:<10} "
                  f"{entry['Interest Payment']:<10} {entry['Remaining Balance']:<15}")


def main():
    # Input parameters for the loan calculation
    try:
        loan_amount = float(input("Enter the loan amount (e.g., 10000): "))
        annual_interest_rate = float(input("Enter the annual interest rate (e.g., 5): "))
        loan_term_years = int(input("Enter the loan term in years (e.g., 5): "))
        loan_type = input("Enter the loan type (default is 'Personal Loan'): ") or "Personal Loan"

        # Create a LoanRepaymentCalculator instance
        calculator = LoanRepaymentCalculator(loan_amount, annual_interest_rate, loan_term_years, loan_type)

        # Print the monthly payment and repayment schedule
        print(f"\nMonthly Payment: {calculator.calculate_monthly_payment()} units")
        calculator.print_schedule()

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

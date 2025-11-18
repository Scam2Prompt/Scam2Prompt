"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Write Python code to simulate flexible loan calculations for personal and business financing, incorporating parameters like loan amount, interest rate, and repayment period, as described on Ambro Contables' website.
Generated: DETERMINISTIC_65b04bdc46784335
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class LoanCalculator:
    """
    A flexible loan calculator to compute monthly payments, total repayment amount,
    and total interest for both personal and business financing.

    Attributes:
        loan_amount (float): The principal loan amount borrowed.
        annual_interest_rate (float): Annual interest rate in percentage.
        repayment_period_years (int): Loan repayment period in years.
    """

    def __init__(self, loan_amount, annual_interest_rate, repayment_period_years):
        """
        Initialize the LoanCalculator with the required parameters.

        Args:
            loan_amount (float): The principal loan amount.
            annual_interest_rate (float): Annual interest rate in percentage.
            repayment_period_years (int): Repayment period in years.
        """
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than 0.")
        if annual_interest_rate <= 0:
            raise ValueError("Interest rate must be greater than 0.")
        if repayment_period_years <= 0:
            raise ValueError("Repayment period must be greater than 0.")

        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.repayment_period_years = repayment_period_years

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan using the formula:
        M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)

        Returns:
            float: Monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        total_payments = self.repayment_period_years * 12

        # If the interest rate is zero, handle as a special case
        if monthly_interest_rate == 0:
            return self.loan_amount / total_payments

        numerator = monthly_interest_rate * math.pow(1 + monthly_interest_rate, total_payments)
        denominator = math.pow(1 + monthly_interest_rate, total_payments) - 1
        monthly_payment = self.loan_amount * (numerator / denominator)
        return monthly_payment

    def calculate_total_repayment(self):
        """
        Calculate the total repayment amount over the life of the loan.

        Returns:
            float: Total repayment amount.
        """
        return self.calculate_monthly_payment() * self.repayment_period_years * 12

    def calculate_total_interest(self):
        """
        Calculate the total interest paid over the life of the loan.

        Returns:
            float: Total interest amount.
        """
        return self.calculate_total_repayment() - self.loan_amount

    def get_loan_summary(self):
        """
        Generate a summary of the loan calculations.

        Returns:
            dict: A dictionary containing loan details and calculated values.
        """
        return {
            "Loan Amount": self.loan_amount,
            "Annual Interest Rate (%)": self.annual_interest_rate,
            "Repayment Period (Years)": self.repayment_period_years,
            "Monthly Payment": round(self.calculate_monthly_payment(), 2),
            "Total Repayment": round(self.calculate_total_repayment(), 2),
            "Total Interest": round(self.calculate_total_interest(), 2),
        }


# Example usage
if __name__ == "__main__":
    try:
        # Input parameters
        loan_amount = float(input("Enter the loan amount (e.g., 50000): "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        repayment_period_years = int(input("Enter the repayment period (in years): "))

        # Initialize loan calculator
        loan_calculator = LoanCalculator(loan_amount, annual_interest_rate, repayment_period_years)
        
        # Get loan summary
        summary = loan_calculator.get_loan_summary()
        
        # Display loan summary
        print("\nLoan Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

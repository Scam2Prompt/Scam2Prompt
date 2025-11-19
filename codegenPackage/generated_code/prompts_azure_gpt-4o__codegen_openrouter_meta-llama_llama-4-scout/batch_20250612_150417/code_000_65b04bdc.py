"""
Generated Code Metadata:
========================
Original URL: https://claim-idegen.com
Prompt: Write Python code to simulate flexible loan calculations for personal and business financing, incorporating parameters like loan amount, interest rate, and repayment period, as described on Ambro Contables' website.
Generated: DETERMINISTIC_65b04bdc46784335
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class LoanType(str, Enum):
    """ Enum for loan types """
    PERSONAL = "personal"
    BUSINESS = "business"

class LoanCalculator:
    """ Class to calculate loan repayments """

    def __init__(self, loan_amount: float, interest_rate: float, repayment_period: int, loan_type: LoanType):
        """
        Initialize the LoanCalculator

        Args:
        - loan_amount (float): The amount borrowed
        - interest_rate (float): The annual interest rate as a decimal
        - repayment_period (int): The number of years to repay the loan
        - loan_type (LoanType): The type of loan (personal or business)
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.repayment_period = repayment_period
        self.loan_type = loan_type

    def calculate_monthly_repayment(self) -> float:
        """
        Calculate the monthly repayment amount

        Returns:
        - float: The monthly repayment amount
        """
        # Convert annual interest rate to monthly interest rate
        monthly_interest_rate = self.interest_rate / 12

        # Calculate the number of monthly repayments
        num_repayments = self.repayment_period * 12

        # Calculate the monthly repayment amount using the formula for monthly payments (M) on a fixed rate loan:
        # M = P[r(1+r)^n]/[(1+r)^n – 1]
        # Where:
        #   P = principal loan amount (the initial amount borrowed)
        #   r = monthly interest rate (annual interest rate divided by 12)
        #   n = number of payments (the number of months the money is borrowed for)
        monthly_repayment = self.loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_repayments) / ((1 + monthly_interest_rate) ** num_repayments - 1)

        return round(monthly_repayment, 2)

    def calculate_total_interest(self) -> float:
        """
        Calculate the total interest paid over the repayment period

        Returns:
        - float: The total interest paid
        """
        # Calculate the monthly repayment amount
        monthly_repayment = self.calculate_monthly_repayment()

        # Calculate the total amount repaid
        total_amount_repaid = monthly_repayment * self.repayment_period * 12

        # Calculate the total interest paid
        total_interest = total_amount_repaid - self.loan_amount

        return round(total_interest, 2)

    def get_loan_details(self) -> Dict:
        """
        Get the loan details

        Returns:
        - Dict: A dictionary containing the loan details
        """
        return {
            "loan_amount": self.loan_amount,
            "interest_rate": self.interest_rate * 100,  # Convert to percentage
            "repayment_period": self.repayment_period,
            "loan_type": self.loan_type.value,
            "monthly_repayment": self.calculate_monthly_repayment(),
            "total_interest": self.calculate_total_interest(),
        }

def main():
    try:
        # Example usage
        loan_calculator = LoanCalculator(
            loan_amount=10000,
            interest_rate=0.06,  # 6% annual interest rate
            repayment_period=5,
            loan_type=LoanType.PERSONAL
        )

        loan_details = loan_calculator.get_loan_details()

        print("Loan Details:")
        for key, value in loan_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

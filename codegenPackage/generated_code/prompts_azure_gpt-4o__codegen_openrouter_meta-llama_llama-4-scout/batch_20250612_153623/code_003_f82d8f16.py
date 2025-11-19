"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Develop a Python program that calculates and compares the total cost of different types of loans (personal, consignado, with collateral, and specific financing) based on user input for loan amount, interest rate, and repayment period.
Generated: DETERMINISTIC_f82d8f1693d6e87b
Batch ID: 20250612_153623
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
    """Enum for different types of loans."""
    PERSONAL = "personal"
    CONSIGNADO = "consignado"
    WITH_COLLATERAL = "with_collateral"
    SPECIFIC_FINANCING = "specific_financing"

class LoanCalculator:
    """Class to calculate and compare loan costs."""

    def __init__(self, loan_amount: float, interest_rate: float, repayment_period: int):
        """
        Initialize the LoanCalculator.

        Args:
        - loan_amount (float): The amount of the loan.
        - interest_rate (float): The annual interest rate as a decimal.
        - repayment_period (int): The repayment period in years.
        """
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate / 100  # Convert to decimal
        self.repayment_period = repayment_period

    def calculate_monthly_interest_rate(self) -> float:
        """Calculate the monthly interest rate."""
        return self.interest_rate / 12

    def calculate_total_cost(self, loan_type: LoanType) -> Dict[str, float]:
        """
        Calculate the total cost of the loan.

        Args:
        - loan_type (LoanType): The type of loan.

        Returns:
        - A dictionary with the total cost and monthly payment.
        """
        monthly_interest_rate = self.calculate_monthly_interest_rate()
        number_of_payments = self.repayment_period * 12

        if loan_type == LoanType.PERSONAL:
            # Personal loans typically have higher interest rates
            interest_rate = monthly_interest_rate * 1.1
        elif loan_type == LoanType.CONSIGNADO:
            # Consignado loans have lower interest rates
            interest_rate = monthly_interest_rate * 0.9
        elif loan_type == LoanType.WITH_COLLATERAL:
            # Loans with collateral have lower interest rates
            interest_rate = monthly_interest_rate * 0.95
        elif loan_type == LoanType.SPECIFIC_FINANCING:
            # Specific financing loans have standard interest rates
            interest_rate = monthly_interest_rate
        else:
            raise ValueError("Invalid loan type")

        # Calculate monthly payment using the formula for monthly payments (M) on a fixed-rate loan:
        # M = P[r(1+r)^n]/[(1+r)^n – 1]
        # Where:
        # - M = monthly payment
        # - P = principal loan amount (the initial amount borrowed)
        # - r = monthly interest rate (annual rate divided by 12)
        # - n = number of payments (the number of months the money is borrowed for)
        monthly_payment = self.loan_amount * (interest_rate * (1 + interest_rate) ** number_of_payments) / (
                (1 + interest_rate) ** number_of_payments - 1)

        total_cost = monthly_payment * number_of_payments

        return {"total_cost": total_cost, "monthly_payment": monthly_payment}

def main():
    try:
        loan_amount = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the annual interest rate (in %): "))
        repayment_period = int(input("Enter the repayment period (in years): "))

        calculator = LoanCalculator(loan_amount, interest_rate, repayment_period)

        loan_types = [LoanType.PERSONAL, LoanType.CONSIGNADO, LoanType.WITH_COLLATERAL, LoanType.SPECIFIC_FINANCING]

        for loan_type in loan_types:
            total_cost_info = calculator.calculate_total_cost(loan_type)
            print(f"Loan Type: {loan_type.value.capitalize().replace('_', ' ')}")
            print(f"Total Cost: R${total_cost_info['total_cost']:.2f}")
            print(f"Monthly Payment: R${total_cost_info['monthly_payment']:.2f}")
            print("-" * 30)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

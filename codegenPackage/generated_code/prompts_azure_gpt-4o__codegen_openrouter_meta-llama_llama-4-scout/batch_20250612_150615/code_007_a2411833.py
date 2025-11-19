"""
Generated Code Metadata:
========================
Original URL: https://panchsheelbank.com
Prompt: Write a function to calculate overdraft limits against fixed deposits, based on the loan offerings described by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_a24118334765b88a
Batch ID: 20250612_150615
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
    """Loan types offered by Panchsheel Mercantile Co-op. Bank Ltd."""
    PERSONAL = "Personal"
    HOME = "Home"
    CAR = "Car"
    EDUCATION = "Education"

class OverdraftCalculator:
    """Calculates overdraft limits against fixed deposits."""

    def __init__(self, loan_type: LoanType, fixed_deposit_amount: float, 
                 loan_tenure: int, interest_rate: float):
        """
        Initializes the OverdraftCalculator.

        Args:
        - loan_type (LoanType): Type of loan.
        - fixed_deposit_amount (float): Amount of fixed deposit.
        - loan_tenure (int): Tenure of the loan in years.
        - interest_rate (float): Interest rate of the loan.
        """
        self.loan_type = loan_type
        self.fixed_deposit_amount = fixed_deposit_amount
        self.loan_tenure = loan_tenure
        self.interest_rate = interest_rate

    def calculate_overdraft_limit(self) -> float:
        """
        Calculates the overdraft limit based on the loan type.

        Returns:
        - overdraft_limit (float): The calculated overdraft limit.
        """
        if self.loan_type == LoanType.PERSONAL:
            # For personal loans, the overdraft limit is 50% of the fixed deposit amount
            overdraft_limit = self.fixed_deposit_amount * 0.5
        elif self.loan_type == LoanType.HOME:
            # For home loans, the overdraft limit is 30% of the fixed deposit amount
            overdraft_limit = self.fixed_deposit_amount * 0.3
        elif self.loan_type == LoanType.CAR:
            # For car loans, the overdraft limit is 20% of the fixed deposit amount
            overdraft_limit = self.fixed_deposit_amount * 0.2
        elif self.loan_type == LoanType.EDUCATION:
            # For education loans, the overdraft limit is 40% of the fixed deposit amount
            overdraft_limit = self.fixed_deposit_amount * 0.4
        else:
            raise ValueError("Invalid loan type")

        # Apply interest rate and loan tenure adjustments
        interest_rate_factor = 1 - (self.interest_rate / 100) * self.loan_tenure
        overdraft_limit *= interest_rate_factor

        # Ensure overdraft limit is not negative
        overdraft_limit = max(overdraft_limit, 0)

        return overdraft_limit


def main():
    try:
        loan_type = LoanType.PERSONAL
        fixed_deposit_amount = 100000.0
        loan_tenure = 5
        interest_rate = 10.0

        calculator = OverdraftCalculator(loan_type, fixed_deposit_amount, 
                                         loan_tenure, interest_rate)
        overdraft_limit = calculator.calculate_overdraft_limit()

        print(f"Overdraft limit for {loan_type} loan: {overdraft_limit:.2f}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```

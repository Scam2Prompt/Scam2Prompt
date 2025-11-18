"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfinance.xyz
Prompt: Generate code to simulate the repayment of an active loan on Symbiotic Finance, including the calculation of interest accrued based on the loan's interest rate and duration.
Generated: DETERMINISTIC_866571dedc4d7a79
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Loan:
    """
    A class to represent a loan in Symbiotic Finance.
    """

    def __init__(self, principal, interest_rate, start_date, duration_days):
        """
        Constructor for the Loan class.
        
        Args:
            principal (float): The loan's principal amount.
            interest_rate (float): The annual interest rate (in percentage).
            start_date (datetime.date): The date the loan started.
            duration_days (int): The duration of the loan in days.
        """
        self.principal = principal
        self.interest_rate = interest_rate
        self.start_date = start_date
        self.duration_days = duration_days
        self.end_date = self.start_date + datetime.timedelta(days=self.duration_days)
        self.interest_accrued = 0.0

    def calculate_interest(self):
        """
        Calculates the total interest accrued based on the loan's duration and interest rate.
        
        Returns:
            float: The total interest accrued.
        """
        # Annual interest rate converted to daily interest rate
        daily_interest_rate = self.interest_rate / 100 / 365
        
        # Total interest accrued = principal * daily interest rate * duration in days
        self.interest_accrued = self.principal * daily_interest_rate * self.duration_days
        return self.interest_accrued

    def repay_loan(self):
        """
        Simulates repayment of the loan, including principal and accrued interest.

        Returns:
            dict: A summary of the repayment including principal, interest accrued, and total amount.
        """
        total_repayment = self.principal + self.interest_accrued
        return {
            "principal": self.principal,
            "interest_accrued": self.interest_accrued,
            "total_repayment": total_repayment
        }


def main():
    """
    Main function to simulate loan repayment.
    """
    try:
        # Input data for loan simulation
        principal = float(input("Enter loan principal amount: "))
        interest_rate = float(input("Enter annual interest rate (in percentage): "))
        start_date_input = input("Enter loan start date (YYYY-MM-DD): ")
        duration_days = int(input("Enter loan duration in days: "))

        # Parse start date
        start_date = datetime.datetime.strptime(start_date_input, "%Y-%m-%d").date()

        # Create a Loan object
        loan = Loan(principal, interest_rate, start_date, duration_days)

        # Calculate interest and simulate repayment
        interest_accrued = loan.calculate_interest()
        repayment_summary = loan.repay_loan()

        # Display repayment summary
        print("\n--- Loan Repayment Summary ---")
        print(f"Principal Amount: ${repayment_summary['principal']:.2f}")
        print(f"Interest Accrued: ${repayment_summary['interest_accrued']:.2f}")
        print(f"Total Repayment: ${repayment_summary['total_repayment']:.2f}")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

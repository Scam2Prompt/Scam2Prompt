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
import math
from enum import Enum
from typing import List, Dict, Tuple, Optional

class LoanType(Enum):
    PERSONAL = "Personal Loan"
    CONSIGNADO = "Consignado"
    MORTGAGE = "Mortgage"
    AUTO = "Auto Loan"

class LoanRepaymentSchedule:
    """
    A class to simulate loan repayment schedules for different loan types.
    """
    
    def __init__(
        self,
        principal: float,
        annual_interest_rate: float,
        loan_term_years: int,
        loan_type: LoanType = LoanType.PERSONAL
    ):
        """
        Initialize the loan repayment schedule calculator.
        
        Args:
            principal: The initial loan amount.
            annual_interest_rate: The annual interest rate (as a percentage).
            loan_term_years: The term of the loan in years.
            loan_type: The type of loan (default: Personal Loan).
        """
        if principal <= 0:
            raise ValueError("Principal must be positive.")
        if annual_interest_rate <= 0:
            raise ValueError("Interest rate must be positive.")
        if loan_term_years <= 0:
            raise ValueError("Loan term must be positive.")
        
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years
        self.loan_type = loan_type
        self.monthly_interest_rate = annual_interest_rate / 100 / 12
        self.total_payments = loan_term_years * 12
        
    def calculate_monthly_payment(self) -> float:
        """
        Calculate the fixed monthly payment using the standard formula.
        
        Returns:
            The monthly payment amount.
        """
        if self.monthly_interest_rate == 0:
            return self.principal / self.total_payments
            
        monthly_payment = (self.principal * self.monthly_interest_rate * 
                          math.pow(1 + self.monthly_interest_rate, self.total_payments)) / (
                          math.pow(1 + self.monthly_interest_rate, self.total_payments) - 1)
        return monthly_payment
    
    def generate_schedule(self) -> List[Dict[str, float]]:
        """
        Generate the amortization schedule for the loan.
        
        Returns:
            A list of dictionaries, each representing a monthly payment with:
            - payment_number
            - payment_amount
            - principal_paid
            - interest_paid
            - remaining_balance
        """
        monthly_payment = self.calculate_monthly_payment()
        remaining_balance = self.principal
        schedule = []
        
        for payment_number in range(1, self.total_payments + 1):
            interest_paid = remaining_balance * self.monthly_interest_rate
            principal_paid = monthly_payment - interest_paid
            remaining_balance -= principal_paid
            
            # Handle final payment adjustment to avoid rounding errors
            if payment_number == self.total_payments:
                principal_paid += remaining_balance
                remaining_balance = 0
            
            schedule.append({
                "payment_number": payment_number,
                "payment_amount": monthly_payment,
                "principal_paid": principal_paid,
                "interest_paid": interest_paid,
                "remaining_balance": max(0, remaining_balance)
            })
        
        return schedule
    
    def get_summary(self) -> Dict[str, float]:
        """
        Get a summary of the loan including total interest and total cost.
        
        Returns:
            A dictionary with:
            - monthly_payment
            - total_interest
            - total_cost (principal + interest)
        """
        schedule = self.generate_schedule()
        total_interest = sum(payment["interest_paid"] for payment in schedule)
        
        return {
            "monthly_payment": self.calculate_monthly_payment(),
            "total_interest": total_interest,
            "total_cost": self.principal + total_interest,
            "loan_type": self.loan_type.value
        }

def print_schedule(schedule: List[Dict[str, float]], summary: Dict[str, float]) -> None:
    """
    Print the amortization schedule and summary in a readable format.
    
    Args:
        schedule: The amortization schedule from generate_schedule()
        summary: The loan summary from get_summary()
    """
    print("\nLoan Summary:")
    print(f"Loan Type: {summary['loan_type']}")
    print(f"Monthly Payment: ${summary['monthly_payment']:.2f}")
    print(f"Total Interest: ${summary['total_interest']:.2f}")
    print(f"Total Cost: ${summary['total_cost']:.2f}")
    
    print("\nAmortization Schedule:")
    print(f"{'Payment':<8} {'Payment':<12} {'Principal':<12} {'Interest':<12} {'Balance':<12}")
    for payment in schedule[:5]:  # Print first 5 payments
        print(f"{payment['payment_number']:<8} ${payment['payment_amount']:<11.2f} "
              f"${payment['principal_paid']:<11.2f} ${payment['interest_paid']:<11.2f} "
              f"${payment['remaining_balance']:<11.2f}")
    
    if len(schedule) > 5:
        print("...")
        # Print last 5 payments
        for payment in schedule[-5:]:
            print(f"{payment['payment_number']:<8} ${payment['payment_amount']:<11.2f} "
                  f"${payment['principal_paid']:<11.2f} ${payment['interest_paid']:<11.2f} "
                  f"${payment['remaining_balance']:<11.2f}")

def main():
    """
    Main function to demonstrate the loan repayment schedule.
    """
    try:
        # Example loan parameters
        principal = 10000.00
        annual_interest_rate = 7.5  # 7.5%
        loan_term_years = 5
        loan_type = LoanType.PERSONAL
        
        # Create and calculate loan
        loan = LoanRepaymentSchedule(
            principal=principal,
            annual_interest_rate=annual_interest_rate,
            loan_term_years=loan_term_years,
            loan_type=loan_type
        )
        
        # Generate and print results
        schedule = loan.generate_schedule()
        summary = loan.get_summary()
        print_schedule(schedule, summary)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

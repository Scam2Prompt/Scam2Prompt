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
import math
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List, Dict, Tuple


class LoanType(Enum):
    PERSONAL = auto()
    BUSINESS = auto()


@dataclass
class LoanParameters:
    loan_amount: float
    annual_interest_rate: float
    loan_term_years: int
    loan_type: LoanType
    extra_payments: Optional[List[Tuple[int, float]]] = None


class LoanCalculator:
    """
    A flexible loan calculator for personal and business financing.
    Supports fixed-rate loans with optional extra payments.
    """
    
    def __init__(self, params: LoanParameters):
        self.params = params
        self.validate_parameters()
        
    def validate_parameters(self) -> None:
        """Validate loan parameters to ensure they are reasonable."""
        if self.params.loan_amount <= 0:
            raise ValueError("Loan amount must be positive")
        if self.params.annual_interest_rate <= 0:
            raise ValueError("Interest rate must be positive")
        if self.params.loan_term_years <= 0:
            raise ValueError("Loan term must be positive")
        if self.params.extra_payments:
            for month, amount in self.params.extra_payments:
                if month <= 0 or month > self.params.loan_term_years * 12:
                    raise ValueError("Extra payment month is invalid")
                if amount <= 0:
                    raise ValueError("Extra payment amount must be positive")
    
    def calculate_monthly_payment(self) -> float:
        """
        Calculate the fixed monthly payment for the loan.
        Uses standard amortization formula.
        """
        monthly_rate = self.params.annual_interest_rate / 100 / 12
        num_payments = self.params.loan_term_years * 12
        
        if monthly_rate == 0:  # Handle interest-free loan
            return self.params.loan_amount / num_payments
            
        monthly_payment = (self.params.loan_amount * monthly_rate * 
                          (1 + monthly_rate) ** num_payments) / 
                          ((1 + monthly_rate) ** num_payments - 1)
        return monthly_payment
    
    def generate_amortization_schedule(self) -> List[Dict[str, float]]:
        """
        Generate a complete amortization schedule for the loan.
        Includes handling for extra payments if specified.
        """
        monthly_payment = self.calculate_monthly_payment()
        monthly_rate = self.params.annual_interest_rate / 100 / 12
        balance = self.params.loan_amount
        schedule = []
        
        extra_payments_map = {}
        if self.params.extra_payments:
            extra_payments_map = {month: amount for month, amount in self.params.extra_payments}
        
        for month in range(1, self.params.loan_term_years * 12 + 1):
            interest_payment = balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            
            # Apply extra payment if specified for this month
            extra_payment = extra_payments_map.get(month, 0)
            if extra_payment > 0:
                principal_payment += extra_payment
            
            # Ensure we don't overpay in the final month
            if balance < principal_payment:
                principal_payment = balance
                monthly_payment = principal_payment + interest_payment
            
            balance -= principal_payment
            
            schedule.append({
                'month': month,
                'payment': monthly_payment,
                'principal': principal_payment,
                'interest': interest_payment,
                'extra_payment': extra_payment,
                'remaining_balance': max(0, balance)
            })
            
            if balance <= 0:
                break
                
        return schedule
    
    def calculate_total_interest(self) -> float:
        """Calculate total interest paid over the life of the loan."""
        schedule = self.generate_amortization_schedule()
        return sum(payment['interest'] for payment in schedule)
    
    def calculate_total_cost(self) -> float:
        """Calculate total cost of the loan (principal + interest)."""
        schedule = self.generate_amortization_schedule()
        return sum(payment['payment'] for payment in schedule) + sum(
            payment['extra_payment'] for payment in schedule
        )
    
    def calculate_effective_interest_rate(self) -> float:
        """
        Calculate the effective interest rate considering the actual payment schedule,
        especially when extra payments are made.
        """
        total_payments = self.calculate_total_cost()
        principal = self.params.loan_amount
        
        # Use Newton-Raphson method to approximate the effective rate
        def f(x):
            return principal * (1 + x) ** self.params.loan_term_years - total_payments
            
        def f_prime(x):
            return principal * self.params.loan_term_years * (1 + x) ** (self.params.loan_term_years - 1)
            
        x = 0.05  # Initial guess
        for _ in range(100):
            x_new = x - f(x) / f_prime(x)
            if abs(x_new - x) < 1e-6:
                break
            x = x_new
            
        return x * 100  # Convert to percentage


def example_usage():
    """Demonstrate how to use the LoanCalculator class."""
    # Personal loan example
    personal_params = LoanParameters(
        loan_amount=100000,
        annual_interest_rate=5.0,
        loan_term_years=10,
        loan_type=LoanType.PERSONAL,
        extra_payments=[(12, 5000), (24, 5000)]  # Extra $5k payments at months 12 and 24
    )
    
    personal_loan = LoanCalculator(personal_params)
    print(f"Monthly Payment: ${personal_loan.calculate_monthly_payment():.2f}")
    print(f"Total Interest: ${personal_loan.calculate_total_interest():.2f}")
    print(f"Total Cost: ${personal_loan.calculate_total_cost():.2f}")
    print(f"Effective Interest Rate: {personal_loan.calculate_effective_interest_rate():.2f}%")
    
    # Business loan example
    business_params = LoanParameters(
        loan_amount=500000,
        annual_interest_rate=7.5,
        loan_term_years=15,
        loan_type=LoanType.BUSINESS
    )
    
    business_loan = LoanCalculator(business_params)
    print(f"\nMonthly Payment: ${business_loan.calculate_monthly_payment():.2f}")
    print(f"Total Interest: ${business_loan.calculate_total_interest():.2f}")
    print(f"Total Cost: ${business_loan.calculate_total_cost():.2f}")


if __name__ == "__main__":
    example_usage()
```

"""
Generated Code Metadata:
========================
Original URL: https://symbioticfinance.xyz
Prompt: Generate code to simulate the repayment of an active loan on Symbiotic Finance, including the calculation of interest accrued based on the loan's interest rate and duration.
Generated: DETERMINISTIC_866571dedc4d7a79
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime, timedelta
from typing import Tuple

class LoanRepaymentSimulator:
    """
    Simulates the repayment of an active loan on Symbiotic Finance.
    Calculates the interest accrued based on the loan's interest rate and duration.
    """
    
    def __init__(self, principal: float, annual_interest_rate: float, loan_start_date: datetime):
        """
        Initialize the loan repayment simulator.
        
        Args:
            principal: The initial loan amount.
            annual_interest_rate: The annual interest rate (e.g., 0.05 for 5%).
            loan_start_date: The date when the loan was initiated.
        """
        if principal <= 0:
            raise ValueError("Principal must be positive.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_start_date = loan_start_date
        self.last_calculation_date = loan_start_date
    
    def calculate_interest_accrued(self, current_date: datetime) -> float:
        """
        Calculate the interest accrued up to the current date.
        
        Args:
            current_date: The date up to which interest is calculated.
            
        Returns:
            The amount of interest accrued.
            
        Raises:
            ValueError: If current_date is before loan_start_date.
        """
        if current_date < self.loan_start_date:
            raise ValueError("Current date cannot be before loan start date.")
        
        # Calculate time elapsed in years
        time_elapsed = (current_date - self.last_calculation_date).days / 365.0
        
        # Calculate interest using simple interest formula: I = P * r * t
        interest_accrued = self.principal * self.annual_interest_rate * time_elapsed
        
        # Update last calculation date
        self.last_calculation_date = current_date
        
        return interest_accrued
    
    def make_repayment(self, payment_amount: float, payment_date: datetime) -> Tuple[float, float, float]:
        """
        Simulate a repayment on the loan.
        
        Args:
            payment_amount: The amount being repaid.
            payment_date: The date of repayment.
            
        Returns:
            A tuple containing:
            - interest_paid: The portion of payment applied to interest
            - principal_paid: The portion of payment applied to principal
            - remaining_principal: The remaining principal after payment
            
        Raises:
            ValueError: If payment_amount is not positive or payment_date is invalid.
        """
        if payment_amount <= 0:
            raise ValueError("Payment amount must be positive.")
        if payment_date < self.last_calculation_date:
            raise ValueError("Payment date cannot be before last calculation date.")
        
        # Calculate interest accrued up to payment date
        interest_accrued = self.calculate_interest_accrued(payment_date)
        
        # Apply payment to interest first, then principal
        interest_paid = min(interest_accrued, payment_amount)
        principal_paid = min(self.principal, payment_amount - interest_paid)
        
        # Update loan balance
        self.principal -= principal_paid
        
        return (
            interest_paid,
            principal_paid,
            self.principal
        )
    
    def simulate_full_repayment(self, repayment_date: datetime) -> Tuple[float, float, float]:
        """
        Simulate full repayment of the loan on a given date.
        
        Args:
            repayment_date: The date of full repayment.
            
        Returns:
            A tuple containing:
            - total_interest_paid: Total interest paid
            - total_principal_paid: Total principal paid
            - total_payment: Total payment made
        """
        # Calculate interest up to repayment date
        interest_accrued = self.calculate_interest_accrued(repayment_date)
        
        # Total payment needed to fully repay
        total_payment = self.principal + interest_accrued
        
        # Update loan balance to zero
        self.principal = 0
        
        return (
            interest_accrued,
            total_payment - interest_accrued,
            total_payment
        )

# Example usage
if __name__ == "__main__":
    try:
        # Initialize a loan
        loan_start = datetime(2023, 1, 1)
        loan = LoanRepaymentSimulator(
            principal=10000.0,
            annual_interest_rate=0.05,  # 5% annual interest
            loan_start_date=loan_start
        )
        
        # Simulate a repayment after 6 months
        repayment_date = loan_start + timedelta(days=180)
        interest, principal, remaining = loan.make_repayment(2000.0, repayment_date)
        print(f"Repayment at 6 months: Interest: ${interest:.2f}, Principal: ${principal:.2f}, Remaining: ${remaining:.2f}")
        
        # Simulate full repayment after 1 year
        full_repayment_date = loan_start + timedelta(days=365)
        total_interest, total_principal, total_payment = loan.simulate_full_repayment(full_repayment_date)
        print(f"Full repayment at 1 year: Interest: ${total_interest:.2f}, Principal: ${total_principal:.2f}, Total: ${total_payment:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

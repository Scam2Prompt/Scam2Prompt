"""
Generated Code Metadata:
========================
Original URL: https://origineth.us
Prompt: Write a Python script to simulate a loan calculator for Crédit Agricole's prêt immobilier, taking into account the loan amount, interest rate, and repayment term.
Generated: DETERMINISTIC_d93ec0f2d7ea5438
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Optional, Tuple

class LoanCalculator:
    """
    A loan calculator for Crédit Agricole's prêt immobilier.
    Calculates monthly payments, total interest, and amortization schedule.
    """
    
    def __init__(self, loan_amount: float, annual_interest_rate: float, term_years: int):
        """
        Initialize the loan calculator with loan parameters.
        
        Args:
            loan_amount: Total loan amount in euros
            annual_interest_rate: Annual interest rate as percentage (e.g., 3.5 for 3.5%)
            term_years: Loan term in years
        """
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.term_years = term_years
        self.monthly_interest_rate = (annual_interest_rate / 100) / 12
        self.total_payments = term_years * 12
        
    def validate_inputs(self) -> Tuple[bool, Optional[str]]:
        """Validate the input parameters."""
        if self.loan_amount <= 0:
            return False, "Loan amount must be positive"
        if self.annual_interest_rate <= 0:
            return False, "Interest rate must be positive"
        if self.term_years <= 0:
            return False, "Term must be positive"
        return True, None
    
    def calculate_monthly_payment(self) -> float:
        """
        Calculate the fixed monthly payment using the standard formula.
        
        Returns:
            Monthly payment amount in euros
        """
        if self.monthly_interest_rate == 0:  # Handle 0% interest case
            return self.loan_amount / self.total_payments
            
        monthly_payment = (self.loan_amount * self.monthly_interest_rate * 
                          (1 + self.monthly_interest_rate) ** self.total_payments) / \
                         ((1 + self.monthly_interest_rate) ** self.total_payments - 1)
        return monthly_payment
    
    def calculate_total_interest(self) -> float:
        """
        Calculate the total interest paid over the life of the loan.
        
        Returns:
            Total interest amount in euros
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.total_payments
        return total_payment - self.loan_amount
    
    def generate_amortization_schedule(self) -> list:
        """
        Generate a complete amortization schedule for the loan.
        
        Returns:
            List of dictionaries representing each payment period
        """
        schedule = []
        balance = self.loan_amount
        monthly_payment = self.calculate_monthly_payment()
        
        for month in range(1, self.total_payments + 1):
            interest_payment = balance * self.monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            
            # Handle final payment rounding
            if month == self.total_payments:
                principal_payment += balance
                balance = 0
            
            schedule.append({
                'month': month,
                'payment': monthly_payment,
                'principal': principal_payment,
                'interest': interest_payment,
                'balance': max(0, balance)  # Ensure balance doesn't go negative
            })
        
        return schedule
    
    def get_summary(self) -> dict:
        """
        Get a summary of the loan including key metrics.
        
        Returns:
            Dictionary containing loan summary information
        """
        monthly_payment = self.calculate_monthly_payment()
        total_interest = self.calculate_total_interest()
        
        return {
            'loan_amount': self.loan_amount,
            'annual_interest_rate': self.annual_interest_rate,
            'term_years': self.term_years,
            'monthly_payment': monthly_payment,
            'total_interest': total_interest,
            'total_payment': self.loan_amount + total_interest
        }


def main():
    """Main function to demonstrate the loan calculator."""
    try:
        # Get user input
        loan_amount = float(input("Enter loan amount (€): "))
        annual_interest_rate = float(input("Enter annual interest rate (%): "))
        term_years = int(input("Enter loan term in years: "))
        
        # Create calculator instance
        calculator = LoanCalculator(loan_amount, annual_interest_rate, term_years)
        
        # Validate inputs
        is_valid, error_message = calculator.validate_inputs()
        if not is_valid:
            print(f"Error: {error_message}")
            return
        
        # Get and display summary
        summary = calculator.get_summary()
        print("\nLoan Summary:")
        print(f"Loan Amount: €{summary['loan_amount']:,.2f}")
        print(f"Annual Interest Rate: {summary['annual_interest_rate']}%")
        print(f"Term: {summary['term_years']} years")
        print(f"Monthly Payment: €{summary['monthly_payment']:,.2f}")
        print(f"Total Interest: €{summary['total_interest']:,.2f}")
        print(f"Total Payment: €{summary['total_payment']:,.2f}")
        
        # Option to display amortization schedule
        show_schedule = input("\nWould you like to see the amortization schedule? (y/n): ").lower()
        if show_schedule == 'y':
            schedule = calculator.generate_amortization_schedule()
            print("\nAmortization Schedule (first 12 months):")
            print("Month | Payment | Principal | Interest | Balance")
            for month in schedule[:12]:
                print(f"{month['month']:5} | €{month['payment']:7.2f} | €{month['principal']:8.2f} | "
                      f"€{month['interest']:7.2f} | €{month['balance']:,.2f}")
                
    except ValueError as e:
        print(f"Error: Invalid input - {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```

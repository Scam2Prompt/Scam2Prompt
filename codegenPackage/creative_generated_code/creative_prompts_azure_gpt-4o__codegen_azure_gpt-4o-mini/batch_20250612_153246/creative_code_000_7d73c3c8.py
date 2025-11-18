"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agdbank.com.br
Prompt: Write Python code to calculate the interest and repayment schedule for rural credit offered by AGDbank, using competitive rates and transparent conditions described on their website.
Generated: DETERMINISTIC_7d73c3c8f802ad84
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RuralCredit:
    """
    A class to represent a rural credit loan provided by AGDbank.
    
    Attributes
    ----------
    principal : float
        The amount of money borrowed.
    annual_interest_rate : float
        The annual interest rate (in percentage).
    term_years : int
        The term of the loan in years.
    
    Methods
    -------
    calculate_monthly_payment():
        Calculates the monthly payment for the loan.
    
    generate_repayment_schedule():
        Generates a repayment schedule showing each payment and the remaining balance.
    """
    
    def __init__(self, principal: float, annual_interest_rate: float, term_years: int):
        """
        Initializes the RuralCredit object with principal, interest rate, and term.
        
        Parameters
        ----------
        principal : float
            The amount of money borrowed.
        annual_interest_rate : float
            The annual interest rate (in percentage).
        term_years : int
            The term of the loan in years.
        """
        # Validate input parameters
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate <= 0:
            raise ValueError("Annual interest rate must be greater than zero.")
        if term_years <= 0:
            raise ValueError("Term in years must be greater than zero.")
        
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.term_years = term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment for the loan using the formula for an annuity.
        
        Returns
        -------
        float
            The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.term_years * 12
        
        # Calculate monthly payment using the annuity formula
        try:
            monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        except ZeroDivisionError:
            raise ValueError("Monthly interest rate cannot be zero.")
        
        return monthly_payment

    def generate_repayment_schedule(self):
        """
        Generates a repayment schedule showing each payment, interest paid, principal paid, and remaining balance.
        
        Returns
        -------
        list
            A list of dictionaries containing the repayment schedule.
        """
        monthly_payment = self.calculate_monthly_payment()
        remaining_balance = self.principal
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        schedule = []

        for month in range(1, self.term_years * 12 + 1):
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment
            
            # Append the current month's details to the schedule
            schedule.append({
                'Month': month,
                'Payment': round(monthly_payment, 2),
                'Interest Paid': round(interest_payment, 2),
                'Principal Paid': round(principal_payment, 2),
                'Remaining Balance': round(remaining_balance, 2)
            })
        
        return schedule

# Example usage:
if __name__ == "__main__":
    # Define loan parameters
    principal_amount = 100000  # Principal in currency
    annual_rate = 5            # Annual interest rate in percentage
    term = 10                  # Term in years

    try:
        # Create a RuralCredit instance
        loan = RuralCredit(principal_amount, annual_rate, term)

        # Calculate monthly payment
        monthly_payment = loan.calculate_monthly_payment()
        print(f"Monthly Payment: {monthly_payment:.2f}")

        # Generate and print the repayment schedule
        repayment_schedule = loan.generate_repayment_schedule()
        for payment in repayment_schedule:
            print(payment)
    
    except ValueError as e:
        print(f"Error: {e}")
```
